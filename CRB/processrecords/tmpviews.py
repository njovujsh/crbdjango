def process_requested_csv(self, request, model, outputformat, headers, extent, filename=None):
        self.myfile = str(model)
        if(filename):
            self.myfile = filename
            if(self.myfile.endswith(".csv")):
                pass
            else:
                if(extent):
                    if "." in extent:
                        self.myfile = self.myfile + str(extent)
                    else:
                        self.myfile = self.myfile + "." + str(extent)

        try:
            self.models = self.get_models(model.upper())
            self.templates = self.get_model_templates(model.upper())
            self.fields = self.parse_model_fields(self.models)

            if(self.templates is None):
                self.data_view_template = self.load_template()
            else:
                self.data_view_template = self.load_template(self.templates)

            if(self.data_view_template):
                if(self.models is not None):
                    self.csv_worker_obj = self.get_csv_workout(model.upper())

                    if(self.csv_worker_obj):
                        self.obj = self.models.objects.all()
                        #if(self.filename):

                        self.csv_handler = self.csv_worker_obj(self.myfile, "excel", self.fields, headers)
                        self.returned = self.csv_handler.write_row_data(self.obj) #.csv(self.fields)
                        return self.returned
                else:
                    self.rendered = self.process_data_context(request, self.data_view_template, self.models)
                    return HttpResponse(self.rendered)
            else:
                pass
        except:
            raise

    def load_template(self, template):
        try:

            if(template):
                return loader.get_template(template)
            else:
                return loader.get_template("dataview.html")
        except:# TemplateDoesNotExists:
            raise

    def get_csv_workout(self, dataset):
        try:
            if(dataset == "FINANCIAL MALPRACTICE DATA"):
                return processcsvs.ProcessCSVFMD
            elif(dataset == "COLLATERAL CREDIT GUARANTOR"):
                return processcsvs.ProcessCSVCCG
            elif(dataset == "COLLATERAL MATERIAL COLLATERAL"):
                return processcsvs.ProcessCSVCMC
            elif(dataset == "BORROWERSTAKEHOLDER"):
                return processcsvs.ProcessCSVBS
            elif(dataset == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return processcsvs.ProcessCSVPIS
            elif(dataset == "BOUNCEDCHEQUES"):
                return processcsvs.ProcessCSVBC
            elif(dataset == "CREDIT APPLICATION"):
                return processcsvs.ProcessCSVCP
            elif(dataset == "CREDITBORROWERACCOUNT"):
                return processcsvs.ProcessCSVCBA
            elif(dataset == "INSTITUTION BRANCH"):
                self.template = "IB_dataview.html"
                return processcsvs.ProcessCSVIB
            elif(dataset == "PARTICIPATING INSTITUTION"):
                return processcsvs.ProcessCSVPI
        except:
            raise

    def process_data_context(self, request, template, datamodel):
        try:
            self.parsed_fields = self.parse_model_fields(datamodel)

            self.data_available = datamodel.objects.all()
            self.now = time.ctime()
            self.context = RequestContext(request, {"modelfields":self.parsed_fields, "availabledata":self.data_available,
                                                    "displaytimes":self.now, "basetitle":mytitle
                                   })

            try:
                #return rendered
                return template.render(self.context)
            except:
                raise

        except:
            raise

    def parse_model_fields(self, model_data):
        """
        Returns the fields coresponding to particular models.
        """
        self.fields = [ ]
        self.mfields = model_data._meta.fields

        for field in self.mfields:
            if field.name in self.fields:
                pass
            else:
                if(field.name == "dateset_ref"):
                    pass 
                else:
                    self.fields.append(field.name)

        #return the model fields
        return self.fields

    def get_models(self, dataset):
        try:
            if(dataset == "FINANCIAL MALPRACTICE DATA"):
                return datamodels.FINANCIAL_MALPRACTICE_DATA
            elif(dataset == "COLLATERAL CREDIT GUARANTOR"):
                return datamodels.COLLATERAL_CREDIT_GUARANTOR
            elif(dataset == "COLLATERAL MATERIAL COLLATERAL"):
                return datamodels.COLLATERAL_MATERIAL_COLLATERAL
            elif(dataset == "BORROWERSTAKEHOLDER"):
                return datamodels.BORROWERSTAKEHOLDER
            elif(dataset == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return datamodels.PARTICIPATINGINSTITUTIONSTAKEHOLDER
            elif(dataset == "BOUNCEDCHEQUES"):
                return datamodels.BOUNCEDCHEQUES
            elif(dataset == "CREDIT APPLICATION"):
                return datamodels.CREDIT_APPLICATION
            elif(dataset == "CREDITBORROWERACCOUNT"):
                return datamodels.CREDITBORROWERACCOUNT
            elif(dataset == "INSTITUTION BRANCH"):
                self.template = "IB_dataview.html"
                return datamodels.INSTITUTION_BRANCH
            elif(dataset == "PARTICIPATING INSTITUTION"):
                return datamodels.PARTICIPATING_INSTITUTION
        except:
            raise

    def get_model_templates(self, dataset):
        try:
            if(dataset == "FINANCIAL MALPRACTICE DATA"):
                return "fmd_dataview.html"
            elif(dataset == "COLLATERAL CREDIT GUARANTOR"):
                return "ccg_dataview.html"
            elif(dataset == "COLLATERAL MATERIAL COLLATERAL"):
                return "cmc_dataview.html"
            elif(dataset == "BORROWERSTAKEHOLDER"):
                return "bs_dataview.html"
            elif(dataset == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return "pis_dataview.html"
            elif(dataset == "BOUNCEDCHEQUES"):
                return "bc_dataview.html"
            elif(dataset == "CREDIT APPLICATION"):
                return "cp_dataview.html"
            elif(dataset == "CREDITBORROWERACCOUNT"):
                return "cba_dataview.html"
            elif(dataset == "INSTITUTION BRANCH"):
                self.templates = "IB_dataview.html"
                return self.templates
            elif(dataset == "PARTICIPATING INSTITUTION"):
                return "pi_dataview.html"
        except:
            raise
    
    def get_model_byID(self, mid):
        try:
            if(mid < 1):
                return None 
            else:
                return record_models.Dataset.objects.get(id=mid)
        except:
            pass 
        
    def grab_headers(self, fileheader):
        try:
            return datamodels.SubmissionHeaders.objects.get(file_identifier=fileheader)
        except:
            pass 
                
    def post(self, request):
        """
        Handle post request.
        """
        try:
            if(request.user.is_authenticated()):
                if(request.method == "POST"):
                    self.headerlist = [ ]
                    
                    self.formats = request.POST.get("outputformat", "")
                    self.outputname = request.POST.get("filename", "")

                    #---grab the needed file headers----#
                    self.headers = request.POST.get("header", "")
                    self.pi_code = request.POST.get("pi_identification_code", "")#file_identifier
                    self.institution_name = request.POST.get("institution_name", "")
                    self.submission_date = request.POST.get("submission_date", "")
                    self.version_number = request.POST.get("version_number", "")
                    self.creation_date = request.POST.get("creation_date", "")
                    self.f_id_code = request.POST.get("file_identifier", "")
                    self.ref_records = request.POST.get("corresponding_records", "")

                    
                    #Grab a set of data headers and needed models
                    self.submission_headers = self.grab_headers(self.f_id_code)
                    self.dataset_model = self.get_model_byID(self.ref_records).dataset
                   
                    #create a list and append the data in
                    self.headerlist.append(self.headers)
                    self.headerlist.append(self.pi_code)
                    self.headerlist.append(self.institution_name)
                    self.headerlist.append(self.submission_date)
                    self.headerlist.append(self.version_number)
                    self.headerlist.append(self.creation_date)
                    self.headerlist.append(self.f_id_code)
                    
                    if(self.ref_records and self.formats):
                        if(self.outputname):

                            #detect spaces
                            if(" " in self.outputname):
                                #request, requesteddataset, outputformat, headers, filename=None
                                self.outputname = self.outputname.replace(" ", "", len(self.outputname))
                                self.redirect = "/requestingoutput/processing/data/%s/%s/%s/" % (str(self.dataset_model), str(self.formats), str(self.outputname))
                                self.rendered = self.process_requested_csv(request, self.dataset_model, self.formats, self.headerlist,  self.formats.lower(), self.outputname)
                                return self.rendered #HttpResponseRedirect(self.redirect)
                            else:
                                self.redirect = "/requestingoutput/processing/data/%s/%s/%s/" % (str(self.dataset_model), str(self.formats), str(self.outputname))
                                #return HttpResponseRedirect(self.redirect)
                                self.rendered = self.process_requested_csv(request, self.dataset_model, self.formats,self.headerlist,  self.formats.lower(), self.outputname)
                                return self.rendered #HttpResponseRedirect(self.redirect)
                        else:
                            self.redirect = "/requestingoutput/processing/data/%s/%s/" % (str(self.dataset_model), str(self.formats))
                            #return HttpResponseRedirect(self.redirect)
                            self.rendered = self.process_requested_csv(request, self.dataset_model, self.formats, self.headerlist,  self.formats.lower())
                            return self.rendered #HttpResponseRedirect(self.redirect)
                    else:
                        return HttpResponse("An output is required.")
                    
                else:
                    pass
            else:
                return HttpResponseRedirect("/")
        except:
            raise
