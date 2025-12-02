with open('day1.txt', 'r') as f:
    pos = 50
    password = 0
    for line in f:
        dir, rot = line[:1], line[1:]
        rot = int(rot)
        if dir == 'L':
            pos = (pos - rot) % 100
        else:
            pos = (pos + rot) % 100
        if pos == 0:
            password += 1
    print(password)

