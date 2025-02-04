from constant import Constant

import datetime

with open(Constant.Basic.buildTimeFile, 'w', encoding='utf-8') as f:
    f.write(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))

