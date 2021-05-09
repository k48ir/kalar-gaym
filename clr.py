# import and other shit
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import sys

#main winhoe
class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		#  title
		self.setWindowTitle("kalar gaym ")

		#beckglaund
		self.setStyleSheet("background:yellow")
		

		#  geometry
		self.setGeometry(100, 100, 500, 500)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

		# counter
		self.count_value = 30

		# score
		self.score_value = 0

		# start flag
		self.start_Flag = False

		# list of possible colour.
		self.color_list = ['red', 'blue', 'green', 'pink', 'black',
				'yellow', 'orange', 'purple', 'brown']


		# method of components
	def UiComponents(self):

		#  head label
		head = QLabel("Color Gaym", self)

		# setting geometry to the head
		head.setGeometry(100, 10, 300, 60)

		# font
		font = QFont('Times', 14)
		font.setBold(True)
		font.setItalic(True)
		font.setUnderline(True)

		# setting font to the head
		head.setFont(font)

		# setting alignment of the head
		head.setAlignment(Qt.AlignCenter)

		# instruction label
		
		instruction = QLabel("Intruction : Enter the mf color not text. "
							, self)

		# making it multi line
		instruction.setWordWrap(True)

		# setting geometry to the label
		instruction.setGeometry(20, 60, 460, 60)

		# creating start button
		start = QPushButton("Start / Reset", self)

		# setting geometry to the push button
		start.setGeometry(200, 120, 100, 35)

		# adding action to the start button
		start.clicked.connect(self.start_action)

		# creating a score label
		self.score = QLabel("Score : 0", self)

		# setting geometry
		self.score.setGeometry(160, 170, 180, 50)

		# setting alignment
		self.score.setAlignment(Qt.AlignCenter)

		# setting font
		self.score.setFont(QFont('Times', 16))

		# setting style sheet
		self.score.setStyleSheet("QLabel"
								"{"
								"border : 2px solid black;"
								"color : green;"
								"background : lightgrey;"
								"}")

		# creating label to show color
		self.color = QLabel("Color name displays here", self)

		# setting geometry
		self.color.setGeometry(50, 230, 400, 120)

		# setting alignment
		self.color.setAlignment(Qt.AlignCenter)

		# setting font
		self.color.setFont(QFont('Times', 25))

		# creating a line edit
		self.input_text = QLineEdit(self)

		# setting geometry
		self.input_text.setGeometry(150, 340, 200, 50)

		# setting font
		self.input_text.setFont(QFont('Arial', 14))

		# making line edit disabled
		self.input_text.setDisabled(True)

		# adding action to it when enter is pressed
		self.input_text.returnPressed.connect(self.input_action)

		# creating a timer label
		self.count = QLabel("30", self)

		# setting geometry
		self.count.setGeometry(225, 430, 50, 50)

		# setting alignment
		self.count.setAlignment(Qt.AlignCenter)

		# setting font
		self.count.setFont(QFont('Times', 14))

		# setting style sheet
		self.count.setStyleSheet("border : 2px solid black;"
								"background : lightgrey;")

		# creating a timer object
		timer = QTimer(self)

		# adding action to the timer
		timer.timeout.connect(self.show_time)

		# start timer
		timer.start(1000)

	def show_time(self):

		if self.start_Flag:

			# showing count value to label
			self.count.setText(str(self.count_value))

			# checking if count value is zero
			if self.count_value == 0:

				# making start flag to false
				self.start_Flag = False

				# making line edit widget disable
				self.input_text.setDisabled(True)


			# decrementing the count value
			self.count_value -= 1




	def start_action(self):

		# making start flag true
		self.start_Flag = True

		# resetting score
		self.score.setText("Score : 0")
		self.score_value = 0

		# resetting count value
		self.count_value = 30

		# clearing line edit text
		self.input_text.clear()

		# making line edit enabled
		self.input_text.setEnabled(True)

		# getting random color
		self.random_color = random.choice(self.color_list)

		# making color choice random color
		self.random_color.lower()

		# setting random color to the label
		self.color.setStyleSheet("color : " + self.random_color + ";")

		# getting another random color name
		random_text = random.choice(self.color_list)

		# setting text to label
		self.color.setText(random_text)



	def input_action(self):

		# get the line edit test
		text = self.input_text.text()

		# making text lower case
		text.lower()

		# checking text with random color
		if text == self.random_color:
			# clearing line edit text
			self.input_text.clear()

			# incrementing score value
			self.score_value += 1

			# setting score to the score label
			self.score.setText("Score : " + str(self.score_value))

			# random color
			self.random_color = random.choice(self.color_list)

			# making color choice random color
			self.random_color.lower()

			# setting random color 
			self.color.setStyleSheet("color : " + self.random_color + ";")

			# getting  color name
			random_text = random.choice(self.color_list)

			# text to label
			self.color.setText(random_text)



#  app
App = QApplication(sys.argv)

#  instance of Window
window = Window()

# Fire it up ......rotr
sys.exit(App.exec())


#"Press Start		 "
							#" Time limit  is 30 seconds"
