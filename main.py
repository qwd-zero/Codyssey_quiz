from inputs import read_number


def show_menu():
    print("\n=== 파이썬·Git 첫걸음 퀴즈 ===")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")


def run():
    while True:
        show_menu()
        choice = read_number("선택: ", 1, 5)

        if choice == 5:
            return

        print("이 기능은 다음 단계에서 연결합니다.")


if __name__ == "__main__":
    try:
        run()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되었습니다.")
    print("퀴즈 게임을 종료합니다.")