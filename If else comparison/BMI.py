#golongan berat badan

BB = int(input('Masukkan berat badan  (kg) = '))
TB = float(input('Masukkan tinggi badan (m) = '))

BMI = BB / (TB * TB)

if float(BMI) <= 17:
    print('Hasil IMT = ',BMI,'=> Kurus, kekurangan berat badan berat')
elif 17 < float(BMI) <= 18.4:
    print('Hasil IMT = ',BMI,'=> Kurus, kekurangan berat badan ringan')
elif 18.4 < float(BMI) <= 25.0:
    print('Hasil IMT = ',BMI,'=> Normal')
elif 25.0 < float(BMI) <= 27.0:
    print('Hasil IMT = ',BMI,'=> Gemuk, kelebihan berat badan ringan')
else:
    print('Hasil IMT = ',BMI,'=> Gemuk, kelebihan berat badan berat')
