nums = []

while len(nums) < 3:
    num = int(input("Digite un numero: "))
    nums.append(num)

avarage = sum(nums) / len(nums)

print(avarage)
