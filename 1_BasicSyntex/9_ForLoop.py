apple_smart = ['iPhone X', 'iPhone 11', 'apple watch', 'iPad']

images = [[10, 10], [30, 60], [640, 480]] #[w,h]

for device in apple_smart:
    print (device)

idx = []

for i in list(range(0, 5)):
    idx.append(i)

print(idx)

for width, height in images:
    print(f"width : {width} height : {height}")