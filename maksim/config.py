# config.py — настройки приложения
import os
import sys

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",          # ← введи свой пароль MySQL
    "database": "chitaigorod",
    "charset": "utf8mb4",
}


def get_app_dir():
    """Корневая папка приложения (работает и в exe)"""
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))


def get_resources_dir():
    return os.path.join(get_app_dir(), "resources")


# Цвета
COLOR_MAIN_BG = "#FFFFFF"
COLOR_SECONDARY_BG = "#ABCFCE"
COLOR_ACCENT = "#546F94"
COLOR_DISCOUNT_HIGH = "#23E1EF"
COLOR_OUT_OF_STOCK = "#D3D3D3"
COLOR_DISCOUNTED_PRICE = "#FF0000"
COLOR_FINAL_PRICE = "#000000"

# Шрифт
FONT_FAMILY = "Comic Sans MS"
FONT_SIZE = 11

RESOURCES_DIR = "resources"
