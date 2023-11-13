const path = require("path")
const { app, Tray, Menu, Notification } = require("electron")
const jalaali = require("jalaali-js")

app.whenReady().then(() => {
    if (process.platform === "win32") app.setAppUserModelId(app.name)

    const contextMenu = Menu.buildFromTemplate([{ label: "Exit", click: () => app.quit() }])

    const tray = new Tray(path.join(__dirname, "icon.ico"))
    tray.setToolTip("Shamsi time")
    tray.setContextMenu(contextMenu)
    tray.on("click", () => showShamsiDateNotification())
})

function showShamsiDateNotification() {
    const jd = jalaali.toJalaali(new Date())

    const NOTIFICATION_TITLE = `${getPersianDayOfWeek()} - ${jd.jd} ${getPersianMonthName(jd.jm)}`
    const NOTIFICATION_BODY = `${jd.jy} . ${jd.jm} . ${jd.jd}`
    const NOTIFICATION_ICON = path.join(__dirname, "icon.ico")

    new Notification({
        title: NOTIFICATION_TITLE,
        body: NOTIFICATION_BODY,
        icon: NOTIFICATION_ICON,
    }).show()
}

function getPersianDayOfWeek() {
    const days = ["یک‌شنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه", "شنبه"]

    return days[new Date().getDay()]
}

function getPersianMonthName(monthNumber) {
    const persianMonths = [
        "فروردین",
        "اردیبهشت",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن",
        "اسفند",
    ]

    return persianMonths[monthNumber - 1]
}

app.on("window-all-closed", () => {
    if (process.platform !== "darwin") app.quit()
})
