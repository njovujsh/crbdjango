import csv
from django.http import HttpResponse
from django.utils.encoding import smart_str 

class ProcessCSV(object):
    """
    Object which will be used to process csv fileformat.
    """
    def __init__(self, filename, dialect, delimiter="|", response=None):
    
        self.response = HttpResponse(content_type="text/csv")
        self.filename = filename 
        self.delimiter = delimiter
        self.dialect = dialect
        self.data_id = "D"
        
        if(response == None):
            #create a csv  object 
            self.response['Content-Disposition'] = "attachment; filename=%s" % str(self.filename)
        else:
            self.response = response
        
        self.writer = csv.writer(self.response, quotechar='"', quoting=csv.QUOTE_ALL, delimiter=self.delimiter, dialect=csv.excel)
        
    def write_headers(self, headers):
        """
        Write the needed header files that describe.
        """
        if(headers):
            self.writer.writerow(headers)
            
    def write_row_header(self, rows):
        
        self.writer.writerow(rows)
           
    def write_row_data(self, data, rows):
        for d in data:
          
            self.writer.writerow([smart_str(unicode(d.id))
                                 ])
        return self.response 
        
    def set_data_id(self, newid):
        self.data_id = newid 
        
    def get_data_id(self):
        return self.data_id
