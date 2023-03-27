import exrex
import random
random.seed(0)

MAX_NUMBER = 10000


key_search = {
    0: ['Biển đăng ký:', '\(Registration Number\)', '\d{2}[A-Z]-(\d{3}\.\d{2}|\d{4})'],
    1: ['Số quản lý:', '\(Vehicle Inspection No\.\)', '\d{4}[A-Z]-\d{6}'],
    2: ['Loại phương tiện: (Type)', None, 'ô tô tải (\(có mui\)|\(có mui phủ bạt\)|\(thùng kín\)|\(có cần cẩu\)|)|ô tô đầu kéo|ô tô con'],
    3: ['Nhãn hiệu: (Mark)', None, 'SUZUKI|KIA|TRUONGGIANG|FUSO|GIAIPHONG|CHEVROLET|HINO|HONDA|CNHTC|SONGHUAJIANG|THACO|MITSUBISHI FUSO|DONGFENG|HUYNDAI|ISUZU|VIETRUNG|DONGBEN|FOTON|CHENGLONG|TERACO|DOTHANH|HYUNDAI|TOYOTA|MERCEDES-BENZ|VINAXUKI|DAIVIET|MITSUBISHI|TRUONgGIANG|VINHPHAT|JAC|LEXUS|VEAM|VIETTRUNG|TMT'],
    4: ['Số loại: (Model code)', None, '[0-9A-Z]{1}[0-9A-Z\/\-\. ]{3,20}[0-9A-Z]{1}'],
    5: ['Số máy: (Engine Number)', None, '[0-9A-Z]{1}[0-9A-Z\*\-\. ]{5,20}'],
    6: ['Số khung: (Chassis Number)', None, '(([A-Z]{2}[0-9A-Z]{1})|(R{1}(R|L|N)[0-9A-Z]{1}))[0-9A-Z]{5}[0-9A-Z]{3}(|-)\d{6}'],
    7: ['Năm, Nước sản xuất:', '\(Manufactured Year and Country\)', '(199\d|20[0-2]\d), (Việt Nam|Việt Nam|Việt Nam|Việt Nam|Việt Nam|Hàn Quốc|Nhật Bản|Indonesia|Thái Lan|Trung Quốc|Mỹ)'],
    8: ['Niên hạn SD:', '\(Lifetime limit to\)', '(20[2-4]\d)'],
    9: [None, 'Kinh doanh vận tải \(Commercial Use\)', '-|X'],
    10: [None, 'Cải tạo \(Modification\)', '-|X'],
    11: ['Công thức bánh xe', '\(Wheel Formula\)', '[2468]{1}[x]{1}[24]{1}'],
    12: [None, 'Vết bánh xe|\(Wheel Tread\)', '1\d{3}[/]{1}1\d{3}'],
    13: [None, 'Kích thước bao: \(Overall Dimension\)', '([3-9]{1}\d{2}[05]{1}|1[0-3]{1}\d{2}[05]{1}) x [1-3]{1}\d{2}[05]{1} x [1-3]{1}\d{2}[05]{1}'],
    14: [None, 'Kích thước lòng thùng xe|\(Inside cargo container dimension\)', '[1-9]{1}\d{2}[0]{1}x[1-2]{1}\d{2}[05]{1}x([1-2]{1}|)\d{2}[05]{1}(|||| \(\d{2}[05]{1}\))'],
    15: ['Chiều dài cơ sở: (Wheelbase)', None, '[1-5]{1}\d{2}[05]{1}(||||||\+[1-5]{1}\d{2}[05]{1}){2}'],
    16: [None, 'Khối lượng bản thân: \(Kerb mass\)', '(([89]{1}\d{1}[05]{1})|([1-3](|\,){1}\d{2}[05]{1}))(| \(kg\)| \(kg\)| \(kg\))'],
    17: [None, 'Khối lượng hàng CC theo TK/CP TGGT:|\(Design/Authorized pay load\)', '(([3-9]{1}\d{1}|[1-9]{1}\d{2}|[12]\d{3})[05]{1})'],
    18: [None, 'Khối lượng toàn bộ theo TK/CP TGGT:|(Design/Authorized total mass)', '([1-9]{1}\d{2}|[12]\d{3})[05]{1}'],
    19: [None, 'Khối lượng kéo theo TK/CP TGGT:|(Design/Authorized towed mass)', None],
    20: ['Số người cho phép chở:', '\(Permissible No. of Pers Carried: seat, stood place, laying place\)', '\d chỗ ngồi, 0 chỗ đứng, (0|[0-4]) chỗ nằm'],
    21: ['Loại nhiên liệu: (Type of Fuel Used)', None, 'Xăng|Diesel'],
    22: [None, 'Thể tích làm việc của động cơ: \(Engine Displacement\)', '\d{3,4} \(cm3\)'],
    23: ['Công suất lớn nhất/tốc độ quay: (Max. output/rpm)', None, '\d{2,3}(|||||\.5)\(kW\)\/\d{2}00vph'],
    24: ['Số sê-ri: (No.)', None, '[EDK][AD]-\d{7}'],
    25: [None, 'Số lượng lốp, cỡ lốp/trục \(Number of tires: Tire size\/axle\)', '[1112223456]: [2222468]; (1[1-9]|[5-9])\.\d[05](R|-)1\d(|||||\((1[1-9]|[5-9])\.\d[05](R|-)1\d\))'],
    26: [None, 'Số phiếu kiểm định|\(Inspection Report No\)', '\d{4}[A-Z]-\d{5}\/2[12]'],
    27: ['(Valid until)', 'Có hiệu lực đến hết ngày', '([12]\d|3[01])\/(0[1-9]|1[0-2])\/20[1-5]\d'],
    28: [None, '\(Issued on: Day/Month/Year\)', '(An Giang|Kon Tum|Bà Rịa – Vũng Tàu|Lai Châu|Bắc Giang|Lâm Đồng|Bắc Kạn\
|Lạng Sơn|Bạc Liêu|Lào Cai|Bắc Ninh|Long An|Bến Tre|Nam Định|Bình Định|Nghệ An|Bình Dương|Ninh Bình\
|Bình Phước|Ninh Thuận|Bình Thuận|Phú Thọ|Cà Mau|Phú Yên|Cần Thơ|Quảng Bình|Cao Bằng|Quảng Nam|Đà Nẵng\
|Quảng Ngãi|Đắk Lắk|Quảng Ninh|Đắk Nông|Quảng Trị|Điện Biên|Sóc Trăng|Đồng Nai|Sơn La|Đồng Tháp|Tây Ninh\
|Gia Lai|Thái Bình|Hà Giang|Thái Nguyên|Hà Nam|Thanh Hóa|Hà Nội|Thừa Thiên Huế|Hà Tĩnh|Tiền Giang\
|Hải Dương|TP Hồ Chí Minh|Hải Phòng|Trà Vinh|Hậu Giang|Tuyên Quang|Hòa Bình|Vĩnh Long|Hưng Yên|Vĩnh Phúc\
|Khánh Hòa|Yên Bái|Kiên Giang), ngày ([12]\d|3[01]) tháng (0[1-9]|1[0-2]) năm (19\d{2}|20[0-4]\d)'],
    29: [None, 'Có lắp thiết bị giám sát hành trình \(Equipped with Tachograph\)', '-|X'],
    30: [None, 'Có lắp camera / \(Equipped with camera\)', '-|X'],
    31: [None, 'Không cấp tem kiểm định \(Inspection stamp was not issued\)', '-|X'],
    32: ['Ghi chú:', None, None]
}

for key in key_search:
    print('key: ', key)
    with open('gen_regex/'+str(key)+'.txt', 'w') as f:
        for i in range(MAX_NUMBER):
            print(key_search[key][2])
            if key_search[key][2] != None:
                val = exrex.getone(key_search[key][2])
                print(val)

                output = val
                if key == 15:
                    output = val
                elif key == 17 or key == 18:
                    output = val + '/' + val + exrex.getone('(| \(kg\)| \(kg\)| \(kg\))')
                else:
                    output = ' ' + val
            else:
                output = ''

            if i % 10 != 9:
                if key_search[key][0] != None:
                    output = key_search[key][0] + output
            else:
                if key_search[key][1] != None:
                    output = exrex.getone(key_search[key][1])
            if len(output) != 0:
                f.write(output.strip() + '\n')
