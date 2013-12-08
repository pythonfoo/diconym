#!/usr/bin/env python 
#-*- coding: utf-8 -*-
""" 
********** DICOnyM Core ***************

DICOnyM is a pythonfoo project based in
the pydicom lib:
    http://code.google.com/p/pydicom/

Project Home: 
    https://github.com/pythonfoo/diconym

Project Members:
    Mechtilde 
    Mikeadvo
    bison
    dodo
    dr1ll
    Oerb
"""
__author__ = "pyhtonfoo"
__copyright__ = "GPL 2013"
__license__ = "GPL v3 Plus" 

import os
import dicom


def isDicom(fullpath):                                                          
    isOk = True                                                                 
    try:                                                                        
        dcm = dicom.read_file(fullpath)                                          
    except Exception as ex:                                                     
        isOk = False                                                            
        # print fullpath                                                          
        # print ex                                                                
    return isOk   

def getFilesFromDir(dirPath):
    dirList = os.listdir(dirPath)                                               
    dcmFiles = {}                                           
    for fname in dirList:                                                       
        fPath = os.path.join(dirPath, fname)                                    
        if isDicom(fPath):
            dcmFiles[fPath] = fname
            #dcmFiles.append(fPath)                                              
    return dcmFiles  

def get_valuesfromImage(filename):                                              
    """                                                                         
    Read data element tag, value, VR, VM, description from DICOM file.          
    """                                                                         
    datalist = []                                                               
    def tagbased_callback(ds, data_element):                                    
        datalist.append((data_element.tag, data_element.value, data_element.VR, data_element.VM, data_element.description))
        
                                                                                
    # Load the current dicom file to get tag- and valuelist                     
    dataset = dicom.read_file(filename)                                         
                                                                                
    # write tag and value into datalist                                         
    dataset.walk(tagbased_callback)                                             
                                                                                
    return datalist 


def anonymize_byWhitelist(whitelist, filename, newfilename):                    
    """                                                                         
    """ 
    def tagbased_callback(ds, data_element):                                    
        """                                                                     
        Delete the value in non Whitelisted Tags                                
        TODO:                                                                   
        """                                                                     
        for whitelisttag in whitelist:                                          
            if data_element.tag != whitelisttag:                                
                data_element.value == ""                                        
                                                                                
    # Load the current dicom file to get tag- and valuelist                     
    dataset = dicom.read_file(filename)                                         
                                                                                
    # write delete nonwhitelist tag values into datalist                        
    dataset.walk(tagbased_callback)                                             
                                                                                
    # save file to newfilename                                                  
    dataset.save(newfilename)
