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


def setup_combo_boxes():
    keys = ['popularity', 'acousticness', 'danceability',
            'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo',
            'valence']
    ui.comboBoxParameters.addItems(
        keys
    )
    ui.comboBoxColors.addItems(["blue", "green", "red", "cyan", "magenta", "yellow", "black", "white"])
    ui.comboBoxType.addItems(["hist", "bar"])
    ui.comboBoxParameters_2.addItems(keys)


def setup_button_listeners():
    ui.horizontalSlider.valueChanged.connect(
        lambda: set_current_value(ui.horizontalSlider.value())
    )
    ui.plot_by_parameter_build.clicked.connect(
        lambda: open_plot_dialog(ui.comboBoxParameters.currentText(), ui.comboBoxColors.currentText(), "hist"))
    ui.top_tracks_calculate.clicked.connect(
        lambda: calculate_top_tracks(ui.comboBoxParameters_2.currentText(), ui.horizontalSlider.value())
    )


def set_current_value(value):
    ui.label_9.setText("Top number:" + str(value))


def calculate_top_tracks(key, count):
    tracks = top_tracks(key, count)
    ui.listWidget_2.clear()
    for i in range(len(tracks)):
        current = tracks[i]
        ui.listWidget_2.addItem(
            current["track_name"] + " - " + current["artist_name"] + "(" + current["genre"] + "," + str(current[
                                                                                                            key]) + ")")


def setup_track_list():
    ui.listWidget.addItems(data["track_name"])
    ui.listWidget.currentRowChanged.connect(handle_row_change)


def handle_row_change():
    ui.genre.setText(data["genre"][ui.listWidget.currentRow()])
    ui.artist_name.setText(data["artist_name"][ui.listWidget.currentRow()])
    ui.track_name.setText(data["track_name"][ui.listWidget.currentRow()])
    ui.track_id.setText(data["track_id"][ui.listWidget.currentRow()])
    ui.popularity.setText(str(data["popularity"][ui.listWidget.currentRow()]))
    ui.acousticness.setText(str(data["acousticness"][ui.listWidget.currentRow()]))
    ui.duration_ms.setText(str(data["duration_ms"][ui.listWidget.currentRow()]))
    ui.energy.setText(str(data["energy"][ui.listWidget.currentRow()]))
    ui.instrumentalness.setText(str(data["instrumentalness"][ui.listWidget.currentRow()]))
    ui.key.setText(str(data["key"][ui.listWidget.currentRow()]))
    ui.liveness.setText(str(data["liveness"][ui.listWidget.currentRow()]))
    ui.loudness.setText(str(data["loudness"][ui.listWidget.currentRow()]))
    ui.danceability.setText(str(data["danceability"][ui.listWidget.currentRow()]))
    ui.mode.setText(str(data["mode"][ui.listWidget.currentRow()]))
    ui.speechiness.setText(str(data["speechiness"][ui.listWidget.currentRow()]))
    ui.tempo.setText(str(data["tempo"][ui.listWidget.currentRow()]))
    ui.time_signature.setText(str(data["time_signature"][ui.listWidget.currentRow()]))
    ui.valence.setText(str(data["valence"][ui.listWidget.currentRow()]))


def read_data():
    return pd.read_csv(os.path.dirname(__file__).replace("scripts", "data") + "\SpotifyFeatures.csv")


if __name__ == "__main__":
    sys.path.insert(0, "..")
    from library.MainWindow import Ui_MainWindow
    from library.PlotDialog import PlotDialog
    from analysis.analysis_methods import top_tracks

    data = read_data()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    setup_combo_boxes()
    setup_track_list()
    setup_button_listeners()

    sys.exit(app.exec_())
