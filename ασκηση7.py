from random import randint
def positionlist(y):
    if y==1 or y==4 or y==7:
        return 0
    if y==2 or y==5 or y==8:
        return 2
    else:
        return 4 

list11 = [["  ","|","  ","|","  "],["  ","|","  ","|","  "],["  ","|","  ","|","  "]]
list22 = ["------------"]
errors = []
print ("Το παιχνίδι ξεκινάει!!!")
print(' '.join(list11[0])+ "\n" + ' '.join(list22)+ "\n" +' '.join(list11[1])+ "\n" +' '.join(list22)+ "\n" +' '.join(list11[2]))
for q in range(9):
    if q%2 == 0:
        players2 = int(input("Παρακαλώ δώσε την θέση: "))
        while players2 in errors or players2>10 or players2<0:
            players2 = int(input("Δώσε έναν εγκυρο αριθμό : "))
        errors.append(players2)
        if players2==3 or players2==6 or players2==9:
            list11[int(players2/3)-1][positionlist(players2)] = " X "
            print(' '.join(list11[0])+ "\n" + ' '.join(list22)+ "\n" +' '.join(list11[1])+ "\n" +' '.join(list22)+ "\n" +' '.join(list11[2]))
        else:
            list11[int(players2/3)][positionlist(players2)] = " X "
            print(' '.join(list11[0])+ "\n" + ' '.join(list22)+ "\n" +' '.join(list11[1])+ "\n" +' '.join(list22)+ "\n" +' '.join(list11[2]))
    else:
        s= randint(1, 9)
        while s in errors:
            s= randint(1, 9)
        errors.append(s)
        print ("Τώρα παίζει ο υπολογιστής!")
        if s==3 or s==6 or s==9:
            list11[int(s/3)-1][positionlist(s)] = " O "
            print(' '.join(list11[0])+ "\n" + ' '.join(list22)+ "\n" +' '.join(list11[1])+ "\n" +' '.join(list22)+ "\n" +' '.join(list11[2]))
        else:
            list11[int(s/3)][positionlist(s)] = " O "
            print(' '.join(list11[0])+ "\n" + ' '.join(list22)+ "\n" +' '.join(list11[1])+ "\n" +' '.join(list22)+ "\n" +' '.join(list11[2]))
    if q >= 5:
        turn = " X "
        players2 = "Παίχτης"
        for x in range(2):
            if list11[0][0]==turn and list11[1][2]==turn and list11[2][4]==turn:
                print(players2 + " Κέρδισε το γύρο!!")
                c = input("Πάτα το enter για να τελειώσει το πρόγραμμα")    
                quit()
            elif list11[0][4]==turn and list11[1][2]==turn and list11[2][0]==turn:
                print(players2 + "  Κέρδισε το γύρο!!")
                c = input("Πάτα το enter για να τελειώσει το πρόγραμμα")    
                quit()   
            elif list11[0][0]==turn and list11[1][0]==turn and list11[2][0]==turn:
                print(players2 + "  Κέρδισε το γύρο!!")
                c = input("Πάτα το enter για να τελειώσει το πρόγραμμα")    
                quit()
            elif list11[0][2]==turn and list11[1][2]==turn and list11[2][2]==turn:
                print(players2 + "  Κέρδισε το γύρο!!")
                c = input("Πάτα το enter για να τελειώσει το πρόγραμμα")    
                quit()
            elif list11[0][4]==turn and list11[1][4]==turn and list11[2][4]==turn:    
                print(players2 + "  Κέρδισε το γύρο!!")
                c = input("Πάτα το enter για να τελειώσει το πρόγραμμα")    
                quit() 	
            for j in range(3):
                win = 0            
                for n in range(0,5,2):
                    if list11[j][n]==turn: 
                        win += 1
                if win == 3:
                    print(players2 + "  Κέρδισε το γύρο!!")
                    c = input("Πάτα το enter για να τελειώσει το πρόγραμμα")    
                    quit()
            turn = " O "
            players2 = "Υπολογιστής"    
c = input("Πάτα το enter για να τελειώσει το πρόγραμμα")
