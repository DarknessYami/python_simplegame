import tkinter as tk

def update_health(health_value):
    # 更新血条长度
    health_bar["length"] = health_value

def attack():
    # 处理攻击判定
    # 假设攻击造成的伤害为 damage
    damage = 20
    current_health = health_bar["length"]
    max_health = 100

    # 更新剩余血量
    remaining_health = current_health - damage

    # 计算剩余血量的百分比
    health_percentage = (remaining_health / max_health) * 100

    # 更新血条
    update_health(health_percentage)

# 创建主窗口
root = tk.Tk()
root.title("战斗系统")

# 创建血条
health_bar = tk.Canvas(root, width=100, height=20, bg="white")
health_bar.pack()

# 初始化血条
update_health(100)

# 创建攻击按钮
attack_button = tk.Button(root, text="攻击", command=attack)
attack_button.pack()

# 运行主循环
root.mainloop()