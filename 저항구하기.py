print("저항의 색띠를 통한 저항값과 허용 오차 구하기")
print("1~3번째 숫자는 0~9까지의 숫자를, 4번째 숫자는 0~2까지의 숫자를 넣으세요!")
print("ex) 6 1 2 0")
color1=['black','brown','red','orange','yellow','green','blue','violet','gray','white']
color2=['gold','silver','none']

while(1):
    try :
        x=input("4개의 숫자 입력:")
        for h in range (1,4):
            print(h,"번째 색띠는",color1[int(x[2*h-2])],"입니다.")
            h+=1
        print("4 번째 색띠는",color2[int(x[6])],"입니다.")
    except ValueError :
        continue
    except IndexError :
        print("정확히 다시 입력하세요.")
        continue
        
    input("이 저항의 저항값과 허용오차는 얼마일까요? 답을 보려면 엔터를 누르시오.")
    a1=(10*int(x[0])+int(x[2]))*10**int(x[4])
    if int(x[6])!=2:
        a2=5+5*int(x[6])
    else:
        a2=20
    print("저항값은",a1,"옴, 오차는",a2,"%입니다.")
    con = input("계속하시려면 엔터, 종료하시려면 Q를 입력해주세요.")
    if con == "Q" or con == 'q' : exit()
