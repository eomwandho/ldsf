"""
/***************************************************************************
 foss4gplugin
                                 A QGIS plugin
 LSDF Site randomization
                             -------------------
        begin                : 2012-04-08
        copyright            : (C) 2012 by Erick Opiyo
                                        Dr Tor Vagen
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
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "LDSF Site randomization tool"
def description():
    return "A plugin tool to generate random site for Land Degradation and Surveillance Framework"
def version():
    return "Version 0.3"
def icon():
    return "icons/icon.png"
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface):
    from ldsf_randsitegen import ldsf_randomsitegen
    return ldsf_randomsitegen(iface)
