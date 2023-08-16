# definir as variaveis
casas_no_tabuleiro = 39 # zero conta como numero
P1_saldo = 1500
P2_saldo = 1500
P1_casa = 0
P2_casa = 0
quantas_rodadas = 1
sorte_temporario = 0
P_casa_temporario = 0
P1_prisão = 0
P2_prisão = 0


# importar random
import random
 
# prints a random value from the list
list1 = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 11, 11, 12]
list2 = [-200, -100, -50, 50, 100, 200]
list3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# loop de jogadas
while quantas_rodadas < 101:
    print("Rodada " + str(quantas_rodadas))

    if P1_prisão == 0:    
        P1_dice = random.choice(list1)
        P1_casa += P1_dice
        if P1_casa > casas_no_tabuleiro:
            P1_casa -= casas_no_tabuleiro
            P1_saldo += 200
    
    P_casa_temporario = P1_casa
    if P_casa_temporario == 1 or P_casa_temporario == 3 or P_casa_temporario == 4 or P_casa_temporario == 5 or P_casa_temporario == 6 or P_casa_temporario == 8 or P_casa_temporario == 9 or P_casa_temporario == 11 or P_casa_temporario == 12 or P_casa_temporario == 13 or P_casa_temporario == 14 or P_casa_temporario == 15 or P_casa_temporario == 16 or P_casa_temporario == 18 or P_casa_temporario == 19 or P_casa_temporario == 21 or P_casa_temporario == 23 or P_casa_temporario == 24 or P_casa_temporario == 25 or P_casa_temporario == 26 or P_casa_temporario == 27 or P_casa_temporario == 28 or P_casa_temporario == 29 or P_casa_temporario == 31 or P_casa_temporario == 32 or P_casa_temporario == 34 or P_casa_temporario == 35 or P_casa_temporario == 37 or P_casa_temporario == 38 or P_casa_temporario == 39:
        if list3[P_casa_temporario] == 1:
            print("P1 parou na sua própria casa " + str(P_casa_temporario) )
        if list3[P_casa_temporario] == 0:
            if P1_saldo > int(P_casa_temporario * 10):
                list3[P_casa_temporario] = 1
                P1_saldo -= P_casa_temporario * 10
                print("P1 parou e comprou a casa " + str(P_casa_temporario))
            else:
                print("P1 parou na casa " + str(P_casa_temporario) + " mas escolheu não comprar pois seu saldo é de £" + str(P1_saldo))
        if list3[P_casa_temporario] == 2:
            P1_saldo -= 100
            P2_saldo += 100
            print("P1 parou na casa " + str(P_casa_temporario) + " que é de P2 e o pagou £100 de aluguel")
    elif P_casa_temporario == 2 or P_casa_temporario == 7 or P_casa_temporario == 17 or P_casa_temporario == 22 or P_casa_temporario == 33 or P_casa_temporario == 36:
        sorte_temporario = random.choice(list2)
        P1_saldo += sorte_temporario
        print("P1 parou no sorte ou revez, a carta dizia: receba " + str(sorte_temporario))
    elif P_casa_temporario == 30:
        if P1_prisão == 0:
            P1_prisão = 2
        else:
            P1_prisão -=1
        print("P1 está na prisão por "+ str(P1_prisão + 1) + " jogada(s)")
    else:
        print("P1 parou na casa " + str(P_casa_temporario))

    if P1_saldo <= 0:
        print("\n\n\n\nP1 declarou falência com o saldo de: -£" + str(int(P1_saldo * -1)) + " e um total de " + str(list3.count(1)) + " casas")
        break




    if P2_prisão == 0:    
        P2_dice = random.choice(list1)
        P2_casa += P2_dice
        if P2_casa > casas_no_tabuleiro:
            P2_casa -= casas_no_tabuleiro
            P2_saldo += 200

    P_casa_temporario = P2_casa
    if P_casa_temporario == 1 or P_casa_temporario == 3 or P_casa_temporario == 4 or P_casa_temporario == 5 or P_casa_temporario == 6 or P_casa_temporario == 8 or P_casa_temporario == 9 or P_casa_temporario == 11 or P_casa_temporario == 12 or P_casa_temporario == 13 or P_casa_temporario == 14 or P_casa_temporario == 15 or P_casa_temporario == 16 or P_casa_temporario == 18 or P_casa_temporario == 19 or P_casa_temporario == 21 or P_casa_temporario == 23 or P_casa_temporario == 24 or P_casa_temporario == 25 or P_casa_temporario == 26 or P_casa_temporario == 27 or P_casa_temporario == 28 or P_casa_temporario == 29 or P_casa_temporario == 31 or P_casa_temporario == 32 or P_casa_temporario == 34 or P_casa_temporario == 35 or P_casa_temporario == 37 or P_casa_temporario == 38 or P_casa_temporario == 39:
        if list3[P_casa_temporario] == 2:
            print("P2 parou na sua própria casa " + str(P_casa_temporario) )
        if list3[P_casa_temporario] == 0:
            if P2_saldo > int(P_casa_temporario * 10):
                list3[P_casa_temporario] = 2
                P2_saldo -= P_casa_temporario * 10
                print("P2 parou e comprou a casa " + str(P_casa_temporario))
            else:
                print("P2 parou na casa " + str(P_casa_temporario) + " mas escolheu não comprar pois seu saldo é de £" + str(P2_saldo))
        if list3[P_casa_temporario] == 1:
            P2_saldo -= 100
            P1_saldo += 100
            print("P2 parou na casa " + str(P_casa_temporario) + " que é de P1 e o pagou £100 de aluguel")
    elif P_casa_temporario == 2 or P_casa_temporario == 7 or P_casa_temporario == 17 or P_casa_temporario == 22 or P_casa_temporario == 33 or P_casa_temporario == 36:
        sorte_temporario = random.choice(list2)
        P2_saldo += sorte_temporario
        print("P2 parou no sorte ou revez, a carta dizia: receba " + str(sorte_temporario))
    elif P_casa_temporario == 30:
        if P2_prisão == 0:
            P2_prisão = 2
        else:
            P2_prisão -=1
        print("P2 está na prisão por "+ str(P2_prisão + 1) + " jogada(s)")
    else:
        print("P2 parou na casa " + str(P_casa_temporario))

    if P2_saldo <= 0:
        print("\n\n\n\nP2 declarou falência com o saldo de: -£" + str(int(P2_saldo * -1)) + " e um total de " + str(list3.count(2)) + " casas")
        break














    print("\n\n\n\n")
    quantas_rodadas += 1