/*
 * handleimport.js
 * 
 * Copyright 2015 Wangolo Joel <wangolo@developer>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * <span class="symbol required"></span>
 * 
 */

$(document).ready(function(){
    $("#handleimport").change(function(){
        var selected_b  = $("#handleimport").val();
        console.log("Importing data here");
        var dataset = $("#handleimport option:selected").text();
        //alert(dataset);
        _selected_data(dataset);
        return false;
    });  
    return false;
});


$(document).ready(function(){
    //call the function that initlizes required fields
    initialize_required();
    //id_standard_forms_Borrowers_Client_Number_chosen
    
    $("#Borrowers_Client_NumberBS_chosen").mouseleave(function(){
       var text = $(".chosen-single span").text();
       
       //var find = '-';
       //var re = new RegExp(find, 'g');
       //str = str.replace(re, '');
        var parsed_text = text.split("-").join("");
        _search_selected_clientRoots(parsed_text);
        return false;
    });
    
    $("#Borrowers_Client_NumberSelect_chosen").mouseleave(function(){
        var text = $(".chosen-single span").text();
        var parsed_text = text.split("-").join("");
        _search_cba_clientRoots(parsed_text);
        return false;
        
    });
    
    $("#Borrowers_Client_NumberCMC_chosen").mouseleave(function(){
        var text = $(".chosen-single span").text();
        var parsed_text = text.split("-").join("");
        _search_cba_clientRoots(parsed_text);
        return false;
        
    });
    
    $("#Borrowers_Client_NumberFRA_chosen").mouseleave(function(){
        var text = $(".chosen-single span").text();
        var parsed_text = text.split("-").join("");
        _search_selected_clientRoots(parsed_text);
        return false;
        
    });
});


function _clientroot_url(){
    return "/importdata/searchbyclient/selectedroot/";
}

function initialize_required(){
    var pcode = $("label.PI_Identification_Code")
    pcode.append("<span class='symbol required'></span>");
    
    var pi = $("label.participating_institution")
    pi.append("<span class='symbol required'></span>");
    
    var st = $("label.Stakeholder_Type")
    st.append("<span class='symbol required'></span>");
    
    var sc = $("label.Stakeholder_Category")
    sc.append("<span class='symbol required'></span>");
    
    var sp = $("label.Shareholder_Percentage")
    sp.append("<span class='symbol required'></span>");
}

function _search_selected_clientRoots(dataset){
    if(dataset){
        $.ajax({
            url:_clientroot_url(),
            type:"get",
            data:{"clientRoot":dataset},
            dataType:"json",
            sync:true,
            
            //begin handling success if dadta is returned
            success:function(json, status, xhr){
                var client_root = json['ClientRoot'];
                var business = json['Business'];
                
                var surname = json['Surname'];
                var firstname = json['Firstname'];
                
                if(surname){
                    var details =  firstname + "     " + surname + "      " + business;
                    $(".client-details").text(details);
                }
                
                else if(business){
                    var details =  business + " " + client_root;
                    $(".client-details").text(details);
                }
            },
            
            failure:function(info){
                alert(info);
            }
        });
    };
};


function _search_cba_clientRoots(dataset){
    if(dataset){
        $.ajax({
            url: "/importdata/renewsearchcba/cba/",
            type:"get",
            data:{"clientRoot":dataset},
            dataType:"json",
            sync:true,
            
            //begin handling success if dadta is returned
            success:function(json, status, xhr){
                client_info = json["Client_Infor"];
                CBA_Accounts = json["CBA_Accounts"];
                
                var sub_select = document.getElementById("id_standard_forms-Borrower_Account_Reference");
                //empty
                sub_select.options.length=0;
                
                console.log(CBA_Accounts);
                for(var key in CBA_Accounts){
                    //console.log(key);
                    sub_select.options.add(new Option(key, CBA_Accounts[key]));
                }
                
                var client_root = client_info['ClientRoot'];
                var business = client_info['Business'];
                
                var surname = client_info['Surname'];
                var firstname = client_info['Firstname'];
                
                if(surname){
                    var details = "    " +  firstname + "     " + surname + "     " + client_root;
                    $(".client-details").text(details);
                }
                
                else{
                    var details =  business + "  " + client_root;
                    $(".client-details").text(details);
                }
            },
            
            failure:function(info){
                alert(info);
            }
        });
    };
};

 
function _search_fra_clientRoots(dataset){
    if(dataset){
        $.ajax({
            url: "/importdata/renewsearchcba/fra/",
            type:"get",
            data:{"clientRoot":dataset},
            dataType:"json",
            sync:true,
            
            //begin handling success if dadta is returned
            success:function(json, status, xhr){
                /*
                document.getElementById("ClientRoot").innerHTML = json['ClientRoot'];
                document.getElementById("Surname").innerHTML = json['Surname'];
                document.getElementById("Business").innerHTML = json['Business'];
                document.getElementById("Firstname").innerHTML = json['Firstname'];
                */
                var client_root = json['ClientRoot'];
                var business = json['Business'];
                
                var surname = json['Surname'];
                var firstname = json['Firstname'];
                
                if(surname ){
                    var details =  firstname + "     " + surname + "     " + client_root;
                    $(".client-details").text(details);
                }
                
                else{
                    var details =  business + "    " + client_root;
                    $(".client-details").text(details);
                }
            },
            
            failure:function(info){
                alert(info);
            }
        });
    };
};
 
$(document).ready(function(){
    $("#id_standard_forms-Applicant_Classification").change(function(){
        //var selected = $("#id_standard_forms-Applicant_Classification").val();
        var selected_choice = $("#id_standard_forms-Applicant_Classification option:selected").val();
        //alert(selected_choice);

        _filter_query(selected_choice);
        return false;
    });
    //return false;

    $("#id_standard_forms-Stakeholder_Type").change(function(){
        //var selected_b = $("#id_standard_forms-Stakeholder_Type").val();
        var selected_choice = $("#id_standard_forms-Stakeholder_Type option:selected").val();
        _filter_query(selected_choice);
        //alert(selected_choice);
        return false;
    });
    
    $("#id_standard_forms-Consumer_Classification").change(function(){
        //var selected_b = $("#id_standard_forms-Stakeholder_Type").val();
        var selected_choice = $("#id_standard_forms-Consumer_Classification option:selected").val();
        _filter_query(selected_choice);
        //alert(selected_choice);
        return false;
    });
    
    $("#id_standard_forms-Borrower_Classification").change(function(){
        //var selected_b = $("#id_standard_forms-Stakeholder_Type").val();
        var selected_choice = $("#id_standard_forms-Borrower_Classification option:selected").val();
        _filter_query(selected_choice);
        //alert(selected_choice);
        return false;
    });
    
    $("#id_standard_forms-Guarantor_Classification").change(function(){
        //var selected_b = $("#id_standard_forms-Stakeholder_Type").val();
        var selected_choice = $("#id_standard_forms-Guarantor_Classification option:selected").val();
        _filter_query(selected_choice);
        //alert(selected_choice);
        return false;
    });
    return false;
});

$(document).ready(function() {
      //  var testEmail = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;
    var testEmail =  /^[ ]*([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]{2,})[ ]*$/i;
    $('input#id_PCI_Forms-PCI_Email_Address').bind('input propertychange', function() {
        if (testEmail.test($(this).val()))
        {
           $(this).css({ 'border':'2px solid green'});
           //$('button.validate').prop("disabled",false);
         }
        else
            {
           $(this).css({ 'border':'2px solid red'});
           //$('button.validate').prop("disabled",true);
        }
    });
});

function _filter_query(choice){
    if(choice == "0"){
        //var element = document.getElementsByClassName("GSCAFB_Business_Name");
        //var element = document.getElementsById("GSCAFB_Business_Name");
        $("#GSCAFB_Business_Name").hide();
        $("#GSCAFB_Trading_Name").hide();
        $("#GSCAFB_Activity_Description").hide();
        $("#GSCAFB_Industry_Sector_Code").hide();
        $("#GSCAFB_Date_Registered").hide();
        $("#GSCAFB_Business_Type_Code").hide();
        //II
        $("#II_Registration_Certificate_Number").hide();
        $("#II_Tax_Identification_Number").hide();
        $("#II_Value_Added_Tax_Number").hide();

        //SHOW DETAILS.
        $("#GSCAFB_Surname").show();
        $("#GSCAFB_Forename1").show();
        $("#GSCAFB_Forename2").show();
        $("#GSCAFB_Forename3").show();
        $("#GSCAFB_Gender").show();
        $("#GSCAFB_Marital_Status").show();
        $("#GSCAFB_Date_of_Birth").show();

        //IDENTITY INFORMATION 
        $("#II_Passport_Number").show();
        $("#II_Drivers_Licence_ID_Number").show();
        $("#II_Voters_PERNO").hide();
        $("#II_Drivers_License_Permit_Number").show();
        $("#II_NSSF_Number").show();
        $("#II_Country_ID").show();
        
        $("#II_Teacher_Registration_Number").show();
        $("#II_Public_Service_Pension_Number").show();
        $("#II_KACITA_License_Number").show();
        $("#II_UPDF_Number").show();
        $("#II_Police_ID_Number").show();

        //EMPLOYEMENT INFORMATION 
        $("#EI_Employment_Type").show();
        $("#EI_Primary_Occupation").show();
        $("#EI_Employer_Name").show();
        $("#EI_Employee_Number").show();
        $("#EI_Employment_Date").show();
        $("#EI_Income_Band").show();
        $("#EI_Salary_Frequency").show();
        $("#II_Nationality").show();
         
    }
    else if (choice == "1"){
        $("#GSCAFB_Business_Name").show();
        $("#GSCAFB_Trading_Name").show();
        $("#GSCAFB_Activity_Description").show();
        $("#GSCAFB_Industry_Sector_Code").show();
        $("#GSCAFB_Date_Registered").show();
        $("#GSCAFB_Business_Type_Code").show();

        //II SHOW
        $("#II_Registration_Certificate_Number").show();
        $("#II_Tax_Identification_Number").show();
        $("#II_Value_Added_Tax_Number").show();

        //HIDE DETAILS.
        $("#GSCAFB_Surname").hide();
        $("#GSCAFB_Forename1").hide();
        $("#GSCAFB_Forename2").hide();
        $("#GSCAFB_Forename3").hide();
        $("#GSCAFB_Gender").hide();
        $("#GSCAFB_Marital_Status").hide();
        $("#GSCAFB_Date_of_Birth").hide();

        //IDENTITY INFORMATION 
        $("#II_Passport_Number").hide();
        $("#II_Drivers_Licence_ID_Number").hide();
        $("#II_Voters_PERNO").hide();
        $("#II_Drivers_License_Permit_Number").hide();
        $("#II_NSSF_Number").hide();
        //$("#II_Country_ID").hide();
        $("#II_Teacher_Registration_Number").hide();
        $("#II_Public_Service_Pension_Number").hide();
        $("#II_KACITA_License_Number").hide();
        $("#II_UPDF_Number").hide();
        $("#II_Police_ID_Number").hide();
//{% if form.name == "II_Police_ID_Number" form.name == "II_UPDF_Number" form.name == "II_KACITA_License_Number" form.name == "II_Public_Service_Pension_Number" form.name == "II_Teacher_Registration_Number" form.name == "II_Passport_Number" or form.name == "II_Drivers_Licence_ID_Number" or form.name == "II_Voters_PERNO" or form.name == "II_Drivers_License_Permit_Number" or form.name == "II_Country_ID" or form.name == "II_NSSF_Number"%}
       
        //EMPLOYEMENT INFORMATION 
        $("#EI_Employment_Type").hide();
        $("#EI_Primary_Occupation").hide();
        $("#EI_Employer_Name").hide();
        $("#EI_Employee_Number").hide();
        $("#EI_Employment_Date").hide();
        $("#EI_Income_Band").hide();
        $("#EI_Salary_Frequency").hide();
        //$("#II_Nationality").hide();
    }
    else{
        alert("Invalid option");
    }
}
function _validation_url(){
    return "/importdata/records/selected/";
}

/*function to handle and send to the server the selected dataset requiring validation*/
function _selected_data(dataset){
    if(dataset){
        $.ajax({
            url:_validation_url(),
            type:"get",
            data:{"importselected":dataset},
            dataType:"json",
            sync:true,
            
            //begin handling success if dadta is returned
            success:function(json, status, xhr){
                //alert(json);
                //alert(json['Records to be validated']);
                document.getElementById("validataing").innerHTML = json['Records to be validated'];
                document.getElementById("recordcount").innerHTML = json["Count"];
                //alert(json["Count"]);
            },
            
            failure:function(info){
                alert(info);
            }
        });
    };
};
 
//id_standard_forms-License_Issuing_Date

$(document).ready(function(){
    $("#id_standard_forms-License_Issuing_Date").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_submission_date").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_standard_forms-Date_Opened").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_standard_forms-Credit_Application_Date").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_standard_forms-Last_Status_Change_Date").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_standard_forms-Credit_Account_Date").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_standard_forms-Transaction_Date").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_standard_forms-Maturity_Date").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_standard_forms-Date_of_First_Payment").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_standard_forms-Last_Payment_Date").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_standard_forms-Credit_Account_Arrears_Date").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_standard_forms-Credit_Account_Closure_Date").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_standard_forms-Cheque_Account_Opened_Date").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_standard_forms-Cheque_Bounce_Date").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_standard_forms-Incident_Date").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_standard_forms-Collateral_Valuation_Expiry_Date").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_standard_forms-Valuation_Date").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_creation_date").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_GSCAFBForms-GSCAFB_Date_of_Birth").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_GSCAFBForms-GSCAFB_Date_Registered").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
    
    $("#id_EIForms-EI_Employment_Date").datepicker({
        yearRange: '1950:2020',
        dateFormat: "yy-mm-dd",
        changeMonth: true,
        changeYear: true
    });
})


$(document).ready(function(){
    $("#id_standard_forms-PI_Identification_Code").change(function(){
    var selected_b  = $("#id_standard_forms-PI_Identification_Code").val();
        //console.log("Importing data here");
        var pivalue = $("#id_standard_forms-PI_Identification_Code option:selected").text();
        //alert(dataset);
        _get_pi_information(pivalue);
        return false;
    });  
    return false;
    
    $("#id_branch_name").change(function(){
    var selected_b  = $("#id_branch_name").val();
        //console.log("Importing data here");
        var pivalue = $("#id_branch_name option:selected").val();
        alert(pivalue);
        //_get_pi_information(pivalue);
        return false;
    });  
    return false;
});

$(document).ready(function(){
    $("#id_branch_name").change(function(){
    var selected_b  = $("#id_branch_name").val();
        //console.log("Importing data here");
        var pivalue = $("#id_branch_name option:selected").val();
        //alert(pivalue);
        _get_branch_information(pivalue);
        return false;
    });  
    return false;
});


function _get_branch_information(value){
    $.ajax({
            url: "/branchpi/searchbranchinformation/",
            type:"get",
            data:{"biID":value},
            dataType:"json",
            sync:true,
            
            //begin handling success if data is returned
            success:function(json, status, xhr){
                //console.log(json)
                //console.log(json["PIVALUE"])
                var value = json["BRANCHCODE"]
                $("#id_branch_code").val(value)
            },
            
            failure:function(info){
                alert(info);
           }
    });
}

function _get_pi_information(value){
    $.ajax({
            url: "/branchpi/searchpiinformation/",
            type:"get",
            data:{"pivalue":value},
            dataType:"json",
            sync:true,
            
            //begin handling success if data is returned
            success:function(json, status, xhr){
                //console.log(json)
                //console.log(json["PIVALUE"])
                var value = json["PIVALUE"]
                $("#id_standard_forms-Institution_Name").val(value)
            },
            
            failure:function(info){
                alert(info);
           }
    });
}
