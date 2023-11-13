import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QCoreApplication
import jdatetime

def get_persian_day_of_week():
    days = ["یک‌شنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه", "شنبه"]
    return days[jdatetime.date.today().weekday() - 1]

def get_persian_month_name():
    persian_months = [
        "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
        "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"
    ]

    current_month = jdatetime.date.today().month
    return persian_months[current_month - 1]

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        super(SystemTrayIcon, self).__init__(icon, parent)
        self.setToolTip("Shamsi time")

        # Right-click menu
        self.menu = QtWidgets.QMenu(parent)
        exit_action = self.menu.addAction("Exit")
        exit_action.triggered.connect(lambda: QCoreApplication.instance().quit())

        # Set the context menu for right-click
        self.setContextMenu(self.menu)

        # Connect the left-click action
        self.activated.connect(self.on_tray_icon_activated)

    def on_tray_icon_activated(self, reason):
        if reason == self.Trigger:
            self.show_notification()

    def show_notification(self):
        jd = jdatetime.date.today()

        title = f"{get_persian_day_of_week()} - {jd.day} {get_persian_month_name()}"
        body = f"{jd.year} - {jd.month} - {jd.day}"
        icon = QtGui.QIcon('icon.ico')
        duration = 4000

        self.showMessage(title, body, icon, duration)

def main():
    app = QtWidgets.QApplication(sys.argv)

    # Set the application name
    app.setApplicationName("Shamsi Time")

    # Ensure QApplication is quit properly when the script is stopped
    app.setQuitOnLastWindowClosed(False)

    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("icon.ico"), w)

    tray_icon.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
