from telebot import types
from telebot.types import WebAppInfo

from repository.lang import translate

university = [
    {
        'name': 'INHA UNIVERSITY',
        'acceptance': '43%',
        'graduate_rate': '85%',
        'average_salary': '$36000',
    },
    {
        'name': 'IT PARK UNIVERSITY',
        'acceptance': '67%',
        'graduate_rate': '30.7%',
        'average_salary': '$36000',
    },
    {
        'name': 'NATIONAL UNIVERSITY OF UZBEKISTAN',
        'acceptance': '10%',
        'graduate_rate': '15%',
        'average_salary': '$31000',
    },
    {
        'name': 'TASHKENT UNIVERSITY OF INTERNATION TECHNOLOGIES',
        'acceptance': '33%',
        'graduate_rate': '83%',
        'average_salary': '$31000',
    },
    {
        'name': 'TASHKENT STATE AGRARIAN UNIVERSITY',
        'acceptance': '18%',
        'graduate_rate': '15%',
        'average_salary': '$23500',
    },
    {
        'name': 'TASHKENT STATE UNIVERSITY OF ECONOMICS',
        'acceptance': '43%',
        'graduate_rate': '36%',
        'average_salary': '$23500',
    },
    {
        'name': 'KHAZAN FEDERAL UNIVERSITY',
        'acceptance': '65%',
        'graduate_rate': '95%',
        'average_salary': '$38400',
    },
    {
        'name': 'ITMO UNIVERSITY',
        'acceptance': '10%',
        'graduate_rate': '34%',
        'average_salary': '$38400',
    },
    {
        'name': 'MOSCOW STATE UNIVERSITY',
        'acceptance': '12%',
        'graduate_rate': '83%',
        'average_salary': '$105928',
    },
    {
        'name': 'NATIONAL RESEARCH UNIVERSITY HIGHER SCHOOL OF ECONOMICS',
        'acceptance': '19%',
        'graduate_rate': '79%',
        'average_salary': '$105928',
    },
    {
        'name': 'LOMONOSOV MOSCOW STATE UNIVERSITY',
        'acceptance': '12%',
        'graduate_rate': '81%',
        'average_salary': '$24000',
    },
    {
        'name': 'BAUMAN MOSCOW STATE TECHNICAL UNIVERSITY',
        'acceptance': '30',
        'graduate_rate': '89%',
        'average_salary': '$24000',
    },
]


def main_keys():
    markup = types.ReplyKeyboardMarkup(row_width=True, resize_keyboard=True)
    btn = types.KeyboardButton(text=translate('universities', 'ru'))
    btn1 = types.KeyboardButton(text=translate('online_courses', 'ru'))
    btn2 = types.KeyboardButton(text=translate('prof_orientation', 'ru'), web_app=WebAppInfo(url='https://master--marvelous-pika-08cf9e.netlify.app/?ru'))
    markup.add(btn)
    markup.add(btn1)
    markup.add(btn2)
    return markup


designUniversities = [
    f"{university[2]['name']}\nAcceptance : {university[2]['acceptance']}\nGraduation rate : {university[2]['graduate_rate']}\nAverage salary : {university[2]['average_salary']}",
    f"{university[3]['name']}\nAcceptance : {university[3]['acceptance']}\nGraduation rate : {university[3]['graduate_rate']}\nAverage salary : {university[3]['average_salary']}",
    f"{university[6]['name']}\nAcceptance : {university[6]['acceptance']}\nGraduation rate : {university[6]['graduate_rate']}\nAverage salary : {university[6]['average_salary']}",
    f"{university[4]['name']}\nAcceptance : {university[4]['acceptance']}\nGraduation rate : {university[4]['graduate_rate']}\nAverage salary : {university[4]['average_salary']}",
]


softwareUniversities = [
    f"{university[0]['name']}\nAcceptance : {university[0]['acceptance']}\nGraduation rate : {university[0]['graduate_rate']}\nAverage salary : {university[0]['average_salary']}",
    f"{university[1]['name']}\nAcceptance : {university[1]['acceptance']}\nGraduation rate : {university[1]['graduate_rate']}\nAverage salary : {university[1]['average_salary']}",
    f"{university[7]['name']}\nAcceptance : {university[7]['acceptance']}\nGraduation rate : {university[7]['graduate_rate']}\nAverage salary : {university[7]['average_salary']}",
    f"{university[6]['name']}\nAcceptance : {university[6]['acceptance']}\nGraduation rate : {university[6]['graduate_rate']}\nAverage salary : {university[6]['average_salary']}",
]


marketingUniversities = [
    f"{university[5]['name']}\nAcceptance : {university[5]['acceptance']}\nGraduation rate : {university[5]['graduate_rate']}\nAverage salary : {university[5]['average_salary']}",
    f"{university[8]['name']}\nAcceptance : {university[8]['acceptance']}\nGraduation rate : {university[8]['graduate_rate']}\nAverage salary : {university[8]['average_salary']}",
    f"{university[10]['name']}\nAcceptance : {university[10]['acceptance']}\nGraduation rate : {university[10]['graduate_rate']}\nAverage salary : {university[10]['average_salary']}",
    f"{university[8]['name']}\nAcceptance : {university[8]['acceptance']}\nGraduation rate : {university[8]['graduate_rate']}\nAverage salary : {university[8]['average_salary']}",
]


users = {}
