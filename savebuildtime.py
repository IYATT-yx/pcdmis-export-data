import datetime

with open('buildtime.py', 'w', encoding='utf-8') as f:
    f.write(f'buildTime = \'{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}\'\n')