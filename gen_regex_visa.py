import exrex
import random
from tqdm import tqdm
random.seed(0)

MAX_NUMBER = 10000


key_search = {
    1: ['SỐ|No', '[A-Z]{1,2} \d{7}'],
    2: ['KÝ HIỆU|Category', 
        'DL|DN|' * 5 + \
        'DH|LĐ|' * 2 + \
        'NG[1-4]|' + \
        'LV[1-2]|' + \
        'HN|TT|VR|SQ|LS|EV|' + \
        'NN[1-3]|' + \
        'PV[1-2]|' + \
        'ĐT(|[1-4])|' + \
        'DN[1-2]|' + \
        'LĐ[1-2]|' + \
        'C1|' + \
        '[A-Z]{1,2}(|[1-4])'],
    3: ['CÓ GIÁ TRỊ TỪ NGÀY|Valid from|ĐẾN NGÀY|until|NGÀY|On', 
        '([12]\d|3[01])' + \
        '(( (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (|20[0-4]\d))|' + \
        '(\/(0[1-9]|1[0-2])\/20[0-4]\d)|' + \
        '(\.(0[1-9]|1[0-2])\.20[0-4]\d))'],
    5: ['SỬ DỤNG MỘT\/NHIỀU LẦN|SU DUNG MOT\/NHIEU LAN|Good for single \/ multiple entries', \
        '01 lần|Nhiều lần|Single entry|Multiple entries|Một lần\/ Single|Single\/Mot Lan|Nhiều lần\/Multiple|Multiple/Nhieu lan'],
    6: ['CẤP CHO NGƯỜI MANG HỘ CHIẾU SỐ|Issued to the holder of passport No', '[A-Z0-9]{9}'],
    7: ['CẤP TẠI|Issued at', \
    'Tân Sơn Nhất|TP.HCM|Nội Bài|Hà Nội|Đà Nẵng|HOA KY|CACK TSN|' * 5 + \
    'Battambang|Mộc Bài|Ottawa|New Delhi|Manila|Vientiane|Sihanoukville']
}

for key in key_search:
    print('key: ', key)
    with open('gen_regex/visa/'+str(key)+'.txt', 'w') as f:
        for i in tqdm(range(MAX_NUMBER)):
            if i % 11 != 10:
                output = exrex.getone(key_search[key][1])
            else:
                output = exrex.getone(key_search[key][0])
            if len(output) != 0:
                f.write(output.strip() + '\n')
