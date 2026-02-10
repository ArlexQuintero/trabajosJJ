nums = []

while len(nums) < 3:
    num = int(input("Digite un numero: "))
    nums.append(num)

if nums[0] > nums[1] and nums[0] > nums[2]:
    print("El numero 1 es el mayor: ", nums[0])
elif nums[1] > nums[0] and nums[1] > nums[2]:
    print("El numero 2 es el mayor: ", nums[1])
else:
    print("El numero 3 es el mayor: ", nums[2])
