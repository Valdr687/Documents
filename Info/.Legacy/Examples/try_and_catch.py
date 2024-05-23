variable = ""
run= True
while run:
    variable = input('Phrase : ')
    try:
        variable = int(variable)
    except ValueError:
        print("Merci d'entrer un nombre.")