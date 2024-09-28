import logging
logger = logging.getLogger(__name__)

def execute():
  logger.debug("execute:debug")
  logger.info("execute:info")
  logger.warning("execute:warning")
  logger.error("execute:error")
  