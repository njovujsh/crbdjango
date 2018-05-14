/*
 * postselect.js
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
 * 
 * var selected_b  = $("#id_standard_forms-Fraud_Choice").val();
 */


//function handle_event(){/
$(document).ready(function(){
    
    $("#id_standard_forms-Category_Code").change(function(){
        var selected_b  = $("#id_standard_forms-Category_Code").val();
        //alert(selected_b);
        var more = $("#id_standard_forms-Category_Code option:selected").text();
        handle_ajax(more);
        return false;
    });  
    return false;
});

//}

//handle_event();


function request_data(data){
    console.log("Requesting data");
    $.ajax({
        url: "/fraudster/category/",
        type: "GET",
        data: {"fraudtype":data},
        dataType:'application/json',
        cache:'false',
        
        success: function(data){
            console.log("something");
            alert(data);
        },
        
        error:function(){
            alert("Error was round");
        },
        
    });
    return false;
};

function handle_ajax(data){
    $.ajax({
        url:"/fraudster/category/",
        type: "get",
        data: {"fraudtype":data},
        dataType:'json',
        async: 'true',
        
        success: function(json, status, xhr){
            //console.log("What is the problem with ajax");
            //alert(json);id_standard_forms-Sub_Category_Code
            var sub_select = document.getElementById("id_standard_forms-Sub_Category_Code");
            
            //empty
            sub_select.options.length=0;
            
            //console.log(json);
            for(var key in json){
                //console.log(key);
                sub_select.options.add(new Option(key, json[key]));
            }
            
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
