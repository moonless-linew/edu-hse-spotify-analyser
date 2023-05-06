from PyQt5 import QtWidgets
import matplotlib
import pandas as pd
import sys
import os


matplotlib.use('Qt5Agg')


def open_plot_dialog(param, color):
    dialog = PlotDialog()
    ax = dialog.figure.add_subplot(111)
    column = data[param]
    ax.hist(column, color=color, bins=ui.bins_slider.value())
    ax.set_title("Number of tracks per parameter")
    dialog.canvas.draw()
    dialog.exec_()


def setup_combo_boxes():
    keys = ['popularity', 'acousticness', 'danceability',
            'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo',
            'valence']
    ui.x_axis.addItems(
        keys
    )
    ui.y_axis.addItems(
        keys
    )
    ui.hist_parameter.addItems(keys)
    ui.artist_parameter.addItems(keys)

    ui.comboBoxTypes.addItems(["linear", "pie"])
    ui.comboBoxParameters_2.addItems(keys)


def setup_listeners():
    ui.horizontalSlider.valueChanged.connect(
        lambda: set_current_value_of_slider1(ui.horizontalSlider.value())
    )
    ui.bins_slider.valueChanged.connect(
        lambda: set_current_value_of_slider2(ui.bins_slider.value())
    )
    ui.build_hist.clicked.connect(
        lambda: open_plot_dialog(ui.hist_parameter.currentText(), "r"))
    ui.top_tracks_calculate.clicked.connect(
        lambda: calculate_top_tracks(ui.comboBoxParameters_2.currentText(), ui.horizontalSlider.value())
    )
    ui.correlation.clicked.connect(
        lambda: corr_matrix(data)
    )


def set_current_value_of_slider1(value):
    ui.label_9.setText("Max number of items: " + str(value))
def set_current_value_of_slider2(value):
    ui.bins.setText("Bins: " + str(value))

def calculate_top_tracks(key, count):
    tracks = top_tracks(key, count, data, reverse=ui.invert.isChecked())
    ui.listWidget_2.clear()
    for i in range(len(tracks)):
        current = tracks[i]
        ui.listWidget_2.addItem(
            current["track_name"] + " - " + current["artist_name"] + "(" + current["genre"] + "," + str(current[
                                                                                                            key]) + ")")


def setup_track_list():
    ui.track_list.addItems(data["track_name"])
    ui.track_list.currentRowChanged.connect(track_list_row_change)
    ui.artist_list.addItems(sorted(set(data["artist_name"])))
    ui.artist_list.currentRowChanged.connect(artist_list_row_change)
    ui.artist_list.setCurrentRow(0)
    ui.artist_parameter.currentTextChanged.connect(artist_list_row_change)


def artist_list_row_change():
    description = describe_artist(ui.artist_list.currentItem().text(),
                                  ui.artist_parameter.currentText(), data)
    if ui.artist_parameter.currentText() in ["key", "mode"]:
        ui.count.setText("")
        ui.mean.setText("")
        ui.std.setText("")
        ui.min.setText("")
        ui.per25.setText("")
        ui.per50.setText("")
        ui.per75.setText("")
        ui.max.setText("")
        ui.count_quality.setText(str(description["count"]))
        ui.unique.setText(str(description["unique"]))
        ui.top.setText(str(description["top"]))
        ui.freq.setText(str(description["freq"]))
    else:
        ui.count.setText(str(description["count"]))
        ui.mean.setText(str(description["mean"]))
        ui.std.setText(str(description["std"]))
        ui.min.setText(str(description["min"]))
        ui.per25.setText(str(description["25%"]))
        ui.per50.setText(str(description["50%"]))
        ui.per75.setText(str(description["75%"]))
        ui.max.setText(str(description["max"]))
        ui.count_quality.setText("")
        ui.unique.setText("")
        ui.top.setText("")
        ui.freq.setText("")


def track_list_row_change():
    ui.genre.setText(data["genre"][ui.track_list.currentRow()])
    ui.artist_name.setText(data["artist_name"][ui.track_list.currentRow()])
    ui.track_name.setText(data["track_name"][ui.track_list.currentRow()])
    ui.track_id.setText(data["track_id"][ui.track_list.currentRow()])
    ui.popularity.setText(str(data["popularity"][ui.track_list.currentRow()]))
    ui.acousticness.setText(str(data["acousticness"][ui.track_list.currentRow()]))
    ui.duration_ms.setText(str(data["duration_ms"][ui.track_list.currentRow()]))
    ui.energy.setText(str(data["energy"][ui.track_list.currentRow()]))
    ui.instrumentalness.setText(str(data["instrumentalness"][ui.track_list.currentRow()]))
    ui.key.setText(str(data["key"][ui.track_list.currentRow()]))
    ui.liveness.setText(str(data["liveness"][ui.track_list.currentRow()]))
    ui.loudness.setText(str(data["loudness"][ui.track_list.currentRow()]))
    ui.danceability.setText(str(data["danceability"][ui.track_list.currentRow()]))
    ui.mode.setText(str(data["mode"][ui.track_list.currentRow()]))
    ui.speechiness.setText(str(data["speechiness"][ui.track_list.currentRow()]))
    ui.tempo.setText(str(data["tempo"][ui.track_list.currentRow()]))
    ui.time_signature.setText(str(data["time_signature"][ui.track_list.currentRow()]))
    ui.valence.setText(str(data["valence"][ui.track_list.currentRow()]))


def read_data():
    return pd.read_csv(os.path.dirname(__file__).replace("scripts", "data") + "\SpotifyFeatures.csv")


if __name__ == "__main__":
    from PyQt5 import QtGui

    sys.path.insert(0, "..")
    from library.ui.MainWindow import Ui_MainWindow
    from library.ui.PlotDialog import PlotDialog
    from library.analysis.analysis_methods import *

    data = read_data()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon("../images/ic_launcher.png"))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    setup_combo_boxes()
    setup_track_list()
    setup_listeners()
    print(describe_artist("Ariana Grande", "key", data))
    sys.exit(app.exec_())
