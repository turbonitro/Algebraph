import random

#definiowanie funkcji rozdzielającej liczby wielocyfrowe na cyfry odseparowane
#sprawdzanie, czy liczba jest większa od 0, następnie wykonanie operacji modulo 10 
#na tej liczbie, aby uzyskać jej ostatnią cyfrę. Cyfra ta jest dodawana do listy digits za 
#pomocą metody append(). Następnie liczba jest dzielona całkowicie przez 10, aby usunąć 
#ostatnią cyfrę. Całość zapętlona w pętli while.
def separate_digits(number):
    digits = []
    while number > 0:
        digit = number % 10
        digits.append(digit)
        number //= 10
    digits.reverse()
    return digits

#deklaracja klasy kodującej losowo litery A-J do konkretnych cyfr, które nie zostały już raz użyte
class DigitEncoder:

#stworzenie trzech atrybutów obiektu: encoding, available_letters oraz used_letters.
#encoding jest to słownik, który mapuje cyfry na odpowiadające im litery. available_letters 
#to lista liter, które są aktualnie dostępne do przypisania do cyfr. used_letters to zbiór liter, 
#które już zostały przypisane do cyfr.
    def __init__(self):
        self.encoding = {}
        self.available_letters = list("ABCDEFGHIJ")
        self.used_letters = set()

#Metoda encode_digit przyjmuje cyfrę jako argument i zwraca literę odpowiadającą tej cyfrze. 
#Jeśli cyfra nie została jeszcze zakodowana, wybierana jest losowa litera z listy available_letters, 
#usuwana z niej, dodawana do zbioru used_letters, a następnie przypisywana do cyfry w słowniku encoding. 
#Następnie funkcja zwraca przypisaną literę.
    def encode_digit(self, digit):
        if digit not in self.encoding:
            letter = random.choice(self.available_letters)
            self.available_letters.remove(letter)
            self.used_letters.add(letter)
            self.encoding[digit] = letter
        return self.encoding[digit]

#encode_list przyjmuje listę cyfr i zwraca listę odpowiadających im liter wywołując metodę 
#encode_digit dla każdej cyfry w liście.
    def encode_list(self, digits):
        return [self.encode_digit(digit) for digit in digits]


#Stworzenie obiektu encoder klasy DigitEncoder    
encoder = DigitEncoder()

#zakodowanie listy cyfr numbers przez wywołanie metody encode_list
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
encoded = encoder.encode_list(numbers)

#definiowanie funkcji generującej jeden przypadek macierzy algebrafu
def generate_plus_matrix():

    while True:
        j = random.randint(100, 999)
        k = random.randint(100, 999)
        l = j + k
        m = random.randint(100, 999)
        n = random.randint(100, 999)
        o = m + m
        p = j + m
        r = k + n
        s = l + o

        break

    #kodowanie wartości wylosowanych jako litery czyli wcześniej zamienianie wartości 
    #liczbowych na pojedyncze cyfry a następnie cyfr na wcześniej zakodowane litery 
    #do nowej tabeli tylko takiej bez cudzysłowów, użycie encodera i wszystko wsadzone w jedną zmienną
    je = (''.join(encoder.encode_list(separate_digits(j))))
    ke = (''.join(encoder.encode_list(separate_digits(k)))) 
    le = (''.join(encoder.encode_list(separate_digits(l))))
    me = (''.join(encoder.encode_list(separate_digits(m))))
    ne = (''.join(encoder.encode_list(separate_digits(n))))
    oe = (''.join(encoder.encode_list(separate_digits(o))))
    pe = (''.join(encoder.encode_list(separate_digits(p))))
    re = (''.join(encoder.encode_list(separate_digits(r))))
    se = (''.join(encoder.encode_list(separate_digits(s))))

    matrix1 = [[None for j in range(5)] for i in range(5)]

    #Wprowadzenie wartości zakodowanych do macierzy1
    matrix1[0][0] = je
    matrix1[0][1] = '+'
    matrix1[0][2] = ke
    matrix1[0][3] = '='
    matrix1[0][4] = le

    matrix1[1][0] = '+'
    matrix1[1][1] = ' '
    matrix1[1][2] = '+'
    matrix1[1][3] = ' '
    matrix1[1][4] = '+'

    matrix1[2][0] = me
    matrix1[2][1] = '+'
    matrix1[2][2] = ne
    matrix1[2][3] = '='
    matrix1[2][4] = oe

    matrix1[3][0] = '='
    matrix1[3][1] = ' '
    matrix1[3][2] = '='
    matrix1[3][3] = ' '
    matrix1[3][4] = '='

    matrix1[4][0] = pe
    matrix1[4][1] = '+'
    matrix1[4][2] = re
    matrix1[4][3] = '='
    matrix1[4][4] = se

    #zwrocenie macierzy
    for i in range(5):
        for j in range(5):
            print(matrix1[i][j], end="\t")
        print("\n")

    #stworzenie listy znaków wchodzącej w skład losowo generowanej maceierzy
    my_list = list(matrix1)

    letters = []


    for sublist in my_list:                                         #przejscie przez każdą pod-listę w liście my_list.
        for item in sublist:                                        #przejscie przez każdy element w podliście
            for letter in item:                                     #przejscie przez każdą literę w elemencie
                if letter.isalpha() and letter not in letters:      #sprawdzemoe czy jest literą alfabetu i czy nie została już dodana do listy liter letters
                    letters.append(letter)                          #dołączenie litery spełnionej powyższe na koniec listy

    letters.sort()
    
    print("Litery wchodzące w skład algebrafu to:", letters)
    print("Wpisz 'q' jezeli chcesz zakończyć działanie programu.")
    print("Rozwiąż algebraf.")
    print("Która liczba odpowiada literze", letters[0], "?")

    #kod właściwej częsci łamigłówki sprawdzający czy wartości wpisywane w konsoli 
    #zgadzają się z zakodowanymi o których podanie prosi kod
    while True:
        guess = input("Podaj liczbę: ")                             #wprowadzenie liczby
        if guess == "q":                                            #przerwij kod wpisując "q"
            break                            
        elif guess.isdigit() and int(guess) in numbers:             #sprawdzanie czy wprowadzona wartość jest liczbą całkowitą i czy znajduje się na liście numbers (cyfr)
            if encoded[int(guess)] == letters[0]:                   #sprawdzanie czy wszystko sie zgadza z pierwszą pozycją listy letters
                print("Brawo! Odgadłeś literę", letters[0])         #litera się zgadza
                letters = letters[1:]                               #litera usunięta z listy
                if not letters:                                     #jeżeli lista jest pusta
                    print("Gratulacje! Rozwiązałeś algebraf!")      #koniec
                    break
                else:                                               #jeżeli nie jest pusta
                    print("Kolejna litera to", letters[0])          #zgadywanie kolejnej litery, teraz pierwsza pozycja po usunięciu poprzedniej jest inna
            else:                                                   #jeżeli nie ta litera
                print("Nie, to nie ta liczba. Spróbuj ponownie.") 
        else:                                                       #jeżeli wklepane coś innego niż cyfra z zakresu 0-9
            print("To nie jest liczba na liście. Spróbuj ponownie.")


#definiowanie funkcji generującej drugi przypadek macierzy algebrafu        
def generate_var_matrix():

    while True:
        a = random.randint(100, 999)
        b = random.randint(100, 999)
        c = a + b
        d = random.randint(1, 99)
        e = random.randint(1, 99)
        f = d * e
        g = a / d
        h = b + e
        i = c - f

        #wprowadzenie warunku że zmienna "i" musi spełniać oba warunki operacji matematycznych
        if i == g + h and i == c - f:
            break

    ae = (''.join(encoder.encode_list(separate_digits(a))))
    be = (''.join(encoder.encode_list(separate_digits(b)))) 
    ce = (''.join(encoder.encode_list(separate_digits(c))))
    de = (''.join(encoder.encode_list(separate_digits(d))))
    ee = (''.join(encoder.encode_list(separate_digits(e))))
    fe = (''.join(encoder.encode_list(separate_digits(f))))
    ge = (''.join(encoder.encode_list(separate_digits(g))))
    he = (''.join(encoder.encode_list(separate_digits(h))))
    ie = (''.join(encoder.encode_list(separate_digits(i))))

    matrix2 = [[None for j in range(5)] for i in range(5)]

    matrix2[0][0] = ae
    matrix2[0][1] = '+'
    matrix2[0][2] = be
    matrix2[0][3] = '='
    matrix2[0][4] = ce

    matrix2[1][0] = ':'
    matrix2[1][1] = ' '
    matrix2[1][2] = '+'
    matrix2[1][3] = ' '
    matrix2[1][4] = '-'

    matrix2[2][0] = de
    matrix2[2][1] = '*'
    matrix2[2][2] = ee
    matrix2[2][3] = '='
    matrix2[2][4] = fe

    matrix2[3][0] = '='
    matrix2[3][1] = ' '
    matrix2[3][2] = '='
    matrix2[3][3] = ' '
    matrix2[3][4] = '='

    matrix2[4][0] = ge
    matrix2[4][1] = '+'
    matrix2[4][2] = he
    matrix2[4][3] = '='
    matrix2[4][4] = ie

    for i in range(5):
        for j in range(5):
            print(matrix2[i][j], end="\t")
        print("\n")

    my_list = list(matrix2)

    letters = []

    for sublist in my_list:
        for item in sublist:
            for letter in item:
                if letter.isalpha() and letter not in letters:
                    letters.append(letter)

    letters.sort()

    letters.sort()
    
    print("Litery wchodzące w skład algebrafu to:", letters)
    print("Wpisz 'q' jezeli chcesz zakończyć działanie programu.")
    print("Rozwiąż algebraf: ")
    print("Która liczba odpowiada literze", letters[0], "?")
    
    while True:
        guess = input("Podaj liczbę: ")
        if guess == "q":
            break
        elif guess.isdigit() and int(guess) in numbers:
            if encoded[int(guess)] == letters[0]:
                print("Brawo! Odgadłeś literę", letters[0])
                letters = letters[1:]
                if not letters:
                    print("Gratulacje! Rozwiązałeś algebraf!")
                    break
                else:
                    print("Kolejna litera to", letters[0])
            else:
                print("Nie, to nie ta liczba. Spróbuj ponownie.")
        else:
            print("To nie jest liczba na liście. Spróbuj ponownie.")
                   
matrixy = (generate_var_matrix, generate_plus_matrix)

#losowanie jednego spośród dwóch algebrafów do rozwiązania
los = random.choice(matrixy)

los()
