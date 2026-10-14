import logging

from .tools import IMG_DIR, try_click_button, config, CONFIRM_BUTTON, BACK_BUTTON
from dataclasses import fields
import time

SOCIAL_ICON = str(IMG_DIR / 'social/social_icon.png')
CLUB_ICON = str(IMG_DIR / 'social/club_icon.png')

logger = logging.getLogger(__name__)

def run_social():
    if not any(getattr(config.social, field.name) for field in fields(config.social)):
        logger.info("Social automation skipped")
        return
    logger.info("Social automation started")

    time.sleep(5)
    while not try_click_button(SOCIAL_ICON):
        time.sleep(1)
        logger.debug("social icon not found")
    logger.info("Social button clicked")
    time.sleep(1)
    try_click_button(CLUB_ICON)
    logger.info("Club button clicked")
    time.sleep(3)
    # INFO: 2 times in case early detection
    try_click_button(CONFIRM_BUTTON, 0.85)
    time.sleep(2)
    try_click_button(CONFIRM_BUTTON, 0.85)
    logger.info("Confirm button clicked")
    time.sleep(2)
    try_click_button(BACK_BUTTON)
    logger.info("Return button clicked")
    time.sleep(5)
    logger.info("Social automation finished")