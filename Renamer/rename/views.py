# -*- coding: utf-8 -*-
# rename/views.py

"""This module provides the Renamer main window."""

from PyQt5.QtWidgets import QWidget
from .ui.window import Ui_window

class Window(QWidget, Ui_window):
    def __init__(self):
        super().__init__()
        self._setupUI()

    def _setupUI(self):
        self.setupUi(self)