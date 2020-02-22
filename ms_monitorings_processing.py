inputfile = str(input('Имя исходного файла: '))
outputfile = str(input('Имя конеченого файла: '))
our_file = open(inputfile)
results = open(outputfile, 'w')
lowest = float(input('Начальная масса: '))
highest = float(input('Конечная масса: '))
for line in our_file.readlines():
    strline = str(line).split(',')
    time = strline[0]
    print(time)
    mass = 0
    sum_int = 0
    for i in range(8, len(strline)):
        data = strline[i].split(' ')
        mass = float(data[0])
        intens = float(data[1])
        if (mass <= highest) and (mass >= lowest):
            sum_int += intens
        try:
            time = float(time)
        except:
            print('error')

    results.write(str(time) + ';' + str(sum_int) + '\n')

our_file.close()
results.close()
