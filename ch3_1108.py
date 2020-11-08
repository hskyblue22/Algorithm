while True:
    n = input("몇 단?")
    if n.isdigit() and len(n)==1 and n != 0:   # 문자열 객체는 isdigit()라는 메서드 가지고 있다.
        break                                  # 문자열이 0이상의 정수인지를 True,False로 반환 -> 정수이면 True되어서 while문 탈출
    else:
        print("숫자만 입력하세요")

n = int(n)
for i in range(1,10):
    print(n,"X",i,"=",n*i)


# 1. try-except
errorfile = open("error.txt","w")
k = 0
try:
    n = int(input("n: "))
    k = 32/n
except ValueError as ve:                  # 사용자가 문자열 등을 입력한 경우
    errorfile.write("valueError: "+str(ve)+"\n")    # TypeError: write() takes exactly one argument (3 given) file.write(,,)안됨
except ZeroDivisionError:                 # n이 0인 경우
    errorfile.write("ZeroDivisionError 발생\n")
except Exception as e:                    # Exception 사용하면 발생한 모든 예외 정보 확인가능
    errorfile.write("type(e)"+str(e)+"\n")    # 예외 또한 객체 
print(k)              # try블록의 오류 발생 여부와 무관하게 실행       

errorfile.close()


# 2. try-finally
try:
    number = input("n: ")
    number = int(number)
finally:             # try블록에서 오류가 발생하든말든 수행
    print(number)    # try블록에서 오류발생할 경우 finally블록마저 끝 -> 프로그램 완전 종료됨
print("Test")


def test():
    try:
        return "A"
    finally:
        print("B")

print(test())            # try(결과값 A 치환) -> finally(B출력)-> 결과값 A 출력
for i in range(100):
    if i == 10:
        try:
            print("C")
            break       # try블록에서 break나 return이 실행되어도 finally는 무조건 실행
        finally:
            print("D")  # try결과에 상관없이 출력됨
print("E")


# 예제 3-9
try:
    file = open("input.txt","r")
except FileNotFoundError:
    print("파일이 없습니다.")
else:
    print(file.read())
    file.close()

# 유제 3-9
file9 = open("구구단출력.txt","w")
try: 
    num = int(input("몇단? "))
except Exception as er:
    file9.write("type(er)"+str(er)+"\n")
else:
    for i in range(1,10):
        file9.write(str(num)+"X"+str(i)+"="+str(num*i)+"\n")
finally:
    file9.close()
