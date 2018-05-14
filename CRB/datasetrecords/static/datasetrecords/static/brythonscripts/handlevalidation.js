/*
 * handlevalidation.js
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
 * 
 */

$(document).ready(function(){
    $("#successvalidationdata").change(function(){
        var selected_dataset = $("#successvalidationdata").val();
        //console.log(selected_dataset);
        //alert(selected_dataset);
        send_selected_dataset(selected_dataset);
        //listen_date_select();
        return false;
    });
    //
    
    $("#validationdata").change(function(){
        var selected = $("#validationdata").val();
        //alert(selected);
        send_selected_data(selected);
    });
    return false;
});


function get_validation_url(){
    return "/validation/begindata/selected/";
}

/*function to handle and send to the server the selected dataset requiring validation*/
function send_selected_data(dataset){
    if(dataset){
        $.ajax({
            url:get_validation_url(),
            type:"get",
            data:{"validationsdataset":dataset},
            dataType:"json",
            sync:true,
            
            //begin handling success if dadta is returned
            success:function(json, status, xhr){
                //alert(json);
                //alert(json['Records to be validated']);
                document.getElementById("validataing").innerHTML = json['Records to be validated'];
                document.getElementById("recordcount").innerHTML = json["Count"];
                var enforcements = json["enforcements"];
                
                var sub_select = document.getElementById("validationrecords");
                sub_select.options.length=0;
                
                for (key in enforcements){
                    //console.log(enforcements[key]);
                    for ( more_key in enforcements[key]){
                        //console.log(more_key);
                        //console.log(enforcements[key][more_key][2]);
                        for (real in enforcements[key][more_key][2]){
                            //console.log(real);
                            sub_select.options.add(new Option(real, real));
                        }
                        //sub_select.options.add(new Option(more_key, more_key));
                    }
                }
            },
            
            failure:function(info){
                alert(info);
            }
        });
    };
};


function send_selected_dataset(dataset){
    if(dataset){
        $.ajax({
            url:"/validation/recentvalidation/successful/",
            type:"get",
            data:{"validationsdataset":dataset},
            dataType:"json",
            sync:true,
            
            //begin handling success if dadta is returned
            success:function(json, status, xhr){
                var records = json["recordsbydate"];
                var sub_select = document.getElementById("successvalidationdatabydate");
                sub_select.options.length=0;
                sub_select.options.add(new Option("Select Options below", "-------------------------------"));
                for (key in records){
                    //console.log(records[key]);
                    sub_select.options.add(new Option(records[key], key));
                }
                
                //listen_date_select();
            },
            
            failure:function(info){
                console.log(info);
            }
        });
    };
};

$(document).ready(function(){
    $("#successvalidationdatabydate").change(function(){
        var get_selection = $("#successvalidationdatabydate option:selected").val();
        var selected_dataset = $("#successvalidationdata").val();
        send_ajax_to_django(get_selection, selected_dataset);
    });
});

function send_ajax_to_django(date_selected, dataset_selected){
    $.ajax({
        url:"/validation/recentvalidation/getbyid/",
        type:"get",
        data:{"validationsdataset":dataset_selected, "validationdate":date_selected},
        dataType:"json",
        sync:true,
        
        success:function(json, status, xhr){
            console.log("Cool"); //#uniqueid
            document.getElementById("uniqueid").innerHTML = json['ID'];
            document.getElementById("rtype").innerHTML = json['rtype'];
            document.getElementById("vdate").innerHTML = json['date'];
            document.getElementById("picode").innerHTML = json['picode'];
            document.getElementById("trecords").innerHTML = json['total'];
            document.getElementById("svalidated").innerHTML = json['successful'];
            document.getElementById("failedrecords").innerHTML = json['failed'];
            document.getElementById("passedfields").innerHTML = json['pfield'];
            document.getElementById("failedfield").innerHTML = json['ffield'];
        },
        
        failure:function(info){
            console.log(info);
        }
    });
};
