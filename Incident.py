from tkinter import *
import tkinter as tk
import random
import Monsterlist

def Getitem_list_(self):
    self.I_label_ = tk.Label(self.Incident_canvas,text="战利品：",font=('微软雅黑',20, "bold"),anchor='nw',justify='left',wraplength=1450)
    self.I_label_.place(x=380,y=75)
    self.I_label_ = tk.Label(self.Incident_canvas,text=self.getitem,font=('微软雅黑',18, "bold"),anchor='nw',justify='left',wraplength=1450)
    self.I_label_.place(x=400,y=150)


def AreaLevel10_Incident(self):
        i = random.randint(1,15)
        # i = 1
        if i == 1:
            self.AreaLevel10_label_ = tk.Label(self.AreaLevel10_canvas,text="你遇到了一群正在吞噬动物尸体的蜘蛛 [Lv1]" + "\n\n是否发起进攻？",font=('微软雅黑',17, "bold"),anchor='nw',justify='left',wraplength=1450)
            self.AreaLevel10_label_.place(x=80,y=30)
            self.AreaLevel10_button_ = tk.Button(self.AreaLevel10_canvas,text="【进入战斗】", anchor="nw", font=("微软雅黑", 18, "bold"),bd=0,command=self.Fight_track)
            self.AreaLevel10_button_.place(x=720,y=330)
            self.M_id = 1
        elif i == 2:
            self.AreaLevel10_label_ = tk.Label(self.AreaLevel10_canvas,text="你遇到了一群正在攻击行人的恐狼 [Lv3]" + "\n\n是否发起进攻？",font=('微软雅黑',17, "bold"),anchor='nw',justify='left',wraplength=1450)
            self.AreaLevel10_label_.place(x=80,y=30)
            self.AreaLevel10_button_ = tk.Button(self.AreaLevel10_canvas,text="【进入战斗】", anchor="nw", font=("微软雅黑", 18, "bold"),bd=0,command=self.Fight_track)
            self.AreaLevel10_button_.place(x=720,y=330)
            self.M_id = 3
        elif i == 3:
            self.AreaLevel10_label_ = tk.Label(self.AreaLevel10_canvas,text="你遇到了一群正在侦查的哥布林斥候 [Lv6]" + "\n\n是否发起进攻？",font=('微软雅黑',17, "bold"),anchor='nw',justify='left',wraplength=1450)
            self.AreaLevel10_label_.place(x=80,y=30)
            self.AreaLevel10_button_ = tk.Button(self.AreaLevel10_canvas,text="【进入战斗】", anchor="nw", font=("微软雅黑", 18, "bold"),bd=0,command=self.Fight_track)
            self.AreaLevel10_button_.place(x=720,y=330)
            self.M_id = 5
        elif i == 4:
            self.AreaLevel10_label_ = tk.Label(self.AreaLevel10_canvas,text="【Boss预警！】你通过了茂密的树林，远处突然传来一阵咆哮声。你小心翼翼地靠近，发现一只巨大的蜘蛛正在追赶一位受伤的旅行者。" + "\n\n是否发起进攻？",font=('微软雅黑',17, "bold"),anchor='nw',justify='left',wraplength=1450)
            self.AreaLevel10_label_.place(x=80,y=30)
            self.AreaLevel10_button_ = tk.Button(self.AreaLevel10_canvas,text="【进入战斗】", anchor="nw", font=("微软雅黑", 18, "bold"),bd=0,command=self.Fight_track)
            self.AreaLevel10_button_.place(x=720,y=330)
            self.M_id = 2
        elif i == 5:
            self.AreaLevel10_label_ = tk.Label(self.AreaLevel10_canvas,text="【Boss预警！】你穿过一片幽暗的森林，突然听到了一个低沉的咆哮声。你警觉地举起武器，环顾四周，发现一只巨大的恐狼正准备袭击你。" + "\n\n是否发起进攻？",font=('微软雅黑',17, "bold"),anchor='nw',justify='left',wraplength=1450)
            self.AreaLevel10_label_.place(x=80,y=30)
            self.AreaLevel10_button_ = tk.Button(self.AreaLevel10_canvas,text="【进入战斗】", anchor="nw", font=("微软雅黑", 18, "bold"),bd=0,command=self.Fight_track)
            self.AreaLevel10_button_.place(x=720,y=330)
            self.M_id = 4
        elif i == 6:
            self.AreaLevel10_label_ = tk.Label(self.AreaLevel10_canvas,text="【Boss预警！】你遭遇了一场剧烈的雷雨，闪电照亮了整个天空。你急忙寻找一个避难所来躲避，最终找到了一个巨大的洞穴。洞穴内部干燥温暖，你安全地度过了雷雨。在洞穴的尽头你遇到了一个身穿链甲，手持巨斧的哥布林队长。" + "\n\n是否发起进攻？",font=('微软雅黑',17, "bold"),anchor='nw',justify='left',wraplength=1450)
            self.AreaLevel10_label_.place(x=80,y=30)
            self.AreaLevel10_button_ = tk.Button(self.AreaLevel10_canvas,text="【进入战斗】", anchor="nw", font=("微软雅黑", 18, "bold"),bd=0,command=self.Fight_track)
            self.AreaLevel10_button_.place(x=720,y=330)
            self.M_id = 6
        elif i == 7:
            self.AreaLevel10_label_ = tk.Label(self.AreaLevel10_canvas,text="你来到了一片神秘的草原，草地上繁花似锦。你小心地走过，突然发现一朵特别美丽的花朵。你弯下腰仔细观察，意外地发现它是一朵能够治愈伤势的神奇之花。你小心地采摘了几朵，并将它们放入草药包中，为今后的冒险留下了宝贵的治疗药品。\n\n【初级药草x2】",font=('微软雅黑',17, "bold"),anchor='nw',justify='left',wraplength=1450)
            self.AreaLevel10_label_.place(x=80,y=30)
            self.getitem.append("【初级药草x2】")
        elif i == 8:
            self.AreaLevel10_label_ = tk.Label(self.AreaLevel10_canvas,text="你来到了一片险恶的沙漠，烈日炎炎，无处可藏。你渴望找到水源，突然发现一座古老的神庙。神庙的深处似乎隐藏着一股神秘的力量，你充满希望地走进去。在迷宫般的通道中，你发现了一口神奇的井泉，汲取了清凉的水，恢复了体力。\n\n【血量回复50%】",font=('微软雅黑',17, "bold"),anchor='nw',justify='left',wraplength=1450)
            self.AreaLevel10_label_.place(x=80,y=30)
            self.HP = int(self.HP) + int(self.HP_Max) *0.5
        elif i == 9:
            self.AreaLevel10_label_ = tk.Label(self.AreaLevel10_canvas,text="你在森林中遇到了一位神秘的女巫，她看起来古怪而神秘。女巫递给你一枚发光的宝石，告诉你它可以为你带来好运和保护。你将宝石系在项链上，并感受到一股神奇的力量环绕着你的身体，似乎能够预知未来的危险。\n\n【智力+1】",font=('微软雅黑',17, "bold"),anchor='nw',justify='left',wraplength=1450)
            self.AreaLevel10_label_.place(x=80,y=30)
            self.Int = int(self.Int) + 1
            self.getitem.append("【智力+1】")
        elif i == 10:
            self.AreaLevel10_label_ = tk.Label(self.AreaLevel10_canvas,text="你来到了一座废弃的古堡，里面弥漫着一股诡异的气氛。你小心地探索着，突然发现一道隐藏的门。你推开门，进入了一个神秘的地下墓穴。墓穴中闪烁着微弱的蓝色光芒，你紧张而激动地继续前行，期待着能够发现宝藏的线索。",font=('微软雅黑',17, "bold"),anchor='nw',justify='left',wraplength=1450)
            self.AreaLevel10_label_.place(x=80,y=30)
        elif i == 11:
            self.AreaLevel10_label_ = tk.Label(self.AreaLevel10_canvas,text="你在山谷中迷路了，四周一片荒凉。正当你绝望之际，你发现一束光线从天空中射下，照亮了前方的道路。你跟随着光线，最终发现了一座神秘的祭坛。祭坛上放着一枚闪耀的宝石，你小心地将它收入囊中，感受到一股神秘的力量注入了你的身体。\n\n【力量+1】",font=('微软雅黑',17, "bold"),anchor='nw',justify='left',wraplength=1450)
            self.AreaLevel10_label_.place(x=80,y=30)
            self.Str = int(self.Str) + 1
            self.getitem.append("【力量+1】")
        elif i == 12:
            self.AreaLevel10_label_ = tk.Label(self.AreaLevel10_canvas,text="你走进一片神秘的森林，树木高大而茂密。在探索的过程中，你遇到了一只受伤的精灵。你心生怜悯，为精灵进行了简单的治疗，精灵感激地向你透露了一个隐藏宝藏的线索。你按照线索找到了宝藏，里面有一件神秘的护甲，能够增强你的防御力。\n\n【防御力+1】",font=('微软雅黑',17, "bold"),anchor='nw',justify='left',wraplength=1450)
            self.AreaLevel10_label_.place(x=80,y=30)
            self.Defense = int(self.Defense) + 1
            self.getitem.append("【防御力+1】")
        elif i == 13:
            self.AreaLevel10_label_ = tk.Label(self.AreaLevel10_canvas,text="你来到了一座险峻的山脉，山峰高耸入云。在攀登的过程中，你不慎滑倒，危机四伏。幸运的是，你及时抓住了一根突出的岩石，保住了生命。\n\n【生命减少20%】",font=('微软雅黑',17, "bold"),anchor='nw',justify='left',wraplength=1450)
            self.AreaLevel10_label_.place(x=80,y=30)
            self.HP = int(self.HP) * 0.2
        elif i == 14:
            self.AreaLevel10_label_ = tk.Label(self.AreaLevel10_canvas,text="你进入了一片神秘的湖泊，湖水清澈而宁静。你决定探索湖底，发现了一座被遗忘的水下宫殿。宫殿中散发出一股神秘的能量，你充满好奇地游走其中。最终，你发现了一块被遗忘的宝石，它散发出耀眼的光芒，能够增强你的敏捷能力。\n\n【敏捷+1】",font=('微软雅黑',17, "bold"),anchor='nw',justify='left',wraplength=1450)
            self.AreaLevel10_label_.place(x=80,y=30)
            self.Agi = int(self.Agi) +1
            self.getitem.append("【敏捷+1】")
        elif i == 15:
            self.AreaLevel10_label_ = tk.Label(self.AreaLevel10_canvas,text="你来到了一片苹果园，农场主看到你走了过来似乎很是高兴。在他口中得知，正因为有像我们这样的冒险者存在，附近很久没有遭到魔物的侵袭了。为表感谢农场主赠送了你一些苹果。\n\n【苹果x3】",font=('微软雅黑',17, "bold"),anchor='nw',justify='left',wraplength=1450)
            self.AreaLevel10_label_.place(x=80,y=30)
            self.getitem.append("【苹果x3】")


