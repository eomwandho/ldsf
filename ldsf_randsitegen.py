"""
/***************************************************************************
 Point Cluster Tool
 V 0.0.1
                                 A QGIS plugin
 A simple example plugin to load shapefiles
                              -------------------
        begin                : 2012-04-08
        copyright            : (C) 2012 by Erick Opiyo
                                           Dr. Tor Vagen
                                           ICRAF GeoScienceLab
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import os.path, sys

sys.path.append( os.path.abspath( os.path.dirname( __file__)) )
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
import pp_randpoints, txt_randpoints, ext_randpoints

class ldsf_randomsitegen:
    def __init__(self, iface):
        self.iface = iface
        
    def initGui(self):
        icon = QIcon(os.path.dirname(__file__) + "/icons/pp_icon.png")
        self.pp_gen = QAction(icon,"Load Point or Polygon Shapefile", self.iface.mainWindow())
        self.pp_gen.setWhatsThis("Tool to generate random sites from either point or polygon shapefile")
        QObject.connect(self.pp_gen, SIGNAL("triggered()"), self.pp_run)
        
        icon = QIcon(os.path.dirname(__file__) + "/icons/csv_icon.png")
        self.txt_gen = QAction(icon,"Load Text or CSV file with points", self.iface.mainWindow())
        self.txt_gen.setWhatsThis("Tool to generate random sites from text or CSV points")
        QObject.connect(self.txt_gen, SIGNAL("triggered()"), self.txt_run)
        
        icon = QIcon(os.path.dirname(__file__) + "/icons/ext_icon.png")
        self.ext_gen = QAction(icon, "Select extent of region from canvas", self.iface.mainWindow())
        self.ext_gen.setWhatsThis("Tool to generate random sites from canvas extent")
        QObject.connect(self.ext_gen, SIGNAL("triggered()"), self.ext_run)
        
        icon = QIcon(os.path.dirname(__file__) + "/icons/about.png")
        self.about_gen = QAction(icon,"About LDSF", self.iface.mainWindow())
        self.about_gen.setWhatsThis("Description of Land degradation surveillance framework")
        QObject.connect(self.about_gen, SIGNAL("triggered()"), self.about)
        
        #Add toolbar button and menu item
        self.iface.addToolBarIcon(self.pp_gen)
        self.iface.addToolBarIcon(self.txt_gen)
        self.iface.addToolBarIcon(self.ext_gen)
        self.iface.addPluginToMenu("&LDSF Site Randomization tool", self.pp_gen)
        self.iface.addPluginToMenu("&LDSF Site Randomization tool", self.txt_gen)
        self.iface.addPluginToMenu("&LDSF Site Randomization tool", self.ext_gen)
        self.iface.addPluginToMenu("&LDSF Site Randomization tool", self.about_gen)
    
    def unload(self):
        self.iface.removePluginMenu("&LDSF Site Randomization tool", self.pp_gen)
        self.iface.removePluginMenu("&LDSF Site Randomization tool", self.txt_gen)
        self.iface.removePluginMenu("&LDSF Site Randomization tool", self.ext_gen)
        self.iface.removePluginMenu("&LDSF Site Randomization tool", self.about_gen)
        
        
        self.iface.removeToolBarIcon(self.pp_gen)
        self.iface.removeToolBarIcon(self.txt_gen)
        self.iface.removeToolBarIcon(self.ext_gen)
        
    def pp_run(self):
        d = pp_randpoints.Dialog(self.iface)
        d.exec_()
        
    def txt_run(self):
        d = txt_randpoints.Dialog(self.iface)
        d.exec_()
        
    def ext_run(self):
        d = ext_randpoints.Dialog(self.iface)
        d.exec_()
        
    def about(self):
        from ui_dlgabout import DlgAbout
        DlgAbout(self.iface.mainWindow()).exec_()
    
    
    
    
    
