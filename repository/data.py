from telebot import types
from telebot.types import WebAppInfo

from repository.lang import translate

university = [
    {
        'name': 'INHA UNIVERSITY',
        'acceptance': '43%',
        'graduate_rate': '85%',
        'average_salary': '$36000',
        "link": "https://inha.uz/"
    },
    {
        'name': 'IT PARK UNIVERSITY',
        'acceptance': '67%',
        'graduate_rate': '30.7%',
        'average_salary': '$36000',
        "link": "https://itpu.uz/",
    },
    {
        'name': 'NATIONAL UNIVERSITY OF UZBEKISTAN',
        'acceptance': '10%',
        'graduate_rate': '15%',
        'average_salary': '$31000',
        "link": "https://nuu.uz/"
    },
    {
        'name': 'TASHKENT UNIVERSITY OF INTERNATION TECHNOLOGIES',
        'acceptance': '33%',
        'graduate_rate': '83%',
        'average_salary': '$31000',
        "link": "https://nuu.uz/"
    },
    {
        'name': 'TASHKENT STATE AGRARIAN UNIVERSITY',
        'acceptance': '18%',
        'graduate_rate': '15%',
        'average_salary': '$23500',
        "link": "https://nuu.uz/",
    },
    {
        'name': 'TASHKENT STATE UNIVERSITY OF ECONOMICS',
        'acceptance': '43%',
        'graduate_rate': '36%',
        'average_salary': '$23500',
        "link": "https://nuu.uz/",
    },
    {
        'name': 'KHAZAN FEDERAL UNIVERSITY',
        'acceptance': '65%',
        'graduate_rate': '95%',
        'average_salary': '$38400',
        "link": "https://kpfu.ru/"
    },
    {
        'name': 'ITMO UNIVERSITY',
        'acceptance': '10%',
        'graduate_rate': '34%',
        'average_salary': '$38400',
        "link": "https://en.itmo.ru/"
    },
    {
        'name': 'MOSCOW STATE UNIVERSITY',
        'acceptance': '12%',
        'graduate_rate': '83%',
        'average_salary': '$105928',
        "link": "https://www.msu.ru/"
    },
    {
        'name': 'NATIONAL RESEARCH UNIVERSITY HIGHER SCHOOL OF ECONOMICS',
        'acceptance': '19%',
        'graduate_rate': '79%',
        'average_salary': '$105928',
        'link': 'http://www.hse.ru/'
    },
    {
        'name': 'LOMONOSOV MOSCOW STATE UNIVERSITY',
        'acceptance': '12%',
        'graduate_rate': '81%',
        'average_salary': '$24000',
        'link': 'https://www.msu.ru/'
    },
    {
        'name': 'BAUMAN MOSCOW STATE TECHNICAL UNIVERSITY',
        'acceptance': '30',
        'graduate_rate': '89%',
        'average_salary': '$24000',
        'link': 'http://www.bmstu.ru/'
    },
]


def main_keys(lang):
    markup = types.ReplyKeyboardMarkup(row_width=True, resize_keyboard=True)
    btn = types.KeyboardButton(text=translate('universities', lang))
    btn1 = types.KeyboardButton(text=translate('online_courses', lang))
    if lang == 'uz':
        btn2 = types.KeyboardButton(text=translate('prof_orientation', lang),
                                    web_app=WebAppInfo(url='https://master--marvelous-pika-08cf9e.netlify.app/?uz'))
    else:
        btn2 = types.KeyboardButton(text=translate('prof_orientation', lang),
                                    web_app=WebAppInfo(url='https://master--marvelous-pika-08cf9e.netlify.app/?ru'))
    markup.add(btn)
    markup.add(btn1)
    markup.add(btn2)
    return markup


designUnis = [
    f"{university[2]['name']}",
    f"{university[3]['name']}",
    f"{university[6]['name']}",
    f"{university[4]['name']}",
]

softUnis = [
    f"{university[0]['name']}",
    f"{university[1]['name']}",
    f"{university[7]['name']}",
    f"{university[6]['name']}",
]

marketingUnis = [
    f"{university[5]['name']}",
    f"{university[8]['name']}",
    f"{university[10]['name']}",
    f"{university[7]['name']}",
]


def designUniversities(lang):
    return [
        f"{university[2]['name']}\n{translate('acceptance', lang)} : {university[2]['acceptance']}\n{translate('graduation_rate', lang)} : {university[2]['graduate_rate']}\n{translate('average_salary', lang)} : {university[2]['average_salary']}\n{translate('link', lang)} : {university[2]['link']}\n\n",
        f"{university[3]['name']}\n{translate('acceptance', lang)} : {university[3]['acceptance']}\n{translate('graduation_rate', lang)} : {university[3]['graduate_rate']}\n{translate('average_salary', lang)} : {university[3]['average_salary']}\n{translate('link', lang)} : {university[3]['link']}\n\n",
        f"{university[6]['name']}\n{translate('acceptance', lang)} : {university[6]['acceptance']}\n{translate('graduation_rate', lang)} : {university[6]['graduate_rate']}\n{translate('average_salary', lang)} : {university[6]['average_salary']}\n{translate('link', lang)} : {university[6]['link']}\n\n",
        f"{university[4]['name']}\n{translate('acceptance', lang)} : {university[4]['acceptance']}\n{translate('graduation_rate', lang)} : {university[4]['graduate_rate']}\n{translate('average_salary', lang)} : {university[4]['average_salary']}\n{translate('link', lang)} : {university[4]['link']}",
    ]


def softwareUniversities(lang):
    return [
        f"{university[0]['name']}\n{translate('acceptance', lang)} : {university[0]['acceptance']}\n{translate('graduation_rate', lang)} : {university[0]['graduate_rate']}\n{translate('average_salary', lang)} : {university[0]['average_salary']}\n{translate('link', lang)} : {university[0]['link']}\n\n",
        f"{university[1]['name']}\n{translate('acceptance', lang)} : {university[1]['acceptance']}\n{translate('graduation_rate', lang)} : {university[1]['graduate_rate']}\n{translate('average_salary', lang)} : {university[1]['average_salary']}\n{translate('link', lang)} : {university[1]['link']}\n\n",
        f"{university[7]['name']}\n{translate('acceptance', lang)} : {university[7]['acceptance']}\n{translate('graduation_rate', lang)} : {university[7]['graduate_rate']}\n{translate('average_salary', lang)} : {university[7]['average_salary']}\n{translate('link', lang)} : {university[7]['link']}\n\n",
        f"{university[6]['name']}\n{translate('acceptance', lang)} : {university[6]['acceptance']}\n{translate('graduation_rate', lang)} : {university[6]['graduate_rate']}\n{translate('average_salary', lang)} : {university[6]['average_salary']}\n{translate('link', lang)} : {university[6]['link']}",
    ]


def marketingUniversities(lang):
    return [
        f"{university[5]['name']}\n{translate('acceptance', lang)} : {university[5]['acceptance']}\n{translate('graduation_rate', lang)} : {university[5]['graduate_rate']}\n{translate('average_salary', lang)} : {university[5]['average_salary']}\n{translate('link', lang)} : {university[5]['link']}\n\n",
        f"{university[8]['name']}\n{translate('acceptance', lang)} : {university[8]['acceptance']}\n{translate('graduation_rate', lang)} : {university[8]['graduate_rate']}\n{translate('average_salary', lang)} : {university[8]['average_salary']}\n{translate('link', lang)} : {university[8]['link']}\n\n",
        f"{university[10]['name']}\n{translate('acceptance', lang)} : {university[10]['acceptance']}\n{translate('graduation_rate', lang)} : {university[10]['graduate_rate']}\n{translate('average_salary', lang)} : {university[10]['average_salary']}\n{translate('link', lang)} : {university[10]['link']}\n\n",
        f"{university[7]['name']}\n{translate('acceptance', lang)} : {university[7]['acceptance']}\n{translate('graduation_rate', lang)} : {university[7]['graduate_rate']}\n{translate('average_salary', lang)} : {university[7]['average_salary']}\n{translate('link', lang)} : {university[7]['link']}",
    ]


uzbUnis = [
    f"{university[0]['name']}",
    f"{university[1]['name']}",
    f"{university[2]['name']}",
    f"{university[3]['name']}",
    f"{university[4]['name']}",
    f"{university[5]['name']}",
]

rusUnis = [
    f"{university[6]['name']}",
    f"{university[7]['name']}",
    f"{university[8]['name']}",
    f"{university[9]['name']}",
    f"{university[10]['name']}",
    f"{university[11]['name']}",
]

users = {}
