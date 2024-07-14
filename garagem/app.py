from garagem_class import Garagem

brasilia = Garagem('brasilia', 'Vw', 1981, 123456,True)
civic = Garagem('Civic hatch vti', 'Honda', 1995, 173456,True)
gallardo = Garagem('Gallardo', 'Lamborghini', 2008, 923356,True)
porsche = Garagem('911 GT3 RS', 'Porsche', 2023, 373456,True)



def main():
    Garagem.listar_carros()
    print()

    brasilia.definir_potencia(61)
    print(brasilia.tipo_preparacao)
    brasilia.alterar_funcionamento(False)

    #foi mexido no motor e agr aumentou
    brasilia.definir_potencia(120)
    brasilia.alterar_funcionamento(True)
    print(brasilia.tipo_preparacao)

#if __name__ == '__main_':
main()