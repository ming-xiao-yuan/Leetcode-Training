import subprocess
import xml.etree.ElementTree as ET
import random
import os

USED_INDICES_FILE = "used_indices.txt"


def main():
    while True:
        choice = input("Press 1 for Blind 75 or Press 2 for Neetcode 150: ")
        if choice == "1":
            tree = ET.parse("blind75.xml")
            break
        elif choice == "2":
            tree = ET.parse("neetcode150.xml")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")

    root = tree.getroot()

    questions = root.findall("question")
    print(len(questions))

    used_indices = load_used_indices()

    while len(used_indices) < len(questions):
        random_index = random.randint(0, len(questions) - 1)
        if random_index in used_indices:
            continue

        random_question = questions[random_index]

        statement = random_question.find("statement").text
        solution_code = random_question.find("solution/code").text

        content = f"{statement}\n"

        input("Press to reveal the question...")

        with open("output_question.txt", "w", encoding="utf-8") as file:
            file.write(content)

        subprocess.Popen(["notepad.exe", "output_question.txt"], shell=True)

        used_indices.add(random_index)
        save_used_indices(used_indices)

        input("Press Enter to reveal the answer...")

        content = f"{solution_code}\n"

        with open("output_answer.txt", "w", encoding="utf-8") as file:
            file.write(content)

        subprocess.Popen(["notepad.exe", "output_answer.txt"], shell=True)

    print("All questions have been used.")


def load_used_indices():
    if not os.path.exists(USED_INDICES_FILE):
        return set()

    with open(USED_INDICES_FILE, "r") as file:
        lines = file.readlines()
        return {int(line.strip()) for line in lines}


def save_used_indices(used_indices):
    with open(USED_INDICES_FILE, "w") as file:
        for index in used_indices:
            file.write(f"{index}\n")


if __name__ == "__main__":
    main()
