size_of_storage = float(input())

counter = 0

while True:
    case_size = input()

    if case_size == "End":
        print(f"Congratulations! All suitcases are loaded!")
        break
    else:
        case_size = float(case_size)

    if case_size > size_of_storage:
        print(f"No more space!")
        break

    size_of_storage -= case_size
    counter += 1

    if counter % 3 == 0:
        size_of_storage -= case_size * 0.10
        if size_of_storage < 0:
            print(f"No more space!")
            counter -= 1
            break

print(f"Statistic: {counter} suitcases loaded.")
