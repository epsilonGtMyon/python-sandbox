import logging
import time
from app.sandbox02 import module01

logger = logging.getLogger(__name__)


def doMain():
  logger.debug("doMain:debug")
  logger.info("doMain:info")
  logger.warning("doMain:warning")
  logger.error("doMain:error")
  logger.info("doMain:日本語")

  module01.execute()

  for i in range(1, 10):
    logger.info(i)
    time.sleep(2)

  try:
    x = 1 / 0
  except ZeroDivisionError:
    # エラーの情報は自動で出力されるそうだ
    logging.exception("0で割られた")

