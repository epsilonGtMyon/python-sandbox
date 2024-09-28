import logging
import logging.handlers

logging.root.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - [%(levelname)s] [%(name)s] - %(message)s')
# ---------------
# StreamHandler
st_handler = logging.StreamHandler()
# LevelはHandlerやLoggerどちらにも設定できる。Handlerが優先
st_handler.setLevel(logging.INFO)

st_handler.setFormatter(formatter)

logging.root.addHandler(st_handler)
# ---------------
# FileHandler
f_handler = logging.FileHandler("./logs/sandbox01.log")

f_handler.setFormatter(formatter)
logging.root.addHandler(f_handler)
# ---------------


logger = logging.getLogger(__name__)

def print_hello():
  logger.debug("Hello debug")
  logger.info("Hello info")
  logger.warning("Hello warning")
  logger.error("Hello error")
  logger.critical("Hello critical")

if __name__ == "__main__":
  print_hello()