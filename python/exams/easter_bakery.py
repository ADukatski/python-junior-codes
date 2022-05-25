flour_price_kg = float(input())
kg_flour = float(input())
kg_sugar = float(input())
number_pack_eggs = int(input())
packages_maya = int(input())

flour_price = kg_flour * flour_price_kg
sugar_price = flour_price_kg - (flour_price_kg * 0.25)
price_eggs = flour_price_kg + (flour_price_kg * 0.10)
price_maya = sugar_price - (sugar_price * 0.80)
sum_sugar = sugar_price * kg_sugar
sum_eggs = number_pack_eggs * price_eggs
sum_maya = packages_maya * price_maya
total = flour_price + sum_maya + sum_sugar + sum_eggs

print(f"{total:.2f}")
