# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'census_tool_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
# BELOW STUFF IS NEW AND WILL BE DELETED ON PYUIC COMMAND

from census import Census
import pandas as pd
import geopandas as gpd
import requests
from PyQt5.QtWidgets import QMessageBox
from qgis.core import QgsVectorLayer, QgsProject
import matplotlib.pyplot as plt
from PyQt5.QtGui import QPixmap
from qgis.PyQt.QtWidgets import QLabel
import tempfile
import os
import zipfile
import shutil

c = Census("bea1b2e41993540c7b3e493a56d71c7a437a41ad")

class PlotDialog(QtWidgets.QDialog):
    def __init__(self, pixmap, image_path):
        super().__init__()
        self.setWindowTitle("Plot")
        self.image_path = image_path
        
        # Create a label to display the image
        self.label = QtWidgets.QLabel(self)
        self.label.setPixmap(pixmap)
        
        # Create a button to download the image
        self.download_button = QtWidgets.QPushButton("Download", self)
        self.download_button.clicked.connect(lambda: self.download_image(image_path))
        
        # Create a button to close the dialog
        self.close_button = QtWidgets.QPushButton("Close", self)
        self.close_button.clicked.connect(self.close)
        
        # Create a vertical layout
        layout = QtWidgets.QVBoxLayout(self)
        
        # Add the download button, label, and close button to the layout
        layout.addWidget(self.label)
        layout.addWidget(self.download_button)
        layout.addWidget(self.close_button)
        
        self.setLayout(layout)
        
        # Set custom geometry (x, y, width, height)
        self.setGeometry(100, 100, 650, 600)
    
    def download_image(self, image_path):
        # Implement download logic here
        self.label.pixmap().save(self.image_path)

# ABOVE STUFF IS NEW AND WILL BE DELETED ON PYUIC COMMAND

class Ui_GetCensusDialogBase(object):
    def setupUi(self, GetCensusDialogBase):
        GetCensusDialogBase.setObjectName("GetCensusDialogBase")
        GetCensusDialogBase.resize(545, 230)
        self.button_box = QtWidgets.QDialogButtonBox(GetCensusDialogBase)
        self.button_box.setGeometry(QtCore.QRect(310, 190, 231, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.stateBox = QtWidgets.QComboBox(GetCensusDialogBase)
        self.stateBox.setGeometry(QtCore.QRect(210, 50, 181, 21))
        self.stateBox.setObjectName("stateBox")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.labelS = QtWidgets.QLabel(GetCensusDialogBase)
        self.labelS.setGeometry(QtCore.QRect(10, 50, 91, 16))
        self.labelS.setLineWidth(1)
        self.labelS.setObjectName("labelS")
        self.addGeo = QtWidgets.QPushButton(GetCensusDialogBase)
        self.addGeo.setGeometry(QtCore.QRect(400, 30, 120, 32))
        self.addGeo.setObjectName("addGeo")
        self.labelC = QtWidgets.QLabel(GetCensusDialogBase)
        self.labelC.setGeometry(QtCore.QRect(10, 80, 101, 16))
        self.labelC.setObjectName("labelC")
        self.labelG = QtWidgets.QLabel(GetCensusDialogBase)
        self.labelG.setGeometry(QtCore.QRect(10, 20, 161, 16))
        self.labelG.setObjectName("labelG")
        self.countyBox = QtWidgets.QComboBox(GetCensusDialogBase)
        self.countyBox.setGeometry(QtCore.QRect(210, 80, 181, 21))
        self.countyBox.setObjectName("countyBox")
        self.acs5Box = QtWidgets.QComboBox(GetCensusDialogBase)
        self.acs5Box.setGeometry(QtCore.QRect(210, 21, 181, 21))
        self.acs5Box.setObjectName("acs5Box")
        self.acs5Box.addItem("")
        self.acs5Box.addItem("")
        self.acs5Box.addItem("")
        self.acs5Box.addItem("")
        self.addData = QtWidgets.QPushButton(GetCensusDialogBase)
        self.addData.setGeometry(QtCore.QRect(400, 70, 120, 32))
        self.addData.setObjectName("addData")
        self.labelZ = QtWidgets.QLabel(GetCensusDialogBase)
        self.labelZ.setGeometry(QtCore.QRect(10, 110, 101, 16))
        self.labelZ.setObjectName("labelZ")
        self.zipcodeBox = QtWidgets.QComboBox(GetCensusDialogBase)
        self.zipcodeBox.setGeometry(QtCore.QRect(210, 110, 181, 21))
        self.zipcodeBox.setObjectName("zipcodeBox")
        self.labelCD = QtWidgets.QLabel(GetCensusDialogBase)
        self.labelCD.setGeometry(QtCore.QRect(10, 140, 181, 16))
        self.labelCD.setObjectName("labelCD")
        self.cdBox = QtWidgets.QComboBox(GetCensusDialogBase)
        self.cdBox.setGeometry(QtCore.QRect(210, 140, 181, 21))
        self.cdBox.setObjectName("cdBox")
        self.Clearbutton = QtWidgets.QPushButton(GetCensusDialogBase)
        self.Clearbutton.setGeometry(QtCore.QRect(400, 110, 120, 32))
        self.Clearbutton.setObjectName("Clearbutton")

        self.retranslateUi(GetCensusDialogBase)
        self.stateBox.setCurrentIndex(-1)
        self.acs5Box.setCurrentIndex(-1)
        self.button_box.accepted.connect(GetCensusDialogBase.accept) # type: ignore
        self.button_box.rejected.connect(GetCensusDialogBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(GetCensusDialogBase)
        # –––––––––––––––––––––––––––––––– NEW STUFF HERE ––––––––––––––––––––––––––––––––

        self.plot_dialog = None   # Initialize label as a class attribute
        self.save_path = None
        self.stateName = ''
        self.geographyName = ''
        self.countyName = ''
        self.zipcodeName = ''
        self.congName = ''
        self.addDataIndex = 0
        self.addGeo.clicked.connect(self.addShapeFile)

        ## what sets off the display dialog window, will change to a plot button on clicked like the addGeo.clicked above
        # self.plotButton.clicked.connect(self.displayPlot)
        self.addData.clicked.connect(self.addCensusVector)
        

        self.pluginPath = os.path.dirname(__file__)
        self.dataFilePath = os.path.join(self.pluginPath, 'data')

        self.fipsCSVPath = os.path.join(self.pluginPath, 'data', 'state-countyFIPS.csv')
        self.fipsDF = pd.read_csv(self.fipsCSVPath)

        self.cdPath = os.path.join(self.pluginPath, 'data', 'congDistrict.csv')
        self.cdDF = pd.read_csv(self.cdPath)

        self.regionData = {
            '01': 3,
            '02': 9,
            '04': 8,
            '05': 7,
            '06': 9,
            '08': 8,
            '09': 1,
            '10': 2,
            '11': 5,
            '12': 4,
            '13': 5,
            '15': 9,
            '16': 8,
            '17': 4,
            '18': 4,
            '19': 6,
            '20': 6,
            '21': 3,
            '22': 7,
            '23': 1,
            '24': 5,
            '25': 1,
            '26': 4,
            '27': 6,
            '28': 3,
            '29': 6,
            '30': 8,
            '31': 6,
            '32': 8,
            '33': 1,
            '34': 2,
            '35': 8,
            '36': 2,
            '37': 5,
            '38': 8,
            '39': 4,
            '40': 7,
            '41': 9,
            '42': 2,
            '44': 1,
            '45': 5,
            '46': 6,
            '47': 3,
            '48': 7,
            '49': 8,
            '50': 1,
            '51': 5,
            '53': 9,
            '54': 5,
            '55': 4,
            '56': 8,
        }
        self.regionDF = pd.DataFrame(self.regionData.items(), columns=['FIPS', 'Division'])

        # update counties and CD box on state change
        self.stateBox.currentIndexChanged.connect(self.updateCounties)
        self.stateBox.currentIndexChanged.connect(self.updateCD)
        self.Clearbutton.clicked.connect(self.clearBoxes)

    # Set off on add Data button
    def addCensusVector(self):
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        self.stateName = self.stateBox.currentText()
        self.geographyName = self.acs5Box.currentText()
        self.countyName = self.countyBox.currentText()
        self.congName = self.cdBox.currentText()
        self.addDataIndex = self.addDataIndex + 1

        if self.geographyName == 'State':
            # print('state geo!')
            shapefilePath = os.path.join(self.pluginPath, 'data', 'tl_2021_us_state','tl_2021_us_state.shp')

            if not os.path.exists(shapefilePath):
                QMessageBox.critical(None, "Error", "Shapefile not found in the data folder.")
                return

            stateGroup = self.fipsDF[self.fipsDF['State'] == self.stateName]
            stateFIP = stateGroup['FIPS'].astype(str).str[:-3].unique()[0]
            # print(stateFIP)

            fileS = gpd.read_file(shapefilePath)
            stateDF = fileS[fileS['STATEFP'] == stateFIP]
            print('stateDF', stateDF)
            temp_shapefile = f'/tmp/temp_shapefile_{self.addDataIndex}.shp'
            stateDF.to_file(temp_shapefile)
            layer = QgsVectorLayer(temp_shapefile, 'censusData'+ self.stateName +str(self.addDataIndex), 'ogr')
            if not layer.isValid():
                print("Layer failed to load!")
            else:
                QgsProject.instance().addMapLayer(layer)

        if self.geographyName == 'County':
            shapefilePath = os.path.join(self.pluginPath, 'data', 'tl_rd22_us_county','tl_rd22_us_county.shp')
            if not os.path.exists(shapefilePath):
                QMessageBox.critical(None, "Error", "Shapefile not found in the data folder.")
                return

            stateGroup = self.fipsDF[self.fipsDF['State'] == self.stateName]
            stateFIP = stateGroup['FIPS'].astype(str).str[:-3].unique()[0]
            print('state FIP', stateFIP)

            fileS = gpd.read_file(shapefilePath)
            # print('fileS', fileS)
            stateDF = fileS[fileS['STATEFP'] == stateFIP]
            # print('stateDF', stateDF)

            if(self.countyBox.currentText() == ''):
                countyDF = stateDF
            else:
                countyDF = stateDF[stateDF['NAMELSAD'] == self.countyName]

            print(countyDF)
            
            temp_shapefile = f'/tmp/temp_shapefile_{self.addDataIndex}.shp'
            countyDF.to_file(temp_shapefile)
            layer = QgsVectorLayer(temp_shapefile, 'censusData'+ self.countyName +str(self.addDataIndex), 'ogr')
            if not layer.isValid():
                print("Layer failed to load!")
            else:
                QgsProject.instance().addMapLayer(layer)
        
        if self.geographyName == 'Congressional District':
            # print('cd geo!')
            shapefilePath = os.path.join(self.pluginPath, 'data', '118thCD','USA_118th_Congressional_Districts.shp')

            if not os.path.exists(shapefilePath):
                QMessageBox.critical(None, "Error", "Shapefile not found in the data folder.")
                return

            stateGroup = self.fipsDF[self.fipsDF['State'] == self.stateName]
            stateFIP = stateGroup['FIPS'].astype(str).str[:-3].unique()[0]
            print(stateFIP)

            fileS = gpd.read_file(shapefilePath)
            print(fileS)
            stateDF = fileS[fileS['STFIPS'] == stateFIP]
            print('state', stateDF)
            
            if(self.cdBox.currentText() == ''):
                countyDF = stateDF
            else:
                countyDF = stateDF[stateDF['CDFIPS'] == self.congName]

            temp_shapefile = f'/tmp/temp_shapefile_{self.addDataIndex}.shp'
            countyDF.to_file(temp_shapefile)
            layer = QgsVectorLayer(temp_shapefile, 'censusData'+str(self.addDataIndex), 'ogr')
            if not layer.isValid():
                print("Layer failed to load!")
            else:
                QgsProject.instance().addMapLayer(layer)

    # goes off when plot button is selected
    # def displayPlot(self):
    #     print('displayPlot()')
    #     # print(self.fipsDF)
    #     # if self.save_path is None:
    #     #     QMessageBox.warning(None, "Error", "Shapefile path is not set")
    #     #     return

    #     self.stateName = self.stateBox.currentText()
    #     self.geographyName = self.acs5Box.currentText()
    #     self.countyName = self.countyBox.currentText()

    #     if self.geographyName == 'State':
    #         print('state geo!')
    #         # Define the path to the shapefile
    #         shapefilePath = os.path.join(self.pluginPath, 'data', 'tl_2021_us_state','tl_2021_us_state.shp')
            
    #         # Check if the shapefile exists
    #         if not os.path.exists(shapefilePath):
    #             QMessageBox.critical(None, "Error", "Shapefile not found in the data folder.")
    #             return

    #         variableList=['B08103_002E', 'B08103_003E', 'B08103_004E', 'B08103_005E', 'B08103_006E', 'B08103_007E']

    #         # variableList = ['B25034_002E','B25034_003E', 'B25034_004E', 'B25034_005E','B25034_006E', 
    #         #      'B25034_007E','B25034_008E', 'B25034_009E', 'B25034_010E', 'B25034_011E']

    #         stateGroup = self.fipsDF[self.fipsDF['State'] == self.stateName]
    #         stateFIP = stateGroup['FIPS'].astype(str).str[:-3].unique()[0]
    #         print(stateFIP)

    #         myData = c.acs5.state((variableList), stateFIP)
    #         myDF = pd.DataFrame(myData)
    #         myDF['region'] = self.regionData[stateFIP]
    #         fileS = gpd.read_file(shapefilePath)
    #         fileS['REGION'] = fileS['REGION'].astype('int64')
    #         # print(myDF)
    #         # print(fileS)
    #         # mergedDF = pd.merge(fileS, myDF, left_on=['REGION'], right_on=['region'], how='inner')
    #         # print(mergedDF)
    #         # mergedDF.plot(column="B08103_002E", legend='TRUE', cmap='Purples')
            
            
    #         myDF = myDF.drop(['state'], axis=1)
    #         myDF = myDF.dropna()
    #         print(myDF)
    #         plt.plot(myDF.values[0])
    #         plt.title('Add Title')

    #         print('here')
    #         temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    #         temp_file.close()  # Close the file so it can be opened by QPixmap
    #         plt.savefig(temp_file.name)
    #         plt.close()         
    #         pixmap = QPixmap(temp_file.name)
    #         # # Get the path to the Downloads directory
    #         downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    #         if self.plot_dialog is None:
    #             # Instantiate PlotDialog with the Downloads path
    #             self.plot_dialog = PlotDialog(pixmap, image_path=os.path.join(downloads_path, 'censusPlot.png'))
    #         else:
    #             self.plot_dialog.label.setPixmap(pixmap)

    #         self.plot_dialog.show()

    #     if self.geographyName == 'County':
    #         # Define the path to the shapefile
    #         shapefilePath = os.path.join(self.pluginPath, 'data', 'tl_2021_us_county','tl_2021_us_county.shp')
            
    #         # Check if the shapefile exists
    #         if not os.path.exists(shapefilePath):
    #             QMessageBox.critical(None, "Error", "Shapefile not found in the data folder.")
    #             return

    #         variableList=['B08103_002E', 'B08103_003E', 'B08103_004E', 
    #         'B08103_005E', 'B08103_006E', 'B08103_007E']

    #         stateGroup = self.fipsDF[self.fipsDF['State'] == self.stateName]
    #         stateFIP = stateGroup['FIPS'].astype(str).str[:-3].unique()[0]

    #         print('state FIP',stateFIP)
    #         countySelect = Census.ALL
    #         print(self.countyName)
    #         if len(self.countyName) > 1:
    #             stateFilter = self.fipsDF[self.fipsDF['State'] == self.stateName]
    #             countyGroup = stateFilter[stateFilter['County'] == self.countyName]
    #             print(countyGroup)
    #             countySelect = countyGroup['FIPS'].astype(str).str[-3:].unique()[0]
    #         print('County FIP', countySelect)

    #         myData = c.acs5.state_county((variableList), stateFIP, countySelect)
    #         myDF = pd.DataFrame(myData)
    #         fileS = gpd.read_file(shapefilePath)
    #         print(myDF)
    #         print(fileS)
    #         mergedDF = pd.merge(fileS, myDF,left_on=['STATEFP', 'COUNTYFP'], right_on=['state','county'], how='inner')
    #         print(mergedDF)
    #         mergedDF.plot(column="B08103_002E", legend='TRUE', cmap='Purples')
            
    #         temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    #         temp_file.close() 
    #         plt.savefig(temp_file.name)
    #         plt.close()
    #         pixmap = QPixmap(temp_file.name)
    #         downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    #         if self.plot_dialog is None:
    #             self.plot_dialog = PlotDialog(pixmap, image_path=os.path.join(downloads_path, 'censusPlot.png'))
    #         else:
    #             self.plot_dialog.label.setPixmap(pixmap)
    #         self.plot_dialog.show()

    #     if self.geographyName == 'Congressional District':
    #         self.stateName = self.stateBox.currentText()
    #         self.geographyName = self.acs5Box.currentText()
    #         # self.congName =

    #         shapefilePath = os.path.join(self.pluginPath, 'data', 'tl_2021_us_cd116','tl_2021_us_cd116.shp')
    #         if not os.path.exists(shapefilePath):
    #             QMessageBox.critical(None, "Error", "Shapefile not found in the data folder.")
    #             return

    #         variableList=['B08103_002E', 'B08103_003E', 'B08103_004E', 
    #         'B08103_005E', 'B08103_006E', 'B08103_007E']

    #         stateGroup = self.fipsDF[self.fipsDF['State'] == self.stateName]
    #         stateFIP = stateGroup['FIPS'].astype(str).str[:-3].unique()[0]
    #         countySelect = Census.ALL
    #         if len(self.countyName) > 1:
    #             stateFilter = self.fipsDF[self.fipsDF['State'] == self.stateName]
    #             countyGroup = stateFilter[stateFilter['County'] == self.countyName]
    #             countySelect = countyGroup['FIPS'].astype(str).str[-3:].unique()[0]

    #         # myData = c.acs5.state_congressional_district((variableList), stateFIP, self.congName)
    #         # myDF = pd.DataFrame(myData)
    #         # fileS = gpd.read_file(shapefilePath)
    #         # print(myDF)
    #         # print(fileS)
    #         # mergedDF = pd.merge(fileS, myDF,left_on=['STATEFP', 'COUNTYFP'], right_on=['state','county'], how='inner')
    #         # print(mergedDF)
    #         # mergedDF.plot(column="B08103_002E", legend='TRUE', cmap='Purples')
            
    #         temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    #         temp_file.close() 
    #         plt.savefig(temp_file.name)
    #         plt.close()
    #         pixmap = QPixmap(temp_file.name)
    #         downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    #         if self.plot_dialog is None:
    #             self.plot_dialog = PlotDialog(pixmap, image_path=os.path.join(downloads_path, 'censusPlot.png'))
    #         else:
    #             self.plot_dialog.label.setPixmap(pixmap)
    #         self.plot_dialog.show()

    #     if self.geographyName == 'Zipcode':
    #         # IMPLEMENT LOGIC FOR self.zipcodeName

    #         shapefilePath = os.path.join(self.pluginPath, 'data', 'tl_2021_us_zcta520','tl_2021_us_zcta520.shp')
    #         if not os.path.exists(shapefilePath):
    #             QMessageBox.critical(None, "Error", "Shapefile not found in the data folder.")
    #             return

    #         variableList=['B08103_002E', 'B08103_003E', 'B08103_004E', 
    #         'B08103_005E', 'B08103_006E', 'B08103_007E']

    #         stateGroup = self.fipsDF[self.fipsDF['State'] == self.stateName]
    #         stateFIP = stateGroup['FIPS'].astype(str).str[:-3].unique()[0]
    #         countySelect = Census.ALL
    #         if len(self.countyName) > 1:
    #             stateFilter = self.fipsDF[self.fipsDF['State'] == self.stateName]
    #             countyGroup = stateFilter[stateFilter['County'] == self.countyName]
    #             countySelect = countyGroup['FIPS'].astype(str).str[-3:].unique()[0]

    #         # myData = c.acs5.state_county((variableList), stateFIP, countySelect)
    #         # myDF = pd.DataFrame(myData)
    #         # fileS = gpd.read_file(shapefilePath)
    #         # print(myDF)
    #         # print(fileS)
    #         # mergedDF = pd.merge(fileS, myDF,left_on=['STATEFP', 'COUNTYFP'], right_on=['state','county'], how='inner')
    #         # print(mergedDF)
    #         # mergedDF.plot(column="B08103_002E", legend='TRUE', cmap='Purples')
            
    #         temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    #         temp_file.close() 
    #         plt.savefig(temp_file.name)
    #         plt.close()
    #         pixmap = QPixmap(temp_file.name)
    #         downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    #         if self.plot_dialog is None:
    #             self.plot_dialog = PlotDialog(pixmap, image_path=os.path.join(downloads_path, 'censusPlot.png'))
    #         else:
    #             self.plot_dialog.label.setPixmap(pixmap)
    #         self.plot_dialog.show()

    # adds counties to combobox dynamically
    def updateCounties(self):
        self.stateName = self.stateBox.currentText()
        self.geographyName = self.acs5Box.currentText()
        self.countyBox.clear()

        countyList = self.fipsDF[self.fipsDF['State'] == self.stateName]['County'].tolist()
        print(countyList)
        self.countyBox.addItem("")
        for county in countyList:
            self.countyBox.addItem(county)

    def updateZipcodes(self):
        pass

    # Adds CD numbers to selector dynamically
    def updateCD(self):
        self.stateName = self.stateBox.currentText()
        self.geographyName = self.acs5Box.currentText()
        self.cdBox.clear()

        cdList = self.cdDF[self.cdDF['State'] == self.stateName]['Districts'].tolist()
        print(cdList)
        self.cdBox.addItem("")
        for cd in cdList:
            print(cd)
            for value in range(cd):
                value += 1
                print(value)
                if(len(str(value)) == 1):
                    value = '0'+str(value)
                self.cdBox.addItem(str(value))

    # goes off when add geography button is pressed, adds one of four files
    def addShapeFile(self):
        print('addShapeFile()')

        self.stateName = self.stateBox.currentText()
        self.geographyName = self.acs5Box.currentText()

        if self.geographyName == 'State' or self.geographyName == 'County':
            print('state geo!')
            # Define the path to the shapefile
            shapefilePath = os.path.join(self.pluginPath, 'data', 'tl_rd22_us_' + str(self.geographyName.lower()), 'tl_rd22_us_'+ str(self.geographyName.lower()) +'.shp')
            
            # Check if the shapefile exists
            if not os.path.exists(shapefilePath):
                QMessageBox.critical(None, "Error", "Shapefile not found in the data folder.")
                return
            
            # Load the shapefile as a vector layer
            layer = QgsVectorLayer(shapefilePath,'US ' + self.geographyName + 's', "ogr")
            
            # Check if the layer is valid
            if not layer.isValid():
                QMessageBox.critical(None, "Error", "Failed to load shapefile.")
                return
            
            # Add the layer to the QGIS project
            QgsProject.instance().addMapLayer(layer)
        
        if self.geographyName == 'Zipcode':
            shapefilePath = os.path.join(self.pluginPath, 'data', 'tl_rd22_us_zcta520','tl_rd22_us_zcta520.shp')
            
            # Check if the shapefile exists
            if not os.path.exists(shapefilePath):
                QMessageBox.critical(None, "Error", "Shapefile not found in the data folder.")
                return
            
            # Load the shapefile as a vector layer
            layer = QgsVectorLayer(shapefilePath, "US Zipcodes", "ogr")
            
            # Check if the layer is valid
            if not layer.isValid():
                QMessageBox.critical(None, "Error", "Failed to load shapefile.")
                return
            
            # Add the layer to the QGIS project
            QgsProject.instance().addMapLayer(layer)

        if self.geographyName == 'Congressional District':
            # print('CD data plot')
            shapefilePath = os.path.join(self.pluginPath, 'data', '118thCD','USA_118th_Congressional_Districts.shp')
            
            # Check if the shapefile exists
            if not os.path.exists(shapefilePath):
                QMessageBox.critical(None, "Error", "Shapefile not found in the data folder.")
                return
            
            # Load the shapefile as a vector layer
            layer = QgsVectorLayer(shapefilePath, "US 118th Congressional District", "ogr")
            
            # Check if the layer is valid
            if not layer.isValid():
                QMessageBox.critical(None, "Error", "Failed to load shapefile.")
                return
            
            # Add the layer to the QGIS project
            QgsProject.instance().addMapLayer(layer)

    def clearBoxes(self):
        self.stateBox.setCurrentIndex(-1)
        self.acs5Box.setCurrentIndex(-1)
        self.countyBox.clear()
        self.zipcodeBox.clear()
        self.cdBox.clear()

    def retranslateUi(self, GetCensusDialogBase):
        _translate = QtCore.QCoreApplication.translate
        GetCensusDialogBase.setWindowTitle(_translate("GetCensusDialogBase", "Census Helper Plugin"))
        self.stateBox.setItemText(0, _translate("GetCensusDialogBase", "Alabama"))
        self.stateBox.setItemText(1, _translate("GetCensusDialogBase", "Alaska"))
        self.stateBox.setItemText(2, _translate("GetCensusDialogBase", "Arizona"))
        self.stateBox.setItemText(3, _translate("GetCensusDialogBase", "Arkansas"))
        self.stateBox.setItemText(4, _translate("GetCensusDialogBase", "California"))
        self.stateBox.setItemText(5, _translate("GetCensusDialogBase", "Colorado"))
        self.stateBox.setItemText(6, _translate("GetCensusDialogBase", "Connecticut"))
        self.stateBox.setItemText(7, _translate("GetCensusDialogBase", "Delaware"))
        self.stateBox.setItemText(8, _translate("GetCensusDialogBase", "District of Columbia"))
        self.stateBox.setItemText(9, _translate("GetCensusDialogBase", "Florida"))
        self.stateBox.setItemText(10, _translate("GetCensusDialogBase", "Georgia"))
        self.stateBox.setItemText(11, _translate("GetCensusDialogBase", "Hawaii"))
        self.stateBox.setItemText(12, _translate("GetCensusDialogBase", "Idaho"))
        self.stateBox.setItemText(13, _translate("GetCensusDialogBase", "Illinois"))
        self.stateBox.setItemText(14, _translate("GetCensusDialogBase", "Indiana"))
        self.stateBox.setItemText(15, _translate("GetCensusDialogBase", "Iowa"))
        self.stateBox.setItemText(16, _translate("GetCensusDialogBase", "Kansas"))
        self.stateBox.setItemText(17, _translate("GetCensusDialogBase", "Kentucky"))
        self.stateBox.setItemText(18, _translate("GetCensusDialogBase", "Louisiana"))
        self.stateBox.setItemText(19, _translate("GetCensusDialogBase", "Maine"))
        self.stateBox.setItemText(20, _translate("GetCensusDialogBase", "Maryland"))
        self.stateBox.setItemText(21, _translate("GetCensusDialogBase", "Massachusetts"))
        self.stateBox.setItemText(22, _translate("GetCensusDialogBase", "Michigan"))
        self.stateBox.setItemText(23, _translate("GetCensusDialogBase", "Minnesota"))
        self.stateBox.setItemText(24, _translate("GetCensusDialogBase", "Mississippi"))
        self.stateBox.setItemText(25, _translate("GetCensusDialogBase", "Missouri"))
        self.stateBox.setItemText(26, _translate("GetCensusDialogBase", "Montana"))
        self.stateBox.setItemText(27, _translate("GetCensusDialogBase", "Nebraska"))
        self.stateBox.setItemText(28, _translate("GetCensusDialogBase", "Nevada"))
        self.stateBox.setItemText(29, _translate("GetCensusDialogBase", "New Hampshire"))
        self.stateBox.setItemText(30, _translate("GetCensusDialogBase", "New Jersey"))
        self.stateBox.setItemText(31, _translate("GetCensusDialogBase", "New Mexico"))
        self.stateBox.setItemText(32, _translate("GetCensusDialogBase", "New York"))
        self.stateBox.setItemText(33, _translate("GetCensusDialogBase", "North Carolina"))
        self.stateBox.setItemText(34, _translate("GetCensusDialogBase", "North Dakota"))
        self.stateBox.setItemText(35, _translate("GetCensusDialogBase", "Ohio"))
        self.stateBox.setItemText(36, _translate("GetCensusDialogBase", "Oklahoma"))
        self.stateBox.setItemText(37, _translate("GetCensusDialogBase", "Oregon"))
        self.stateBox.setItemText(38, _translate("GetCensusDialogBase", "Pennsylvania"))
        self.stateBox.setItemText(39, _translate("GetCensusDialogBase", "Rhode Island"))
        self.stateBox.setItemText(40, _translate("GetCensusDialogBase", "South Carolina"))
        self.stateBox.setItemText(41, _translate("GetCensusDialogBase", "South Dakota"))
        self.stateBox.setItemText(42, _translate("GetCensusDialogBase", "Tennessee"))
        self.stateBox.setItemText(43, _translate("GetCensusDialogBase", "Texas"))
        self.stateBox.setItemText(44, _translate("GetCensusDialogBase", "Utah"))
        self.stateBox.setItemText(45, _translate("GetCensusDialogBase", "Vermont"))
        self.stateBox.setItemText(46, _translate("GetCensusDialogBase", "Virginia"))
        self.stateBox.setItemText(47, _translate("GetCensusDialogBase", "Washington"))
        self.stateBox.setItemText(48, _translate("GetCensusDialogBase", "West Virginia"))
        self.stateBox.setItemText(49, _translate("GetCensusDialogBase", "Wisconsin"))
        self.stateBox.setItemText(50, _translate("GetCensusDialogBase", "Wyoming"))
        self.labelS.setText(_translate("GetCensusDialogBase", "Select State:"))
        self.addGeo.setText(_translate("GetCensusDialogBase", "Add Geography"))
        self.labelC.setText(_translate("GetCensusDialogBase", "Select County:"))
        self.labelG.setText(_translate("GetCensusDialogBase", "Select ACS5 Geography:"))
        self.acs5Box.setItemText(0, _translate("GetCensusDialogBase", "County"))
        self.acs5Box.setItemText(1, _translate("GetCensusDialogBase", "Congressional District"))
        self.acs5Box.setItemText(2, _translate("GetCensusDialogBase", "State"))
        self.acs5Box.setItemText(3, _translate("GetCensusDialogBase", "Zipcode"))
        self.addData.setText(_translate("GetCensusDialogBase", "Add Data"))
        self.labelZ.setText(_translate("GetCensusDialogBase", "Select Zipcode:"))
        self.labelCD.setText(_translate("GetCensusDialogBase", "Select Congressional District:"))
        self.Clearbutton.setText(_translate("GetCensusDialogBase", "Clear Data "))
