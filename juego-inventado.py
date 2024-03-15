mport random

def generar_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def mostrar_color(color):
    print("Color generado:", color)

def main():
    while True:
        color = generar_color()
        mostrar_color(color)
        respuesta = input("¿Desea generar otro color? (s/n): ").lower()
        if respuesta != 's':
            break

if __name__ == "__main__":
    main()