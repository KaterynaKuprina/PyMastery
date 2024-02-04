run_time = [10, 15, 20, 25, 30]
kcal_min = 4.2
kcal_time = []

for i in run_time:
    kcal_time.append(i * kcal_min)
    print(f'{i}min - {i * kcal_min} kcal')