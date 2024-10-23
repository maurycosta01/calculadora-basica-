import time #importei uma biblioteca de tempo pra nao fechar quando o resultado do print for exibido 
msg = input ("bem vindo a calculadora basica presione ENTER") # so mensagem de bem vindo 


opçao = input ("digite a escolhida + , - , / , *,** :") # colocando opçao pro usuario ver o que ele
if opçao == "+": # defini a opçao  usando if nao pode ser usado em mais de uma 
   m1 =int(input("digite seu primeiro numero :"))#int para numero que sejam inteiros 
   m2 =int(input("digite seu segundo numero "))
   soma1 = m1 + m2
   print("sua conta foi {} + {} = {}.".format(m1,m2,soma1))
   time.sleep(5)#aqui codigo mais tempo 
   

elif opçao == "-" : # elif permitido ser usado em mais de uma 
   mm1 = float(input("digite seu primeiro numero:")) # float para numero que sejam quebrados ou com pontos
   mm2 = float(input("digite seu segundo numero:"))
   somam1 = mm1 - mm2
   print("sua conta foi {} - {} = {}".format(mm1,mm2,somam1))
   time.sleep(5)
elif  opçao == "/" :
   d1 = float(input("digite seu primeiro numero:"))
   d2 = float(input("digite seu segundo numero :"))
   dsoma = d1 / d2
   print("sua conta foi {} / {} = {}".format(d1,d2,dsoma))
   time.sleep(5)

elif opçao == "**":
   p1 = float(input("digite seu primeiro numero:"))
   p2 = float(input("digite seu segundo numero:"))
   poten = p1 ** p2
   print("sua conta foi {} elevado {} = {} ".format(p1,p2,poten))
   time.sleep(5)
elif opçao == "*":
   v1 = float(input("digite seu primeiro numero:"))
   v2 = float(input("digite seu segundo numero:"))
   vezes = v1 * v2
   print("sua conta foi {} X {} = {}".format(v1,v2,vezes))
   time.sleep(5)
   