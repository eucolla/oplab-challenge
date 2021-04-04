# bubble sort()

def bubblesort(sequence):

    number = len(sequence)

    for n in range(number - 1):
        flag = 0
        for i in range(number - 1):
            if sequence[i] > sequence[i + 1]:
                tmp = sequence[i]
                sequence[i] = sequence[i + 1]
                sequence[i + 1] = tmp
                flag = 1
        if flag == 0:
            break
    return sequence

# Implementation bubble sort


num = int(input('Enter the amount of values: '))
value = list()
for c in range(1, num + 1):
    x = int(input(f'Enter the {c}# value: '))
    while x in value:
        print('Existing value!')
        x = int(input(f'Enter the {c}# value: '))

    value.append(x)

print(f'The generated list is: {value}')

x = value

result = bubblesort(value)

print(f'The bubble sort is: {result}')

# Tá pronto o sorvetinho
