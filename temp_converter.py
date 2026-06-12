temp = input("What is the temperature?")
choice = input("Converte (F) to (c)?")
choice = choice.upper()
temp = float(temp)

if choice == 'F':
    result = (temp - 32) *5/9
    print (f"{temp :0.1f} F = {result :0.1f} C")

elif choice =='C':
    result = (temp * 9/5) + 32
    print (f"{temp :0.1f} C = {result :0.1f} F")