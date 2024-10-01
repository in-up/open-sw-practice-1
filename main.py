def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

while True:
    formula = input("두 정수와 연산자를 포함한 수식 입력, 또는 'q'로 프로그램 종료 (예: 3 + 4)\n-> ")
    
    if formula.lower() == 'q':
        break
    
    try:
        a, op, b = map(str, formula.split())
        a = int(a)
        b = int(b)
    except ValueError:
        print("[X] 다시 시도해주세요.")
        continue
    
    result = None
    
    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    elif op == '/':
        result = div(a, b)
    else:
        print("[X] 유효하지 않은 연산자입니다.")
        continue
    
    if result is not None:
        print(f'[계산 결과] {result}')
