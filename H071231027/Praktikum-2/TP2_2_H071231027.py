x = input("Masukkan Input Pertama : ")
y = input("Masukkan Input Kedua : ")
z = input("Masukkan Input Ketiga : ")
match x, y, z:
    case "vertebrado", "ave", "carnivoro":
        print("aguia")
    case "vertebrado", "ave", "onivoro":
        print("pomba")
    case "vertebrado", "mamifero", "onivoro":
        print("homem")
    case "vertebrado", "mamifero", "herbivoro":
        print("vaca")
    case "invertebrado", "inseto", "hematofago":
        print("pulga")
    case "invertebrado", "inseto", "herbivoro":
        print("lagarta")
    case "invertebrado", "anelido", "hematofago":
        print("sanguessuga")
    case "invertebrado", "anelido", "onivoro":
        print("minhoca")
    case _:
        print("Invalid input")
        

