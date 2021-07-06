import sys
from PyQt5.QtWidgets import *
from  PyQt5.QtCore  import*
from PyQt5.QtWebEngineWidgets import *
class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow,self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar=QToolBar()
        self.addToolBar(navbar)

        back_btm=QAction('Back',self)
        back_btm.triggered.connect(self.browser.back)
        navbar.addAction(back_btm)

        foeward_btm = QAction('Forward', self)
        foeward_btm.triggered.connect(self.browser.forward)
        navbar.addAction(foeward_btm)

        reload_btm = QAction('Refresh', self)
        reload_btm.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btm)

        home_btm = QAction('Home', self)
        home_btm.triggered.connect(self.navigate_home)
        navbar.addAction(home_btm)

        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)


        self.browser.urlChanged.connect(self.update_url)



    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,q):
        self.url_bar.setText(q.toString())





app=QApplication(sys.argv)
QApplication.setApplicationName("AI Browser")
window=Mainwindow()
app.exec_()