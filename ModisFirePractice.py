#import os

#import numpy as np
#import numpy.ma as ma
#import matplotlib.pyplot as plt
#import geopandas as gpd
#import rasterio as rio
#import earthpy as et
#import earthpy.spatial as es
#from glob import glob

#plt.ion()

#os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))


import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.env.overwriteOutput = True
import os
import matplotlib.pyplot as plt
from statistics import mean 

fcs = r'C:\Users\jw\Desktop\code test\codeTest_Fire2017\fire2017_all_250over.shp'

fields= ['OBJECTID','Julian_Dat','ET_Mean','EVI_Mean','NDVI_Mean','LAI_Mean','PPT_Mean','Temp_Mean','Aspct_Mean','LFM_Mean']

tempSHP = r"C:\Users\jw\Desktop\code test\testOutput\temp.shp"


##ET_List = [f for f in os.listdir(r'D:\Fire data\ET Factor and fill value\output') if f.endswith('update.tif')]
##arcpy.env.workspace = r'D:\Fire data\ET Factor and fill value\output'
###loop trough the shape file 
##with arcpy.da.UpdateCursor(fcs, fields) as cursor:
##        for row in cursor:
##                expression = 'OBJECTID=' + str(row[0])  
##                #get the day of fire event
##                fireD = int(str(row[1][4:8]))
##                #get the year of fire event 
##                fireY = int(row[1][0:4])

##                print('The fire day is '+str(fireD))
##                print('The fire year is '+str(fireY))

##                ##create a temp mask to select with
##                arcpy.MakeFeatureLayer_management(fcs,'temp')
##                tempMask = arcpy.SelectLayerByAttribute_management('temp','NEW_SELECTION',expression)
##                arcpy.CopyFeatures_management(tempMask, tempSHP)
               
##                #tempRaster = "C:\\Users\\jw\\Desktop\\code test\\testOutput\\" + str(row[0]) + '.tif'
    
##                ##input the raster -->search raster by date join here
##                ##search the ET file folder 
##                tempET = []
##                for i in ET_List:  #loop through the ETfile list 
##                    fileDateStr = i[23:30] # when i =0: "2016353"     '2017001'
##                    #fileDateNum = int(fileDateStr) #2016353           '2017001'
##                    fileY = int(fileDateStr[0:4])#2016                '2017'
##                    fileD = int(fileDateStr[4:7])#353                 '1'
                     
##                ##get precondition period: 32 DAYS ahead of fire   
##                #no need to worry about leap year situation
                                     
##                    if fireD > 32:                                              
##                        day = fireD -32
##                        year = fireY
##                        #fireRange = str(year)+str(day)
##                        #print(timePeriod)
##                        #use file date comepare with timePeriod to get file fall into 32 range but 7 day(ET in this case) before fire date
##                        if fileD > day and fileD <fireD-7:
##                                print('This is the file within the range: ' + fileDateStr)
##                                tempET.append(i)



##                #if the fire day is less than 32 it will deal with the leap year situation 
##                    elif fireD < 32:
        
##                        if fireY == 2001 or 2005 or 2009 or 2013 or 2017:                     #if the day is less than 32 and it is the next year of a leap year
##                            rangeY = fireY -1                                                   #set the year back 1 year 
##                            rangeD  = 366 - (32-fireD)                                           #leap year 366 days 
##                            #fireRange=str(rangeY)+str(rangeD )                                     #get 32 day ahead of fire date and creat new julian date
##                        else:
##                           rangeY = fireY -1                                        
##                           rangeD = 365 - (32-fireD)                               
##                           #fireRange = str(rangeY)+str(rangeD )      
           
                                   
##                        if (fileY <= fireY) and (fileY >= rangeY):
##                    #files 
##                            if (fileY < fireY) and (fileY == rangeY):
##                                if fileD > rangeD:
##                                    print("this file is within the range, the file date is "+ fileDateStr)
##                                    tempET.append(i)
##                    #files that has the same year of fire                                               
##                            elif (fileY == fireY) and (fileY > rangeY):
##                                if fileD < fireD-7:
##                                    print("this file is within the range and has the same year number of the fire event, file date is "+ fileDateStr)
##                                    tempET.append(i)
##                print(tempET)
##                MeanValue = []
##                #loop through the selected ET raster layers 
##                for inRaster in tempET:

##                    #inRaster = r"C:\Users\jw\Desktop\code test\Indices for real\ET projected\MOD16A2.006_ET_500m_doy2016361_aid0001_Update.tif"

##                    ##extract by temp mask 
##                    #outExtractByMask = ExtractByMask(inRaster, tempSHP) 
##                    outExtractByMask = arcpy.Clip_management(inRaster,'#','#',tempSHP,'ClippingGeometry')
##                    print('working on '+ str(row[0]))
   
##                    #outExtractByMask.save(tempRaster)
##                    arcpy.CalculateStatistics_management(outExtractByMask)
                   
##                    ##what if more raster layer needed in this step
                    


##                    ##get the MEAN value
##                    try:
##                        IndexMeanResult = arcpy.GetRasterProperties_management(outExtractByMask,'MEAN')
                    
##                        MeanValue.append(float(IndexMeanResult.getOutput(0)))
                    
##                        print('mean value:' + str(mean(MeanValue)))
##                        row[2]=mean(MeanValue)
##                        cursor.updateRow(row)
##                    except:
##                        continue
                
                
##===================================================================================================================================================================

##EVI_List = [f for f in os.listdir(r'D:\Fire data\EVI Factor and fill value\output') if f.endswith('update.tif')]
##arcpy.env.workspace = r'D:\Fire data\EVI Factor and fill value\output'


###loop trough the shape file 
##with arcpy.da.UpdateCursor(fcs, fields) as cursor:
##        for row in cursor:
##                expression = 'OBJECTID=' + str(row[0])  
##                #get the day of fire event
##                fireD = int(str(row[1][4:8]))
##                #get the year of fire event 
##                fireY = int(row[1][0:4])

##                print('The fire day is '+str(fireD))
##                print('The fire year is '+str(fireY))

##                ##create a temp mask to select with
##                arcpy.MakeFeatureLayer_management(fcs,'temp')
##                tempMask = arcpy.SelectLayerByAttribute_management('temp','NEW_SELECTION',expression)
##                arcpy.CopyFeatures_management(tempMask, tempSHP)
               
##                #tempRaster = "C:\\Users\\jw\\Desktop\\code test\\testOutput\\" + str(row[0]) + '.tif'
    
##                ##input the raster -->search raster by date join here
##                ##search the ET file folder 
##                tempEVI = []
##                for i in EVI_List:  #loop through the ETfile list 
##                    fileDateStr = i[33:40] # when i =0: "2016353"     '2017001'
##                    #fileDateNum = int(fileDateStr) #2016353           '2017001'
##                    fileY = int(fileDateStr[0:4])#2016                '2017'
##                    fileD = int(fileDateStr[4:7])#353                 '1'
                     
##                ##get precondition period: 32 DAYS ahead of fire   
##                #no need to worry about leap year situation
                                     
##                    if fireD > 32:                                              
##                        day = fireD -32
##                        year = fireY
##                        #fireRange = str(year)+str(day)
##                        #print(timePeriod)
##                        #use file date comepare with timePeriod to get file fall into 32 range but 7 day(ET in this case) before fire date
##                        if fileD > day and fileD <fireD-15:
##                                print('This is the file within the range: ' + fileDateStr)
##                                tempEVI.append(i)



##                #if the fire day is less than 32 it will deal with the leap year situation 
##                    elif fireD < 32:
        
##                        if fireY == 2001 or 2005 or 2009 or 2013 or 2017:                     #if the day is less than 32 and it is the next year of a leap year
##                            rangeY = fireY -1                                                   #set the year back 1 year 
##                            rangeD  = 366 - (32-fireD)                                           #leap year 366 days 
##                            #fireRange=str(rangeY)+str(rangeD )                                     #get 32 day ahead of fire date and creat new julian date
##                        else:
##                           rangeY = fireY -1                                        
##                           rangeD = 365 - (32-fireD)                               
##                           #fireRange = str(rangeY)+str(rangeD )      
           
                                   
##                        if (fileY <= fireY) and (fileY >= rangeY):
##                    #files 
##                            if (fileY < fireY) and (fileY == rangeY):
##                                if fileD > rangeD:
##                                    print("this file is within the range, the file date is "+ fileDateStr)
##                                    tempEVI.append(i)
##                    #files that has the same year of fire                                               
##                            elif (fileY == fireY) and (fileY > rangeY):
##                                if fileD < fireD-15:
##                                    print("this file is within the range and has the same year number of the fire event, file date is "+ fileDateStr)
##                                    tempEVI.append(i)
##                print(tempEVI)
##                MeanValue = []
##                #loop through the selected ET raster layers 
##                for inRaster in tempEVI:

##                    #inRaster = r"C:\Users\jw\Desktop\code test\Indices for real\ET projected\MOD16A2.006_ET_500m_doy2016361_aid0001_Update.tif"

##                    ##extract by temp mask 
##                    #outExtractByMask = ExtractByMask(inRaster, tempSHP) 
##                    outClipMask = arcpy.Clip_management(inRaster,'#','#',tempSHP,'ClippingGeometry')
##                    print('working on '+ str(row[0]))
   
##                    #outExtractByMask.save(tempRaster)
##                    arcpy.CalculateStatistics_management(outClipMask)
                   
##                    ##what if more raster layer needed in this step
                    


##                    ##get the MEAN value
##                    try:
##                        IndexMeanResult = arcpy.GetRasterProperties_management(outClipMask,'MEAN')
                    
##                        MeanValue.append(float(IndexMeanResult.getOutput(0)))
                    
##                        print('mean value:' + str(mean(MeanValue)))
##                        row[3]=mean(MeanValue)
##                        cursor.updateRow(row)
##                    except:
##                        continue

####======================================================================================================================================================================

##NDVI_List = [f for f in os.listdir(r'D:\Fire data\NDVI Factor and fill value\output') if f.endswith('update.tif')]
##arcpy.env.workspace = r'D:\Fire data\NDVI Factor and fill value\output'


###loop trough the shape file 
##with arcpy.da.UpdateCursor(fcs, fields) as cursor:
##        for row in cursor:
##                expression = 'OBJECTID=' + str(row[0])  
##                #get the day of fire event
##                fireD = int(str(row[1][4:8]))
##                #get the year of fire event 
##                fireY = int(row[1][0:4])

##                print('The fire day is '+str(fireD))
##                print('The fire year is '+str(fireY))

##                ##create a temp mask to select with
##                arcpy.MakeFeatureLayer_management(fcs,'temp')
##                tempMask = arcpy.SelectLayerByAttribute_management('temp','NEW_SELECTION',expression)
##                arcpy.CopyFeatures_management(tempMask, tempSHP)
               
##                #tempRaster = "C:\\Users\\jw\\Desktop\\code test\\testOutput\\" + str(row[0]) + '.tif'
    
##                ##input the raster -->search raster by date join here
##                ##search the ET file folder 
##                tempNDVI = []
##                for i in NDVI_List:  #loop through the ETfile list 
##                    fileDateStr = i[34:41] # when i =0: "2016353"     '2017001'
##                    #fileDateNum = int(fileDateStr) #2016353           '2017001'
##                    fileY = int(fileDateStr[0:4])#2016                '2017'
##                    fileD = int(fileDateStr[4:7])#353                 '1'
                     
##                ##get precondition period: 32 DAYS ahead of fire   
##                #no need to worry about leap year situation
                                     
##                    if fireD > 32:                                              
##                        day = fireD -32
##                        year = fireY
##                        #fireRange = str(year)+str(day)
##                        #print(timePeriod)
##                        #use file date comepare with timePeriod to get file fall into 32 range but 7 day(ET in this case) before fire date
##                        if fileD > day and fileD <fireD-15:
##                                print('This is the file within the range: ' + fileDateStr)
##                                tempNDVI.append(i)



##                #if the fire day is less than 32 it will deal with the leap year situation 
##                    elif fireD < 32:
        
##                        if fireY == 2001 or 2005 or 2009 or 2013 or 2017:                     #if the day is less than 32 and it is the next year of a leap year
##                            rangeY = fireY -1                                                   #set the year back 1 year 
##                            rangeD  = 366 - (32-fireD)                                           #leap year 366 days 
##                            #fireRange=str(rangeY)+str(rangeD )                                     #get 32 day ahead of fire date and creat new julian date
##                        else:
##                           rangeY = fireY -1                                        
##                           rangeD = 365 - (32-fireD)                               
##                           #fireRange = str(rangeY)+str(rangeD )      
           
                                   
##                        if (fileY <= fireY) and (fileY >= rangeY):
##                    #files 
##                            if (fileY < fireY) and (fileY == rangeY):
##                                if fileD > rangeD:
##                                    print("this file is within the range, the file date is "+ fileDateStr)
##                                    tempNDVI.append(i)
##                    #files that has the same year of fire                                               
##                            elif (fileY == fireY) and (fileY > rangeY):
##                                if fileD < fireD-15:
##                                    print("this file is within the range and has the same year number of the fire event, file date is "+ fileDateStr)
##                                    tempNDVI.append(i)
##                print(tempNDVI)
##                MeanValue = []
##                #loop through the selected ET raster layers 
##                for inRaster in tempNDVI:

##                    #inRaster = r"C:\Users\jw\Desktop\code test\Indices for real\ET projected\MOD16A2.006_ET_500m_doy2016361_aid0001_Update.tif"

##                    ##extract by temp mask 
##                    #outExtractByMask = ExtractByMask(inRaster, tempSHP) 
##                    outClipMask = arcpy.Clip_management(inRaster,'#','#',tempSHP,'ClippingGeometry')
##                    print('working on '+ str(row[0]))
   
##                    #outExtractByMask.save(tempRaster)
##                    arcpy.CalculateStatistics_management(outClipMask)
                   
##                    ##what if more raster layer needed in this step
                    


##                    ##get the MEAN value
##                    try:
##                        IndexMeanResult = arcpy.GetRasterProperties_management(outClipMask,'MEAN')
                    
##                        MeanValue.append(float(IndexMeanResult.getOutput(0)))
                    
##                        print('mean value:' + str(mean(MeanValue)))
##                        row[4]=mean(MeanValue)
##                        cursor.updateRow(row)
##                    except:
##                        continue

##=================================================================================================================================================================

##LFM_List = [f for f in os.listdir(r'D:\Fire data\LFM') if f.endswith('LFM.tif')]
##arcpy.env.workspace = r'D:\Fire data\LFM'


###loop trough the shape file 
##with arcpy.da.UpdateCursor(fcs, fields) as cursor:
##        for row in cursor:
##                expression = 'OBJECTID=' + str(row[0])  
##                #get the day of fire event
##                fireD = int(str(row[1][4:8]))
##                #get the year of fire event 
##                fireY = int(row[1][0:4])

##                print('The fire day is '+str(fireD))
##                print('The fire year is '+str(fireY))

##                ##create a temp mask to select with
##                arcpy.MakeFeatureLayer_management(fcs,'temp')
##                tempMask = arcpy.SelectLayerByAttribute_management('temp','NEW_SELECTION',expression)
##                arcpy.CopyFeatures_management(tempMask, tempSHP)
               
##                #tempRaster = "C:\\Users\\jw\\Desktop\\code test\\testOutput\\" + str(row[0]) + '.tif'
    
##                ##input the raster -->search raster by date join here
##                ##search the ET file folder 
##                tempLFM = []
##                for i in LFM_List:  #loop through the ETfile list 
##                    fileDateStr = i[24:31] # when i =0: "2016353"     '2017001'
##                    #fileDateNum = int(fileDateStr) #2016353           '2017001'
##                    fileY = int(fileDateStr[0:4])#2016                '2017'
##                    fileD = int(fileDateStr[4:7])#353                 '1'
                     
##                ##get precondition period: 32 DAYS ahead of fire   
##                #no need to worry about leap year situation
                                     
##                    if fireD > 32:                                              
##                        day = fireD -32
##                        year = fireY
##                        #fireRange = str(year)+str(day)
##                        #print(timePeriod)
##                        #use file date comepare with timePeriod to get file fall into 32 range but 7 day(ET in this case) before fire date
##                        if fileD > day and fileD <fireD-7:
##                                print('This is the file within the range: ' + fileDateStr)
##                                tempLFM.append(i)



##                #if the fire day is less than 32 it will deal with the leap year situation 
##                    elif fireD < 32:
        
##                        if fireY == 2001 or 2005 or 2009 or 2013 or 2017:                     #if the day is less than 32 and it is the next year of a leap year
##                            rangeY = fireY -1                                                   #set the year back 1 year 
##                            rangeD  = 366 - (32-fireD)                                           #leap year 366 days 
##                            #fireRange=str(rangeY)+str(rangeD )                                     #get 32 day ahead of fire date and creat new julian date
##                        else:
##                           rangeY = fireY -1                                        
##                           rangeD = 365 - (32-fireD)                               
##                           #fireRange = str(rangeY)+str(rangeD )      
           
                                   
##                        if (fileY <= fireY) and (fileY >= rangeY):
##                    #files 
##                            if (fileY < fireY) and (fileY == rangeY):
##                                if fileD > rangeD:
##                                    print("this file is within the range, the file date is "+ fileDateStr)
##                                    tempLFM.append(i)
##                    #files that has the same year of fire                                               
##                            elif (fileY == fireY) and (fileY > rangeY):
##                                if fileD < fireD-7:
##                                    print("this file is within the range and has the same year number of the fire event, file date is "+ fileDateStr)
##                                    tempLFM.append(i)
##                print(tempLFM)
##                MeanValue = []
##                #loop through the selected ET raster layers 
##                for inRaster in tempLFM:

##                    #inRaster = r"C:\Users\jw\Desktop\code test\Indices for real\ET projected\MOD16A2.006_ET_500m_doy2016361_aid0001_Update.tif"

##                    ##extract by temp mask 
##                    #outExtractByMask = ExtractByMask(inRaster, tempSHP) 
##                    outClipMask = arcpy.Clip_management(inRaster,'#','#',tempSHP,'ClippingGeometry')
##                    print('working on '+ str(row[0]))
   
##                    #outExtractByMask.save(tempRaster)
##                    arcpy.CalculateStatistics_management(outClipMask)
                   
##                    ##what if more raster layer needed in this step
                    


##                    ##get the MEAN value
##                    try:
##                        IndexMeanResult = arcpy.GetRasterProperties_management(outClipMask,'MEAN')
                    
##                        MeanValue.append(float(IndexMeanResult.getOutput(0)))
                    
##                        print('mean value:' + str(mean(MeanValue)))
##                        row[9]=mean(MeanValue)
##                        cursor.updateRow(row)
##                    except:
##                        continue

####=======================================================================================================================================================================================

##Temp_list = [f for f in os.listdir(r'C:\Users\jw\Desktop\code test\Pricipitation2017\output') if f.endswith('asc.tif')]
##arcpy.env.workspace = r'D:\C:\Users\jw\Desktop\code test\Pricipitation2017\output'
##print(Temp_list[0][27:29])

###loop trough the shape file 
##with arcpy.da.UpdateCursor(fcs, fields) as cursor:
##        for row in cursor:
##                expression = 'OBJECTID=' + str(row[0])  
##                #get the day of fire event
##                fireD = int(str(row[1][4:8]))
##                #get the year of fire event 
##                fireY = int(row[1][0:4])

##                print('The fire day is '+str(fireD))
##                print('The fire year is '+str(fireY))

##                ##create a temp mask to select with
##                arcpy.MakeFeatureLayer_management(fcs,'temp')
##                tempMask = arcpy.SelectLayerByAttribute_management('temp','NEW_SELECTION',expression)
##                arcpy.CopyFeatures_management(tempMask, tempSHP)
               
##                #tempRaster = "C:\\Users\\jw\\Desktop\\code test\\testOutput\\" + str(row[0]) + '.tif'
    
##                ##input the raster -->search raster by date join here
##                ##search the ET file folder 
                
##                for i in Temp_list:  
##                    Month = int(i[27:29])
##                    if fireD> 0 and fireD <=31:
##                        inRaster = Temp_list[0]
##                        print('now is Jan')
##                        outClipMask = arcpy.Clip_management(inRaster,'#','#',tempSHP,'ClippingGeometry')
##                        print('working on '+ str(row[0]))
   
##                        #outExtractByMask.save(tempRaster)
##                        arcpy.CalculateStatistics_management(outClipMask)
                   
##                        ##what if more raster layer needed in this step
                    

##                        MeanValue = []
##                        ##get the MEAN value
##                        try:
##                            IndexMeanResult = arcpy.GetRasterProperties_management(outClipMask,'MEAN')
                    
##                            MeanValue.append(float(IndexMeanResult.getOutput(0)))
                    
##                            print('mean value:' + str(mean(MeanValue)))
##                            row[7]=mean(MeanValue)
##                            cursor.updateRow(row)
##                        except:
##                            continue


##                    elif fireD> 31 and int(fireD/30) == Month:
##                        inRaster = i
##                        print('now is using data from month: '+ str(Month))
                 


##                        #inRaster = r"C:\Users\jw\Desktop\code test\Indices for real\ET projected\MOD16A2.006_ET_500m_doy2016361_aid0001_Update.tif"

##                        ##extract by temp mask 
##                        #outExtractByMask = ExtractByMask(inRaster, tempSHP) 
##                        outClipMask = arcpy.Clip_management(inRaster,'#','#',tempSHP,'ClippingGeometry')
##                        print('working on '+ str(row[0]))
   
##                        #outExtractByMask.save(tempRaster)
##                        arcpy.CalculateStatistics_management(outClipMask)
                   
##                        ##what if more raster layer needed in this step
                    

##                        MeanValue = []
##                        ##get the MEAN value
##                        try:
##                            IndexMeanResult = arcpy.GetRasterProperties_management(outClipMask,'MEAN')
                    
##                            MeanValue.append(float(IndexMeanResult.getOutput(0)))
                    
##                            print('mean value:' + str(mean(MeanValue)))
##                            row[7]=mean(MeanValue)
##                            cursor.updateRow(row)
##                        except:
##                            continue


#####====================================================================================================================================================================================
##Aspect

arcpy.env.workspace = r'D:\Fire data\ca dem overall\output'


#loop trough the shape file 
with arcpy.da.UpdateCursor(fcs, fields) as cursor:
        for row in cursor:
                expression = 'OBJECTID=' + str(row[0])  
                #get the day of fire event
                fireD = int(str(row[1][4:8]))
                #get the year of fire event 
                fireY = int(row[1][0:4])

                print('The fire day is '+str(fireD))
                print('The fire year is '+str(fireY))

                ##create a temp mask to select with
                arcpy.MakeFeatureLayer_management(fcs,'temp')
                tempMask = arcpy.SelectLayerByAttribute_management('temp','NEW_SELECTION',expression)
                arcpy.CopyFeatures_management(tempMask, tempSHP)
               

                MeanValue = []


                inRaster = "CA_ASPECT.tif"

                ##extract by temp mask 
                #outExtractByMask = ExtractByMask(inRaster, tempSHP) 
                outClipMask = arcpy.Clip_management(inRaster,'#','#',tempSHP,'ClippingGeometry')
                print('working on '+ str(row[0]))
   
                #outExtractByMask.save(tempRaster)
                arcpy.CalculateStatistics_management(outClipMask)
                   
                ##what if more raster layer needed in this step
                    


                ##get the MEAN value
                try:
                    IndexMeanResult = arcpy.GetRasterProperties_management(outClipMask,'MEAN')
                    
                    MeanValue.append(float(IndexMeanResult.getOutput(0)))
                    
                    print('mean value:' + str(mean(MeanValue)))
                    row[8]=mean(MeanValue)
                    cursor.updateRow(row)
                except:
                    continue