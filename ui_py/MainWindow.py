# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import tweepy_streamer

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(779, 600)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")
		self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
		self.tabWidget.setSizePolicy(sizePolicy)
		self.tabWidget.setObjectName("tabWidget")
		self.tabLiveTweets = QtWidgets.QWidget()
		self.tabLiveTweets.setObjectName("tabLiveTweets")
		self.gridLayout_2 = QtWidgets.QGridLayout(self.tabLiveTweets)
		self.gridLayout_2.setObjectName("gridLayout_2")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.progressBarStream = QtWidgets.QProgressBar(self.tabLiveTweets)
		self.progressBarStream.setProperty("value", 24)
		self.progressBarStream.setObjectName("progressBarStream")
		self.horizontalLayout.addWidget(self.progressBarStream)
		self.pushButtonStream = QtWidgets.QPushButton(self.tabLiveTweets)
		self.pushButtonStream.setObjectName("pushButtonStream")
		self.horizontalLayout.addWidget(self.pushButtonStream)
		self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 2)
		self.textEditNumTweets = QtWidgets.QTextEdit(self.tabLiveTweets)
		self.textEditNumTweets.setMaximumSize(QtCore.QSize(100, 30))
		self.textEditNumTweets.setObjectName("textEditNumTweets")
		self.gridLayout_2.addWidget(self.textEditNumTweets, 2, 1, 1, 1)
		self.textEditHashtags = QtWidgets.QTextEdit(self.tabLiveTweets)
		self.textEditHashtags.setMaximumSize(QtCore.QSize(16777215, 50))
		self.textEditHashtags.setObjectName("textEditHashtags")
		self.gridLayout_2.addWidget(self.textEditHashtags, 1, 1, 1, 1)
		self.labelHashtags = QtWidgets.QLabel(self.tabLiveTweets)
		self.labelHashtags.setObjectName("labelHashtags")
		self.gridLayout_2.addWidget(self.labelHashtags, 1, 0, 1, 1)
		self.labelNumTweets = QtWidgets.QLabel(self.tabLiveTweets)
		self.labelNumTweets.setObjectName("labelNumTweets")
		self.gridLayout_2.addWidget(self.labelNumTweets, 2, 0, 1, 1)
		self.frame = QtWidgets.QFrame(self.tabLiveTweets)
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.pushButtonDataframe = QtWidgets.QPushButton(self.frame)
		self.pushButtonDataframe.setObjectName("pushButtonDataframe")
		self.verticalLayout_2.addWidget(self.pushButtonDataframe)
		self.gridLayout_2.addWidget(self.frame, 4, 0, 1, 2)
		self.tabWidget.addTab(self.tabLiveTweets, "")
		self.tabUserTweets = QtWidgets.QWidget()
		self.tabUserTweets.setObjectName("tabUserTweets")
		self.tabWidget.addTab(self.tabUserTweets, "")
		self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 20))
		self.menubar.setObjectName("menubar")
		self.menuFile = QtWidgets.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.actionQuit = QtWidgets.QAction(MainWindow)
		self.actionQuit.setObjectName("actionQuit")
		self.actionQuit.setShortcut('Ctrl+Q')
		self.actionQuit.triggered.connect(self.close_application)
		
		self.menuFile.addAction(self.actionQuit)
		self.menubar.addAction(self.menuFile.menuAction())

		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		self.pushButtonStream.clicked.connect(self.push_button_stream)
		self.progressBarStream.setValue(0)

	def close_application(self):
		print("Exiting Application")
		sys.exit()

	def push_button_stream(self):
		tweets_filename = "new_tweets.json"
		hashtags = self.textEditHashtags.toPlainText()
		hashtags = hashtags.strip(', ')
		hashtags = hashtags.split(',')	
		print(type(hashtags))
		print(hashtags)
		num_tweets = self.textEditNumTweets.toPlainText()
		num_tweets = num_tweets.strip()
		try:
			num_tweets = int(num_tweets)
		except:
			print("Not a number")
		myTwitterStreamer = tweepy_streamer.TwitterStreamer()
		myTwitterStreamer.stream_tweets(tweets_filename, hashtags, num_tweets)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButtonStream.setText(_translate("MainWindow", "Start Streaming"))
		self.labelHashtags.setText(_translate("MainWindow", "Enter hashtags(separated by commas):"))
		self.labelNumTweets.setText(_translate("MainWindow", "Enter number of tweets:"))
		self.pushButtonDataframe.setText(_translate("MainWindow", "Print Dataframe to console"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLiveTweets), _translate("MainWindow", "Live Tweets"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabUserTweets), _translate("MainWindow", "User Tweets"))
		self.menuFile.setTitle(_translate("MainWindow", "&File"))
		self.actionQuit.setText(_translate("MainWindow", "&Quit"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

