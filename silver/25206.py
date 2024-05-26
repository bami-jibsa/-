names = []
hacs = []
pys = []

for _ in range(20):
    name, hac, py = input().split()
    if py != "P":
        names.append(name)
        hacs.append(float(hac))
        pys.append(py)

def mx(grade, credits):
    grade_map = {
        "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
        "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0
    }
    return grade_map.get(grade, 0.0) * credits


total_points = 0.0
total_credits = 0.0

for i in range(len(hacs)):
    total_points += mx(pys[i], hacs[i])
    total_credits += hacs[i]

if total_credits > 0:
    gpa = total_points / total_credits
    print(f"{gpa:.6f}")
else:
    print("0.000000")
