/*
 * searchrecords.js
 *
 * Copyright 2015 wangolo joel <wangolo@wangolo-3020>
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
 *
 *
 */

//function handle_event(){/
$(document).ready(function(){
    auto_pupolate_SCI_Fields();
});

//}

//handle_event();mouseover


function auto_pupolate_SCI_Fields(){
    $("input#id_PCI_Forms-PCI_Building_Unit_Number").keyup(function(){
        var searching = $('input#id_PCI_Forms-PCI_Building_Unit_Number').val();
        $("input#id_SCI_Forms-SCI_Unit_Number").val(searching);
    });
    
    $("input#id_PCI_Forms-PCI_Building_Name").keyup(function(){
        var building_name = $('input#id_PCI_Forms-PCI_Building_Name').val();
        $("input#id_SCI_Forms-SCI_Unit_Name").val(building_name);
    });
    
    $("input#id_PCI_Forms-PCI_Floor_Number").keyup(function(){
        var floor_number = $('input#id_PCI_Forms-PCI_Floor_Number').val();
        $("input#id_SCI_Forms-SCI_Floor_Number").val(floor_number);
    });
    
    $("input#id_PCI_Forms-PCI_Plot_or_Street_Number").keyup(function(){
        var street_number = $('input#id_PCI_Forms-PCI_Plot_or_Street_Number').val();
        $("input#id_SCI_Forms-SCI_Plot_or_Street_Number").val(street_number);
    });
    
    $("input#id_PCI_Forms-PCI_Plot_or_Street_Number").keyup(function(){
        var street_number = $('input#id_PCI_Forms-PCI_Plot_or_Street_Number').val();
        $("input#id_SCI_Forms-SCI_Plot_or_Street_Number").val(street_number);
    });
    
    $("input#id_PCI_Forms-PCI_LC_or_Street_Name").keyup(function(){
        var lcstreet_number = $('input#id_PCI_Forms-PCI_LC_or_Street_Name').val();
        $("input#id_SCI_Forms-SCI_LC_or_Street_Name").val(lcstreet_number);
    });
    
    $("input#id_PCI_Forms-PCI_Suburb").keyup(function(){
        var suburb = $('input#id_PCI_Forms-PCI_Suburb').val();
        $("input#id_SCI_Forms-SCI_Suburb").val(suburb);
    });
    
    $("input#id_PCI_Forms-PCI_Village").keyup(function(){
        var pci_village = $('input#id_PCI_Forms-PCI_Village').val();
        $("input#id_SCI_Forms-SCI_Village").val(pci_village);
    });
    
    $("input#id_PCI_Forms-PCI_PO_Box_Number").keyup(function(){
        var pci_boxnumber = $('input#id_PCI_Forms-PCI_PO_Box_Number').val();
        $("input#id_SCI_Forms-SCI_PO_Box_Number").val(pci_boxnumber);
    });
    
    $("input#id_PCI_Forms-PCI_Post_Office_Town").keyup(function(){
        var office_town = $('input#id_PCI_Forms-PCI_Post_Office_Town').val();
        $("input#id_SCI_Forms-SCI_Post_Office_Town").val(office_town);
    });
    
    $("input#id_SCI_Forms-SCI_Post_Office_Town").keyup(function(){
        var post_office_town = $('input#id_PCI_Forms-PCI_Post_Office_Town').val();
        $("input#id_SCI_Forms-SCI_Post_Office_Town").val(post_office_town);
    });
    
    $("input#id_PCI_Forms-PCI_Period_At_Address").keyup(function(){
        var period_at_adress = $('input#id_PCI_Forms-PCI_Period_At_Address').val();
        $("input#id_SCI_Forms-SCI_Period_At_Address").val(period_at_adress);
    });
    
    $("input#id_PCI_Forms-PCI_Primary_Number_Telephone_Number").keyup(function(){
        var pci_num_phone = $('input#id_PCI_Forms-PCI_Primary_Number_Telephone_Number').val();
        $("input#id_SCI_Forms-SCI_Primary_Number_Telephone_Number").val(pci_num_phone);
    });
    
    $("input#id_PCI_Forms-PCI_Mobile_Number_Telephone_Number").keyup(function(){
        var pci_other_telephone = $('input#id_PCI_Forms-PCI_Mobile_Number_Telephone_Number').val();
        $("input#id_SCI_Forms-SCI_Mobile_Number_Telephone_Number").val(pci_other_telephone);
    });
    
    $("input#id_PCI_Forms-PCI_Facsimile_Number").keyup(function(){
        var face_number = $('input#id_PCI_Forms-PCI_Facsimile_Number').val();
        $("input#id_SCI_Forms-SCI_Facsimile_Number").val(face_number);
    });
    
    $("input#id_PCI_Forms-PCI_Email_Address").keyup(function(){
        var pci_email = $('input#id_PCI_Forms-PCI_Email_Address').val();
        $("input#id_SCI_Forms-SCI_Email_Address").val(pci_email);
    });
    //id_SCI_Forms-SCI_Other_Number_Telephone_Number
    $("input#id_PCI_Forms-PCI_Web_site").keyup(function(){
        var pci_website = $('input#id_PCI_Forms-PCI_Web_site').val();
        $("input#id_SCI_Forms-SCI_Web_site").val(pci_website);
    });
    
    $("input#id_PCI_Forms-PCI_Other_Number_Telephone_Number").keyup(function(){
        var pci_website = $('input#id_PCI_Forms-PCI_Other_Number_Telephone_Number').val();
        $("input#id_SCI_Forms-SCI_Other_Number_Telephone_Number").val(pci_website);
    });
};

function handle_ajax(data, dataset){
    var url = "/record/searchingbyajax/" + dataset
    $.ajax({
        url:url,
        type: "get",
        data: {"dataset":data},
        dataType:'json',
        async: 'true',

        success: function(json, status, xhr){
            alert('something');
        },

        failure: function(info){
            alert("Got some failure");
        }
    });

};

function get_data(data){
    $.get("/fraudster/category/", {"fraudtype": data}, function(json){
        $("#id_standard_forms-Category_Code").html(json);
        console.log("Working like a charm");
        alert("I have finally worked");
    });
}

/*
<script>
 jQuery(document).ready(function($) {
      //  var testEmail = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;
      <!-- another regex filter you can use -->
      var testEmail =    /^[ ]*([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]{2,})[ ]*$/i;
      jQuery('input#email').bind('input propertychange', function() {
        if (testEmail.test(jQuery(this).val()))
        {
           jQuery(this).css({ 'border':'1px solid green'});
           jQuery('button.validate').prop("disabled",false);
         } else
         {
           jQuery(this).css({ 'border':'1px solid red'});
           jQuery('button.validate').prop("disabled",true);
         }
       });
});
</script>
*/
