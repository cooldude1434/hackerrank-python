
eng_count = int(input())
eng_roll = set(input().split())

frn_count = int(input())
frn_roll = set(input().split())

print(len(eng_roll.difference(frn_roll)))
