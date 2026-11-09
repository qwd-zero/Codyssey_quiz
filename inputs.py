def read_number(prompt: str, minimum: int, maximum: int) -> int:
    while True:
        raw = input(prompt).strip()

        if not raw:
            print("빈 입력입니다. 숫자를 입력하세요.")
            continue

        try:
            value = int(raw)
        except ValueError:
            print(f"정수를 입력하세요. 허용 범위는 {minimum}~{maximum}입니다.")
            continue

        if minimum <= value <= maximum:
            return value

        print(f"{minimum}~{maximum} 사이의 숫자를 입력하세요.")

def read_text(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("빈 문자열은 등록할 수 없습니다. 다시 입력하세요.")
