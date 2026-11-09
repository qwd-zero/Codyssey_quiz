import random

from defaults import make_default_quizzes
from inputs import read_number


class QuizGame:
    def __init__(self):
        self.quizzes = make_default_quizzes()

    def show_menu(self):
        print("\n=== 파이썬·Git 첫걸음 퀴즈 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

    def play(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 메뉴 2에서 먼저 추가하세요.")
            return

        round_quizzes = self.quizzes.copy()
        random.shuffle(round_quizzes)
        total = len(round_quizzes)
        correct = 0
        print(f"\n퀴즈를 시작합니다! (총 {total}문제)")

        for number, quiz in enumerate(round_quizzes, start=1):
            quiz.show(number)
            guess = read_number("정답 입력 (1~4): ", 1, 4)

            if quiz.is_correct(guess):
                correct += 1
                print("정답입니다!")
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        points = correct * 100 // total
        print(f"\n결과: {total}문제 중 {correct}문제 정답! ({points}점)")

    def run(self):
        while True:
            self.show_menu()
            choice = read_number("선택: ", 1, 5)

            if choice == 1:
                self.play()
            elif choice == 5:
                return
            else:
                print("이 기능은 다음 단계에서 연결합니다.")
