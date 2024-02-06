idade=int(input("Informe sua idade: "))

if idade<=18:
    print("adolescente")
elif idade<30:
    print("jovem")
elif idade<59:
    print("adulto")
else:
    print("melhor idade")