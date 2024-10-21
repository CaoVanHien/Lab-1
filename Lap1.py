# Mã màu ANSI cho màu trắng và xanh lam
WHITE = '\u001b[47m'  # Nền trắng
BLUE = '\u001b[44m'   # Nền xanh lam
END = '\u001b[0m'     # Đặt lại màu về mặc định

# Tạo hình ảnh lá cờ Phần Lan trong terminal
for i in range(9):  # Tạo 9 dòng cho lá cờ
    if 3 <= i <= 5:  # Các dòng 4, 5, 6 có dải màu xanh ngang
        print( BLUE + " " * 40 + END)
    else:  # Các dòng còn lại là nền trắng với dải xanh dọc
        print(WHITE + " " * 10 + BLUE + " " * 7 + WHITE + " " * 23 + END)
print()





import math

def draw_two_circles_touching(radius):
    diameter = 2 * radius
    for y in range(-radius, radius + 1):
        for x in range(-radius * 2, radius * 2 + 1):
            # Hình tròn thứ nhất (tâm ở vị trí (-radius, 0))
            if math.sqrt((x + radius)**2 + y**2) <= radius:
                print("*", end="")
            # Hình tròn thứ hai (tâm ở vị trí (radius, 0))
            elif math.sqrt((x - radius)**2 + y**2) <= radius:
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Xuống dòng sau mỗi hàng

# Gọi hàm với bán kính là 5
draw_two_circles_touching(5)
print ()






def plot_function():
    height = 9   # Số dòng theo chiều Y
    width = 18   # Chiều rộng theo chiều X (gấp đôi để phù hợp với tỷ lệ)
    
    for y in range(height, -1, -1):  # Lặp qua từng dòng từ dưới lên
        line = ""
        for x in range(width + 1):   # Lặp qua từng ký tự trong một dòng
            if x == 0 and y == 0:
                line += "+"  # Điểm giao nhau của hai trục
            elif x == 0:
                line += "|"  # Trục Y
            elif y == 0:
                line += "_"  # Trục X
            elif y == x // 2:  # Kiểm tra xem điểm có thuộc đồ thị y = x / 2 không
                line += "*"
            else:
                line += " "  # Khoảng trống
        print(line)

plot_function()
print()





def filter_number():
    # Mã màu cho terminal
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'
    
    # Mở file an toàn và xử lý lỗi nếu không tìm thấy
    try:
        with open('d:/ProjectPython/Lab-1/sequence.txt', 'r') as file:
            filtered_list = []  # Đổi tên biến list
            count = 0
            count_all = 0
            
            for line in file:
                number = line.strip()
                if number:  # Kiểm tra xem dòng có rỗng không
                    try:
                        num = float(number)
                        count_all += 1
                        # Điều kiện lọc
                        if (5 <= num <= 10) or (-10 <= num <= -5):
                            filtered_list.append(num)
                            count += 1
                    except ValueError:
                        print(f"Không thể chuyển đổi '{number}' thành số thực. Bỏ qua dòng.")
            
            # Tính tỷ lệ phần trăm
            if count_all > 0:
                percent = (count / count_all) * 100
            else:
                percent = 0

            # In ra kết quả
            print("List: ", end="")
            print(filtered_list)
            
            print(f'{GREEN}{"  "}{END}{" Từ 5 đến 10 và Từ -10 đến -5 | Số lượng: "}{count}{" | Tỷ lệ phần trăm: "}{round(percent , 1)}{" %"}')
            print(f'{RED}{"  "}{END}{" Các số khác | Số lượng: "}{count_all - count}{" | Tỷ lệ phần trăm: "}{round(100-percent , 1)}{" %"}')

    except FileNotFoundError:
        print("Lỗi: Không tìm thấy tệp 'sequence.txt'.")

# Gọi hàm
filter_number()
print()




import os
import time

def clear_console():
    # Sử dụng 'cls' cho Windows, 'clear' cho các hệ điều hành khác
    os.system('cls' if os.name == 'nt' else 'clear')

def animation():
    frames = [
        "Khung hình 1: 🌟",
        "Khung hình 2: 🌙",
        "Khung hình 3: 🌈"
    ]
    
    while True:
        for frame in frames:
            clear_console()  # Làm sạch console
            print(frame)     # In khung hình hiện tại
            time.sleep(2)    # Tạm dừng 2 giây giữa các khung hình

# Gọi hàm hoạt ảnh
animation()
