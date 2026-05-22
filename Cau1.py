price = float(input("Nhập đơn giá của sản phẩm: "))
quantity = int(input("Nhập số lượng mua: "))

total = price * quantity

if total >= 1000000:
    total = total - total * 0.1
    print(f"Số tiền khách phải thanh toán là: {total}")
else:
    print(f"Số tiền khách phải thanh toán là: {total}")
    