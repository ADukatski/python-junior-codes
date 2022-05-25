number_cakes = int(input())
number_pack_eggs = int(input())
number_sweets = int(input())

price_cake = number_cakes * 3.20
price_eggs = number_pack_eggs * 4.35
price_sweets = number_sweets * 5.40
paint_price = number_pack_eggs * 12 * 0.15
total = price_cake + price_eggs + price_sweets + paint_price
print(f"{total:.2f}")