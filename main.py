def while_else():
    # list of fruits
    my_list = ['papaya', 'banana', 'pineapple', 'mango', 'grapes']
    new_fruit = input('Welche Frucht möchten Sie der Liste ergänzen?\n')

    size = len(my_list)  # length/size of the list
    i = 0

    # iterating through the fruit list
    while i < size:
        if my_list[i] == new_fruit:
            print('Frucht bereits vorhanden')
            break
        i += 1
    else:
        my_list.append(new_fruit)

    print(f'Inhalt der Liste: {my_list}')

def if_in():
    # list of fruits
    my_list = ['papaya', 'banana', 'pineapple', 'mango', 'grapes']
    new_fruit = input('Welche Frucht möchten Sie der Liste ergänzen?\n')

    if new_fruit in my_list:
        print('Frucht bereits vorhanden')
    else:
        my_list.append(new_fruit)

    print(f'Inhalt der Liste: {my_list}')

if __name__ == '__main__':
    while_else()
    if_in()
