budget = float(input())
kg_flour = float(input())

kg_eggs = kg_flour * 0.75
one_l_milk = kg_flour + (kg_flour * 0.25)

bread_price = kg_eggs + kg_flour + one_l_milk * 0.25
# 1 pack eggs , 1 kg flour and 250ml milk

loaf = 0
colored_eggs = 0

while budget >= bread_price:

    loaf += 1
    budget -= bread_price
    colored_eggs += 3

    if loaf % 3 == 0:
        colored_eggs -= (loaf - 2)


print(f'You made {loaf} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
