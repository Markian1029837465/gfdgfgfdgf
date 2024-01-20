from memo_card_layout import *
from PyQt5.QtWidgets import*
from random import*
right_ans = 0
yes = 'Правильно'
no = 'Невірно'
change_ask = -1# зміннює текст запитання
list_ask = ['Що таке крихке, що ламається навіть при згадці',"Що піднімається і опускається, але залишається на тому самому місці? ",'Що піднімається, але ніколи не падає?','Найбільша річка України','периметр прямокутника','яка площа Укаїни ']
list_yes = ['тиша','сходи','твій вік','Дніпро','сума довжин всіх сторін фігури',' 603 628 км²']
list_no1 = ['слово','драбина','вода ','Амазонка','довжин однієї сторони фігури',' 605 608 км²']
list_no2 = ['банан',' гірка','Дніпро','Інгулець','довжин трьох сторін фігури',' 603 598 км²']
list_no3 = ['персик','різкий спуск вниз ','басейн','Десна','сума довжин двох сторін фігури', '603 609 км²']
radio_list = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
shuffle(radio_list)
right = radio_list[0]
wrong1 = radio_list[1]
wrong2 = radio_list[2]
wrong3= radio_list[3]
def show_data():
    global change_ask
    change_ask+=1
    question.setText(list_ask[change_ask])
    correct.setText(list_yes[change_ask])
    Result.setText(list_yes[change_ask])
    right.setText(list_yes[change_ask])
    wrong1.setText(list_no1[change_ask])
    wrong2.setText(list_no2[change_ask])
    wrong3.setText(list_no3[change_ask])

def check_result():

   ''' перевірка, чи правильна відповідь обрана
   якщо відповідь була обрана, то напис "правильно/неправильно" набуває потрібного
   значення і показується панель відповідей
   '''
   question.setText(list_yes[change_ask])
   global right_ans
   correct = right.isChecked() # у цьому радіобаттоні лежить наша відповідь!
   if correct:
       # відповідь вірна, запишемо
       Result.setText(yes) # напис "правильно" або "неправильно"
       showresult()
       right_ans+=1
       btn_Menu.setText(f'Ви відповіли вірно: {right_ans} раз(и) з {len(list_ask)}')


   else:
       incorrect = wrong1.isChecked() or wrong2.isChecked() or wrong3.isChecked()
       if incorrect:
           # відповідь невірна, запишемо і відобразимо у статистиці
           Result.setText(no) # напис "правильно" або "неправильно"
           showresult()
def click_OK(self):
   global right_ans

   # поки що перевіряємо питання, якщо ми в режимі питання, інакше нічого
   if btn_OK.text() == 'Відповісти':
       check_result()

   elif btn_OK.text() != 'Відповісти':
       btn_OK.setText('Відповісти')

       showquestion()
       show_data()
   print(right_ans)
win  = QWidget()
win.resize(500,500)
win.move(100,100)
win.setWindowTitle('Вікторина')
win.setLayout(layout_card)

show_data()


btn_OK.clicked.connect(click_OK)


win.show()
app.exec_()

