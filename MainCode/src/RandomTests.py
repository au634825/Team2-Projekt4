res = b'[8, 8, 64, 1.0, 0, 14]'.decode("utf-8")
print(type(res))
print(res)
res = eval(res)

print(type(res))

print(res[0])
for el in res:
    print(el)