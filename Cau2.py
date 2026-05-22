password = '123456'
count = 0
while count != 3:
    input_password = int(input("Vui lòng nhập mật khẩu: "))
    
    if input_password == int(password):
        print("Đăng nhập thành công!")
        break
    else:
        count +=1 
        print("Mật khẩu sai, Vui lòng nhập lại!")
    
    if count == 3:
        print("Tài khoản bị khóa!")
        break
        