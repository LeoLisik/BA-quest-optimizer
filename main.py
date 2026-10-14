import os
import sys
from pathlib import Path
import logging
import psutil
import pygetwindow as gw
import time
import pyautogui
from ba_quest_optimizer.tools import try_click_button, try_locate, config, reconnect, close_notice
from ba_quest_optimizer.cafe import run_cafe
from ba_quest_optimizer.social import run_social
import cv2

IMG_DIR = Path(__file__).resolve().parent / 'target_buttons'

CLOSE_MENU_NOTIFY_BUTTON = str(IMG_DIR / 'close_notif_button.png')
START_GAME_BUTTON = str(IMG_DIR / 'start_game_button.png')
MENU_CHECK_IMG = str(IMG_DIR / 'menu_check_img.png')
DAILY_ATTENDANCE_IMG = str(IMG_DIR / 'daily_attendance_img.png')
MENU_BUTTON = str(IMG_DIR / 'menu_button.png')

def is_game_running(process_name):
    return any(proc.name().lower() == process_name.lower() for proc in psutil.process_iter())

def maximize_game_window(window_title_part):
    windows = [w for w in gw.getWindowsWithTitle(window_title_part) if w.visible]
    if windows:
        win = windows[0]
        win.activate()
        time.sleep(1)
        win.maximize()
        return True
    return False

def press_start() -> bool:
    if try_locate(MENU_BUTTON):
        pyautogui.click(pyautogui.size().width / 2, pyautogui.size().height / 2)
        logger.debug("start pressed")
        return True
    return False

def prepare_game():
    logger.info('Prepare game started')
    while not try_locate(MENU_CHECK_IMG, confidence=0.95):
        reconnect()
        time.sleep(0.1)
        close_notice()
        time.sleep(0.1)
        press_start()
        time.sleep(1)
        try_click_button(DAILY_ATTENDANCE_IMG)
        time.sleep(1)
        logger.info('Searching for menu...')
    while not try_click_button(CLOSE_MENU_NOTIFY_BUTTON, confidence=0.9):
        time.sleep(1)
        logger.info('Searching for menu notice')
    time.sleep(3)
    logger.info('Prepare game finished')

def setup_logging():
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setLevel(config.logs_level)

    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(config.logs_level)

    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logger = logging.getLogger()
    logger.setLevel(config.logs_level)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

logger = setup_logging()
if __name__ == "__main__":
    GAME_PROCESS = config.game_process
    GAME_WINDOW = config.game_window_title
    logger.debug(f"CONFIG: {config=}")

    if config.start_game:
        os.startfile("steam://rungameid/3557620")
        logger.info("Game launched")
        time.sleep(30)

    if not is_game_running(GAME_PROCESS):
        logger.info("Game not detected, exit")
        exit()
    elif maximize_game_window(GAME_WINDOW):
        logger.info("Game window activated")
        time.sleep(2)
        pyautogui.click(pyautogui.size().width/2,pyautogui.size().height/2)
    else:
        logger.info("Game not detected, exit")
        exit()

    if config.prepare_game:
        prepare_game()
        time.sleep(1)

    run_cafe()
    run_social()
