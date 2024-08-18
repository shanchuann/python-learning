# 分苹果
apple = 14
children = 4
print("每人苹果数:", apple // children)
print("剩下苹果数:", apple - (apple // children) * children)
print("总共分出苹果:", (apple // children) * children)