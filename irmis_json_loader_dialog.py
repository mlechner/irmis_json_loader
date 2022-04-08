# -*- coding: utf-8 -*-
"""
/***************************************************************************
 IrmisJsonLoaderDialog
                                 A QGIS plugin
 This plugin imports IRMIS Json files into QGIS
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-04-04
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Marco Lechner / Bundesamt für Strahlenschutz
        email                : mlechner@bfs.de
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

import os
from datetime import datetime

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'irmis_json_loader_dialog_base.ui'))

# https://iec.iaea.org/IRMIS/Visualisation/api/GetAggregatedMeasurements?eventId=255059cb-2c86-43b5-85cf-197694578554&startDate=2022-02-01%2000%3A00&endDate=2022-04-09%200%3A00&valueType=latest&minimumConfidentiality=2&measurementTypeId=1&measurementSubTypeId=1&surveyTypeIds=5&includeRoutineData=true&includeEmergencyData=true

now = datetime.now()
irmishtml_latest = '''
<a href="http:www.imis.bfs.de/geoportal/q=2022-04-08&amp;type=latest">
'''
irmishtml_latest += '''
  <span style=" text-decoration: underline; color:#0000ff;">http:www.imis.bfs.de/geoportal/?type=latestfoo&measureend=
'''
irmishtml_latest += datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
irmishtml_latest += '''
</span></a>
'''

irmishtml_max = '''
<a href="http:www.imis.bfs.de/geoportal/q=2022-04-08&amp;type=latest">
'''
irmishtml_max += '''
  <span style=" text-decoration: underline; color:#0000ff;">http:www.imis.bfs.de/geoportal/q=2022-04-08&amp;type=maxbar</span>
'''
irmishtml_max += '''
</a>
'''


class IrmisJsonLoaderDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(IrmisJsonLoaderDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.textBrowser_latest.setHtml(irmishtml_latest)
        self.textBrowser_max.setHtml(irmishtml_max)
        print("gui set up")