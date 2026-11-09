from quiz import Quiz


def make_default_quizzes() -> list[Quiz]:
    return [
        Quiz(
            "input()으로 7을 입력하면 반환값의 자료형은?",
            ["int", "str", "bool", "list"],
            2,
        ),
        Quiz(
            "파이썬에서 여러 값을 순서대로 담고 append()로 추가할 수 있는 자료형은?",
            ["dict", "int", "list", "bool"],
            3,
        ),
        Quiz(
            "README.md의 변경 내용을 다음 커밋에 포함하도록 준비하는 명령은?",
            ["git add README.md", "git log", "git status", "git diff"],
            1,
        ),
        Quiz(
            "파이썬에서 JSON 파일을 읽기 위해 open()에 전달할 모드는?",
            ["w", "a", "x", "r"],
            4,
        ),
        Quiz(
            "원격 Git 저장소를 새 로컬 폴더로 처음 복제하는 명령은?",
            ["git push", "git clone", "git commit", "git merge"],
            2,
        ),
    ]
