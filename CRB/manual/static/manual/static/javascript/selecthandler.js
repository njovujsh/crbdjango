/*
 * selecthandler.js
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


function handle_select(){
    var selecthandler = document.getElementById("form-field-select-1");
    var selected_option = selecthandler.options[selecthandler.selectedIndex].text;
    alert(selected_option);
}

function handle_dropdown_by_select(dropdown){
    if(dropdown){
        var current_index = dropdown.selectedIndex
        var selected_value = dropdown.options[current_index].text;
        var request_url = "/value/get/"  + selected_value.toString() + "/";
        //var url = top.location.href = request_url;
        alert(build_request_url(request_url));
    }
    else{
        alert("Void");
    }
}


function build_request_url(request_urls){
    /*Dynamically build a url to perform a request on the server
     * end
    */
    var base_url = top.location.href;

    if(request_urls){
        //return base_url.toString() = request_urls.toString();
        base_url = request_urls;
        return base_url;
	}
    else{
        return -1; //base url required
    }


}

