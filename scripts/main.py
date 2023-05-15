"""
Главный модуль для запуска приложения. В нем конфигурируются все кнопки
и все текстовые поля.
"""
import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import matplotlib
import pandas as pd
import warnings

warnings.filterwarnings("ignore")
matplotlib.use('Qt5Agg')


def setup_combo_boxes():
    """
    Функция для конфигурации выпадающих меню
    """
    keys = ['popularity', 'acousticness', 'danceability',
            'energy', 'instrumentalness', 'key', 'liveness', 'loudness',
            'mode', 'speechiness', 'tempo',
            'valence']
    keys_without_quality = ['popularity', 'acousticness', 'danceability',
                            'energy', 'instrumentalness', 'liveness',
                            'loudness', 'speechiness', 'tempo',
                            'valence'
                            ]
    genres = {'Jazz', 'Folk', 'Hip-Hop', 'Reggaeton', 'Anime', 'Electronic', 'Blues', 'Rock', 'Rap',
              'Alternative', 'Classical', 'Pop', 'Soundtrack', 'A Capella', 'Indie',
              "Children's Music", 'Children’s Music', 'Country', 'Reggae', 'Comedy', 'Dance', 'R&B',
              'Ska', 'Soul', 'Opera', 'Movie', 'World'}

    ui.x_axis.addItems(
        keys
    )
    ui.y_axis.addItems(
        keys_without_quality
    )
    ui.hist_parameter.addItems(keys)
    ui.artist_parameter.addItems(keys_without_quality)

    ui.comboBoxTypes.addItems(["bar", "plot", "dot"])
    ui.comboBoxParameters_2.addItems(keys)
    ui.genre_2.addItems(genres)


def setup_listeners():
    """
    Функция для конфигурации 
    триггеров на кнопки и слайдеры
    """
    ui.horizontalSlider.valueChanged.connect(
        lambda: ui.label_9.setText("Max number of items: " +
                                   str(ui.horizontalSlider.value()))
    )
    ui.bins_slider.valueChanged.connect(
        lambda: ui.bins.setText("Bins: " + str(ui.bins_slider.value()))
    )
    ui.build_hist.clicked.connect(
        lambda: anlib.count_of_tracks(
            ui.hist_parameter.currentText(), ui.bins_slider.value(), data))
    ui.top_tracks_calculate.clicked.connect(
        lambda: calculate_top_tracks(
            ui.comboBoxParameters_2.currentText(), ui.horizontalSlider.value())
    )
    ui.correlation.clicked.connect(
        lambda: anlib.corr_matrix(data)
    )
    ui.popularity_plot.clicked.connect(
        lambda: anlib.artist_evolution(
            ui.artist_list.currentItem().text(),
            data, ui.artist_parameter.currentText())
    )
    ui.plot_by_parameter_build.clicked.connect(
        lambda: anlib.average(ui.x_axis.currentText(), ui.y_axis.currentText(),
                              data, ui.comboBoxTypes.currentText())
    )
    ui.polar_graph.clicked.connect(
        lambda: anlib.polar_graph_for_all(data)
    )
    ui.polar_track.clicked.connect(
        lambda: anlib.polar_graph_for_track(str(data["track_id"][ui.track_list.currentRow()]), data,
                                            str(data["track_name"][ui.track_list.currentRow()]))
    )
    ui.genre_evolution_2.clicked.connect(
        lambda: anlib.genre_evolution(ui.genre_2.currentText(), data)
    )


def calculate_top_tracks(key, count):
    """
    Функция выводящая в список топ треков
    """
    tracks = anlib.top_tracks(data, key, count, ui.dateEdit.date().year(),
                              ui.dateEdit_2.date().year(), ui.invert.isChecked())
    ui.listWidget_2.clear()
    for i in range(len(tracks)):
        current = tracks[i]
        ui.listWidget_2.addItem(
            current["track_name"] + " - " + current["artist_name"] + "("
            + current["genre"] + "," +
            str(current[key]) + ")")


def setup_lists():
    """
    Функция для конфигурации 
    списка с треками
    """
    ui.track_list.setCurrentRow(0)
    ui.track_list.addItems(data["track_name"].map(str))
    ui.track_list.currentRowChanged.connect(track_list_row_change)
    ui.artist_list.addItems(sorted(set(data["artist_name"])))
    ui.artist_list.currentRowChanged.connect(artist_list_row_change)
    ui.artist_list.setCurrentRow(0)
    ui.artist_parameter.currentTextChanged.connect(artist_list_row_change)


def artist_list_row_change():
    """
    Функция для обработки изменений 
    выделенного элемента из списка артистов
    """
    description = anlib.describe_artist(ui.artist_list.currentItem().text(),
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
    """
    Функция для обработки изменений 
    выделенного элемента из списка треков
    """
    ui.genre.setText(
        data["genre"][ui.track_list.currentRow()])
    ui.artist_name.setText(
        data["artist_name"][ui.track_list.currentRow()])
    ui.track_name.setText(
        data["track_name"][ui.track_list.currentRow()])
    ui.track_id.setText(
        data["track_id"][ui.track_list.currentRow()])
    ui.popularity.setText(
        str(data["popularity"][ui.track_list.currentRow()]))
    ui.acousticness.setText(
        str(data["acousticness"][ui.track_list.currentRow()]))
    ui.duration_ms.setText(
        str(data["duration_ms"][ui.track_list.currentRow()]))
    ui.energy.setText(
        str(data["energy"][ui.track_list.currentRow()]))
    ui.instrumentalness.setText(
        str(data["instrumentalness"][ui.track_list.currentRow()]))
    ui.key.setText(
        str(data["key"][ui.track_list.currentRow()]))
    ui.liveness.setText(
        str(data["liveness"][ui.track_list.currentRow()]))
    ui.loudness.setText(
        str(data["loudness"][ui.track_list.currentRow()]))
    ui.danceability.setText(
        str(data["danceability"][ui.track_list.currentRow()]))
    ui.mode.setText(
        str(data["mode"][ui.track_list.currentRow()]))
    ui.speechiness.setText(
        str(data["speechiness"][ui.track_list.currentRow()]))
    ui.tempo.setText(
        str(data["tempo"][ui.track_list.currentRow()]))
    ui.time_signature.setText(
        str(data["time_signature"][ui.track_list.currentRow()]))
    ui.valence.setText(
        str(data["valence"][ui.track_list.currentRow()]))


def read_data():
    """
    Функция для считывания базы данных
    """
    return pd.read_csv(os.path.dirname(__file__).replace("scripts", "data")
                       + "/SpotifyFeaturesLast.csv")


if __name__ == "__main__":
    sys.path.insert(0, "..")
    from library.ui.MainWindow import Ui_MainWindow
    import library.analysis.analysis_methods as anlib

    data = read_data()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon("../images/ic_launcher.png"))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    setup_combo_boxes()
    setup_lists()
    setup_listeners()
    sys.exit(app.exec_())
