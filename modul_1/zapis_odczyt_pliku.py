with open('../modul2_wyciek_hasla/odczyt.txt') as input_file, open('zapis.txt', mode='w') as output_file:
    sum =0
    for line in input_file:
        number = int(line.strip())
        sum += number
    output_file.write(str(sum))
