# Импорты библиотек
from random import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGroupBox, QRadioButton, QHBoxLayout, QButtonGroup
from random import shuffle  # Импорт функции перемешивания ответов
# ----------- Класс -----------
class Question():
    def __init__(self,question7, right_answer, wrong1, wrong2, wrong3):
        self.question7 = question7
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    

# ----------- Функции -----------
# Функция для задания вопроса и ответов
def ask(q: Question):
    #Перемешивает и отображает варианты ответов на вопрос
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question7)
    question3.setText(q.right_answer)
    show_question()


# Функция для проверки ответа
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
        print('статистика в процентах',main_win.score / main_win.total * 100)
    else:
        show_correct('Неверно')
    


# Функция для отображения результата (правильный/неправильный)
def show_correct(res):
    question2.setText(res)
    show_answer()
       

# Функция для показа вопроса
def show_question():
    #Подготавливает интерфейс для следующего вопроса
    Button.setText('Ответить')
    RadioGroupBox.show()
    question.show()
    RadioGroupBox1.hide()
    question1.hide()
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

# Функция для показа ответа
def show_answer():
    Button.setText('Следующий вопрос')
    RadioGroupBox.hide()
    question.hide()
    RadioGroupBox1.show()
    question1.show()

# Проверка текущего состояния кнопки
def check():
    if Button.text() == 'Ответить':
        check_answer()
    elif Button.text() == 'Следующий вопрос':
        next_question()
#Функция для соедущего вопроса
def next_question():
    main_win.total += 1
    cur_queston = randint(0,len(question_list) -1)
    q = question_list[cur_queston]
    ask(q)
    print('статистика в процентах',main_win.score / main_win.total * 100)
    
    
    

#Создание приложения и интерфейса
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory card')  # Название приложения

# Вопросы и группы виджетов
question = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответов')  # Группа вариантов ответов
RadioGroupBox1 = QGroupBox('Результат теста')  # Группа для результата ответа
question1 = QLabel('Самый сложный вопрос в мире!')
question2 = QLabel('Правильно/Неправильно')
question3 = QLabel('Правильный ответ')

#количиство вопросов -1 
main_win.cur_queston = -1



# Варианты ответов (радиокнопки)
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Алеуты')
rbtn_4 = QRadioButton('Чулымцы')
#Вопросы в перемешку
question_list = []
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]  # Список для перемешивания ответов
#Статистика
main_win.total = 0
main_win.score = 0

# Экземпляры 
q1 = Question('РАВНО - 1','0','0','0','бебебебе')
question_list.append(q1)
q2 = Question('Сколько пальцев на ноге','5','4','1','52')
question_list.append(q2)
q3 = Question('Кто придумал закон Ньютона','Ньютона','Менделеев','Аристотель','Эйнштейн')
question_list.append(q3)
q4 = Question('Когда впервые упоминается праздник являющийся прообразом современного Нового года?','Третье тысячелетие до н. э.','100г','200г','300г')
question_list.append(q4)
q5 = Question('Где впервые начали украшать елку еще в Средневековье?','Германия','Франция','Париж','Турция')
question_list.append(q5)
q6 = Question('Где впервые появились елочные игрушки из стекла?','В Швеции','Дания','Германия','Финляндия')
question_list.append(q6)
q7 = Question('2+2','2','2+2','3','4')
question_list.append(q7)
q8 = Question('корень 4','2','1','1','1')
question_list.append(q8)
q9 = Question('35*12','420','470','180','11111111')
question_list.append(q9)
q10 = Question('1/0','на ноль делить не льзя','0','2','11')
question_list.append(q10)

# Группа радиокнопок для управления
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# Кнопка ответа
Button = QPushButton('Ответить')

# ----------- Компоновка виджетов -----------
# Компоновка для группы результатов
layout_ans1_1 = QVBoxLayout()
layout_ans1_2 = QVBoxLayout()
layout_ans1_3 = QVBoxLayout()

layout_ans1_1.addWidget(question2)  # Правильно/Неправильно
layout_ans1_2.addWidget(question3)  # Правильный ответ
layout_ans1_3.addLayout(layout_ans1_1)
layout_ans1_3.addLayout(layout_ans1_2)
RadioGroupBox1.setLayout(layout_ans1_3)

# Компоновка для вариантов ответов
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

# Главная компоновка
layout_line1H = QHBoxLayout()
layout_line2H = QHBoxLayout()
layout_line3H = QHBoxLayout()

layout_line1H.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line1H.addWidget(question1, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2H.addWidget(RadioGroupBox)
layout_line2H.addWidget(RadioGroupBox1)
layout_line3H.addStretch(1)
layout_line3H.addWidget(Button, stretch=2)
layout_line3H.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1H, stretch=2)
layout_card.addLayout(layout_line2H, stretch=8)
layout_card.addLayout(layout_line3H, stretch=1)
main_win.setLayout(layout_card)


# ----------- Инициализация интерфейса -----------
RadioGroupBox1.hide()  # Скрыть группу результата
question1.hide()       # Скрыть вопрос результата
Button.clicked.connect(check)  # Привязка кнопки к функции check
next_question()
# Запуск приложения
main_win.show()
app.exec()
