from random import random

from telebot import TeleBot
from telebot import types
from repository.lang import translate
from repository.data import main_keys, university
import service.survey_result

TOKEN = "6931512974:AAH7oux6l4Hd7B30zqfGTWSB9GoXmfscCTw"

bot = TeleBot(TOKEN)

university = university


@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    message_id = message.message_id
    bot.delete_message(chat_id, message_id)
    markup = types.InlineKeyboardMarkup(row_width=True)
    btn1 = types.InlineKeyboardButton(text='Русский язык🇷🇺', callback_data='ru')
    btn2 = types.InlineKeyboardButton(text="O'zbek tili🇺🇿", callback_data='uz')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, '<b>Выберите язык: <code>|</code> Til tanlang</b>', parse_mode='HTML',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    user_id = call.from_user.id
    markup = main_keys()

    if call.data == 'ru' or call.data == 'uz':
        bot.send_message(user_id, translate('choose_option', 'ru'), reply_markup=markup)
        return
    elif call.data == 'prog_k':
        res = '''
                Course: "Programming for Everybody (Getting Started with Python)"
                Description: Offered by the University of Michigan, this course is a beginner-friendly introduction to programming using Python.
                URL: [Programming for Everybody](https://www.coursera.org/specializations/python)

                Course: "Introduction to Computer Science and Programming Using Python"
                Description: This course, provided by MIT on edX, is designed for beginners and covers fundamental concepts in computer science using Python.
                URL: [MITx Computational Thinking Using Python](https://www.edx.org/professional-certificate/mitx-computational-thinking-using-python)

                Course: "Intro to Programming with Python"
                Description: Udacity's course is aimed at beginners and covers the basics of programming using Python, including data types, functions, and control flow.
                URL: [Intro to Python](https://www.udacity.com/course/introduction-to-python--ud1110)

                Course: "Learn Python"
                Description: Codecademy offers an interactive and hands-on approach to learning Python, covering syntax, functions, and data structures.
                URL: [Learn Python](https://www.codecademy.com/learn/learn-python-3)

                Course: "Intro to JavaScript: Drawing & Animation"
                Description: Khan Academy provides a beginner-friendly introduction to programming with JavaScript, focusing on creating drawings and animations.
                URL: [Intro to JavaScript](https://www.khanacademy.org/computing/computer-programming)
                '''
    elif call.data == 'design_k':
        res = '''
                Course: "Graphic Design Specialization"
                Description: Offered by the California Institute of the Arts, this specialization covers the principles of graphic design, including color theory, typography, and image making.
                URL: [Graphic Design Specialization](https://www.coursera.org/specializations/graphic-design)

                Course: "User Experience Design"
                Description: Udacity's UX Design course teaches the principles of user-centered design, usability testing, and prototyping to create effective and user-friendly interfaces.
                URL: [UX/UI Design Course](https://www.udacity.com/course/user-experience-design--ud849)

                Course: "Introduction to Graphic Design"
                Description: This course, provided by the University of Texas at Austin on edX, introduces students to the principles and elements of graphic design.
                URL: [Introduction to Graphic Design](https://www.edx.org/professional-certificate/introduction-to-graphic-design)

                Course: "Logo Design with Draplin: Secrets of Shape, Type, and Color"
                Description: Led by designer Aaron Draplin, this Skillshare course focuses on logo design, covering the creative process and practical tips for creating effective logos.
                URL: [Logo Design with Draplin](https://www.skillshare.com/classes/Logo-Design-with-Draplin-Secrets-of-Shape-Type-and-Color/2045627376)

                Course: "Human-Computer Interaction (HCI)"
                Description: IDF offers a comprehensive course on HCI, covering the principles of interaction design, usability, and user research.
                URL: [Human-Computer Interaction](https://www.interaction-design.org/courses/human-computer-interaction)
                '''
    elif call.data == 'market_k':
        res = '''
                Course: "Digital Marketing Specialization"
                Description: Offered by the University of Illinois, this specialization covers the strategic aspects of digital marketing, including SEO, social media, and analytics.
                URL: [Digital Marketing Specialization](https://www.coursera.org/specializations/digitalmarketing)

                Course: "The Complete Digital Marketing Course - 12 Courses in 1"
                Description: This comprehensive Udemy course covers various aspects of digital marketing, including SEO, social media, email marketing, and Google AdWords.
                URL: [Digital Marketing Course on Udemy](https://www.udemy.com/course/learn-digital-marketing-course/)

                Course: "Social Media Marketing Professional Certificate"
                Description: Offered by Boston University, this edX course provides a deep dive into social media marketing strategies, content creation, and analytics.
                URL: [Social Media Marketing Course](https://www.edx.org/professional-certificate/social-media-marketing)

                Course: "Fundamentals of Digital Marketing"
                Description: Google's free online course covers the basics of digital marketing, including search engine optimization (SEO), social media, and email marketing.
                URL: [Fundamentals of Digital Marketing](https://learndigital.withgoogle.com/digitalgarage/course/digital-marketing)

                Course: "Inbound Marketing Certification"
                Description: HubSpot's Inbound Marketing Certification covers the methodology of inbound marketing, including content creation, social promotion, and lead nurturing.
                URL: [Inbound Marketing Certification](https://academy.hubspot.com/courses/inbound)
                '''
    elif call.data == 'prog_ish':
        res = '''
                Job: "Software Developer"
                Description: Develop and maintain software applications using programming languages like Python, Java, or JavaScript.
                URL: [Software Developer Jobs on Indeed](https://www.indeed.com/q-Software-Developer-jobs.html)

                Job: "Data Scientist"
                Description: Analyze and interpret complex data sets to inform business decision-making.
                URL: [Data Scientist Jobs on LinkedIn](https://www.linkedin.com/jobs/data-scientist-jobs/)

                Job: "Web Developer"
                Description: Design and implement web applications using HTML, CSS, and JavaScript.
                URL: [Web Developer Jobs on Glassdoor](https://www.glassdoor.com/Job/web-developer-jobs-SRCH_KO0,12.htm)
                '''
    elif call.data == 'design_ish':
        res = '''
                Job: "Graphic Designer"
                Description: Create visual concepts using computer software or by hand to communicate ideas that inspire, inform, and captivate consumers.
                URL: [Graphic Designer Jobs on SimplyHired](https://www.simplyhired.com/search?q=graphic+designer)

                Job: "UX/UI Designer"
                Description: Design user experiences and user interfaces for digital products, ensuring a seamless and visually appealing interaction.
                URL: [UX/UI Designer Jobs on Monster](https://www.monster.com/jobs/q-ux-ui-designer-jobs.aspx)

                Job: "Motion Graphics Designer"
                Description: Create animated graphics and visual effects for video content.
                URL: [Motion Graphics Designer Jobs on Creativepool](https://creativepool.com/jobs/motion-graphics-designer)
                '''
    elif call.data == 'market_ish':
        res = '''
                Job: "Digital Marketing Specialist"
                Description: Plan and execute digital marketing campaigns, including SEO, social media, and email marketing.
                URL: [Digital Marketing Specialist Jobs on Indeed](https://www.indeed.com/q-Digital-Marketing-Specialist-jobs.html)

                Job: "Content Marketing Manager"
                Description: Develop and implement content marketing strategies to drive brand awareness and customer engagement.
                URL: [Content Marketing Manager Jobs on LinkedIn](https://www.linkedin.com/jobs/content-marketing-manager-jobs/)

                Job: "Social Media Coordinator"
                Description: Manage and create content for social media platforms to enhance brand presence and engage with the audience.
                URL: [Social Media Coordinator Jobs on Glassdoor](https://www.glassdoor.com/Job/social-media-coordinator-jobs-SRCH_KO0,24.htm)
                '''
    elif call.data == 'universities':
        res = ''
    else:
        res = "No information available"

    bot.send_message(call.message.chat.id, res, parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def handle_messages(message: types.Message):
    if message.text == translate('universities', 'ru'):
        pass
    elif message.text == translate('online_courses', 'ru'):
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton(translate('soft_courses', 'ru'), callback_data='prog_k')
        item2 = types.InlineKeyboardButton(translate('design_courses', 'ru'), callback_data='design_k')
        item3 = types.InlineKeyboardButton(translate('marketing_courses', 'ru'), callback_data='market_k')
        markup.row(item1)
        markup.row(item2)
        markup.row(item3)
        bot.send_message(message.chat.id, translate('choose_course', 'ru'), reply_markup=markup)
    elif message.text == translate('prof_orientation', 'ru'):
        user_id = message.from_user.id
        bot.send_message(user_id, translate('prof_info', 'ru'))


@bot.message_handler(content_types=['web_app_data'])
def survey_result(web_mess):
    print(web_mess)
    print(web_mess.web_app_data.data)
    a = web_mess.web_app_data.data.split(', ')[0]
    b = web_mess.web_app_data.data.split(', ')[1]
    c = web_mess.web_app_data.data.split(', ')[2]
    data = service.survey_result.calculatePercent(a, b, c)
    res = service.survey_result.show_percent(data[0], data[1], data[2])
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=translate('universities', 'ru'), callback_data='universities')
    btn2 = types.InlineKeyboardButton(text=translate('online_courses', 'ru'), callback_data='online_courses')
    btn3 = types.InlineKeyboardButton(text=translate('jobs', 'ru'), callback_data='jobs')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    bot.send_message(web_mess.chat.id, res, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def software(call):
    uzb_list = ['inha', 'itpark', 'national_uni', 'intertech', 'agrar', 'economics']
    if call.data in uzb_list:
        global state
        state = "DTM"
        bot.send_message(call.message.chat.id, 'DTM : ')

    else:
        rus_list = ['itmo', 'kazan', 'research_uni', 'lomonosov']
        if call.data in rus_list:
            global state
            state = "ege"
            bot.send_message(call.message.chat.id, 'ЕГЭ : ')


@bot.message_handler(content_types=['text'])
def score(message):
    num = int(message.text)
    if state == 'DTM':
        if 100 <= num <= 150:
            bot.send_message(message.chat.id, f'KIRISH SHANSINGIZ : {random.randint(61, 70)}')
        elif num >= 151:
            bot.send_message(message.chat.id, f'KIRISH SHANSINGIZ : {random.randint(73, 90)}')
        else:
            bot.send_message(message.chat.id, 'ERROR')
    elif state == 'ege':
        if 70 <= num <= 78:
            bot.send_message(message.chat.id, f'KIRISH SHANSINGIZ : {random.randint(61, 70)}')
        elif num > 78:
            bot.send_message(message.chat.id, f'KIRISH SHANSINGIZ : {random.randint(73, 85)}')
        else:
            bot.send_message(message.chat.id, 'ERROR')


if __name__ == '__main__':
    bot.infinity_polling()
