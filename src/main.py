import sys

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtCore import QObject, pyqtSignal

class Backend(QObject):

    def __init__(self):
        QObject.__init__(self)
    updated = pyqtSignal(str, arguments=['updater'])

QQuickWindow.setSceneGraphBackend('software')
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.load('./ui/main.qml')
back_end = Backend()
engine.rootObjects()[0].setProperty('backend', back_end)

sys.exit(app.exec())