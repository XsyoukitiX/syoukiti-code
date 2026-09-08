#2026/9/6
print("＾ー＾ゲーム＾ー＾")
print("ルール：あなたはポイントを持っています。ポイントを賭けて6面ダイスを振り、結果によりポイントが変動したりします")
print("ポイントが0になったらゲームオーバー、ポイントが10000になったらゲームクリア")
print("所持ポイントをP,賭けるポイントをWPと呼びます")
print("（変動の詳細を知りたい時は「dice」と入力）")

P = 200 #Pは所持ポイント　初期ポイントは２００
import random
count = 1
while True:
    D = random.randint(1,6) #Dはダイスの目
    print("《", count, "ターン目》 ", "所持ポイント：", P)
    IN = input("賭けるポイントを入力：")
    if IN == "dice": #diceか判断
          print("1:WP倍率0 /2:WP倍率0.5 /3,4:WP倍率1 /5:WP倍率1.5 /6:WP倍率2.5")
    else: #diceでなければ
       if IN.isdecimal(): #整数値なら
           IN = int(IN)
           if 1 <= IN <= P:
               count += 1
               if D == 1:
                   print("ダイスの目", D, "-WP倍率0-")
                   P = P - IN

               if D == 2:
                 print("ダイスの目", D, "-WP倍率0.5-") 
                 P = P - IN + IN // 2   

               if D == 3 or D == 4:
                print("ダイスの目", D, "-WP倍率1-")

               if D == 5:
                print("ダイスの目", D, "-WP倍率1.5-")
                P = P + IN + IN // 2

               if D == 6:  
                print("ダイスの目", D, "-WP倍率2.5-")
                P = P + 2 * IN + IN // 2

           else:
               print("ERROR 1～Pの範囲で入力されていません") 

       else:
           print("ERROR 整数値が入力されていません")   

    if P >= 10000:
        print("P=", P)
        print("GAME CLEAR")
        print("クリア", count, "ターン目")
        break

    if P == 0:
        print("GAME OVER")    
        break
    #END