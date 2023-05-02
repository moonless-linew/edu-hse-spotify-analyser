# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(493, 697)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../PycharmProjects/pythonProject3/ic_launcher.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(2)
        self.label.setMidLineWidth(5)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 2, 1)
        self.comboBoxParameters = QtWidgets.QComboBox(self.frame)
        self.comboBoxParameters.setObjectName("comboBoxParameters")
        self.gridLayout.addWidget(self.comboBoxParameters, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.frame_2 = QtWidgets.QFrame(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBoxType = QtWidgets.QComboBox(self.frame_2)
        self.comboBoxType.setObjectName("comboBoxType")
        self.gridLayout_2.addWidget(self.comboBoxType, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.comboBoxColors = QtWidgets.QComboBox(self.frame_2)
        self.comboBoxColors.setObjectName("comboBoxColors")
        self.gridLayout_2.addWidget(self.comboBoxColors, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.line_3 = QtWidgets.QFrame(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.line_3.setFont(font)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.frame_3 = QtWidgets.QFrame(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tempo = QtWidgets.QLabel(self.frame_3)
        self.tempo.setText("")
        self.tempo.setObjectName("tempo")
        self.gridLayout_3.addWidget(self.tempo, 8, 3, 1, 1)
        self.time_signature = QtWidgets.QLabel(self.frame_3)
        self.time_signature.setText("")
        self.time_signature.setObjectName("time_signature")
        self.gridLayout_3.addWidget(self.time_signature, 9, 3, 1, 1)
        self.instrumentalness = QtWidgets.QLabel(self.frame_3)
        self.instrumentalness.setText("")
        self.instrumentalness.setObjectName("instrumentalness")
        self.gridLayout_3.addWidget(self.instrumentalness, 0, 3, 1, 1)
        self.valence = QtWidgets.QLabel(self.frame_3)
        self.valence.setText("")
        self.valence.setObjectName("valence")
        self.gridLayout_3.addWidget(self.valence, 10, 3, 1, 1)
        self.duration_ms = QtWidgets.QLabel(self.frame_3)
        self.duration_ms.setText("")
        self.duration_ms.setObjectName("duration_ms")
        self.gridLayout_3.addWidget(self.duration_ms, 9, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 2, 2, 1, 1)
        self.mode = QtWidgets.QLabel(self.frame_3)
        self.mode.setText("")
        self.mode.setObjectName("mode")
        self.gridLayout_3.addWidget(self.mode, 6, 3, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.gridLayout_3.addWidget(self.label_33, 10, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.gridLayout_3.addWidget(self.label_30, 7, 2, 1, 1)
        self.artist_name = QtWidgets.QLabel(self.frame_3)
        self.artist_name.setText("")
        self.artist_name.setObjectName("artist_name")
        self.gridLayout_3.addWidget(self.artist_name, 1, 1, 1, 1)
        self.popularity = QtWidgets.QLabel(self.frame_3)
        self.popularity.setText("")
        self.popularity.setObjectName("popularity")
        self.gridLayout_3.addWidget(self.popularity, 6, 1, 1, 1)
        self.energy = QtWidgets.QLabel(self.frame_3)
        self.energy.setText("")
        self.energy.setObjectName("energy")
        self.gridLayout_3.addWidget(self.energy, 10, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 5, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.danceability = QtWidgets.QLabel(self.frame_3)
        self.danceability.setText("")
        self.danceability.setObjectName("danceability")
        self.gridLayout_3.addWidget(self.danceability, 8, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 10, 0, 1, 1)
        self.loudness = QtWidgets.QLabel(self.frame_3)
        self.loudness.setText("")
        self.loudness.setObjectName("loudness")
        self.gridLayout_3.addWidget(self.loudness, 5, 3, 1, 1)
        self.liveness = QtWidgets.QLabel(self.frame_3)
        self.liveness.setText("")
        self.liveness.setObjectName("liveness")
        self.gridLayout_3.addWidget(self.liveness, 2, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.gridLayout_3.addWidget(self.label_29, 6, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 7, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.gridLayout_3.addWidget(self.label_32, 9, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 8, 0, 1, 1)
        self.genre = QtWidgets.QLabel(self.frame_3)
        self.genre.setText("")
        self.genre.setObjectName("genre")
        self.gridLayout_3.addWidget(self.genre, 0, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 5, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 6, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout_3.addWidget(self.label_31, 8, 2, 1, 1)
        self.track_name = QtWidgets.QLabel(self.frame_3)
        self.track_name.setText("")
        self.track_name.setObjectName("track_name")
        self.gridLayout_3.addWidget(self.track_name, 2, 1, 1, 1)
        self.speechiness = QtWidgets.QLabel(self.frame_3)
        self.speechiness.setText("")
        self.speechiness.setObjectName("speechiness")
        self.gridLayout_3.addWidget(self.speechiness, 7, 3, 1, 1)
        self.track_id = QtWidgets.QLabel(self.frame_3)
        self.track_id.setText("")
        self.track_id.setObjectName("track_id")
        self.gridLayout_3.addWidget(self.track_id, 5, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout_3.addWidget(self.label_26, 1, 2, 1, 1)
        self.acousticness = QtWidgets.QLabel(self.frame_3)
        self.acousticness.setText("")
        self.acousticness.setObjectName("acousticness")
        self.gridLayout_3.addWidget(self.acousticness, 7, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 9, 0, 1, 1)
        self.key = QtWidgets.QLabel(self.frame_3)
        self.key.setText("")
        self.key.setObjectName("key")
        self.gridLayout_3.addWidget(self.key, 1, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spotify Dataset Analysis App"))
        self.label.setText(_translate("MainWindow", "Spotify Dataset Analysis"))
        self.label_2.setText(_translate("MainWindow", "Musical parameter"))
        self.label_5.setText(_translate("MainWindow", "Diagram type"))
        self.label_6.setText(_translate("MainWindow", "Diagram color"))
        self.pushButton.setText(_translate("MainWindow", "Build plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Plot via parameter"))
        self.label_3.setText(_translate("MainWindow", "Tracks from datasource"))
        self.label_27.setText(_translate("MainWindow", "liveness:"))
        self.label_33.setText(_translate("MainWindow", "valence:"))
        self.label_4.setText(_translate("MainWindow", "genre:"))
        self.label_30.setText(_translate("MainWindow", "speechiness:"))
        self.label_12.setText(_translate("MainWindow", "track_id:"))
        self.label_8.setText(_translate("MainWindow", "artist_name:"))
        self.label_18.setText(_translate("MainWindow", "energy:"))
        self.label_10.setText(_translate("MainWindow", "track_name:"))
        self.label_29.setText(_translate("MainWindow", "mode:"))
        self.label_15.setText(_translate("MainWindow", "acousticness:"))
        self.label_32.setText(_translate("MainWindow", "time_signature:"))
        self.label_16.setText(_translate("MainWindow", "danceability:"))
        self.label_28.setText(_translate("MainWindow", "loudness:"))
        self.label_14.setText(_translate("MainWindow", "popularity:"))
        self.label_31.setText(_translate("MainWindow", "tempo:"))
        self.label_26.setText(_translate("MainWindow", "key:"))
        self.label_17.setText(_translate("MainWindow", "duration_ms:"))
        self.label_24.setText(_translate("MainWindow", "instrumentalness:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Track analysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Preferences"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
