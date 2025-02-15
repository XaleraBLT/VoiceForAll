import subprocess, sys

def text_to_speech(text:str):
    command = [
        "piper",
        "--model", "ru_RU-dmitri-medium",
        "--output_file", "res.wav"
    ]

    process = subprocess.run(command, input=text, text=True, capture_output=True)

    if process.returncode == 0:
        return "Аудиофайл res.wav успешно создан"
    else:
        return "Ошибка:", process.stderr

if __name__ == "__main__":
    text = input("Введите текст: ").encode(sys.stdin.encoding or "utf-8").decode("utf-8")
    print(text_to_speech(text))

