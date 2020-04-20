def avg_from_file(f):
    from re import search
    with open(f, 'r') as f:
        lines = f.readlines()
    avg = 0.
    for line in lines:
        avg += float(search(r'\s?(\d+)\s?', line).group(0))
        print(float(search(r'\s?(\d+)\s?', line).group(0)))
    avg /= len(lines)
    return avg

print(avg_from_file('test.txt'))
