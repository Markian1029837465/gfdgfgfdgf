from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QFont
app = QApplication([])
right_ans  =1
btn_Menu = QLabel('Ви відповіли вірно:  раз(и) ',alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

font = QFont('Arial',30)
btn_Menu.setFont(font)
btn_OK = QPushButton('Відповісти')
question = QLabel('')# тут зявиться наше запитання
font = QFont('Arial',19)
question.setFont(font)
RadioGroupBox = QGroupBox('Варіанти відповідей')
RadioGroup = QButtonGroup()
rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
AnsGroupBox = QGroupBox('Результат тесту')
Result = QLabel('')

correct = QLabel('')
layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)

layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
leyout_res = QVBoxLayout()
leyout_res.addWidget(Result,alignment = (Qt.AlignLeft | Qt.AlignTop))
leyout_res.addWidget(Result,alignment = Qt.AlignHCenter,stretch =3)
AnsGroupBox.setLayout(leyout_res)
AnsGroupBox.hide()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
line1.addWidget(btn_Menu)



line2.addWidget(question,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

line3.addWidget(RadioGroupBox)
line3.addWidget(AnsGroupBox)
line4.addWidget(btn_OK)
layout_card = QVBoxLayout()
layout_card.addLayout(line1)
layout_card.addLayout(line2)
layout_card.addLayout(line3)
layout_card.addLayout(line4)
layout_card.setSpacing(5)

def showresult():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Наступне запитання')
def showquestion():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Відповісти')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
