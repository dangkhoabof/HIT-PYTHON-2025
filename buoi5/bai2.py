students = [
    {"id": 1, "name": "An", "score": 8.5},
    {"id": 2, "name": "Bình", "score": 7.2},
    {"id": 3, "name": "Chi", "score": 9.0}
]
def find_by_id(data: list[dict], id: int) :
    for student in data:
        if student["id"] == id:
            return student
    return None


def filter_by_score(data, min_score):
    result = []
    for student in data:
        if student["score"] >= min_score:
            result.append(student)
    return result


def sort_by_score(data, reverse=False):
    temp = data[:]
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            if reverse:
                if temp[i]["score"] < temp[j]["score"]:
                    temp[i], temp[j] = temp[j], temp[i]
            else:
                if temp[i]["score"] > temp[j]["score"]:
                    temp[i], temp[j] = temp[j], temp[i]
    return temp


def add_student(data, student_dict):
    if "id" not in student_dict or "name" not in student_dict or "score" not in student_dict:
        print("Lỗi: sinh viên phải có id, name, score")
        return
    data.append(student_dict)

def remove_student(data, id):
    for i in range(len(data)):
        if data[i]["id"] == id:
            data.pop(i)
            return True
    return False


def statistics(data):
    if len(data) == 0:
        return 0, None, None

    total = 0
    highest = data[0]
    lowest = data[0]

    for student in data:
        total += student["score"]
        if student["score"] > highest["score"]:
            highest = student
        if student["score"] < lowest["score"]:
            lowest = student

    mean_score = total / len(data)
    return mean_score, highest, lowest


print("1. Tìm id = 2       :", find_by_id(students, 2))
print("2. Điểm >= 8.0      :", filter_by_score(students, 8.0))
print("3. Sắp xếp tăng dần :", sort_by_score(students))
print("   Sắp xếp giảm dần :", sort_by_score(students, reverse=True))


add_student(students, {"id": 4, "name": "Dũng", "score": 6.8})
print("4. Sau khi thêm Dũng:", [s["name"] for s in students])


avg, best, worst = statistics(students)
print(f"5. Điểm trung bình: {avg:.2f}")
print(f"   Cao nhất: {best['name']} ({best['score']})")
print(f"   Thấp nhất: {worst['name']} ({worst['score']})")



print(find_by_id(students, 1))
print(students)