
/*
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
 */
$(document).ready(function(){
    
    $("#id_PCI_Forms-PCI_Region").change(function(){
        var selected_b  = $("#id_PCI_Forms-PCI_Region").val();
        $("#id_SCI_Forms-SCI_Region").val(selected_b);
        var selected_region = $("#id_PCI_Forms-PCI_Region option:selected").text();
        _ajax_2_django_sender(selected_region, "id_PCI_Forms-PCI_District");
        return false;
    });  
    //
    $("#id_PCI_Forms-PCI_District").change(function(){
        var selected_b  = $("#id_PCI_Forms-PCI_District").val();
        //alert(selected_b);id_SCI_Forms-SCI_District
        $("#id_SCI_Forms-SCI_District").val(selected_b);
        var district_region = $("#id_PCI_Forms-PCI_District option:selected").text();
        //alert(selected_region);
        _ajax_2_django_get_districts_sub(district_region, "id_PCI_Forms-PCI_County_or_Town");
        return false;
    });  
    
    $("#id_PCI_Forms-PCI_County_or_Town").change(function(){
        var selected_b  = $("#id_PCI_Forms-PCI_County_or_Town").val();
       $("#id_SCI_Forms-SCI_County_or_Town").val(selected_b);
        var district_region = $("#id_PCI_Forms-PCI_County_or_Town option:selected").text();
        //var district_region = $("#id_PCI_Forms-PCI_Parish option:selected").text();
        //alert(selected_region);
        _ajax_2_django_get_parishes_sub(district_region, "id_PCI_Forms-PCI_Parish");
        return false;
    });  
    
    /*Handling the secondary contact information*/
    $("#id_SCI_Forms-SCI_Region").change(function(){
        var selected_b  = $("#id_SCI_Forms-SCI_Region").val();
        //alert(selected_b);
        var selected_region = $("#id_SCI_Forms-SCI_Region option:selected").text();
        _ajax_2_django_sender(selected_region, "id_SCI_Forms-SCI_District");
        return false;
    });  
    
    $("#id_SCI_Forms-SCI_District").change(function(){
        var selected_b  = $("#id_SCI_Forms-SCI_District").val();
        //alert(selected_b);
        var selected_region = $("#id_SCI_Forms-SCI_District option:selected").text();
        _ajax_2_django_get_districts_sub(selected_region, "id_SCI_Forms-SCI_County_or_Town");
        return false;
    });  
    
    $("#id_SCI_Forms-SCI_County_or_Town").change(function(){
        var selected_b  = $("#id_SCI_Forms-SCI_County_or_Town").val();
        //alert(selected_b);
        var selected_region = $("#id_SCI_Forms-SCI_County_or_Town option:selected").text();
        _ajax_2_django_get_parishes_sub(selected_region, "id_SCI_Forms-SCI_Parish");
        return false;
    });

    //Dynamically set the value of id_SCI_Forms-SCI_Parish
    $("#id_PCI_Forms-PCI_Parish").change(function(){
        var selected_b  = $("#id_PCI_Forms-PCI_Parish").val();
        $("#id_SCI_Forms-SCI_Parish").val(selected_b);
        return false;
    });

    //Dynamically change id_PCI_Forms-PCI_Country_Code
    $("#id_PCI_Forms-PCI_Country_Code").change(function(){
        var selected_b  = $("#id_PCI_Forms-PCI_Country_Code").val();
        $("#id_SCI_Forms-SCI_Country_Code").val(selected_b);
        return false;
    });  
    
    //Dynamically change id_PCI_Forms-PCI_Country_Code
    $("#id_PCI_Forms-PCI_Flag_of_Ownership").change(function(){
        var selected_b  = $("#id_PCI_Forms-PCI_Flag_of_Ownership").val();
        $("#id_SCI_Forms-SCI_Flag_for_ownership").val(selected_b);
        return false;
    });  
    
    return false;
});


function _ajax_2_django_sender(selected_region, elementid){

    $.ajax({
        url:"/regionhandler/parseregiondistricts/",
        type:"get",
        data:{"region":selected_region},
        dataType:"json",
        async:true,
        
        success: function(results, status, xhr){
            var pci_district = document.getElementById(elementid);
            var sci_district = document.getElementById("id_SCI_Forms-SCI_District");
            //nullify the records
            pci_district.options.length=0;
            sci_district.options.length=0;
            
            for(var key in results){
                //console.log(key);
                pci_district.options.add(new Option(key, results[key]));
                sci_district.options.add(new Option(key, results[key]));
            }
        },
        
        failure: function(details){
            console.log("ERROG WA RECEIVED FAILURE");
            alert(details);
        }
    });
}

function _ajax_2_django_get_districts_sub(district_region, elementid){

    $.ajax({
        url:"/regionhandler/parseselectedistricts/",
        type:"get",
        data:{"district":district_region},
        dataType:"json",
        async:true,
        
        success: function(results, status, xhr){
            var pci_district = document.getElementById(elementid);
            var sci_district = document.getElementById("id_SCI_Forms-SCI_County_or_Town");
            //nullify the records
            pci_district.options.length=0;
            sci_district.options.length=0;
            
            for(var key in results){
                //console.log(key);
                pci_district.options.add(new Option(key, results[key]));
                sci_district.options.add(new Option(key, results[key]));
            }
        },
        
        failure: function(details){
            console.log("ERROG WA RECEIVED FAILURE");
            alert(details);
        }
    });
}

function _ajax_2_django_get_parishes_sub(district, elementid){

    $.ajax({
        url:"/regionhandler/getparishes/",
        type:"get",
        data:{"division":district},
        dataType:"json",
        async:true,
        
        success: function(results, status, xhr){
            var pci_district = document.getElementById(elementid);
            var sci_district = document.getElementById("id_SCI_Forms-SCI_Parish");
            
            //nullify the records
            pci_district.options.length=0;
            sci_district.options.length=0;
            
            for(var key in results){
                //console.log(key);
                pci_district.options.add(new Option(key, results[key]));
                sci_district.options.add(new Option(key, results[key]));
            }
        },
        
        failure: function(details){
            console.log("ERROG WA RECEIVED FAILURE");
            alert(details);
        }
    });
}
