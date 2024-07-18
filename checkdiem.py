import requests

def uutien(number, diemuutien):
    if number <= 22.5:
        return diemuutien
    result = ((30 - number) / 7.5) * diemuutien
    return result

sbd = input("Nhập số báo danh (SBD): ")
diemuutien = input("Nhập điểm ưu tiên (nếu có)): ")
diemuutien = eval(diemuutien)
try:
    scraping_url = "https://dantri.com.vn/thpt/1/0/99/" + sbd + "/2024/0.2/search-gradle.htm"
    payload = {}
    headers = {}
    response = requests.request(
        "GET", scraping_url, headers=headers, data=payload)
    info = response.json()['student']
    diemtoan = eval(info['toan'])
    diemvan = eval(info['van'])
    diemanh = eval(info['ngoaiNgu'])
    diemdia = 0
    if info['vatLy'] is None:
        diemly = 0;
        diemhoa = 0;
        diemsinh = 0;
        diemgdcd = eval(info['gdcd'])
        diemsu = eval(info['lichSu'])
        diemdia = eval(info['diaLy'])
    elif info['diaLy'] is None:
        diemly = eval(info['vatLy'])
        diemhoa = eval(info['hoaHoc'])
        diemsinh = eval(info['sinhHoc'])
        diemsu = 0;
        diemdia = 0;    
        diemgdcd = 0;
    diema00 = diemtoan + diemly + diemhoa
    diema01 = diemtoan + diemly + diemanh
    diemb00 = diemtoan + diemhoa + diemsinh
    diemc00 = diemvan + diemsu + diemdia
    diemd = diemtoan + diemvan + diemanh

    print("Số báo danh:" + info['sbd'])
    print("Điểm Toán: " + str(diemtoan))
    print("Điểm Văn:  " + str(diemvan))
    print("Điểm Anh:  " + str(diemanh))
    if diemly == 0:
        print("Điểm Sử:   " + str(diemsu))
        print("Điểm Địa:  " + str(diemdia))
        print("Điểm GDCD: " + str(diemgdcd))
        print("Điểm khối C00: " + format(diemc00 + uutien(diemc00, diemuutien), ".2f")+ " (điểm khi chưa cộng: " + str(diemc00) + ")")
        print("Điểm khối D:   " + format(diemd + uutien(diemd, diemuutien), ".2f")+ " (điểm khi chưa cộng: " + str(diemd) + ")")
    elif diemsu == 0:
        print("Điểm Lý:   " + str(diemly))
        print("Điểm Hoá:  " + str(diemhoa))
        print("Điểm Sinh: " + str(diemsinh))
        print("Điểm khối A00: " + format(diema00 + uutien(diema00, diemuutien), ".2f")+ " (điểm khi chưa cộng: " + str(diema00) + ")")
        print("Điểm khối A01: " + format(diema01 + uutien(diema01, diemuutien), ".2f")+ " (điểm khi chưa cộng: " + str(diema01) + ")")
        print("Điểm khối B00: "+ format(diemb00 + uutien(diemb00, diemuutien), ".2f")+ " (điểm khi chưa cộng: " + str(diemb00) + ")")
        print("Điểm khối D:   " + format(diemd + uutien(diemd, diemuutien), ".2f")+ " (điểm khi chưa cộng: " + str(diemd) + ")")
except:
    print("Gặp lỗi")