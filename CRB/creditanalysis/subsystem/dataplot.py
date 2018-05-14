#  dataplot.py
#  
#  Copyright 2015 root <root@wangolo-OptiPlex-3020>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

import matplotlib.pyplot as plt 
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

class PlotValidatedRecords(object):
    def __init__(self, records=None, labels=None, explode=[0, 0.1, 0.1], title="Ploted Graph", figure=(14, 10)):
        """
        Method for ploting graphs.
        """
        self.records = records
        self.labels = labels 
        self.explode = explode
        self.figure = figure 
        self.xlabel = None 
        self.ylabel = None
        self.title = None 
        self.showlegend = True 
        self.save_path = None 
        self.name = None 
        
    def plot_pie(self, save=True, records=None, labels=None):
        if(records):
            self.set_record(record)
            
        if(labels):
            self.set_label(labels)
            
        try:
            plt.figure(figsize=self.get_figure())
            #print "Labels ", self.get_labels()
            #print "Records ", self.get_records()
            #print "Explode ", self.get_explode()
            plt.pie(self.get_records(), explode=self.get_explode(), labels=self.get_labels(), autopct='%0.1f%%', shadow=True)
            plt.title(self.get_title())
            plt.legend()
        except Exception as e:
            raise 
        else:
            if(save):
                print "Save path is ", self.get_savepath()
                plt.savefig(self.get_savepath())
                return True 
            else:
                return True
            
    def set_savepath(self, newpath):
        self.save_path = newpath
        
    def set_record(self, newrecords):
        self.records = newrecords
        
    def set_label(self, label):
        self.labels = label 
        
    def set_exlode(self, explod):
        self.explode = explod 
        
    def set_figure(self, figure):
        self.figure = figure 
        
    def set_title(self, title):
        self.title = title  
        
    def get_explode(self):
        return self.explode 
        
    def get_records(self):
        return self.records 
        
    def get_labels(self):
        return self.labels 
    
    def get_figure(self):
        return self.figure 
        
    def get_title(self):
        return self.title
        
    def get_savepath(self):
        return self.save_path 
        

#if __name__=="__main__":
    #P = PlotValidatedRecords()
    #P.set_label(["Total Number of Records", "Successful Validations", "Unsuccessful Validations"])
    #P.set_record([250, 50, 25])
    #P.set_savepath("/home/wangolo/cool.png")
    #P.set_title("Testing the validations of resultsA")
    #print "Labels are ", P.get_labels()
    #P.plot_pie()
