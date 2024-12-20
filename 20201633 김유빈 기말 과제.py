import random
import json

# 30명의 학생 데이터 랜덤 생성
def generate_students():
    students = []
    for _ in range(30):
        name = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
        age = random.randint(18, 22)
        score = random.randint(0, 100)
        students.append({"이름": name, "나이": age, "성적": score})
    return students

# 파일에 학생 정보 저장
def save_students_to_file(students, filename="students.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

# 파일에서 학생 정보를 불러오기
def load_students_from_file(filename="students.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

# 정렬 알고리즘 구현
def selection_sort(data, key, reverse=False):
    n = len(data)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if (data[j][key] < data[idx][key]) != reverse:
                idx = j
        data[i], data[idx] = data[idx], data[i]

def insertion_sort(data, key, reverse=False):
    for i in range(1, len(data)):
        current = data[i]
        j = i - 1
        while j >= 0 and (data[j][key] > current[key]) != reverse:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current

# 비재귀적인 퀵 정렬
def quick_sort(data, key, reverse=False):
    stack = [(0, len(data) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(data, low, high, key, reverse)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

def partition(data, low, high, key, reverse):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if (data[j][key] < pivot[key]) != reverse:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1

def radix_sort(data, key):
    max_val = max(student[key] for student in data)
    exp = 1
    while max_val // exp > 0:
        counting_sort(data, key, exp)
        exp *= 10

def counting_sort(data, key, exp):
    n = len(data)
    output = [None] * n
    count = [0] * 10

    for student in data:
        index = (student[key] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (data[i][key] // exp) % 10
        output[count[index] - 1] = data[i]
        count[index] -= 1

    for i in range(n):
        data[i] = output[i]

# 학생 목록 출력
def display_students(students):
    print("\n학생 목록:")
    for student in students:
        print(student)

def main():
    students = load_students_from_file()
    if not students:
        students = generate_students()
        save_students_to_file(students)

    display_students(students)

    while True:
        print("\n메뉴:")
        print("1. 이름을 기준으로 정렬하기")
        print("2. 나이를 기준으로 정렬하기")
        print("3. 성적을 기준으로 정렬하기")
        print("4. 프로그램 종료하기")

        choice = input("원하시는 메뉴를 선택하세요 : ")

        if choice == '4':
            print("프로그램을 종료합니다.")
            break

        field_map = {'1': "이름", '2': "나이", '3': "성적"}
        if choice not in field_map:
            print("잘못된 선택입니다. 다시 시도하세요.")
            continue

        key = field_map[choice]
        print("\n정렬 알고리즘:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        print("4. 기수 정렬 (성적 기준만 가능)")

        algo_choice = input("원하시는 정렬 방식을 선택하세요: ")
        reverse = input("오름차순(0) 또는 내림차순(1): ") == '1'

        if algo_choice == '1':
            selection_sort(students, key, reverse)
        elif algo_choice == '2':
            insertion_sort(students, key, reverse)
        elif algo_choice == '3':
            quick_sort(students, key, reverse)
        elif algo_choice == '4' and key == "성적":
            radix_sort(students, key)
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
            continue

        display_students(students)
        save_students_to_file(students)

if __name__ == "__main__":
    main()
