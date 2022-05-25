weight = int(input())
length = int(input())
height = int(input())

free_space = weight * length * height
package_counter = 0

while True:
    number_package = input()

    if number_package == "Done":
        left = abs(free_space - package_counter)
        print(f"{left} Cubic meters left.")
        break
    number_package = int(number_package)
    package_counter += number_package

    if package_counter >= free_space:
        need = abs(free_space - package_counter)
        print(f"No more free space! You need {need} Cubic meters more.")
        break