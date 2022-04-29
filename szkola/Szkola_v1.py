import json



slownik_szkola = {"slownik_nauczyciele": [],"slownik_klas": [], "slownik_sale": [], "slownik_wychowawcy": [], "slownik_uczniowie": []}
listaSlownikNauczyciel = []
listaSlownikKlasa = []
listaSlownikUczen = []
listaSlownikSala = []
listaSlownikWychowawca = []




class Nauczyciel:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    def dodaj(self):
        listaSlownikNauczyciel.append(f"{self.imie, self.nazwisko}") 
        print("Dodaj nauczyciela")
        print("Imię: " + self.imie)
        print("Nazwisko: " + self.nazwisko)
        print(f"Dodano nauczyciela {self.imie} {self.nazwisko}")
    
class Klasa:
    def __init__(self, nazwa):
        self.nazwa = nazwa
    def dodaj(self):
        listaSlownikKlasa.append(self.nazwa)
        print("Dodaj klasę")
        print("Nazwa klasy: " + self.nazwa)
        print(f"Dodano klasę {self.nazwa}")
    def __repr__(self) -> str:
        return f"{self.nazwa}"

class Sala:
    def __init__(self, nazwa):
        self.nazwa = nazwa
    def dodaj(self):
        listaSlownikSala.append(self.nazwa)
        print("Dodaj salę")
        print("Nazwa sali: " + self.nazwa)
        print(f"Dodano salę {self.nazwa}")
class Uczen(Klasa):
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        super().__init__(nazwa)
    def dodaj(self):
        listaSlownikUczen.append([f"Uczen: {self.imie, self.nazwisko, self.nazwa}"])
        print("Dodaj ucznia")
        print("Imię: " + self.imie)
        print("Nazwisko: " + self.nazwisko)
        print("Klasa: " + self.nazwa)
        print(f"Dodano ucznia {self.imie} {self.nazwisko} do klasy {self.nazwa}")
class Wychowawca:
    def __init__(self, nauczyciel, klasa):
        self.nauczyciel = nauczyciel
        self.klasa = klasa
    def dodaj(self):
        listaSlownikWychowawca.append([f"Wychowawca: {self.nauczyciel, self.klasa}"]) 
        print("Dodaj wychowawcę")
        print("Nauczyciel: " + self.nauczyciel)
        print("Do klasy: " + self.klasa)
        print(f"Dodano wychowawcę {self.nauczyciel} do klasy {self.klasa}")
    def __repr__(self) -> str:
        return f"Wychowawca: {self.nauczyciel} do klasy {self.klasa.__repr__()}"


def podtwierdzenie():
    podtwierdzenie_zm = input("Czy chcesz kontynuować? (t/n)")
    if podtwierdzenie_zm == "t":
        return True
    elif podtwierdzenie_zm == "n":
        return False
    else:
        print("Niepoprawna odpowiedź")
        return podtwierdzenie()
# def zalodowanie_info():
#     print("Załadowanie informacji")
#     slownik_szkola["slownik_klas"] = listaSlownikKlasa
#     slownik_szkola["slownik_nauczyciele"] = listaSlownikNauczyciel
#     slownik_szkola["slownik_sale"] = listaSlownikSala
#     slownik_szkola["slownik_wychowawcy"] = listaSlownikWychowawca
#     slownik_szkola["slownik_uczniowie"] = listaSlownikUczen
    
#     with open("dane_nauczyciele.txt", "r") as plik:
#         for linia in plik:
#             linia = linia.strip()
#             linia = linia.split(",")
#             nauczyciel = Nauczyciel(linia[0], linia[1])
#             nauczyciel.dodaj()
#     with open("dane_klas.txt", "r") as plik:
#         for linia in plik:
#             linia = linia.strip()
#             linia = linia.split(",")
#             klasa = Klasa(linia[0])
#             klasa.dodaj()
#     with open("dane_sale.txt", "r") as plik:
#         for linia in plik:
#             linia = linia.strip()
#             linia = linia.split(",")
#             sala = Sala(linia[0])
#             sala.dodaj()
#     with open("dane_uczniowie.txt", "r") as plik:
#         for linia in plik:
#             linia = linia.strip()
#             linia = linia.split(",")
#             uczen = Uczen(linia[0], linia[1])
#             uczen.dodaj()
#     with open("dane_wychowawcy.txt", "r") as plik:
#         for linia in plik:
#             linia = linia.strip()
#             linia = linia.split(",")
#             wychowawca = Wychowawca(linia[0], linia[1], linia[2])
#             wychowawca.dodaj()


def zapis_do_json():
    slownik_szkola["slownik_klas"] = listaSlownikKlasa
    slownik_szkola["slownik_nauczyciele"] = listaSlownikNauczyciel
    slownik_szkola["slownik_sale"] = listaSlownikSala
    slownik_szkola["slownik_wychowawcy"] = listaSlownikWychowawca
    slownik_szkola["slownik_uczniowie"] = listaSlownikUczen
    with open("dane.json", "w") as plik:
        json.dump(slownik_szkola, plik)
def przypisanie_info():
    
    slownik_szkola["slownik_klas"] = listaSlownikKlasa
    slownik_szkola["slownik_nauczyciele"] = listaSlownikNauczyciel
    slownik_szkola["slownik_sale"] = listaSlownikSala
    slownik_szkola["slownik_wychowawcy"] = listaSlownikWychowawca
    slownik_szkola["slownik_uczniowie"] = listaSlownikUczen

    


# zaladowanie_info_z_pliku()
wybor_nauczyciela = ()
while True:
    
    
    print("1 dodaj nauczyciela")
    print("2 dodaj klasę")
    print("3 dodaj salę")
    print("4 dodaj uczniów")
    print("5 dodaj wychowawcę")
    print("6 wyświetl informacje")
    print("7 wyjdź")
    wybor = input("Wybierz opcję: ")
    if wybor == "1":
        przypisanie_info()
        if podtwierdzenie():
            print("Dodaj nauczyciela")
            imie = input("Podaj imię: ")
            nazwisko = input("Podaj nazwisko: ")
            nauczyciel = Nauczyciel(imie, nazwisko)
            nauczyciel.dodaj()
        else:
            print("Nie dodano nauczyciela")
    elif wybor == "2":
        przypisanie_info()
        if podtwierdzenie():
            print("Dodaj klasę")
            nazwa = input("Podaj nazwę klasy: ")
            klasa = Klasa(nazwa)
            slownik_szkola["slownik_klas"].append(klasa)
            # klasa.dodaj()
        else:
            print("Nie dodano klasy")
    elif wybor == "3":
        przypisanie_info()
        if podtwierdzenie():
            print("Dodaj salę")
            nazwa = input("Podaj nazwę sali: ")
            sala = Sala(nazwa)
            sala.dodaj()
        else:
            print("Nie dodano sali")
    elif wybor == "4":
        przypisanie_info()
        if podtwierdzenie():
            print("Dodaj uczniów")
            imie = input("Podaj imię: ")
            nazwisko = input("Podaj nazwisko: ")
            print("Wybierz klasę: ")
            for klasa in slownik_szkola["slownik_klas"]:
                print(klasa)
            
            nazwa = input("Podaj nazwę klasy: ")
            while True:
                if nazwa in slownik_szkola["slownik_klas"]:
                    break
                else:
                    print("Nie ma takiej klasy")
                    nazwa = input("Podaj nazwę klasy: ")
            uczen = Uczen(imie, nazwisko)
            uczen.dodaj()
        else:
            print("Nie dodano uczniów")
    elif wybor == "5":
        przypisanie_info()
        if podtwierdzenie():
            print("Dodaj wychowawcę")
            print("wybierz nauczyciela: ")
            for nauczyciel in enumerate(slownik_szkola["slownik_nauczyciele"]):
                print(nauczyciel)
            numer = int(input("Podaj numer przypisany do nauczyciela: "))
            while True:
                nauczyciel = slownik_szkola["slownik_nauczyciele"][numer]
                print("wybierz klase:")
                print(slownik_szkola["slownik_klas"])
                for index, klasa in  enumerate(slownik_szkola["slownik_klas"]):
                    print(index, klasa.nazwa)
                numer2 = int(input("Podaj numer klasy:"))
                klasa = slownik_szkola["slownik_klas"][numer2]
                break

            slownik_szkola["slownik_wychowawcy"].append(Wychowawca(nauczyciel, klasa))
            print(slownik_szkola["slownik_wychowawcy"].__repr__())
                    
                    
                

            #     if imie in slownik_szkola["slownik_nauczyciele"]:
            #         break
            #     else:
            #         print("Nie ma takiego nauczyciela")
            #         imie = input("Podaj nazwę nauczyciela: ")
            # print("Wybierz klasę: ")
            
            
            
            # print("Wybierz klasę: ")
            # for klasa in slownik_szkola["slownik_klas"]:
            #     print(klasa)
            # nazwa = input("Podaj nazwę klasy: ")
            # while True:
            #     if nazwa in slownik_szkola["slownik_klas"]:
            #         break
            #     else:
            #         print("Nie ma takiej klasy")
            #         #nazwa = input("Podaj nazwę klasy: ")
                    
            
        else:
            print("Nie dodano wychowawców")
    elif wybor == "6":
        przypisanie_info()
        if podtwierdzenie():
            print("Wyświetl informacje")
            print("1 Wyświetl nauczycieli")
            print("2 Wyświetl klasy")
            print("3 Wyświetl salę")
            print("4 Wyświetl uczniów")
            print("5 Wyświetl wychowawców")
            print("6 Wyświetl wszystko")
            wybor = input("Wybierz opcję: ")
            if wybor == "1":
                print("Wyświetl nauczycieli")
                print("Nauczyciele: ")
                print(slownik_szkola["slownik_nauczyciele"])
                # for key, value in slownik_szkola["slownik_nauczyciele"]["Nauczyciele"].items():
                #     print(f"{key} {value}")
            elif wybor == "2":
                print("Wyświetl klasy")
                print("Klasy: ")
                print(slownik_szkola["slownik_klas"])
                # for key, value in slownik_szkola["slownik_klas"]["Klasy"].items():
                #     print(f"{key} {value}")
            elif wybor == "3":
                print("Wyświetl salę")
                print("Sale: ")
                print(slownik_szkola["slownik_sale"])
                # for key, value in slownik_szkola["slownik_sale"]["Sale"].items():
                #     print(f"{key} {value}")
            elif wybor == "4":
                print("Wyświetl uczniów")
                print("Uczniowie: ")
                print(slownik_szkola["slownik_uczniowie"])
                # for key, value in slownik_szkola["slownik_uczniowie"]["Uczniowie"].items():
                #     print(f"{key} {value}")
            elif wybor == "5":
                
                print("Wyświetl wychowawców")
                print("Wychowawcy: ")
                print(slownik_szkola["slownik_wychowawcy"])
                # for key, value in slownik_szkola["slownik_wychowawcy"]["Wychowawcy"].items():
                #     print(f"{key} {value}")
            elif wybor == "6":

                print(slownik_szkola)
                print("Wyświetl wszystko")
                print("Nauczyciele: ")
                # for key, value in slownik_szkola["slownik_nauczyciele"].items():
                #     print(f"{key} {value}")
                # print("Klasy: ")
                # for key, value in slownik_szkola["slownik_klas"].items():
                #     print(f"{key} {value}")
                # print("Sale: ")
                # for key, value in slownik_szkola["slownik_sale"].items():
                #     print(f"{key} {value}")
                # print("Uczniowie: ")
                # for key, value in slownik_szkola["slownik_uczniowie"].items():
                #     print(f"{key} {value}")
                # print("Wychowawcy: ")
                # for key, value in slownik_szkola["slownik_wychowawcy"].items():
                #     print(f"{key} {value}")
        else:
            print("Nie wyświetlono informacji")

    elif wybor == "7":
    
        if podtwierdzenie():
            print("Dziękuję za skorzystanie z programu")
            print("Informacje wprowadzone podczas działania programu zostały zapisane w pliku")
            przypisanie_info()
            zapis_do_json()
            
            with open("dane_nauczyciele.txt", "w") as plik:
                plik.write(f'{slownik_szkola["slownik_nauczyciele"]}')
            with open("dane_klas.txt", "w") as plik:
                plik.write(f'{slownik_szkola["slownik_klas"]}')
            with open("dane_sale.txt", "w") as plik:
                plik.write(f'{slownik_szkola["slownik_sale"]}')
            with open("dane_uczniowie.txt", "w") as plik:
                plik.write(f'{slownik_szkola["slownik_uczniowie"]}')
            with open("dane_wychowawcy.txt", "w") as plik:
                plik.write(f'{slownik_szkola["slownik_wychowawcy"]}')
            break
        else:
            print("Nie wylogowano z programu")
        
    
#zrobic jeden slownik
#zrobic wyswietlenie
#zapisywanie do roznych plikow 
#odczyt z plikow 
#dziedziczenie slownikow


#jakos pozniej zrobic grficzny interface