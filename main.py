inputfile = str(input('Имя исходного файла: '))
outputfile = str(input('Имя конеченого файла: '))
our_file = open(inputfile)
results = open(outputfile,'w')
lowest = float(input('Начальная масса: '))
highest = float(input('Конечная масса: '))
for line in our_file.readlines():
    strline = str(line).split(';')
    time = strline[0]
    print(time)
    mass = 0
    sum_int = 0
    for i in range(1, int((len(strline) - 1) / 2) + 1):
        if strline[2*i-1] != '' and strline[2*i] != '':
            mass = float(strline[2*i-1])
            intens = float(strline[2*i])
            if (mass <= highest) and (mass >= lowest):
                sum_int += intens
            try:
                time = float(time)
            except:
                print('error')

    results.write(str(time)+';'+str(sum_int)+'\n')

our_file.close()
results.close()
