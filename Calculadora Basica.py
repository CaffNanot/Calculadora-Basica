num1 = int(input("Insira um número :"))     #Receber o primeiro número

oper = str(input("Insira a operação desejada :")) #Receber o tipo de operação

num2 = int(input("Isira outro número :"))   #Receber o segundo número

#Condições da Calculadora
if (oper == "+") :
    print(num1 + num2)
elif(oper == "-"):
    print (num1 - num2)
elif(oper == "*"):
    print(num1 * num2)
elif(oper == "/"):
    print(num1 / num2)
else:
    print("Acho que algo deu errado!")

    
