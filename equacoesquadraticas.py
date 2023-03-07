import math

def jogar():
    a, b, c = menu()
    delta = calcdelta(a, b, c)
    imprimerespostax1(delta, a, b)
    imprimerespostax2(delta, a, b)

def menu():
    print("___________________________________________")
    print("Programa para calcular equacoes quadraticas")
    print("___________________________________________")
    print("Codigo criado por FahFah")
    print("___________________________________________")
    a = int(input("Digite o valor de A..."))
    b = int(input("Digite o valor de B..."))
    c = int(input("Digite o valor de C..."))
    print("{}x² + {}x + {} = 0".format(a, b, c))
    return a, b, c

def calcdelta(a, b, c):
    delta = (int(b) ** 2 - (4 * int(a) * int(c)))
    print("Delta igual a {}".format(delta))
    return(delta)

def imprimerespostax1(delta, a, b):
    x1 = (b * -1 + (math.sqrt(delta)))
    x1 = x1 / (2 * a)
    print("x1...{}".format(x1))

def imprimerespostax2(delta, a, b):
    x2 = (b * -1 - (math.sqrt(delta)))
    x2 = x2 / (2 * a)
    print("x1...{}".format(x2))

if(__name__ == "__main__"):
    jogar()