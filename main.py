import random

#Mayusculas cuando no se va cambiar algo, es una constante
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#Maquina
ROWS = 3
COLS = 3

#Simbolos
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

#Valores
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    #Chequeamos cada fila
    for line in range(lines):
        #Todos los simbolos tienen que ser igual
        symbol = columns[0][line]
        for column in columns:
            #Si los simbolos no son el mismo, quebramos
            symbol_to_check = column[line]
            if symbol!= symbol_to_check:
                break
        else:
            #Esto es que el usuario gano
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# Tenemos 3, entonces debemos esperar 3
def get_slot_machine_spin(rows, cols, symbols):
    #Esto es una lista en python
    all_symbols = []
    #Puedo tener la llave y el simbolo
    for symbol, symbol_count in symbols.items():
        #_ usamos el underscore, anonimamente sin importar el contador
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    
    #Empezamos por definir la lista de columnas
    columns = []
    #Generamos las columnas para cada columna que tenemos, si tenemos 3 lo de abajo pasa 3 veces
    for _ in range(cols):
        column = []
        #[:] esto significa una copia
        current_symbols = all_symbols[:]
        #loop en el numero de valores que necesitamos generar que es igual al numero de filas
        for _ in range(rows):
            #Esto selecciona un valor random de la lista
            value = random.choice(current_symbols)
            #Removemos el valor para no escogerlo de nuevo
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

#Funcion para imprimir de manera bonita las columnas
def print_slot_machine(columns):
    #Transposing
    for row in range (len(columns[0])):
        for i, column in enumerate (columns):
            #Index es -1
            if i != len(columns) - 1:
                #| esto es un separador, se usa tambien si no voy a imprimir la ultima linea
                print(column[row], "|", end=" | ")
            else:
                #end=" | " es para imprimir en la misma linea
                #end=" \n " es para moverse a la siguiente linea despues de cada columna
                print(column[row], end=" | ")  

        print()

def deposit():
    while True:
        amount = input ("What would you like to deposit? $")
        if amount.isdigit():
            #Para convertir lo del string a int
            amount = int (amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater that 0.")
        else:
            print("Please enter a number.")
            
    return amount

#Primero el numero de lineas, y luego la cantidad
def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            #Para convertir lo del string a int
            lines = int(lines)
            #Para chequear si un valor esta entre dos valores
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines
            
def get_bet():
    while True:
        amount = input ("What would you like to bet on each line? $")
        if amount.isdigit():
            #Para convertir lo del string a int
            amount = int (amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
            
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You  do not have enough to bet that amount, your current balance is: {balance}")
        else:
            break

    print (f"You're betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings( slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
#Para llamar una funcion solo ponemos el nombre y ()
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input ("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")
    
main()