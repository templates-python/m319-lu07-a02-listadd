def while_else():
    # list of fruits
    my_list = ['papaya', 'banana', 'pineapple', 'mango', 'grapes']
    new_fruit = input('Welche Frucht möchten Sie der Liste ergänzen?\n')


    #TODO: Iterieren Sie über die Liste der Früchte um zu überprüfen ob new_fruit bereits in der Liste ist,
    # ist die Frucht new_fruit vorhanden, geben Sie aus 'Frucht bereits vorhanden'
    # ist new_fruit nicht vorhanden, so fügen Sie diese der Liste hinzu.
    # Verwenden Sie dazu eine while-else-Anweisung


    print(f'Inhalt der Liste: {my_list}')

def if_in():
    # list of fruits
    my_list = ['papaya', 'banana', 'pineapple', 'mango', 'grapes']
    new_fruit = input('Welche Frucht möchten Sie der Liste ergänzen?\n')

    # TODO: Prüfen Sie mit if-in ob die Frucht new_fruit schon der Liste my_list existiert.
    # ist die Frucht new_fruit vorhanden, geben Sie aus 'Frucht bereits vorhanden'
    # ist new_fruit nicht vorhanden, so fügen Sie diese der Liste hinzu.

    print(f'Inhalt der Liste: {my_list}')

if __name__ == '__main__':
    while_else()
    if_in()
