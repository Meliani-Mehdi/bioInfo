# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_bioInfo(object):
    def setupUi(self, bioInfo):
        if not bioInfo.objectName():
            bioInfo.setObjectName(u"bioInfo")
        bioInfo.resize(1280, 720)
        bioInfo.setMinimumSize(QSize(1280, 720))
        bioInfo.setStyleSheet(u"/* ========================================\n"
"   BIOPYTHON GUI - BIOLOGY THEME STYLESHEET\n"
"   Color Palette: DNA Blues, Cell Greens, Lab Whites\n"
"   ======================================== */\n"
"\n"
"/* MAIN WINDOW & BASE STYLING */\n"
"QMainWindow {\n"
"    background-color: #f5f9f7;\n"
"    color: #2c3e36;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: #f5f9f7;\n"
"    color: #2c3e36;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"	border: 0px;\n"
"}\n"
"\n"
"/* PUSH BUTTONS - DNA Helix Inspired */\n"
"QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #4a9d7f, stop:1 #3d8269);\n"
"    color: white;\n"
"    border: 2px solid #2d6550;\n"
"    border-radius: 6px;\n"
"    padding: 8px 16px;\n"
"    font-weight: bold;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #5bb591, stop:1 #4a9d7"
                        "f);\n"
"    border: 2px solid #3d8269;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2d6550;\n"
"    border: 2px solid #1f4539;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #c8d6d1;\n"
"    color: #8a9a94;\n"
"    border: 2px solid #b0c0ba;\n"
"}\n"
"\n"
"/* PRIMARY ACTION BUTTON - Chlorophyll Green */\n"
"QPushButton#primaryButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #6cb86c, stop:1 #52a352);\n"
"    border: 2px solid #3d8c3d;\n"
"}\n"
"\n"
"QPushButton#primaryButton:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #7dcc7d, stop:1 #6cb86c);\n"
"}\n"
"\n"
"/* DANGER BUTTON - Caution Red */\n"
"QPushButton#dangerButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #d97676, stop:1 #c25c5c);\n"
"    border: 2px solid #a84545;\n"
"}\n"
"\n"
"QPushButton#dan"
                        "gerButton:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #e68a8a, stop:1 #d97676);\n"
"}\n"
"\n"
"/* LINE EDITS & TEXT INPUTS - Lab Equipment Style */\n"
"QLineEdit, QTextEdit, QPlainTextEdit {\n"
"    background-color: white;\n"
"    color: #2c3e36;\n"
"    border: 2px solid #b8d4c8;\n"
"    border-radius: 4px;\n"
"    padding: 6px;\n"
"    selection-background-color: #4a9d7f;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {\n"
"    border: 2px solid #4a9d7f;\n"
"    background-color: #fcfffe;\n"
"}\n"
"\n"
"QLineEdit:disabled, QTextEdit:disabled, QPlainTextEdit:disabled {\n"
"    background-color: #e8f0ec;\n"
"    color: #8a9a94;\n"
"}\n"
"\n"
"/* COMBO BOXES - Microscope Dropdown Style */\n"
"QComboBox {\n"
"    background-color: white;\n"
"    color: #2c3e36;\n"
"    border: 2px solid #b8d4c8;\n"
"    border-radius: 4px;\n"
"    padding: 6px 10px;\n"
"    min-width: 100px;\n"
""
                        "}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #4a9d7f;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #3d8269;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iOCIgdmlld0JveD0iMCAwIDEyIDgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTEgMUw2IDZMMTEgMSIgc3Ryb2tlPSIjM2Q4MjY5IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPjwvc3ZnPg==);\n"
"    width: 12px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    border: 2px solid #4a9d7f;\n"
"    selection-background-color: #d4ebe2;\n"
"    selection-color: #2c3e36;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* SPIN BOXES - Measurement Controls */\n"
"QSpinBox, QDoubleSpinBox {\n"
"    background-color: white;\n"
"    color: #2c3e36;\n"
"    border: 2px solid #b8d4c8;\n"
"    border-radius: 4px;\n"
"    padding: 4"
                        "px;\n"
"}\n"
"\n"
"QSpinBox:focus, QDoubleSpinBox:focus {\n"
"    border: 2px solid #4a9d7f;\n"
"}\n"
"\n"
"QSpinBox::up-button, QDoubleSpinBox::up-button {\n"
"    background-color: #e8f0ec;\n"
"    border-left: 1px solid #b8d4c8;\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QSpinBox::down-button, QDoubleSpinBox::down-button {\n"
"    background-color: #e8f0ec;\n"
"    border-left: 1px solid #b8d4c8;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QDoubleSpinBox::up-button:hover,\n"
"QSpinBox::down-button:hover, QDoubleSpinBox::down-button:hover {\n"
"    background-color: #d4ebe2;\n"
"}\n"
"\n"
"/* CHECKBOXES - Experiment Checklist Style */\n"
"QCheckBox {\n"
"    spacing: 8px;\n"
"    color: #2c3e36;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border: 2px solid #4a9d7f;\n"
"    border-radius: 3px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    border: 2px solid #3d8269;\n"
"    backg"
                        "round-color: #f0f9f5;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #4a9d7f;\n"
"    border: 2px solid #3d8269;\n"
"    image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iMTAiIHZpZXdCb3g9IjAgMCAxMiAxMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMSA1TDQgOEwxMSAxIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPjwvc3ZnPg==);\n"
"}\n"
"\n"
"/* RADIO BUTTONS - Sample Selection */\n"
"QRadioButton {\n"
"    spacing: 8px;\n"
"    color: #2c3e36;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border: 2px solid #4a9d7f;\n"
"    border-radius: 9px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #3d8269;\n"
"    background-color: #f0f9f5;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: white;\n"
"    border: 2px solid #3d8269;\n"
"}\n"
"\n"
"QRadioButton::i"
                        "ndicator:checked::after {\n"
"    content: \"\";\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"    background-color: #4a9d7f;\n"
"}\n"
"\n"
"/* SLIDERS - Gradient Controls */\n"
"QSlider::groove:horizontal {\n"
"    height: 6px;\n"
"    background-color: #d4ebe2;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: #4a9d7f;\n"
"    border: 2px solid #3d8269;\n"
"    width: 16px;\n"
"    margin: -6px 0;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: #5bb591;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    width: 6px;\n"
"    background-color: #d4ebe2;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background-color: #4a9d7f;\n"
"    border: 2px solid #3d8269;\n"
"    height: 16px;\n"
"    margin: 0 -6px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* PROGRESS BARS - DNA Replication Style */\n"
"QProgressBar {\n"
"    background-color: #e8f0ec;\n"
"    "
                        "border: 2px solid #b8d4c8;\n"
"    border-radius: 6px;\n"
"    text-align: center;\n"
"    color: #2c3e36;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                      stop:0 #4a9d7f, stop:0.5 #5bb591, stop:1 #4a9d7f);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* TAB WIDGET - Laboratory Notebook */\n"
"QTabWidget::pane {\n"
"    border: 2px solid #b8d4c8;\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"    top: -1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #e8f0ec;\n"
"    color: #2c3e36;\n"
"    border: 2px solid #b8d4c8;\n"
"    border-bottom: none;\n"
"    padding: 8px 20px;\n"
"    margin-right: 2px;\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: white;\n"
"    border-color: #4a9d7f;\n"
"    border-bottom: 2px solid white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTabBar:"
                        ":tab:hover:!selected {\n"
"    background-color: #d4ebe2;\n"
"}\n"
"\n"
"/* GROUP BOXES - Experiment Sections */\n"
"QGroupBox {\n"
"    background-color: white;\n"
"    border: 2px solid #b8d4c8;\n"
"    border-radius: 6px;\n"
"    margin-top: 12px;\n"
"    padding-top: 16px;\n"
"    font-weight: bold;\n"
"    color: #3d8269;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 12px;\n"
"    padding: 0 8px;\n"
"    background-color: white;\n"
"    color: #3d8269;\n"
"}\n"
"\n"
"/* SCROLL BARS - Microscope Slide Style */\n"
"QScrollBar:vertical {\n"
"    background-color: #e8f0ec;\n"
"    width: 14px;\n"
"    border-radius: 7px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #4a9d7f;\n"
"    border-radius: 6px;\n"
"    min-height: 30px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: #5bb591;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::s"
                        "ub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background-color: #e8f0ec;\n"
"    height: 14px;\n"
"    border-radius: 7px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #4a9d7f;\n"
"    border-radius: 6px;\n"
"    min-width: 30px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: #5bb591;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    width: 0px;\n"
"}\n"
"\n"
"/* LIST & TABLE VIEWS - Data Display */\n"
"QListView, QTreeView, QTableView {\n"
"    background-color: white;\n"
"    alternate-background-color: #f5f9f7;\n"
"    border: 2px solid #b8d4c8;\n"
"    border-radius: 4px;\n"
"    selection-background-color: #d4ebe2;\n"
"    selection-color: #2c3e36;\n"
"    outline: none;\n"
"}\n"
"\n"
"QListView::item:hover, QTreeView::item:hover, QTableView::item:hover {\n"
"    background-color: #e8f0ec;\n"
"}\n"
"\n"
"QTableView QHeaderView:"
                        ":section {\n"
"    background-color: #4a9d7f;\n"
"    color: white;\n"
"    padding: 6px;\n"
"    border: none;\n"
"    border-right: 1px solid #3d8269;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* MENU BAR - Lab Equipment Style */\n"
"QMenuBar {\n"
"    background-color: #3d8269;\n"
"    color: white;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: transparent;\n"
"    padding: 6px 12px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: #4a9d7f;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background-color: #2d6550;\n"
"}\n"
"\n"
"/* MENU - Dropdown Style */\n"
"QMenu {\n"
"    background-color: white;\n"
"    border: 2px solid #4a9d7f;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 8px 30px 8px 12px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #d4ebe2;\n"
"    color: #2c3e36;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
""
                        "    background-color: #b8d4c8;\n"
"    margin: 4px 8px;\n"
"}\n"
"\n"
"/* TOOLBAR - Lab Bench Style */\n"
"QToolBar {\n"
"    background-color: #e8f0ec;\n"
"    border: none;\n"
"    border-bottom: 2px solid #b8d4c8;\n"
"    spacing: 4px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    border: 2px solid transparent;\n"
"    border-radius: 4px;\n"
"    padding: 6px;\n"
"    color: #2c3e36;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #d4ebe2;\n"
"    border: 2px solid #4a9d7f;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #b8d4c8;\n"
"}\n"
"\n"
"/* STATUS BAR - Microscope Base */\n"
"QStatusBar {\n"
"    background-color: #3d8269;\n"
"    color: white;\n"
"    border-top: 2px solid #2d6550;\n"
"}\n"
"\n"
"/* TOOLTIPS - Info Labels */\n"
"QToolTip {\n"
"    background-color: #2c3e36;\n"
"    color: white;\n"
"    border: 2px solid #4a9d7f;\n"
"    border-radius: 4px;\n"
"    padding: 6px;\n"
"    opacity: 230;\n"
"}\n"
"\n"
"/* SP"
                        "LITTERS - Dividers */\n"
"QSplitter::handle {\n"
"    background-color: #b8d4c8;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 3px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 3px;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background-color: #4a9d7f;\n"
"}")
        self.verticalLayout = QVBoxLayout(bioInfo)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(bioInfo)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 64))
        self.frame.setStyleSheet(u"QWidget {\n"
"    background-color: #e8f0ec;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(100, 0))
        self.widget.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.widget)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(20)
        font.setBold(True)
        font.setStrikeOut(False)
        font.setStyleStrategy(QFont.PreferAntialias)
        font.setHintingPreference(QFont.PreferNoHinting)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.select_DNA = QComboBox(self.frame)
        self.select_DNA.setObjectName(u"select_DNA")
        self.select_DNA.setMinimumSize(QSize(124, 0))
        self.select_DNA.setMaximumSize(QSize(350, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        self.select_DNA.setFont(font1)

        self.horizontalLayout_2.addWidget(self.select_DNA)


        self.verticalLayout.addWidget(self.frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(bioInfo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(240, 0))
        self.frame_2.setStyleSheet(u"QWidget {\n"
"    background-color: #e8f0ec;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #4a9d7f, stop:1 #3d8269);\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.info_page = QPushButton(self.frame_2)
        self.info_page.setObjectName(u"info_page")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.info_page.setFont(font2)

        self.verticalLayout_5.addWidget(self.info_page)

        self.trans_page = QPushButton(self.frame_2)
        self.trans_page.setObjectName(u"trans_page")
        self.trans_page.setFont(font2)

        self.verticalLayout_5.addWidget(self.trans_page)

        self.motif_page = QPushButton(self.frame_2)
        self.motif_page.setObjectName(u"motif_page")
        self.motif_page.setFont(font2)

        self.verticalLayout_5.addWidget(self.motif_page)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font2)

        self.verticalLayout_5.addWidget(self.pushButton_4)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font2)

        self.verticalLayout_5.addWidget(self.pushButton)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font2)

        self.verticalLayout_5.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font2)

        self.verticalLayout_5.addWidget(self.pushButton_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_2)

        self.stackedWidget = QStackedWidget(bioInfo)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.enter_seq = QWidget()
        self.enter_seq.setObjectName(u"enter_seq")
        self.enter_seq.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.horizontalLayout_3 = QHBoxLayout(self.enter_seq)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.load_btn = QPushButton(self.enter_seq)
        self.load_btn.setObjectName(u"load_btn")
        self.load_btn.setMinimumSize(QSize(116, 64))
        self.load_btn.setMaximumSize(QSize(256, 64))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(18)
        font3.setBold(True)
        self.load_btn.setFont(font3)

        self.horizontalLayout_3.addWidget(self.load_btn)

        self.stackedWidget.addWidget(self.enter_seq)
        self.info_window = QWidget()
        self.info_window.setObjectName(u"info_window")
        self.verticalLayout_2 = QVBoxLayout(self.info_window)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.info_window)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 200))
        self.frame_3.setMaximumSize(QSize(16777215, 200))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.info1 = QFrame(self.frame_3)
        self.info1.setObjectName(u"info1")
        self.info1.setStyleSheet(u"background-color: rgb(191, 248, 195);\n"
"border-radius: 16px\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.info1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(12, 12, 12, 12)
        self.id_label = QLabel(self.info1)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.id_label)

        self.len_label = QLabel(self.info1)
        self.len_label.setObjectName(u"len_label")
        self.len_label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.len_label)

        self.type_label = QLabel(self.info1)
        self.type_label.setObjectName(u"type_label")
        self.type_label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.type_label)


        self.verticalLayout_3.addWidget(self.info1)

        self.info2 = QFrame(self.frame_3)
        self.info2.setObjectName(u"info2")
        self.info2.setStyleSheet(u"background-color: rgb(191, 248, 195);\n"
"border-radius: 16px\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.info2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(12, 12, 12, 12)
        self.gc_label = QLabel(self.info2)
        self.gc_label.setObjectName(u"gc_label")
        self.gc_label.setFont(font1)

        self.horizontalLayout_5.addWidget(self.gc_label)

        self.atgc_label = QLabel(self.info2)
        self.atgc_label.setObjectName(u"atgc_label")
        self.atgc_label.setFont(font1)

        self.horizontalLayout_5.addWidget(self.atgc_label)

        self.mw_label = QLabel(self.info2)
        self.mw_label.setObjectName(u"mw_label")
        self.mw_label.setFont(font1)

        self.horizontalLayout_5.addWidget(self.mw_label)


        self.verticalLayout_3.addWidget(self.info2)

        self.desc_label = QLabel(self.frame_3)
        self.desc_label.setObjectName(u"desc_label")
        self.desc_label.setFont(font1)

        self.verticalLayout_3.addWidget(self.desc_label)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.info_window)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.base_table = QTableWidget(self.frame_4)
        if (self.base_table.columnCount() < 4):
            self.base_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.base_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.base_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.base_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.base_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.base_table.rowCount() < 1):
            self.base_table.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.base_table.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFlags(Qt.ItemIsEnabled);
        self.base_table.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFlags(Qt.ItemIsEnabled);
        self.base_table.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFlags(Qt.ItemIsEnabled);
        self.base_table.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFlags(Qt.ItemIsEnabled);
        self.base_table.setItem(0, 3, __qtablewidgetitem8)
        self.base_table.setObjectName(u"base_table")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.base_table.sizePolicy().hasHeightForWidth())
        self.base_table.setSizePolicy(sizePolicy)
        self.base_table.setMinimumSize(QSize(500, 60))
        self.base_table.setMaximumSize(QSize(500, 63))
        self.base_table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.base_table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.base_table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

        self.verticalLayout_4.addWidget(self.base_table)

        self.scrollArea = QScrollArea(self.frame_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 50))
        self.scrollArea.setMaximumSize(QSize(16777215, 50))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 141, 50))
        self.horizontalLayout_6 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.sequence_view = QLabel(self.scrollAreaWidgetContents)
        self.sequence_view.setObjectName(u"sequence_view")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(18)
        self.sequence_view.setFont(font4)

        self.horizontalLayout_6.addWidget(self.sequence_view)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.info_window)
        self.trans_window = QWidget()
        self.trans_window.setObjectName(u"trans_window")
        self.verticalLayout_6 = QVBoxLayout(self.trans_window)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.holder_trans = QScrollArea(self.trans_window)
        self.holder_trans.setObjectName(u"holder_trans")
        self.holder_trans.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.holder_trans.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1014, 636))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lab_DNA = QLabel(self.scrollAreaWidgetContents_4)
        self.lab_DNA.setObjectName(u"lab_DNA")
        self.lab_DNA.setFont(font4)

        self.verticalLayout_7.addWidget(self.lab_DNA)

        self.scrollArea_3 = QScrollArea(self.scrollAreaWidgetContents_4)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy1)
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 996, 76))
        self.horizontalLayout_8 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.DNA_seq = QLabel(self.scrollAreaWidgetContents_3)
        self.DNA_seq.setObjectName(u"DNA_seq")
        sizePolicy.setHeightForWidth(self.DNA_seq.sizePolicy().hasHeightForWidth())
        self.DNA_seq.setSizePolicy(sizePolicy)
        self.DNA_seq.setFont(font4)

        self.horizontalLayout_8.addWidget(self.DNA_seq)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_7.addWidget(self.scrollArea_3)

        self.lab_rev = QLabel(self.scrollAreaWidgetContents_4)
        self.lab_rev.setObjectName(u"lab_rev")
        self.lab_rev.setFont(font4)

        self.verticalLayout_7.addWidget(self.lab_rev)

        self.scrollArea_2 = QScrollArea(self.scrollAreaWidgetContents_4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy1.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy1)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 996, 76))
        self.horizontalLayout_7 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.rev_comp = QLabel(self.scrollAreaWidgetContents_2)
        self.rev_comp.setObjectName(u"rev_comp")
        self.rev_comp.setFont(font4)

        self.horizontalLayout_7.addWidget(self.rev_comp)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_7.addWidget(self.scrollArea_2)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_6)

        self.scrollArea_5 = QScrollArea(self.scrollAreaWidgetContents_4)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        sizePolicy1.setHeightForWidth(self.scrollArea_5.sizePolicy().hasHeightForWidth())
        self.scrollArea_5.setSizePolicy(sizePolicy1)
        self.scrollArea_5.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 996, 76))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.trans_DNA_RNA = QLabel(self.scrollAreaWidgetContents_5)
        self.trans_DNA_RNA.setObjectName(u"trans_DNA_RNA")
        self.trans_DNA_RNA.setFont(font4)

        self.verticalLayout_8.addWidget(self.trans_DNA_RNA)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_7.addWidget(self.scrollArea_5)

        self.label_2 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_2)

        self.scrollArea_4 = QScrollArea(self.scrollAreaWidgetContents_4)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy2)
        self.scrollArea_4.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 996, 76))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollAreaWidgetContents_7.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_7.setSizePolicy(sizePolicy3)
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.trans_RNA_PRO = QLabel(self.scrollAreaWidgetContents_7)
        self.trans_RNA_PRO.setObjectName(u"trans_RNA_PRO")
        sizePolicy.setHeightForWidth(self.trans_RNA_PRO.sizePolicy().hasHeightForWidth())
        self.trans_RNA_PRO.setSizePolicy(sizePolicy)
        self.trans_RNA_PRO.setFont(font4)

        self.verticalLayout_9.addWidget(self.trans_RNA_PRO)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_7.addWidget(self.scrollArea_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.holder_trans.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_6.addWidget(self.holder_trans)

        self.stackedWidget.addWidget(self.trans_window)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(bioInfo)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(bioInfo)
    # setupUi

    def retranslateUi(self, bioInfo):
        bioInfo.setWindowTitle(QCoreApplication.translate("bioInfo", u"bioInfo", None))
        self.label.setText(QCoreApplication.translate("bioInfo", u"BIO PYTHON", None))
        self.info_page.setText(QCoreApplication.translate("bioInfo", u"Information", None))
        self.trans_page.setText(QCoreApplication.translate("bioInfo", u"Transform", None))
        self.motif_page.setText(QCoreApplication.translate("bioInfo", u"Motif Search", None))
        self.pushButton_4.setText(QCoreApplication.translate("bioInfo", u"Alignment", None))
        self.pushButton.setText(QCoreApplication.translate("bioInfo", u"Visualization", None))
        self.pushButton_5.setText(QCoreApplication.translate("bioInfo", u"NCBI Fetch", None))
        self.pushButton_6.setText(QCoreApplication.translate("bioInfo", u"Export", None))
        self.load_btn.setText(QCoreApplication.translate("bioInfo", u"Load Sequance", None))
        self.id_label.setText(QCoreApplication.translate("bioInfo", u"ID: -", None))
        self.len_label.setText(QCoreApplication.translate("bioInfo", u"Length: -", None))
        self.type_label.setText(QCoreApplication.translate("bioInfo", u"Type: -", None))
        self.gc_label.setText(QCoreApplication.translate("bioInfo", u"GC%: -", None))
        self.atgc_label.setText(QCoreApplication.translate("bioInfo", u"AT/GC Ratio: -", None))
        self.mw_label.setText(QCoreApplication.translate("bioInfo", u"Molecular Weight: -", None))
        self.desc_label.setText(QCoreApplication.translate("bioInfo", u"Description: -", None))
        ___qtablewidgetitem = self.base_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("bioInfo", u"A", None));
        ___qtablewidgetitem1 = self.base_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("bioInfo", u"T", None));
        ___qtablewidgetitem2 = self.base_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("bioInfo", u"C", None));
        ___qtablewidgetitem3 = self.base_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("bioInfo", u"G", None));
        ___qtablewidgetitem4 = self.base_table.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("bioInfo", u"    COUNT    ", None));

        __sortingEnabled = self.base_table.isSortingEnabled()
        self.base_table.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.base_table.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("bioInfo", u"-", None));
        ___qtablewidgetitem6 = self.base_table.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("bioInfo", u"-", None));
        ___qtablewidgetitem7 = self.base_table.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("bioInfo", u"-", None));
        ___qtablewidgetitem8 = self.base_table.item(0, 3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("bioInfo", u"-", None));
        self.base_table.setSortingEnabled(__sortingEnabled)

        self.sequence_view.setText(QCoreApplication.translate("bioInfo", u"    -   -   -   -", None))
        self.lab_DNA.setText(QCoreApplication.translate("bioInfo", u"DNA :", None))
        self.DNA_seq.setText(QCoreApplication.translate("bioInfo", u"- - - -", None))
        self.lab_rev.setText(QCoreApplication.translate("bioInfo", u"Reverse Complement :", None))
        self.rev_comp.setText(QCoreApplication.translate("bioInfo", u"- - - -", None))
        self.label_6.setText(QCoreApplication.translate("bioInfo", u"Transcription (DNA \u2192 RNA) :", None))
        self.trans_DNA_RNA.setText(QCoreApplication.translate("bioInfo", u"- - - -", None))
        self.label_2.setText(QCoreApplication.translate("bioInfo", u"Translation (RNA \u2192 Protein)", None))
        self.trans_RNA_PRO.setText(QCoreApplication.translate("bioInfo", u"- - - -", None))
    # retranslateUi

