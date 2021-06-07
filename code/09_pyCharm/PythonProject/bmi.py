def bmi_calculate():
    weight_kg = float(str.replace(input("Gewicht in kg: "), ",", "."))
    size_m = float(str.replace(input("Körpergröße in m: "), ",", "."))

    bmi = weight_kg / (size_m ** 2)

    print(f'BMI is: {round(bmi)}')


bmi_calculate()