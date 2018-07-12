#!/usr/bin/env python

from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from QtPyVCP.widgets.form_widgets.main_window import VCPMainWindow

# Setup logging
from QtPyVCP.utilities import logger
LOG = logger.getLogger('QtPyVCP.' + __name__)

from QtPyVCP.core import Status, Action, Prefs, Info
STATUS = Status()
ACTION = Action()
PREFS = Prefs()
INFO = Info()

import xyz_ui

class MainWindow(VCPMainWindow):
    def __init__(self, ui_file):
        super(MainWindow, self).__init__(ui_file=ui_file)
        # uic.loadUi(ui_file, self)

        # ui = xyz_ui.Ui_Form()
        # ui.setupUi(self)

        print "Hurray ", self

    #==========================================================================
    #  Add/Override methods and slots below to customize the main window
    #==========================================================================

    # This slot will be automatically connected to a menu item named 'Test'
    # created in QtDesigner.
    @pyqtSlot()
    def on_actionTest_triggered(self):
        print 'Test action triggered'
        # implement the action here
