 self.picode = self.get_picode()

                self.branchcodes  = num_rows[:3]
                try:
                    if(len(self.branchcodes) == 3):
                        self.branch_code_founds = self.search_defaultheader(self.branchcodes[0])
                except branchmodel.DefaultHeaders.DoesNotExist:
                    #self.branchdetails = self.save_branchdetails(num_rows[:3])
                    if(len(self.branchcodes) == 3):
                        self.branchdetails = self.save_branchdetails(self.branchcodes)
                        self.client_number = num_rows[3:]
                        self.clientdetails = self.save_clientdetails(self.client_number)
                        self.save_cap = self.save_partialdata(num_rows[:3], self.clientdetails, self.picode, self.branchcodes[0])
                else:
                    self.client_number = num_rows[3:]
                    if(len(self.branchcodes) == 3):
                        self.clientdetails = self.save_clientdetails(self.client_number)
                        self.save_cap = self.save_partialdata(num_rows[:3], self.clientdetails, self.picode, self.branchcodes[0])
            else:
                self.row_data = num_rows #self.excel_reader.get_row_values(0, n)
                self.indexed_data = self.row_data[1:-1]
                self.branch_codes = self.search_defaultheader(self.indexed_data)
                try:
                    self.found_headers =  self.search_header(self.branch_codes)
                    try:
                        self.indexed_data = self.row_data[2:-1]
                        #self.branch_headers = self.get_picode(self.indexed_data)
                        self.branch_headers = self.search_defaultheader(self.indexed_data)
                        self.brancheader = self.search_defaultheader(self.branch_headers)

                        try:
                            self.indexed_data = self.row_data[3:-1]
                            self.saved = self.save_legacy(self.indexed_data, self.found_headers, self.brancheader)
                            
                        except datamodels.CREDIT_APPLICATION.DoesNotExist:
                            self.indexed_data = self.row_data[3:-1]
                            self.saved = self.save_legacy(self.indexed_data, self.found_headers, self.brancheader)
                             
                    except branchmodel.DefaultHeaders.DoesNotExist:
                        self.saved_header = self.save_defaultbranchode(self.branch_headers)
                        self.indexed_data = self.row_data[3:-1]
                        self.saved = self.save_legacy(self.indexed_data, self.found_headers, self.saved_header)
                        
                except branchmodel.RequiredHeader.DoesNotExist:
                    self.saved_object = self.save_branchode(self.branch_codes)
                    try:
                        self.indexed_data = self.row_data[2:-1]
                        self.branch_headers = self.get_picode(self.indexed_data)
                        self.brancheader = self.search_defaultheader(self.branch_headers)

                        self.indexed_data = self.row_data[3:-1]
                        self.saved = self.save_legacy(self.indexed_data, self.saved_object, self.saved_header)
                           
                    except branchmodel.DefaultHeaders.DoesNotExist:
                        self.saved_header = self.save_defaultbranchode(self.branch_headers)
                        self.indexed_data = self.row_data[3:-1]
                        self.saved = self.save_legacy(self.indexedr, self.saved_object, self.saved_header)
