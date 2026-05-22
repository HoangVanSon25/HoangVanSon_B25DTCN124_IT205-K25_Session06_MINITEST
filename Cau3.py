number_of_valid_packages = int(input("Số thùng hàng hợp lệ: "))
total_product = 0
total_packages = 0
for i in range(number_of_valid_packages):
    print(f"Nhập số lượng của thùng thứ {i+1}")
    total_number_of_products = int(input("Nhập số lượng sản phẩm: "))
    
    if number_of_valid_packages == 0 :
        break
    else:
        if total_number_of_products < 0:
            print("Số lượng không hợp lệ, bỏ qua thùng này!")
            continue
    
        if total_number_of_products == 0:
            continue
                
        if total_number_of_products > 0 :
            total_product += total_number_of_products
            total_packages += 1
        
print(f"Tổng số thùng hàng đã đếm: {total_packages}")
print(f"Tổng số sản phẩm thu được: {total_product}")
        