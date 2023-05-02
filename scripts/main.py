from PyQt5 import QtWidgets
import matplotlib
import pandas as pd
import sys
import os
matplotlib.use('Qt5Agg')


def open_plot_dialog(param, color, type):
    dialog = PlotDialog()
    ax = dialog.figure.add_subplot(111)
    column = data[param]
    ax.hist(column, color=color)
    dialog.canvas.draw()
    dialog.exec_()


def setupComboBoxes():
    ui.comboBoxParameters.addItems(
        ['popularity', 'acousticness', 'danceability',
         'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo',
         'valence']
        )
    ui.comboBoxColors.addItems(["blue", "green", "red", "cyan", "magenta", "yellow", "black", "white"])
    ui.comboBoxType.addItems(["hist", "bar"])


def setupButtonListeners():
    ui.pushButton.clicked.connect(
        lambda: open_plot_dialog(ui.comboBoxParameters.currentText(), ui.comboBoxColors.currentText(), "hist"))


def readData():
    return pd.read_csv(os.path.dirname(__file__).replace("scripts", "data") + "\SpotifyFeatures.csv")


if __name__ == "__main__":
    sys.path.insert(0, "..")
    from library.MainWindow import Ui_MainWindow
    from library.PlotDialog import PlotDialog
    data = readData()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    setupComboBoxes()
    setupButtonListeners()

    sys.exit(app.exec_())
