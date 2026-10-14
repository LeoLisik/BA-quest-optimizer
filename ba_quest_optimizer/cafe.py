import logging

import pyscreeze
from .tools import config, IMG_DIR, try_click_button, try_locate, close_notice, CONFIRM_BUTTON, BACK_BUTTON
from dataclasses import fields
import time
import pyautogui

CAFE_ICON = str(IMG_DIR / 'cafe/cafe_icon.png')
CAFE_CHARACTER_MARK = str(IMG_DIR / 'cafe/character_mark.png')
CAFE_INVITATION_BUTTON = str(IMG_DIR / 'cafe/invite_button.png')
CAFE_STUDENT_INVITATION_BUTTON = str(IMG_DIR / 'cafe/invite_student_button.png')
CAFE_SWITCH_BUTTON = str(IMG_DIR / 'cafe/cafe_switch.png')
CAFE_EARNINGS_BUTTON = str(IMG_DIR / 'cafe/cafe_earnings.png')
CAFE_EARNINGS_CLAIM_BUTTON = str(IMG_DIR / 'cafe/cafe_claim.png')

CAFE_CHARACTERS_SEARCH_TIME = 60

logger = logging.getLogger(__name__)

def cafe_click_characters():
    timer = time.monotonic()
    while time.monotonic() - timer < CAFE_CHARACTERS_SEARCH_TIME:
        try:
            pos = pyscreeze.locateOnScreen(
            CAFE_CHARACTER_MARK,
            confidence=0.43
        )
        except pyscreeze.ImageNotFoundException as ex:
            logger.debug(f"not enough confidence for character\n{ex}")
            pos = None
        if pos is not None:
            pyautogui.click(pos.left + 100, pos.top + 20)
            logger.info("character found and clicked")
            # wait for animation
            time.sleep(4)
            pyautogui.click(pyautogui.size().width/2,pyautogui.size().height/2)

# FIXME: Unstable student number that will be clicked
def cafe_invite_character(character_number = 0):
    while not try_click_button(CAFE_INVITATION_BUTTON):
        logger.debug("cafe invitation button not found")
        time.sleep(2)
    logger.info("Invite button clicked")
    # wait for list to show
    time.sleep(1)

    matches = None
    while not matches:
        img = pyautogui.screenshot()
        try:
            matches = list(pyautogui.locateAll(CAFE_STUDENT_INVITATION_BUTTON, img, confidence=0.9))
        except pyautogui.ImageNotFoundException:
            logger.debug("invitation buttons not found")
            matches = None
    logger.info("Invitation buttons found")

    matches.sort(key=lambda box: box.top)
    target_box = matches[character_number]
    pyautogui.click(pyautogui.center(target_box))
    logger.info(f"Invite character {character_number} clicked")

    # wait for confirmation to show
    time.sleep(2)
    try_click_button(CONFIRM_BUTTON)
    logger.info("Confirm button clicked")
    # time of inviting
    time.sleep(3)

def cafe_collect_earnings():
    try_click_button(CAFE_EARNINGS_BUTTON)
    logger.info("Earnings button clicked")
    # wait for animation
    time.sleep(1)
    try_click_button(CAFE_EARNINGS_CLAIM_BUTTON)
    logger.info("Earnings claim button clicked")
    time.sleep(3)
    pyautogui.click()
    time.sleep(1)
    close_notice()
    logger.info("Close earnings notice clicked")
    time.sleep(1)

def run_cafe():
    if not any(getattr(config.cafe, field.name) for field in fields(config.cafe)):
        logger.info("Cafe automation skipped")
        return
    logger.info("Cafe automation started")

    time.sleep(5)
    while not try_click_button(CAFE_ICON):
        logger.debug("cafe button not found")
        time.sleep(1)
    logger.info("Cafe button clicked")

    # INFO: wait for load
    while not try_locate(CAFE_SWITCH_BUTTON):
        logger.debug("searching for cafe...")
        time.sleep(2)
    time.sleep(1)
    logger.info("Cafe found")

    # INFO: 2 times in case early detection
    for i in range(2):
        try_click_button(CONFIRM_BUTTON)
        time.sleep(2)
    logger.info("Visit students confirm clicked or skipped")

    if config.cafe.collect_earnings:
        cafe_collect_earnings()

    if config.cafe.invite_cafe_1:
        cafe_invite_character(0)

    if config.cafe.characters_touch_cafe_1:
        cafe_click_characters()

    if not config.cafe.invite_cafe_2 or not config.cafe.characters_touch_cafe_2:
        logger.info("Second cafe skipped")
        return

    while not try_click_button(CAFE_SWITCH_BUTTON):
        logger.warning("cafe switch button not found")
        time.sleep(1)
    logger.info("Cafe switch button clicked")
    # INFO: wait for load
    while not try_locate(CAFE_SWITCH_BUTTON):
        logger.debug("searching for cafe 2...")
        time.sleep(2)
    logger.info("Cafe 2 found")
    time.sleep(1)

    # INFO: 2 times in case early detection
    for i in range(2):
        try_click_button(CONFIRM_BUTTON)
        time.sleep(2)
    logger.info("Visit students confirm clicked or skipped")

    if config.cafe.invite_cafe_2:
        cafe_invite_character(1)

    if config.cafe.characters_touch_cafe_2:
        cafe_click_characters()

    time.sleep(2)
    try_click_button(BACK_BUTTON)
    logger.info("Return button clicked")
    time.sleep(5)
    logger.info("Cafe automation finished")