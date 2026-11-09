from game import QuizGame


def main():
    game = QuizGame()

    try:
        game.load()
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되었습니다.")

    try:
        if not game.save():
            print("저장되지 않은 변경이 있습니다.")
    except KeyboardInterrupt:
        print("\n저장이 중단되었습니다. 마지막으로 저장된 상태가 유지됩니다.")

    print("퀴즈 게임을 종료합니다.")


if __name__ == "__main__":
    main()
