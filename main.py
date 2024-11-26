import random

lower_alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] ## lower_alphabets 변수를 추가

upper_alphabets = [] ## 대문자를 저장할 빈 리스트

for alphabet in lower_alphabets: ## lower_alphabets 변수를 alphabet에 대입 (a~z)
  upper_alphabets.append(alphabet.upper()) ## append 펑션을 사용하여 문자열끝에 대문자로 변환 하여 upper_alphabets에 추가 
alphabet  = lower_alphabets + upper_alphabets # 소문자와 대문자를 결한한 List

numbers   = [str(i) for i in range(0, 10) ] ## range 펑션으로 1~9까지 i 안에 string으로 저장

symblos   = ["!", "#", "$", "%", "&", "*", "(", ")", "+"] ## 특수문자 리스트

num_of_alphabets = 9 ## 추가할 문자열의 수
num_of_numbers = 3 ## 추가할 숫자의 수
num_of_symbols = 2 ## 추가할 특수문자의 수

strong_password = [] ## 패스워드를 구성할 리스트

for i in range(0, num_of_alphabets): ## 알파벳을 랜덤하게 선택하여 추가
  strong_password.append(alphabet[random.randint(0, len(alphabet)-1)]) 
  
for i in range(0, num_of_numbers): ## 0~num_of_numbers의 변수에따라 i의 값을 추가
  strong_password.append(numbers[random.randint(0, len(numbers)-1)]) ## 0~number(마지막 인덱스포함) 문자열의 개수를 확인하고 random.randint 펑션을 사용하여 랜덤으로 문자열의 맨끝에 추가하고 strong_password에 값을 추가

for i in range(0, num_of_symbols): ## 0~num_of_symbols의 변수에따라 i의 값을 추가
  strong_password.append(symblos[random.randint(0, num_of_symbols)-1])

random.shuffle(strong_password) ##random.shuffle(섞음)펑션으로 무작위로 패스워드를 생성

print("".join(strong_password)) ## join 펑션으로 List 문자열을 하나로 결합하여 출력 
