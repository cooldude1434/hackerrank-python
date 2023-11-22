height, width = map(int, input().split())
final_result = {}

for i in range(1, (int(height)//2)+1):
    line = (".|."*(2*i-1)).center(width, "-")
    final_result[i-1] = final_result[height-i] = line
final_result[height//2] = ("WELCOME".center(width, "-"))
for line in range(height):
    print(final_result[line])
