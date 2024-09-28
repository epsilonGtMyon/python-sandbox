from app.sandbox02 import log_setting

# yamlから読み込む
log_setting.load_log_setting()

from app.sandbox02 import sandbox02


sandbox02.doMain()
