# ВВОДНАЯ ЧАСТЬ
import telebot
from telebot import types
import re
from docx import Document
import os

token = ""

bot = telebot.TeleBot(token)

CHECKMARK_EMOJI = "\u2705"
ONE_EMOJI = "\u0031\uFE0F\u20E3"
TWO_EMOJI = "\u0032\uFE0F\u20E3"
THREE_EMOJI = "\u0033\uFE0F\u20E3"
EXCLAM_EMOJI = "\u26A0\uFE0F"
FIRE_EMOJI = "\U0001F525"
SHIP_EMOJI = "\U0001F680"
CELEBRATE_EMOJI = "\U0001F389"
CARD_EMOJI = "\U0001F4B3"

# Функция для заполнения шаблона документа
def fill_template(template_path, output_path, data):
    # Загрузка шаблона
    doc = Document(template_path)

    # Замена плейсхолдеров на данные
    for paragraph in doc.paragraphs:
        # Флаг, чтобы проверить, были ли изменения в параграфе
        replaced = False

        # Проходим по всем run в параграфе
        for run in paragraph.runs:
            for key, value in data.items():
                placeholder = f"{{{{{key}}}}}"  # Плейсхолдер в формате {{key}}
                if placeholder in run.text:
                    # Заменяем плейсхолдер на значение, сохраняя форматирование
                    run.text = run.text.replace(placeholder, str(value))
                    replaced = True

        # Если плейсхолдер не найден в runs, проверяем весь текст параграфа
        if not replaced:
            for key, value in data.items():
                placeholder = f"{{{{{key}}}}}"
                if placeholder in paragraph.text:
                    # Заменяем текст в параграфе (без сохранения форматирования)
                    paragraph.text = paragraph.text.replace(placeholder, str(value))

    # Сохранение нового документа
    doc.save(output_path)
