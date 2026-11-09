import json
import random
from pathlib import Path
from tempfile import TemporaryDirectory

from defaults import make_default_quizzes
from inputs import read_number, read_text
from quiz import Quiz


STATE_FILE = Path(__file__).resolve().with_name("state.json")


class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = None
        self.dirty = False
        self.can_save = True

    def load(self):
        try:
            with STATE_FILE.open("r", encoding="utf-8") as source:
                data = json.load(source)

            if not isinstance(data, dict) or not isinstance(data.get("quizzes"), list):
                raise ValueError("quizzes는 배열이어야 합니다.")
            if "best_score" not in data:
                raise ValueError("best_score 필드가 없습니다.")

            quizzes = [Quiz.from_dict(item) for item in data["quizzes"]]
            best = data["best_score"]

        except FileNotFoundError:
            print("첫 실행입니다. 기본 퀴즈로 시작합니다.")
        except ValueError as error:
            print(f"저장 데이터가 손상되었습니다. 기본 퀴즈로 복구합니다. ({error})")
        except OSError as error:
            self.can_save = False
            print(f"파일을 읽을 수 없어 기본 퀴즈로 진행합니다. ({error})")
            print("기존 파일을 보호하기 위해 이번 실행의 저장을 건너뜁니다.")
        else:
            self.quizzes = quizzes
            self.best_score = best
            print(f"저장된 데이터를 불러왔습니다. (퀴즈 {len(quizzes)}개)")
            return

        self.quizzes = make_default_quizzes()
        self.best_score = None
        if self.can_save:
            self.dirty = True
            self.save()

    def save(self) -> bool:
        if not self.dirty:
            return True
        if not self.can_save:
            print("기존 파일을 읽지 못해 변경 사항을 저장할 수 없습니다.")
            return False

        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
        }

        try:
            with TemporaryDirectory(dir=STATE_FILE.parent, prefix=".quiz-save-") as folder:
                temporary = Path(folder) / "state.json"
                with temporary.open("w", encoding="utf-8") as target:
                    json.dump(data, target, ensure_ascii=False, indent=2)
                    target.write("\n")
                temporary.replace(STATE_FILE)
        except OSError as error:
            print(f"저장에 실패했습니다. 폴더의 쓰기 권한과 남은 공간을 확인하세요. ({error})")
            return False

        self.dirty = False
        return True

    def show_menu(self):
        print("\n=== 도전! 일반상식 퀴즈 ===")
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

    def add_quiz(self):
        print("새로운 퀴즈를 추가합니다.")
        question = read_text("문제를 입력하세요: ")

        choices = []
        for number in range(1, 5):
            choices.append(read_text(f"선택지 {number}: "))

        answer = read_number("정답 번호 (1~4): ", 1, 4)

        self.quizzes.append(Quiz(question, choices, answer))
        self.dirty = True
        if self.save():
            print("퀴즈가 추가되었습니다!")
        else:
            print("퀴즈를 메모리에 추가했습니다. 종료 시 저장을 다시 시도합니다.")

    def run(self):
        while True:
            self.show_menu()
            choice = read_number("선택: ", 1, 5)

            if choice == 1:
                self.play()
            elif choice == 2:
                self.add_quiz()
            elif choice == 5:
                return
            else:
                print("이 기능은 다음 단계에서 연결합니다.")
