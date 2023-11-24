import sys
import os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QCoreApplication, QTimer
from shamsi_time_online import get_shamsi_time_info_online
from shamsi_time_offline import get_shamsi_time_info_offline

def main():
    app = QtWidgets.QApplication(sys.argv)

    # Set the application name
    app.setApplicationName("Shamsi Time")

    # Ensure QApplication is quit properly when the script is stopped
    app.setQuitOnLastWindowClosed(False)

    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("assets/app-icon.png"), w)

    tray_icon.show()
    sys.exit(app.exec_())

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        super(SystemTrayIcon, self).__init__(icon, parent)
        self.setToolTip("Shamsi time")

        # Right-click menu
        self.menu = QtWidgets.QMenu(parent)
        exit_action = self.menu.addAction("Exit")
        exit_action.triggered.connect(lambda: QCoreApplication.instance().quit())

        # Add a flag to track notification state
        self.notification_shown = False

        # Set the context menu for right-click
        self.setContextMenu(self.menu)

        # Connect the left-click action
        self.activated.connect(self.on_tray_icon_activated)

        # Connect the messageClicked signal to reset_notification_state
        self.messageClicked.connect(self.reset_notification_state)

        # Initialize a QTimer
        self.reset_timer = QTimer(self)
        self.reset_timer.timeout.connect(self.reset_notification_state)

    def on_tray_icon_activated(self, reason):
        if reason == self.Trigger:
            # Show notification only if it hasn't been shown before
            if not self.notification_shown:
                self.show_notification()
                self.notification_shown = True

    def show_notification(self):
        read_time_online = read_config_file("config.txt") == "on"

        shamsi_time_info = None
        if read_time_online:
            shamsi_time_info = get_shamsi_time_info_online()

        if not shamsi_time_info:
            shamsi_time_info = get_shamsi_time_info_offline()

        print(read_time_online)

        title, body, icon, duration = format_shamsi_time_info(shamsi_time_info)
        self.showMessage(title, body, icon, duration)

        # Start the timer to reset the flag after the notification duration
        self.reset_timer.start(duration)

    def reset_notification_state(self):
        # Reset the flag and stop the timer if it's running
        self.notification_shown = False
        if self.reset_timer.isActive():
            self.reset_timer.stop()

def read_config_file(file_path):
    default_setting = "off"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if "online=" in line:
                    return line.strip().split("=")[1]
                
    return default_setting

def format_shamsi_time_info(shamsi_time_info):
    year = shamsi_time_info["year"]
    month = shamsi_time_info["month"]
    day = shamsi_time_info["day"]
    name_of_the_month = shamsi_time_info["name_of_the_month"]
    name_of_the_day = shamsi_time_info["name_of_the_day"]

    occasion = shamsi_time_info.get("occasion", None)
    is_holiday = shamsi_time_info.get("is_holiday", None)

    title = f"{name_of_the_day} - {day} {name_of_the_month}"

    body = f"{year}/{month}/{day}"
    if occasion:
        holiday_message = "تعطیل رسمی - " if is_holiday else ""
        body = f"{body} - online\n\
            {holiday_message}{occasion}"
        
    icon = QtGui.QIcon(get_emoji_for_day(name_of_the_day))
    duration = 4000
        
    return title, body, icon, duration

def get_emoji_for_day(day_name):
    day_to_emoji_icon = {
        "یک‌شنبه": "assets/days-of-the-week/sunday.png",
        "دوشنبه": "assets/days-of-the-week/monday.png",
        "سه‌شنبه": "assets/days-of-the-week/tuesday.png",
        "چهارشنبه": "assets/days-of-the-week/wednesday.png",
        "پنج‌شنبه": "assets/days-of-the-week/thursday.png",
        "جمعه": "assets/days-of-the-week/friday.png",
        "شنبه": "assets/days-of-the-week/saturday.png"
    }

    return day_to_emoji_icon.get(day_name)

if __name__ == '__main__':
    main()
