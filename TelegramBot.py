from msvcrt import kbhit
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from id import token
from random import randint

bot = Bot(token = token)
dp = Dispatcher(bot)

word = ['арбуз', 'дверь', 'ягода', 'текст', 'атлас', 'базар', 'дырка', 'давуч', 'нефть', 'сосуд', 'ябеда']

o = len(word)

x = 0


# инлайн клавиатура
kb1 = InlineKeyboardMarkup()

kb1_btn1 = InlineKeyboardButton('связаться с поддержкой', url='https://t.me/cykarlk')

kb1.add(kb1_btn1)

# клавиатура
kb0 = ReplyKeyboardMarkup(resize_keyboard=True)

kb0_btn1 = KeyboardButton('🎮 Играть')
kb0_btn2 = KeyboardButton('📎 Правила')

kb0.add(kb0_btn1, kb0_btn2)


kb2 = ReplyKeyboardMarkup(resize_keyboard=True)

kb2_btn1 = KeyboardButton('/start')

kb2.add(kb2_btn1)


#         START
@dp.message_handler(commands = 'start')
async def process_photo(message: types.Message):
    await bot.send_message(message.from_user.id, ('🤖: 👋 Привет! Я — бот интеллектуальной игры «Intermath». Для ознакомления с правилами игры нажми на «Правила».'), reply_markup=kb0)




#         GAME

@dp.message_handler(lambda message: message.text in '🎮 Играть')
async def process_photo(message: types.Message):
    await bot.send_message(message.from_user.id, ('Вы начали игру'))
    global x
    x = word[randint(0, (o-1))]
    await bot.send_message(message.from_user.id, ('Введите существительное из 5-ти букв'))
    @dp.message_handler(lambda message: message.text)
    async def process_photo(message: types.Message):
        r = str(message.text)
        if len(message.text) <= 5:
            if message.text == x:
                await bot.send_message(message.from_user.id, ('Ура вы угадали слово!'))
            else:
                for i in range(0, 5):
                    for y in range(0, 5):
                        if x[i] == r[y]: 
                            if i == y:
                                await bot.send_message(message.from_user.id, (f'Ого вы угадали, {i+1}-я буква этого слова: {x[i]}'))
                            else:
                                await bot.send_message(message.from_user.id, (f'В этом слоове есть буква: {x[i]}, но она на другом месте'))
        else:
            await bot.send_message(message.from_user.id, ('нет, в этом слове больше 5 букв'))




#       RULE

@dp.message_handler(lambda message: message.text in '📎 Правила' )
async def process_photo(message: types.Message):
    await bot.send_message(message.from_user.id, ('📔Правила игры «Intermath» максимально просты! У тебя есть 6 попыток угадать загаданное мной слово из 5 букв (подсказка–слова только существительные). Есть ты смог отгадать слово, то ты получаешь балл. Если не угадал–начинаешь заново. Хочешь начать? Жми «Игать».'))
    await bot.send_message(message.from_user.id, ('💡Вся основная информация находится снизу, но если что-то не понятно, обращайся в поддержку.'), reply_markup=kb1)
    print(message.from_user.id)




while True:
    executor.start_polling(dp, skip_updates=True)