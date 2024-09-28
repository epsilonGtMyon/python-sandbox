import logging
import logging.config

import yaml

# fileConfigよりもdictConfigのがいいらしい
# https://docs.python.org/ja/3/library/logging.config.html#logging-config-dictschema

def load_log_setting():
  """
  ログ設定の読み込み
  """
  with open("logging_sandbox02.yaml", encoding='utf-8') as f:
    log_dict = yaml.full_load(f)
    # print(log_dict)
    logging.config.dictConfig(log_dict)
