import logging
from pathlib import Path
from config import config
import pyautogui
import cv2

IMG_DIR = Path(__file__).resolve().parent.parent / 'target_buttons'

RECONNECT_BUTTON = str(IMG_DIR / 'reconnect_button.png')
CLOSE_NOTICE_BUTTON = str(IMG_DIR / 'close_notice_button.png')
CONFIRM_BUTTON = str(IMG_DIR / 'confirm_button.png')
BACK_BUTTON = str(IMG_DIR / 'back_button.png')

logger = logging.getLogger(__name__)

def try_click_button(button, confidence=0.9) -> bool:
    try:
        pos = pyautogui.locateOnScreen(button, confidence=confidence)
    except pyautogui.ImageNotFoundException:
        return False
    if pos is not None:
        pyautogui.click(pos.left+pos.width/2, pos.top+pos.height/2)
        logger.debug(f"{button} clicked")
    return True

def try_locate(img, confidence=0.9) -> bool:
    try:
        pyautogui.locateOnScreen(img,confidence=confidence)
        return True
    except pyautogui.ImageNotFoundException:
        return False

def reconnect() -> bool:
    if try_click_button(RECONNECT_BUTTON):
        logger.debug("reconnect executed")
        return True
    return False

def close_notice() -> bool:
    if try_click_button(CLOSE_NOTICE_BUTTON):
        logger.debug("notice closed")
        return True
    return False