x = int(input()) #정수형으로 변환하고 x 변수에 저장
sum = 0 # sum 변수에 0을 할당

for _ in range(int(input())):
    #for문을 사용하여 _ 무의미한 변수를 선언하고 range() 함수에 횟수만큼 반복 
    a,b= map(int, input().split())
    #map함수와 input 함수 split 메소드를 사용하여 두 개의 정수형 값을 입력받음 a,b변수에 각가 저장 
    sum += a * b #sum 변수에 a*b 값을 더해줌
    print("yes") if sum == x else print("No") #yes 문자열을 출력하거나 no 문자열을 출력함
    
  