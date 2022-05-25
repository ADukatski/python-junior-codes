period = int(input())

day_counter = 1
reviewed_patient = 0
non_reviewed_patient = 0
doctors = 7

for p in range(1, period + 1):
    patients = int(input())

    if day_counter % 3 == 0:
        if non_reviewed_patient > reviewed_patient:
            doctors += 1
    else:
        pass

    if patients > doctors:
        non_reviewed_patient += patients - doctors
        reviewed_patient += doctors
    elif patients <= doctors:
        reviewed_patient += patients

    day_counter += 1

print(f"Treated patients: {reviewed_patient}.")
print(f"Untreated patients: {non_reviewed_patient}.")