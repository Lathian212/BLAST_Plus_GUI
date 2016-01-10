'''
Created on Jan 10, 2016

@author: lathian
'''
class CallBack_Handlers(object):
    def __init__(self):
        pass
        
    def loadHandler(self):
        """Handles load file button putting selected file into -query"""
        pass
    def saveHandler(self):
        """Handles save file button putting selected file into -out"""
        pass
    def blastnTypeHandler(self):
        """map the blastn_type IntVar to right set for the StringVar in the dictionary -task option """
        #print('self.blastn_type.get() = '+ str(self.blastn_type.get()))
        pass 
    def outputFmtHandler(self, row):
        print('Row inside outputSelected = ' + str(row))