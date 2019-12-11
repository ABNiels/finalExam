import sys

def main():
    temp_ll = eval(sys.argv[1])
    file = open('sensor_temp.txt', 'r')

    runningSum = 0;
    underTemp = 0; 
    numTemp = 0;
    for line in file.read().split('\n')[2:-1]:
        numTemp += 1
        runningSum += eval(line)
        if eval(line) < temp_ll:
            underTemp += 1

    average = runningSum / numTemp

    print('''
        CPE 422/522 Final Exam
File name of sensor temperatures: {0}
Number of temperatures below {1}: {2}
Average Temperature: {3}
'''.format(sys.argv[0], temp_ll, underTemp, average))

if __name__ == "__main__":
    main()
