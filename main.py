import telebot
points = 0
bot = telebot.TeleBot('7709064856:AAFeN2d7_9Du0mCwJlv-vZz6Kbg-3cI-V0w')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Привет, я бот про глобальное потепление! Ты можешь вызвать викторину командой /quiz.Пояснение глобального потепления:/glwr")

@bot.message_handler(commands=['quiz'])
def quiz(message):
    bot.send_message(message.chat.id, "Писать букву ответа!!!\n1 вопрос:Что такое глобальное потепление?\nа) Повышение температуры в одной стране\nб) Повышение средней температуры на всей планете\nв) Понижение температуры зимой")
    bot.register_next_step_handler(message, handle_q1)

def handle_q1(message):
    if message.text.strip().lower() == "б":
        bot.send_message(message.chat.id, "Молодец!")
        
    else:
        bot.send_message(message.chat.id, "Неправильный ответ(,правильный ответ:б) Повышение средней температуры на всей планете")
    
    bot.send_message(message.chat.id, "2 вопрос:Сколько лет мы ведем наблюдение за уровнем температуры на земле?\nа) около 100 лет\nб)где-то 50 лет\nв) 250 лет")
    bot.register_next_step_handler(message, handle_q2)

def handle_q2(message):
    if message.text.strip().lower() == "а":
        bot.send_message(message.chat.id, "Верно!")
        
    else:
        bot.send_message(message.chat.id, "Нет, правильный ответ:а) около 100 лет")

    bot.send_message(message.chat.id, "3 вопрос:На сколько выросла средняя температура с 1905 года?\nа)на три градуса\nб)не выросла\nв)на один градус")
    bot.register_next_step_handler(message, handle_q3)

def handle_q3(message):
    if message.text.strip().lower() == "в":
        bot.send_message(message.chat.id, "Так держать")
        
    else:
        bot.send_message(message.chat.id, "Нет(, правильный ответ:в) на один градус")

    bot.send_message(message.chat.id, "4 вопрос:Какой газ в атмосфере чаще всего вызывает парниковый эффект?\nа) Кислород\nб) Углекислый газ (CO₂)\nв) Азот")
    bot.register_next_step_handler(message, handle_q4)

def handle_q4(message):
    if message.text.strip().lower() == "б":
        bot.send_message(message.chat.id, "лучший")
        
    else:
        bot.send_message(message.chat.id, "Нет(, правильный ответ:б) Углекислый газ (CO₂)")

    bot.send_message(message.chat.id, "5 вопрос: Как влияет глобальное потепление на уровень моря?\nа) Он остаётся прежним\nб) Он понижается\nв) Он повышается из-за таяния льдов")
    bot.register_next_step_handler(message, handle_q5)

def handle_q5(message):
    if message.text.strip().lower() == "в":
        bot.send_message(message.chat.id, "красавчик")
        
    else:
        bot.send_message(message.chat.id, "Нет(, правильный ответ:в) Он повышается из-за таяния льдов")

    bot.send_message(message.chat.id, "6 вопрос:Какой из этих способов помогает бороться с глобальным потеплением?\nа) Сжигание большего количества топлива\nб) Посадка деревьев\nв) Увеличение количества машин")
    bot.register_next_step_handler(message, handle_q6)

def handle_q6(message):
    if message.text.strip().lower() == "б":
        bot.send_message(message.chat.id, "верно!")
        
    else:
        bot.send_message(message.chat.id, "Нет(, правильный ответ:б) Посадка деревьев")

    bot.send_message(message.chat.id, "7 вопрос:Какое из последствий связано с глобальным потеплением?\nа) Рост числа снежных дней\nб) Сильные засухи и наводнения\nв) Увеличение популяции пингвинов")
    bot.register_next_step_handler(message, handle_q7)

def handle_q7(message):
    if message.text.strip().lower() == "б":
        bot.send_message(message.chat.id, "молодец")
        
    else:
        bot.send_message(message.chat.id, "Нет(, правильный ответ:б) Сильные засухи и наводнения")

    bot.send_message(message.chat.id, "8 вопрос:Какой источник энергии считается чистым? \nа) Уголь \nб) Бензин \nв) Солнечная энергия")
    bot.register_next_step_handler(message, handle_q8)

def handle_q8(message):
    if message.text.strip().lower() == "в":
        bot.send_message(message.chat.id, "красавчик")
        
    else:
        bot.send_message(message.chat.id, "Нет(, правильный ответ:в) Солнечная энергия")

    bot.send_message(message.chat.id, "9 вопрос:Что происходит с ледниками из-за глобального потепления? \nа) Они тают \nб) Они увеличиваются  \nв) Ничего ")
    bot.register_next_step_handler(message, handle_q9)

def handle_q9(message):
    if message.text.strip().lower() == "а":
        bot.send_message(message.chat.id, "лучший")
        
    else:
        bot.send_message(message.chat.id, "Нет(, правильный ответ:а) Они тают ")

    bot.send_message(message.chat.id, "10 вопрос:Какая страна выбрасывает больше всего CO₂? \nа) Франция \nб) Китай \nв) Канада")
    bot.register_next_step_handler(message, handle_q10)

def handle_q10(message):
    if message.text.strip().lower() == "б":
        bot.send_message(message.chat.id, "молодец")
        points += 1
        bot.send_message(message.chat.id, "Викторина подошла к концу")
    else:
        bot.send_message(message.chat.id, "Нет(, правильный ответ:б) Китай")
        bot.send_message(message.chat.id, "Викторина подошла к концу,у тебя набралось",points,"баллов")
    
@bot.message_handler(commands=['glwr'])
def abrigan(message):
    bot.send_message(message.chat.id,"Простыми словами Глобальное потепление — распространенное название изменения климата, которое идет уже около двух веков\nПокрывая Землю, выбросы парниковых газов задерживают солнечное тепло. Это приводит к глобальному потеплению и изменению климата. В настоящее время планета нагревается быстрее, чем когда-либо в истории человечества. Повышение температуры со временем меняет погодные условия и нарушает обычный природный баланс")

bot.polling()