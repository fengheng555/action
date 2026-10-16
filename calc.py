# 简易计算器，后续可以继续加功能
def add(a, b):
return a + b

def sub(a, b):
return a - b

if __name__ == "__main__":
print("===简易计算器===")
num1 = float(input("输入第一个数字："))
op = input("输入运算符 + 或 -：")
num2 = float(input("输入第二个数字："))

if op == "+":
res = add(num1, num2)
elif op == "-":
res = sub(num1, num2)
else:
res = "不支持该运算符"
print(f"结果：{res}")

