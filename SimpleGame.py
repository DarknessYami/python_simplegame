from tkinter import *
import tkinter as tk
from tkinter import messagebox

import random

import Incident #导入事件模组
import Monsterlist#导入怪物属性列表

#Bug汇总处
#1、如果进入战斗直接点击下一回合的话，就会执行空白画布接下来玩家不能攻击，怪物不能攻击。——————战斗系统管理

#代码编写进程 - 2023.6.14
#完善了等级系统，也做好了升级提升技能点。 该做 技能点 加点功能 了


class SimpleGame:
    HP = 0.0
    HP_Max = 0.0
    Attact = 0
    Defense = 0
    name = "未设定"
    Race = "未设定"
    Magical_adaptability = 0.0
    Magical_adaptabilityUP = 0.0
    Str = 0
    Str_coefficient = 0.0
    Agi = 0
    Agi_coefficient = 0.0
    Int = 0
    Int_coefficient = 0.0
    Player_Level = 1
    Player_now = 0
    Player_get = 0
    Player_need = 1000
    Skinpoint = 0
    Skinpoint_str = 0
    Skinpoint_agi = 0
    Skinpoint_int = 0
    Crit_p = 0.0              #暴击概率
    Crit_d = 1.5              #暴击伤害  
    Crit_r = 0.0              #暴击抵抗
    Sidestep_p = 0.0          #闪避概率
    Sidestep_r = 0.0          #闪避抵抗
    Attact_deepen = 0.0       #伤害加深
    Attact_deduction = 0.0    #伤害减免
    Luck = 10.0    

    ps = 100                  #当前体力
    ps_max = 100              #最大体力
    track = None              #战斗系统——怪物追踪
    round = 0                 #战斗系统——显示回合数
    G_round = 0               #战斗系统——系统回合数
    getitem = []              #战利品

    M_id = None               #怪物id
    M_HP = 0
    M_Damage = 0
    M_Defense = 0
    M_name = "              "
    M_Crit_p = 0.0              #怪物暴击概率
    M_Crit_d = 0.0              #怪物暴击伤害  
    M_Crit_r = 0.0              #怪物暴击抵抗
    M_Sidestep_p = 0.0          #怪物闪避概率
    M_Sidestep_r = 0.0          #怪物闪避抵抗
    M_Damage_deepen = 0.0       #怪物伤害加深
    M_Damage_deduction = 0.0    #怪物伤害减免
    M_Luck = 0.0
    M_exp = 0

    def __init__(self,master):
        self.win = master
        self.win.geometry("1280x800")
        self.win.title("为美好的小暗献上祝福！ -开发版本beta-0.1-  测试ing")
        self.Player_Create_set() # 创建新建人物窗口
        self.PlayTheGame()# 创建游戏主要窗口
        self.MenuGameCanvas() #创建开始界面窗口
        self.Player_create_info()
        self.player_set_start()

    def MenuGameCanvas(self):# 主页画布
        self.GameCanvas = tk.Canvas(self.win,width=1280,height=800,highlightthickness=0,borderwidth=0)
        self.GameCanvas.place(x=0,y=0)
        self.Game_logo = tk.PhotoImage(file="python_simplegame\\mainimg\\Title.png")
        self.GameCanvas_img1 = self.GameCanvas.create_image(0,0,image=self.Game_logo,anchor='nw')
        self.GameCanvas_buttom1 = tk.PhotoImage(file="python_simplegame\\mainimg\\kaishiyouxi.png")
        self.GameCanvas_buttom2 = tk.PhotoImage(file="python_simplegame\\mainimg\\jixuyouxi.png")
        self.GameCanvas_buttom3 = tk.PhotoImage(file="python_simplegame\\mainimg\\tuichuyoxui.png")
        self.GameCanvas_c_buttom1 = tk.Button(self.GameCanvas,image=self.GameCanvas_buttom1,bd=0,command=self.Player_Create)
        self.GameCanvas_c_buttom2 = tk.Button(self.GameCanvas,image=self.GameCanvas_buttom2,bd=0,command=self.PlayTheGameToplevel_change)
        self.GameCanvas_c_buttom3 = tk.Button(self.GameCanvas,image=self.GameCanvas_buttom3,bd=0,command=self.win.quit)
        self.GameCanvas_c_buttom1.place(x=325,y=320)
        self.GameCanvas_c_buttom2.place(x=325,y=400)
        self.GameCanvas_c_buttom3.place(x=325,y=480)
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#
#
#—————————————————————————————————————————————————↓↓↓↓↓人物存档管理↓↓↓↓↓——————————————————————————————————————————————————————————————————————————————————
    def Player_file(self):  # 创建人物存档
        try:
            with open("python_simplegame/save/Player_save.txt", 'w') as f:
                f.write(str(self.name) + '\n')  # 姓名
                f.write(str(self.Race) + '\n')  # 种族
                f.write(str(self.Magical_adaptability) + '\n')  # 魔法适应程度
                f.write(str(self.Str) + '\n')  # 力量
                f.write(str(self.Str_coefficient) + '\n')  # 力量成长系数
                f.write(str(self.Agi) + '\n')  # 敏捷
                f.write(str(self.Agi_coefficient) + '\n')  # 敏捷成长系数
                f.write(str(self.Int) + '\n')  # 智力
                f.write(str(self.Int_coefficient) + '\n')  # 智力成长系数
                f.write(str(self.ps) + '\n')   # 当前体力值
                f.write(str(self.ps_max) + '\n')   # 最大体力值
                f.write(str(self.Player_Level) + '\n')   # 玩家等级
                f.write(str(self.Player_now) + '\n')   # 当前经验值
                f.write(str(self.Player_need) + '\n')   # 所需经验值
            messagebox.showinfo("保存成功", "人物存档已保存")
        except Exception as e:
            messagebox.showerror("保存失败", str(e))
    def Player_file_login(self):  # 读取人物存档
        try:
            with open("python_simplegame/save/Player_save.txt", 'r') as f:
                lines = f.readlines()
                self.name = lines[0].strip()  # 姓名
                self.Race = lines[1].strip()  # 种族
                self.Magical_adaptability = lines[2].strip()  # 魔法适应程度
                self.Str = lines[3].strip()  # 力量
                self.Str_coefficient = lines[4].strip()  # 力量成长系数
                self.Agi = lines[5].strip()  # 敏捷
                self.Agi_coefficient = lines[6].strip()  # 敏捷成长系数
                self.Int = lines[7].strip()  # 智力
                self.Int_coefficient = lines[8].strip()  # 智力成长系数
                self.ps = lines[9].strip()  # 当前体力值
                self.ps_max = lines[10].strip()  # 最大体力值
                self.Player_Level = lines[11].strip()   # 玩家等级
                self.Player_now = lines[12].strip()   # 当前经验值
                self.Player_need = lines[13].strip()   # 所需经验值
            messagebox.showinfo("读取成功", "已读取人物存档")
        except Exception as e:
            messagebox.showerror("读取失败", str(e))

#—————————————————————————————————————————————————↑↑↑↑↑人物存档管理↑↑↑↑↑——————————————————————————————————————————————————————————————————————————————————
#
#
#
#—————————————————————————————————————————————————↓↓↓↓↓人物属性管理↓↓↓↓↓——————————————————————————————————————————————————————————————————————————————————
    def player_level(self):#等级系统 
        self.Player_Level_nowset = int(self.Player_now) + int(self.Player_get)
        self.Player_Level_needset = int(self.Player_need)
        while int(self.Player_Level_nowset) >= int(self.Player_Level_needset):
            self.Player_Level = int(self.Player_Level) + 1
            self.Skinpoint = self.Skinpoint + 4
            self.Player_Level_nowset = int(self.Player_Level_nowset) - int(self.Player_Level_needset)
            self.Player_Level_needset = int(self.Player_Level) * 100 + int(self.Player_Level_needset)
            self.Player_need = int(self.Player_Level_needset)
            self.Player_now = int(self.Player_Level_nowset)
            self.create_play_game_main_canvas__Characterattributes()

    def player_hp(self):#玩家血量系统
        self.HP_MaxGet = int(self.Str) + 100 * 4
    def player_Attact(self):#玩家攻击力系统
        self.AttactGet = 20 + int(self.Str) *0.5
    def player_defense(self):#玩家防御力系统
        self.DefenseGet = 5 + int(self.Agi) * 0.2
    def player_Magical_adaptability(self):#玩家魔法适应程度
        self.Magical_adaptabilityUP = self.Magical_adaptability
        self.Magical_adaptabilityGet = "{:.2f}".format(float(self.Magical_adaptabilityUP) + int(self.Int) * 0.1)
    def player_luckey(self):#玩家幸运值
        self.LuckGet = 10 + int(self.Int) * 0.2
    def player_Crit_p(self):#玩家暴击概率
        self.Crit_pGet = int(self.Agi) * 0.1
    def player_Sidestep_p(self):#玩家闪避概率
        self.Sidestep_pGet = int(self.Agi) * 0.1

    #确认属性后进行属性加减然后返回大厅界面
    def create_play_game_main_canvas_playerinforeload(self):
        #生命值
        self.player_hp()
        self.HP_Max = "                     "
        self.HP_Max = self.HP_MaxGet
        self.HP = "                     "
        self.HP = self.HP_MaxGet
        #攻击力
        self.player_Attact()
        self.Attact = "                     "
        self.Attact = self.AttactGet
        #防御力
        self.player_defense()
        self.Defense = "                     "
        self.Defense = self.DefenseGet
        #魔法适应程度
        self.player_Magical_adaptability()
        self.Magical_adaptabilityUP = "                     "
        self.Magical_adaptabilityUP = self.Magical_adaptabilityGet
        #运气
        self.player_luckey()
        self.Luck = "                     "
        self.Luck = self.LuckGet
        #暴击概率
        self.player_Crit_p()
        self.Crit_p = "                     "
        self.Crit_p = self.Crit_pGet
        #闪避概率
        self.player_Sidestep_p()
        self.Sidestep_p = "                     "
        self.Sidestep_p = self.Sidestep_pGet
        self.create_play_game_main_canvas()

    #每次返回大厅界面的时候进行表面刷新并确认属性使用
    def create_play_game_main_canvas_playerinforeload_2(self): 
        #生命值
        self.player_hp()
        self.HP_Max = "                     "
        self.HP_Max = self.HP_MaxGet
        self.HP = "                     "
        self.HP = self.HP_MaxGet
        #攻击力
        self.player_Attact()
        self.Attact = "                     "
        self.Attact = self.AttactGet
        #防御力
        self.player_defense()
        self.Defense = "                     "
        self.Defense = self.DefenseGet
        #魔法适应程度
        self.player_Magical_adaptability()
        self.Magical_adaptabilityUP = "                     "
        self.Magical_adaptabilityUP = self.Magical_adaptabilityGet
        #运气
        self.player_luckey()
        self.Luck = "                     "
        self.Luck = self.LuckGet
        #暴击概率
        self.player_Crit_p()
        self.Crit_p = "                     "
        self.Crit_p = self.Crit_pGet
        #闪避概率
        self.player_Sidestep_p()
        self.Sidestep_p = "                     "
        self.Sidestep_p = self.Sidestep_pGet
#—————————————————————————————————————————————————↑↑↑↑↑人物属性管理↑↑↑↑↑——————————————————————————————————————————————————————————————————————————————————
#
#
#
#—————————————————————————————————————————————————↓↓↓↓↓战斗系统管理↓↓↓↓↓——————————————————————————————————————————————————————————————————————————————————

    def Fight_track(self):
        if self.M_id == 1:
            Monsterlist.zhizhu(self)
        elif self.M_id == 2:
            Monsterlist.boss_zhizhu(self)
        elif self.M_id == 3:
            Monsterlist.konglang(self)
        elif self.M_id == 4:
            Monsterlist.boss_konglang(self)
        elif self.M_id == 5:
            Monsterlist.gebulinchihou(self)
        elif self.M_id == 6:
            Monsterlist.boss_gebulinchihou(self)
        self.Fight_f_() #启动战斗画面


    def Fight_luckjudgment(self):
        pluck = self.Luck
        mluck = self.M_Luck
        if pluck > mluck:
            self.first = 1
        elif pluck == mluck:
            judgment = random.randint(1,2)
            if judgment == 1:
                self.first = 1
            elif judgment == 2:
                self.first = 2
        elif mluck > pluck:
            self.first = 2


    def Fight_hp_j(self):
        if self.HP < 0:
            self.Fight_canvas_setup()  # 加载画布
            self.Fight_random_c = tk.Button(self.PlayTheGame,text="【退出战斗】", anchor="nw", font=("微软雅黑", 18, "bold"),bd=0,command=self.create_play_game_main_canvas)
            self.Fight_random_c.place(x=475,y=750)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 17, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=150)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=155)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 17, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=75)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="你不幸重伤倒地。怪物获得了胜利",font=('微软雅黑', 17, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=70)
            
            
        if self.M_HP < 0:
            self.Fight_canvas_setup()  # 加载画布
            self.Fight_random_c = tk.Button(self.PlayTheGame,text="【退出战斗】", anchor="nw", font=("微软雅黑", 18, "bold"),bd=0,command=self.create_play_game_main_canvas)
            self.Fight_random_c.place(x=475,y=750)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 17, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=150)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=155)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 17, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=75)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="怪物被你斩杀！你获得了胜利",font=('微软雅黑', 17, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=70)
            self.exp

    def FightPlayer_PA(self):
        damage = self.Attact - self.M_Defense
        self.M_HP -= damage

        self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="你对其造成了" + str(damage) + "点物理伤害",font=('微软雅黑', 17, "bold"), anchor='nw', justify='left', wraplength=475, bg=None)
        self.Fight_text.place(x=15, y=150)
        self.G_round = 2
        self.round += 1
    def FightMonster_PA(self):
        damage = self.M_Damage - self.Defense
        self.HP -= damage

        self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="怪物对你造成了" + str(damage) + "点物理伤害",font=('微软雅黑', 17, "bold"), anchor='nw', justify='left', wraplength=475, bg=None)
        self.Fight_text.place(x=15, y=150)
        self.G_round = 1
        self.round += 1

    #战斗系统的画面设置
    def Fight_canvas_setup(self):
        self.Fight_canvas_ = tk.Canvas(self.PlayTheGame, width=1920, height=1080, bg=None)
        self.Fight_canvas_.place(x=0, y=0) 
        #————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        #怪物血条旁边的详细血量（暂定）
        self.Fight_canvas_.create_text(450,150,text=self.M_HP,anchor="nw", fill="black", font=("微软雅黑", 18))
        #怪物血条
        def Fight_canvas_M_hpset():
            self.Fight_canvas_Redset = tk.Canvas(self.PlayTheGame, width=395, height=25, bg="#9c9c9c")
            self.Fight_canvas_Redset.place(x=130, y=180)   
            parent_width_1 = self.Fight_canvas_Redset.winfo_width() # 获取self.Fight_canvas_Redset父容器的宽度
            relative_width_1 = parent_width_1 * 1.0  # 设置为self.Fight_canvas_Redset父容器宽度的100%                         
            self.Fight_canvas_Red = tk.Canvas(self.Fight_canvas_Redset, width=relative_width_1, height=15, bg="#c4161e")
            self.Fight_canvas_Red.place(x=5, y=5)
        self.PlayTheGame.after(100, Fight_canvas_M_hpset)  # 延迟100毫秒后执行Fight_canvas_M_hpset函数
        Fight_canvas_M_hpset()
        #————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        #人物血条旁边的详细血量（暂定）
        self.Fight_canvas_.create_text(1200,450,text=self.HP,anchor="nw", fill="black", font=("微软雅黑", 18))
        #人物血条
        def Fight_canvas_hpset():
            self.Fight_canvas_Greenset = tk.Canvas(self.PlayTheGame, width=395, height=25, bg="#9c9c9c")
            self.Fight_canvas_Greenset.place(x=960, y=480)
            parent_width_2 = self.Fight_canvas_Greenset.winfo_width() # 获取self.Fight_canvas_Greenset父容器的宽度
            relative_width_2 = parent_width_2 * 1.0  # 设置为self.Fight_canvas_Greenset父容器宽度的100%
            self.Fight_canvas_Green = tk.Canvas(self.Fight_canvas_Greenset, width=relative_width_2, height=15, bg="#277f00")
            self.Fight_canvas_Green.place(x=5, y=5)
        self.PlayTheGame.after(100, Fight_canvas_hpset)  # 延迟100毫秒后执行Fight_canvas_hpset函数
        Fight_canvas_hpset()
        #————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

        self.Fight_canvas_.create_text(970, 405, text=self.name + "[Level:   " + str(self.Player_Level) + "  ]", anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.Fight_canvas_.create_text(140, 140, text=self.M_name, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        #人物
        self.Fight_canvas_playerimg = tk.PhotoImage(file="python_simplegame\\playerimg\\player.png")
        self.Fight_canvas_.create_image(1024, 530, image=self.Fight_canvas_playerimg, anchor="nw")
        #战斗记录                                                                          "#d4d4d4"
        self.Fight_canvas_noteset = tk.Canvas(self.PlayTheGame, width=500, height=1030, bg=None)
        self.Fight_canvas_noteset.place(x=1400, y=20)  
        self.Fight_canvas_noteset.create_text(8, 8, text="战斗记录", anchor="nw", fill="black", font=("微软雅黑", 17, "bold"))
        #技能栏
        self.Fight_canvas_skillset = tk.Canvas(self.PlayTheGame, width=760, height=230, bg="#d4d4d4")
        self.Fight_canvas_skillset.place(x=620, y=820)
        self.Fight_canvas_skillchoose_0 = tk.Button(self.PlayTheGame,text="物理攻击", anchor="nw", font=("微软雅黑", 17, "bold"),bd=0,)
        self.Fight_canvas_skillchoose_0.place(x=500,y=820)     
        self.Fight_canvas_skillchoose_1 = tk.Button(self.PlayTheGame,text="魔法技能", anchor="nw", font=("微软雅黑", 17, "bold"),bd=0,)
        self.Fight_canvas_skillchoose_1.place(x=500,y=880)
        self.Fight_canvas_.create_text(470, 877,text="◆",fill="black",font=("微软雅黑", 24, "bold"), anchor="nw")
        self.Fight_canvas_skillchoose_2 = tk.Button(self.PlayTheGame,text="道具", anchor="nw", font=("微软雅黑", 17, "bold"),bd=0,)
        self.Fight_canvas_skillchoose_2.place(x=520,y=940)
        self.Fight_canvas_skillchoose_3 = tk.Button(self.PlayTheGame,text="逃跑", anchor="nw", font=("微软雅黑", 17, "bold"),bd=0,command=self.create_play_game_main_canvas)
        self.Fight_canvas_skillchoose_3.place(x=520,y=1000)
        #人物立绘 x446 y574
        self.Fight_canvas_playerimg_1 = tk.PhotoImage(file="python_simplegame\\playerimg\\player_set.png")
        self.Fight_canvas_.create_image(0, 530, image=self.Fight_canvas_playerimg_1, anchor="nw")
        #怪物立绘
        self.Fight_canvas_monsterimg = tk.PhotoImage(file="python_simplegame\\Monsterimg\\zhizhu.png")
        self.Fight_canvas_.create_image(200, 240, image=self.Fight_canvas_monsterimg, anchor="nw")


    #                                               首要回合进行先后手的判定-随后进入s1回合
    def Fight_f_(self):

        self.Fight_canvas_setup()  # 加载画布
        self.Fight_luckjudgment()  # 加载先后手判定
        self.Fightnext = 0
        if self.first == 1:
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=150)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=155)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=75)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="第" + str(self.round+1) + "回合" + "你拿到了先手优势！开始你的操作",font=('微软雅黑', 17, "bold"), anchor='nw', justify='left', wraplength=475, bg=None)
            self.Fight_text.place(x=15, y=75)
            self.Fight_canvas_skillchoose_0 = tk.Button(self.PlayTheGame, text="物理攻击", anchor="nw",font=("微软雅黑", 17, "bold"), bd=0, command=self.FightPlayer_PA)
            self.Fight_canvas_skillchoose_0.place(x=500, y=820)
            self.first = 0
            self.Fight_random_c = tk.Button(self.PlayTheGame,text="【下一回合】", anchor="nw", font=("微软雅黑", 18, "bold"),bd=0,command=self.Fight_s_1)
            self.Fight_random_c.place(x=475,y=750)
        if self.first == 2:
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=150)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=155)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=75)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="第" + str(self.round) + "回合" + "怪物拿到了先手优势！请注意你的状态",font=('微软雅黑', 17, "bold"), anchor='nw', justify='left', wraplength=475, bg=None)
            self.Fight_text.place(x=15, y=75)
            self.FightMonster_PA()  # 怪物进行攻击
            self.first = 0
            self.Fight_random_c = tk.Button(self.PlayTheGame,text="【下一回合】", anchor="nw", font=("微软雅黑", 18, "bold"),bd=0,command=self.Fight_s_1)
            self.Fight_random_c.place(x=475,y=750)
    
    #                                              s1回合 承接首要回合和s2回合的来回判定
    def Fight_s_1(self):
        self.Fight_canvas_setup()  # 加载画布
        self.Fight_random_c = tk.Button(self.PlayTheGame,text="【下一回合】", anchor="nw", font=("微软雅黑", 18, "bold"),bd=0,command=self.Fight_s_2)
        self.Fight_random_c.place(x=475,y=750)
        if self.G_round == 1:
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=150)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=155)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=75)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="第" + str(self.round) + "回合" + "怪物的回合结束了，现在是你的回合！",font=('微软雅黑', 17, "bold"), anchor='nw', justify='left', wraplength=475, bg=None)
            self.Fight_text.place(x=15, y=75)
            self.Fight_canvas_skillchoose_0 = tk.Button(self.PlayTheGame, text="物理攻击", anchor="nw",font=("微软雅黑", 17, "bold"), bd=0,command=self.FightPlayer_PA)
            self.Fight_canvas_skillchoose_0.place(x=500, y=820)
            self.Fight_hp_j() #玩家hp和怪物hp的检测

        if self.G_round == 2:
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=150)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=155)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=75)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="第" + str(self.round) + "回合" + "你的回合结束了，现在是怪物的回合！请注意你的状态",font=('微软雅黑', 17, "bold"), anchor='nw', justify='left', wraplength=475, bg=None)
            self.Fight_text.place(x=15, y=75)
            self.FightMonster_PA()  # 怪物进行攻击
            self.Fight_hp_j() #玩家hp和怪物hp的检测
    #                                              s2回合 承接s1回合和s2回合的来回判定
    def Fight_s_2(self):
        self.Fight_canvas_setup()  # 加载画布
        self.Fight_random_c = tk.Button(self.PlayTheGame,text="【下一回合】", anchor="nw", font=("微软雅黑", 18, "bold"),bd=0,command=self.Fight_s_1)
        self.Fight_random_c.place(x=475,y=750)
        if self.G_round == 1:
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=150)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=155)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=75)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="第" + str(self.round) + "回合" + "怪物的回合结束了，现在是你的回合！",font=('微软雅黑', 17, "bold"), anchor='nw', justify='left', wraplength=475, bg=None)
            self.Fight_text.place(x=15, y=75)
            self.Fight_canvas_skillchoose_0 = tk.Button(self.PlayTheGame, text="物理攻击", anchor="nw",font=("微软雅黑", 17, "bold"), bd=0,command=self.FightPlayer_PA)
            self.Fight_canvas_skillchoose_0.place(x=500, y=820)
            self.Fight_hp_j() #玩家hp和怪物hp的检测
        if self.G_round == 2:
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=150)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=155)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="                                                                     ",font=('微软雅黑', 50, "bold"), anchor='nw', justify='left', wraplength=475,bg=None)
            self.Fight_text.place(x=15, y=75)
            self.Fight_text = tk.Label(self.Fight_canvas_noteset, text="第" + str(self.round) + "回合" + "你的回合结束了，现在是怪物的回合！请注意你的状态",font=('微软雅黑', 17, "bold"), anchor='nw', justify='left', wraplength=475, bg=None)
            self.Fight_text.place(x=15, y=75)
            self.FightMonster_PA()  # 怪物进行攻击
            self.Fight_hp_j() #玩家hp和怪物hp的检测
                        
                        

#—————————————————————————————————————————————————↑↑↑↑↑战斗系统管理↑↑↑↑↑——————————————————————————————————————————————————————————————————————————————————
#
#
#
#—————————————————————————————————————————————————↓↓↓↓↓随机事件管理↓↓↓↓↓——————————————————————————————————————————————————————————————————————————————————
    def Incident_order(self):
        self.ps_if_()
        self.Incident_canvas = tk.Canvas(self.PlayTheGame, width=1920, height=775, bg=None)
        self.Incident_canvas.place(x=-2, y=0)
        self.I_label_ = tk.Label(self.Incident_canvas,text="体力值:",font=('微软雅黑',17, "bold"),anchor='nw')
        self.I_label_.place(x=50,y=50)
        self.I_label_ = tk.Label(self.Incident_canvas,text=self.ps,font=('微软雅黑',17, "bold"),anchor='nw')
        self.I_label_.place(x=150,y=50)
        self.I_label_ = tk.Label(self.Incident_canvas,text="/",font=('微软雅黑',17, "bold"),anchor='nw')
        self.I_label_.place(x=200,y=50)
        self.I_label_ = tk.Label(self.Incident_canvas,text=self.ps_max,font=('微软雅黑',17, "bold"),anchor='nw')
        self.I_label_.place(x=220,y=50)
        self.I_label_ = tk.Label(self.Incident_canvas,text="每当你探索一次，就会失去10点体力，体力为0时则将会禁止继续探索。（回复体力的方法：食用能回复体力的道具、探索奇遇等等）",font=('微软雅黑',17),anchor='nw')
        self.I_label_.place(x=350,y=150)
        self.I_button_ = tk.Button(self.Incident_canvas,text="继续", anchor="nw", font=("微软雅黑", 18, "bold"),bd=0,command=self.AreaLevel10_canvas_)
        self.I_button_.place(x=950,y=540)
    def AreaLevel10_canvas_(self):
        if int(self.ps) > 0:
            self.ps = int(self.ps) - 10
            self.Incident_order()
            self.AreaLevel10_canvas = tk.Canvas(self.Incident_canvas, width=1550, height=430, bg=None)
            self.AreaLevel10_canvas.place(x=185, y=150)
            self.AreaLevel10_button_ = tk.Button(self.AreaLevel10_canvas,text="继续", anchor="nw", font=("微软雅黑", 18, "bold"),bd=0,command=self.AreaLevel10_AG)
            self.AreaLevel10_button_.place(x=765,y=390)
            Incident.AreaLevel10_Incident(self)
        else:
            self.ps_if_()
    def AreaLevel10_AG(self):
        self.ps_if_()
        self.Incident_canvas = tk.Canvas(self.PlayTheGame, width=1920, height=775, bg=None)
        self.Incident_canvas.place(x=-2, y=0)
        self.I_label_ = tk.Label(self.Incident_canvas,text="体力值:",font=('微软雅黑',17, "bold"),anchor='nw')
        self.I_label_.place(x=50,y=50)
        self.I_label_ = tk.Label(self.Incident_canvas,text=self.ps,font=('微软雅黑',17, "bold"),anchor='nw')
        self.I_label_.place(x=150,y=50)
        self.I_label_ = tk.Label(self.Incident_canvas,text="/",font=('微软雅黑',17, "bold"),anchor='nw')
        self.I_label_.place(x=200,y=50)
        self.I_label_ = tk.Label(self.Incident_canvas,text=self.ps_max,font=('微软雅黑',17, "bold"),anchor='nw')
        self.I_label_.place(x=220,y=50)
        self.AreaLevel10_canvas_()
    def ps_if_(self):
        if int(self.ps) <= 0:
            self.Incident_canvas = tk.Canvas(self.PlayTheGame, width=1920, height=775, bg=None)
            self.Incident_canvas.place(x=-2, y=0)
            self.I_label_ = tk.Label(self.Incident_canvas,text="体力值:",font=('微软雅黑',17, "bold"),anchor='nw')
            self.I_label_.place(x=50,y=50)
            self.I_label_ = tk.Label(self.Incident_canvas,text=self.ps,font=('微软雅黑',17, "bold"),anchor='nw')
            self.I_label_.place(x=150,y=50)
            self.I_label_ = tk.Label(self.Incident_canvas,text="/",font=('微软雅黑',17, "bold"),anchor='nw')
            self.I_label_.place(x=200,y=50)
            self.I_label_ = tk.Label(self.Incident_canvas,text=self.ps_max,font=('微软雅黑',17, "bold"),anchor='nw')
            self.I_label_.place(x=220,y=50)
            self.I_label_ = tk.Label(self.Incident_canvas,text="你透支了全部体力。感到疲惫不堪无法前行！",font=('微软雅黑',18,"bold"),anchor='nw',justify='left')
            self.I_label_.place(x=400,y=150)
            self.AreaLevel10_button_ = tk.Button(self.Incident_canvas,text="【返回城镇】", anchor="nw", font=("微软雅黑", 18, "bold"),bd=0,command=self.Getitem_list)
            self.AreaLevel10_button_.place(x=900,y=490)
            self.AreaLevel10_button_ = tk.Button(self.Incident_canvas,text="继续", anchor="nw", font=("微软雅黑", 18, "bold"),bd=0,command=self.AreaLevel10_AG)
            self.AreaLevel10_button_.place(x=950,y=540)
    def Getitem_list(self):
        if int(self.ps) == 0:
            self.Incident_canvas = tk.Canvas(self.PlayTheGame, width=1920, height=775, bg=None)
            self.Incident_canvas.place(x=-2, y=0)
            self.I_label_ = tk.Label(self.Incident_canvas,text="体力值:",font=('微软雅黑',17, "bold"),anchor='nw')
            self.I_label_.place(x=50,y=50)
            self.I_label_ = tk.Label(self.Incident_canvas,text=self.ps,font=('微软雅黑',17, "bold"),anchor='nw')
            self.I_label_.place(x=150,y=50)
            self.I_label_ = tk.Label(self.Incident_canvas,text="/",font=('微软雅黑',17, "bold"),anchor='nw')
            self.I_label_.place(x=200,y=50)
            self.I_label_ = tk.Label(self.Incident_canvas,text=self.ps_max,font=('微软雅黑',17, "bold"),anchor='nw')
            self.I_label_.place(x=220,y=50)
            Incident.Getitem_list_(self)
            self.getitem = []
            self.AreaLevel10_button_ = tk.Button(self.Incident_canvas,text="继续", anchor="nw", font=("微软雅黑", 18, "bold"),bd=0,command=self.create_play_game_main_canvas)
            self.AreaLevel10_button_.place(x=950,y=540)
#—————————————————————————————————————————————————↑↑↑↑↑随机事件管理↑↑↑↑↑——————————————————————————————————————————————————————————————————————————————————
#
#
#
#
#—————————————————————————————————————————————————↓↓↓↓↓创建角色系统↓↓↓↓↓——————————————————————————————————————————————————————————————————————————————————       
    def Player_Create_set(self):
        # 创建新游戏切换窗口
        self.Player_Create_set = tk.Toplevel(self.win,width=1280,height=800)
        self.Player_Create_set.iconbitmap('python_simplegame\\qiji.ico')
        self.Player_Create_set.title("你正在塑造你的小人……")
        self.Player_Create_set.withdraw()
    def Player_Create(self):
        self.Player_Create_set.deiconify()
        self.win.withdraw()
    def Player_create_info(self):  
        self.Playerinfo_label0 = tk.Label(self.Player_Create_set,text="开始创建人物的初始属性",font=('微软雅黑',15),anchor='nw')
        self.Playerinfo_label0.place(x=25,y=20)
        self.Playerinfo_label1 = tk.Label(self.Player_Create_set,text="————————————————————",font=('微软雅黑',15),anchor='nw')
        self.Playerinfo_label1.place(x=25,y=50)
        self.Playerinfo_label2 = tk.Label(self.Player_Create_set,text="姓名:",font=('微软雅黑',15),anchor='nw')
        self.Playerinfo_label2.place(x=25,y=85)
        self.Playerinfo_label3 = tk.Label(self.Player_Create_set,text="种族:",font=('微软雅黑',15),anchor='nw')
        self.Playerinfo_label3.place(x=25,y=110)
        self.Playerinfo_label4 = tk.Label(self.Player_Create_set,text="魔法适应程度:",font=('微软雅黑',15),anchor='nw')
        self.Playerinfo_label4.place(x=25,y=135)
        self.Playerinfo_label5 = tk.Label(self.Player_Create_set,text="————————————————————",font=('微软雅黑',15),anchor='nw')
        self.Playerinfo_label5.place(x=25,y=160)
        self.Playerinfo_label6 = tk.Label(self.Player_Create_set,text="力量:",font=('微软雅黑',15),anchor='nw')
        self.Playerinfo_label6.place(x=25,y=185)
        self.Playerinfo_label7 = tk.Label(self.Player_Create_set,text="力量成长系数:",font=('微软雅黑',15),anchor='nw')
        self.Playerinfo_label7.place(x=25,y=210)
        self.Playerinfo_label8 = tk.Label(self.Player_Create_set,text="敏捷:",font=('微软雅黑',15),anchor='nw')
        self.Playerinfo_label8.place(x=25,y=235)
        self.Playerinfo_label9 = tk.Label(self.Player_Create_set,text="敏捷成长系数:",font=('微软雅黑',15),anchor='nw')
        self.Playerinfo_label9.place(x=25,y=260)
        self.Playerinfo_label10 = tk.Label(self.Player_Create_set,text="智力:",font=('微软雅黑',15),anchor='nw')
        self.Playerinfo_label10.place(x=25,y=285)
        self.Playerinfo_label11 = tk.Label(self.Player_Create_set,text="智力成长系数:",font=('微软雅黑',15),anchor='nw')
        self.Playerinfo_label11.place(x=25,y=310)
        self.Playerinfo_label12 = tk.Label(self.Player_Create_set,text="————————————————————",font=('微软雅黑',15),anchor='nw')
        self.Playerinfo_label12.place(x=25,y=335)
        #创建人物面板的结束游戏
        self.GameShoutdowm = tk.Button(self.Player_Create_set,text='结束游戏',font=('微软雅黑',17),width=8,height=1,bd=1,command=self.win.quit)
        self.GameShoutdowm.place(x=550,y=730)
        self.Player_create_info_reload()
    def Player_create_info_reload(self): 
        self.Playerinfo_label20 = tk.Label(self.Player_Create_set,text=self.name ,font=('微软雅黑',14),anchor='nw')
        self.Playerinfo_label20.place(x=75,y=85)
        self.Playerinfo_label21 = tk.Label(self.Player_Create_set,text=self.Race,font=('微软雅黑',14),anchor='nw')
        self.Playerinfo_label21.place(x=75,y=110)
        self.Playerinfo_label22 = tk.Label(self.Player_Create_set,text=self.Magical_adaptability,font=('微软雅黑',14),anchor='nw')
        self.Playerinfo_label22.place(x=160,y=135)
        self.Playerinfo_label23 = tk.Label(self.Player_Create_set,text=self.Str,font=('微软雅黑',14),anchor='nw')
        self.Playerinfo_label23.place(x=85,y=185)
        self.Playerinfo_label24 = tk.Label(self.Player_Create_set,text=self.Str_coefficient,font=('微软雅黑',14),anchor='nw')
        self.Playerinfo_label24.place(x=160,y=210)
        self.Playerinfo_label25 = tk.Label(self.Player_Create_set,text=self.Agi,font=('微软雅黑',14),anchor='nw')
        self.Playerinfo_label25.place(x=85,y=235)
        self.Playerinfo_label26 = tk.Label(self.Player_Create_set,text=self.Agi_coefficient,font=('微软雅黑',14),anchor='nw')
        self.Playerinfo_label26.place(x=160,y=260)
        self.Playerinfo_label27 = tk.Label(self.Player_Create_set,text=self.Int,font=('微软雅黑',14),anchor='nw')
        self.Playerinfo_label27.place(x=85,y=285)
        self.Playerinfo_label28 = tk.Label(self.Player_Create_set,text=self.Int_coefficient,font=('微软雅黑',14),anchor='nw')
        self.Playerinfo_label28.place(x=160,y=310)
    def player_set_start(self): 
        self.player_set_start_canvas = tk.Canvas(self.Player_Create_set,width=750,height=740,bg=None)
        self.player_set_start_canvas.place(x=500,y=0)
        self.player_set_start_button = tk.Button(self.player_set_start_canvas,text='开始创建人物',font=('微软雅黑',13),width=10,height=1,bd=2,command=self.playername)
        self.player_set_start_button.place(x=325,y=50)
    def playername(self):  
        self.playername_canvas = tk.Canvas(self.Player_Create_set,width=700,height=650,bg=None)
        self.playername_canvas.place(x=550,y=0)
        self.playername = tk.Label(self.playername_canvas,text='请输入你的角色名称',font=('微软雅黑',16),bg=None,anchor='nw')
        self.playername.place(x=260,y=20)
        self.playername_Entry = tk.Entry(self.playername_canvas,width=15,bd=3,font=('微软雅黑',14))
        self.playername_Entry.place(x=270,y=70)
        self.GameStart = tk.Button(self.playername_canvas,text='确定',font=('微软雅黑',14),bd=3,width=5,command=self.playername_set)
        self.GameStart.place(x=320,y=120)
        self.playername = tk.Label(self.playername_canvas,text='你在一场突发事件中不幸丢失了自己的性命',font=('微软雅黑',14),bg=None,anchor=CENTER)
        self.playername.place(x=180,y=200)
        self.playername = tk.Label(self.playername_canvas,text='在你失去意识之前你还能听到怀中被保护的孩子的呼喊声',font=('微软雅黑',14),bg=None,anchor=CENTER)
        self.playername.place(x=140,y=230)
        self.playername = tk.Label(self.playername_canvas,text='被你的行动而感动的女神决定赋予你第二次生命',font=('微软雅黑',14),bg=None,anchor=CENTER)
        self.playername.place(x=170,y=260)
        self.playername = tk.Label(self.playername_canvas,text='「赋予一个优雅而不失情调的名字来响彻蒂斯亚克大陆吧!」',font=('微软雅黑',14),bg=None,anchor=CENTER)
        self.playername.place(x=130,y=290)
    def playername_set(self): 
        self.name = "                                                               "
        self.Player_create_info_reload()
        self.name = self.playername_Entry.get()
        self.Player_create_info_reload()
        self.player_race()
    def player_race(self):  #                                                           bg="#ffca58"
        self.player_race_canvas = tk.Canvas(self.Player_Create_set,width=750,height=740,bg=None)
        self.player_race_canvas.place(x=500,y=0)
        self.player_race = tk.Label(self.player_race_canvas,text='在天地大战之前,你作为一名可敬的生命诞生于这个世界上。',font=('微软雅黑',14),anchor='nw',bg=None)
        self.player_race.place(x=180,y=40)
        self.player_race = tk.Label(self.player_race_canvas,text='假如给你一次机会,你会想要转生成哪个种族？',font=('微软雅黑',14),anchor='nw',bg=None)
        self.player_race.place(x=200,y=70)
        self.player_race_choose = tk.Button(self.player_race_canvas,text='(第7位阶)森精种',font=('微软雅黑',12),bd=2,width=13,command=self.player_race_1)
        self.player_race_choose.place(x=210,y=120)
        self.player_race_choose = tk.Button(self.player_race_canvas,text='(第8位阶)地精种',font=('微软雅黑',12),bd=2,width=13,command=self.player_race_2)
        self.player_race_choose.place(x=210,y=170)
        self.player_race_choose = tk.Button(self.player_race_canvas,text='(第9位阶)妖精种',font=('微软雅黑',12),bd=2,width=13,command=self.player_race_3)
        self.player_race_choose.place(x=210,y=220)
        self.player_race_choose = tk.Button(self.player_race_canvas,text='(第10位阶)机凯种',font=('微软雅黑',12),bd=2,width=13,command=self.player_race_4)
        self.player_race_choose.place(x=210,y=270)
        self.player_race_choose = tk.Button(self.player_race_canvas,text='(第11位阶)妖魔种',font=('微软雅黑',12),bd=2,width=13,command=self.player_race_5)
        self.player_race_choose.place(x=210,y=320)
        self.player_race_choose = tk.Button(self.player_race_canvas,text='(第12位阶)吸血种',font=('微软雅黑',12),bd=2,width=13,command=self.player_race_6)
        self.player_race_choose.place(x=430,y=120)
        self.player_race_choose = tk.Button(self.player_race_canvas,text='(第13位阶)月咏种',font=('微软雅黑',12),bd=2,width=13,command=self.player_race_7)
        self.player_race_choose.place(x=430,y=170)
        self.player_race_choose = tk.Button(self.player_race_canvas,text='(第14位阶)兽人种',font=('微软雅黑',12),bd=2,width=13,command=self.player_race_8)
        self.player_race_choose.place(x=430,y=220)
        self.player_race_choose = tk.Button(self.player_race_canvas,text='(第15位阶)海栖种',font=('微软雅黑',12),bd=2,width=13,command=self.player_race_9)
        self.player_race_choose.place(x=430,y=270)
        self.player_race_choose = tk.Button(self.player_race_canvas,text='(第16位阶)人类种',font=('微软雅黑',12),bd=2,width=13,command=self.player_race_10)
        self.player_race_choose.place(x=430,y=320)
        self.player_race_choose = tk.Button(self.player_race_canvas,text='确定种族',font=('微软雅黑',12),bd=3,width=6,command=self.player_choose_1)
        self.player_race_choose.place(x=620,y=318)
    def player_race_1(self):
        self.Race = "       "
        self.Magical_adaptability = "       "
        self.Str = "       "
        self.Str_coefficient = "       "
        self.Agi = "       "
        self.Agi_coefficient = "       "
        self.Int = "       "
        self.Int_coefficient = "       "       
        self.Player_create_info_reload()
        self.Race = "森精种"
        self.Magical_adaptability = 50
        self.Str = 2
        self.Str_coefficient = 0.1
        self.Agi = 2
        self.Agi_coefficient = 0.1
        self.Int = 16
        self.Int_coefficient = 0.8        
        self.Player_create_info_reload()
    def player_race_2(self):
        self.Race = "       "
        self.Magical_adaptability = "       "
        self.Str = "       "
        self.Str_coefficient = "       "
        self.Agi = "       "
        self.Agi_coefficient = "       "
        self.Int = "       "
        self.Int_coefficient = "       "       
        self.Player_create_info_reload()
        self.Race = "地精种"
        self.Magical_adaptability = 50
        self.Str = 2
        self.Str_coefficient = 0.1
        self.Agi = 2
        self.Agi_coefficient = 0.2
        self.Int = 16
        self.Int_coefficient = 0.7    
        self.Player_create_info_reload()
    def player_race_3(self):
        self.Race = "       "
        self.Magical_adaptability = "       "
        self.Str = "       "
        self.Str_coefficient = "       "
        self.Agi = "       "
        self.Agi_coefficient = "       "
        self.Int = "       "
        self.Int_coefficient = "       "       
        self.Player_create_info_reload()
        self.Race = "妖精种"
        self.Magical_adaptability = 50
        self.Str = 2
        self.Str_coefficient = 0.2
        self.Agi = 3
        self.Agi_coefficient = 0.3
        self.Int = 15
        self.Int_coefficient = 0.5   
        self.Player_create_info_reload()
    def player_race_4(self):
        self.Race = "       "
        self.Magical_adaptability = "       "
        self.Str = "       "
        self.Str_coefficient = "       "
        self.Agi = "       "
        self.Agi_coefficient = "       "
        self.Int = "       "
        self.Int_coefficient = "       "       
        self.Player_create_info_reload()
        self.Race = "机凯种"
        self.Magical_adaptability = 40
        self.Str = 5
        self.Str_coefficient = 0.2
        self.Agi = 5
        self.Agi_coefficient = 0.3
        self.Int = 10
        self.Int_coefficient = 0.4
        self.Player_create_info_reload()
    def player_race_5(self):
        self.Race = "       "
        self.Magical_adaptability = "       "
        self.Str = "       "
        self.Str_coefficient = "       "
        self.Agi = "       "
        self.Agi_coefficient = "       "
        self.Int = "       "
        self.Int_coefficient = "       "       
        self.Player_create_info_reload()
        self.Race = "妖魔种"
        self.Magical_adaptability = 35
        self.Str = 9
        self.Str_coefficient = 0.4
        self.Agi = 9
        self.Agi_coefficient = 0.4
        self.Int = 2
        self.Int_coefficient = 0.2   
        self.Player_create_info_reload()
    def player_race_6(self):
        self.Race = "       "
        self.Magical_adaptability = "       "
        self.Str = "       "
        self.Str_coefficient = "       "
        self.Agi = "       "
        self.Agi_coefficient = "       "
        self.Int = "       "
        self.Int_coefficient = "       "       
        self.Player_create_info_reload()
        self.Race = "吸血种"
        self.Magical_adaptability = 30
        self.Str = 8
        self.Str_coefficient = 0.2
        self.Agi = 15
        self.Agi_coefficient = 0.7
        self.Int = 2
        self.Int_coefficient = 0.1    
        self.Player_create_info_reload()
    def player_race_7(self):
        self.Race = "       "
        self.Magical_adaptability = "       "
        self.Str = "       "
        self.Str_coefficient = "       "
        self.Agi = "       "
        self.Agi_coefficient = "       "
        self.Int = "       "
        self.Int_coefficient = "       "       
        self.Player_create_info_reload()
        self.Race = "月咏种"
        self.Magical_adaptability = 20
        self.Str = 5
        self.Str_coefficient = 0.1
        self.Agi = 5
        self.Agi_coefficient = 0.2
        self.Int = 10
        self.Int_coefficient = 0.7   
        self.Player_create_info_reload()
    def player_race_8(self):
        self.Race = "       "
        self.Magical_adaptability = "       "
        self.Str = "       "
        self.Str_coefficient = "       "
        self.Agi = "       "
        self.Agi_coefficient = "       "
        self.Int = "       "
        self.Int_coefficient = "       "       
        self.Player_create_info_reload()
        self.Race = "兽人种"
        self.Magical_adaptability = 15
        self.Str = 10
        self.Str_coefficient = 0.5
        self.Agi = 7
        self.Agi_coefficient = 0.2
        self.Int = 3
        self.Int_coefficient = 0.3   
        self.Player_create_info_reload()
    def player_race_9(self):
        self.Race = "       "
        self.Magical_adaptability = "       "
        self.Str = "       "
        self.Str_coefficient = "       "
        self.Agi = "       "
        self.Agi_coefficient = "       "
        self.Int = "       "
        self.Int_coefficient = "       "       
        self.Player_create_info_reload()
        self.Race = "海栖种"
        self.Magical_adaptability = 15
        self.Str = 5
        self.Str_coefficient = 0.1
        self.Agi = 8
        self.Agi_coefficient = 0.2
        self.Int = 7
        self.Int_coefficient = 0.7    
        self.Player_create_info_reload()
    def player_race_10(self):
        self.Race = "       "
        self.Magical_adaptability = "       "
        self.Str = "       "
        self.Str_coefficient = "       "
        self.Agi = "       "
        self.Agi_coefficient = "       "
        self.Int = "       "
        self.Int_coefficient = "       "       
        self.Player_create_info_reload()
        self.Race = "人类种"
        self.Magical_adaptability = 0
        self.Str = 5
        self.Str_coefficient = 0.1
        self.Agi = 5
        self.Agi_coefficient = 0.2
        self.Int = 10
        self.Int_coefficient = 0.7   
        self.Player_create_info_reload()
    def player_choose_1(self):
        self.player_choose = tk.Canvas(self.Player_Create_set,width=750,height=740,bg=None)
        self.player_choose.place(x=500,y=0)
        self.player_choose_label = tk.Label(self.player_choose,text='在你幼年的时候,你曾经…………',font=('微软雅黑',14),anchor='nw',bg=None)
        self.player_choose_label.place(x=200,y=40)
        self.player_race_choose = tk.Button(self.player_choose,text='1.在大街上奔跑',font=('微软雅黑',12),bd=2,command=self.player_choose_1_1)
        self.player_race_choose.place(x=200,y=100)
        self.player_race_choose = tk.Button(self.player_choose,text='2.在庭院玩泥巴',font=('微软雅黑',12),bd=2,command=self.player_choose_1_2)
        self.player_race_choose.place(x=200,y=150)
        self.player_race_choose = tk.Button(self.player_choose,text='3.与小孩一起玩',font=('微软雅黑',12),bd=2,command=self.player_choose_1_3)
        self.player_race_choose.place(x=200,y=200)
    def player_choose_1_1(self):
        self.Str = self.Str + 1
        self.Agi = self.Agi + 1
        self.Player_create_info_reload()
        self.player_choose_2()
    def player_choose_1_2(self):
        self.Str = self.Str + 1
        self.Int = self.Int + 1
        self.Player_create_info_reload()
        self.player_choose_2()
    def player_choose_1_3(self):
        self.Agi = self.Agi + 1
        self.Int = self.Int + 1
        self.Player_create_info_reload()
        self.player_choose_2()
    def player_choose_2(self):
        self.player_choose = tk.Canvas(self.Player_Create_set,width=750,height=740,bg=None)
        self.player_choose.place(x=500,y=0)
        self.player_choose_label = tk.Label(self.player_choose,text='在你少年的时候,你曾经…………',font=('微软雅黑',14),anchor='nw',bg=None)
        self.player_choose_label.place(x=200,y=40)
        self.player_race_choose = tk.Button(self.player_choose,text='1.首次尝试魔法',font=('微软雅黑',12),bd=2,command=self.player_choose_2_1)
        self.player_race_choose.place(x=200,y=100)
        self.player_race_choose = tk.Button(self.player_choose,text='2.商人的小帮手',font=('微软雅黑',12),bd=2,command=self.player_choose_2_2)
        self.player_race_choose.place(x=200,y=150)
        self.player_race_choose = tk.Button(self.player_choose,text='3.铁匠的学徒',font=('微软雅黑',12),bd=2,command=self.player_choose_2_3)
        self.player_race_choose.place(x=200,y=200)
    def player_choose_2_1(self):
        self.Int = self.Int + 3
        self.Player_create_info_reload()
        self.player_choose_3()
    def player_choose_2_2(self):
        self.Agi = self.Agi + 3
        self.Player_create_info_reload()
        self.player_choose_3()
    def player_choose_2_3(self):
        self.Str = self.Str + 3
        self.Player_create_info_reload()
        self.player_choose_3()
    def player_choose_3(self):
        self.player_choose = tk.Canvas(self.Player_Create_set,width=750,height=740,bg=None)
        self.player_choose.place(x=500,y=0)
        self.player_choose_label = tk.Label(self.player_choose,text='在你青年的时候,你曾经…………',font=('微软雅黑',14),anchor='nw',bg=None)
        self.player_choose_label.place(x=200,y=40)
        self.player_race_choose = tk.Button(self.player_choose,text='1.学会了第一个魔法！',font=('微软雅黑',12),bd=2,command=self.player_choose_3_1)
        self.player_race_choose.place(x=200,y=100)
        self.player_race_choose = tk.Button(self.player_choose,text='2.有了自己的一番事业',font=('微软雅黑',12),bd=2,command=self.player_choose_3_2)
        self.player_race_choose.place(x=200,y=150)
        self.player_race_choose = tk.Button(self.player_choose,text='3.锻炼身体,提高身体的各项能力',font=('微软雅黑',12),bd=2,command=self.player_choose_3_3)
        self.player_race_choose.place(x=200,y=200)
    def player_choose_3_1(self):
        self.Int = self.Int + 4
        self.Player_create_info_reload()
        self.player_choose_4()
    def player_choose_3_2(self):
        self.Int = self.Int + 2
        self.Agi = self.Agi + 2
        self.Player_create_info_reload()
        self.player_choose_4()
    def player_choose_3_3(self):
        self.Str = self.Str + 2
        self.Int = self.Int + 2
        self.Player_create_info_reload()
        self.player_choose_4()
    def player_choose_4(self):
        self.player_choose = tk.Canvas(self.Player_Create_set,width=750,height=740,bg=None)
        self.player_choose.place(x=500,y=0)
        self.player_choose_label = tk.Label(self.player_choose,text='但不幸天地大战爆发,所有的种族都陷入了恐慌。此时的你决定……',font=('微软雅黑',14),anchor='nw',bg=None)
        self.player_choose_label.place(x=200,y=40)
        self.player_race_choose = tk.Button(self.player_choose,text='1.响应号召。想要为种族奉献出自己的一份力量！',font=('微软雅黑',12),bd=2,command=self.player_choose_4_1)
        self.player_race_choose.place(x=200,y=100)
        self.player_race_choose = tk.Button(self.player_choose,text='2.躲避战乱。带领自己的家人避开战争进行隐居过活。',font=('微软雅黑',12),bd=2,command=self.player_choose_4_2)
        self.player_race_choose.place(x=200,y=150)
        self.player_race_choose = tk.Button(self.player_choose,text='3.坚守岗位。你认为此时的你唯有坚守岗位才是对种族的最大帮助！',font=('微软雅黑',12),bd=2,command=self.player_choose_4_3)
        self.player_race_choose.place(x=200,y=200)
    def player_choose_4_1(self):
        self.Str = self.Str + 3
        self.Agi = self.Agi + 2
        self.Int = self.Int + 1
        self.Player_create_info_reload()
        self.player_choose_5()
    def player_choose_4_2(self):
        self.Str = self.Str + 2
        self.Agi = self.Agi + 3
        self.Int = self.Int + 1
        self.Player_create_info_reload()
        self.player_choose_5()
    def player_choose_4_3(self):
        self.Str = self.Str + 2
        self.Agi = self.Agi + 1
        self.Int = self.Int + 3
        self.Player_create_info_reload()
        self.player_choose_5()
    def player_choose_5(self):
        self.player_choose = tk.Canvas(self.Player_Create_set,width=750,height=740,bg=None)
        self.player_choose.place(x=500,y=0)
        self.player_choose_label = tk.Label(self.player_choose,text='不久后你回家便发现房门敞开。呼唤家人也没有反应',font=('微软雅黑',14),anchor='nw',bg=None)
        self.player_choose_label.place(x=200,y=40)
        self.player_choose_label = tk.Label(self.player_choose,text='这时忽然客房内传来很大的声响并伴有吵闹声,你决定前往查看。',font=('微软雅黑',14),anchor='nw',bg=None)
        self.player_choose_label.place(x=200,y=80)
        self.player_choose_label = tk.Label(self.player_choose,text='此时你发现歹徒正要对你的妹妹出手，你没有再三犹豫',font=('微软雅黑',14),anchor='nw',bg=None)
        self.player_choose_label.place(x=200,y=120)
        self.player_choose_label = tk.Label(self.player_choose,text='立马冲上前趁歹徒还没有反应过来给予了致命一击！',font=('微软雅黑',14),anchor='nw',bg=None)
        self.player_choose_label.place(x=200,y=160)
        self.player_choose_label = tk.Label(self.player_choose,text='你从妹妹的口中得知，家里人都被歹徒杀害。',font=('微软雅黑',14),anchor='nw',bg=None)
        self.player_choose_label.place(x=200,y=200)
        self.player_choose_label = tk.Label(self.player_choose,text='此时的你悲痛欲绝，你决定……',font=('微软雅黑',14),anchor='nw',bg=None)
        self.player_choose_label.place(x=200,y=240)        
        self.player_race_choose = tk.Button(self.player_choose,text='1.眼下重要的是保护好妹妹，前往一个新的地方。',font=('微软雅黑',12),bd=2,command=self.player_choose_5_1)
        self.player_race_choose.place(x=200,y=300)
        self.player_race_choose = tk.Button(self.player_choose,text='2.从此隐姓埋名，不招惹任何麻烦。',font=('微软雅黑',12),bd=2,command=self.player_choose_5_2)
        self.player_race_choose.place(x=200,y=350)
        self.player_race_choose = tk.Button(self.player_choose,text='3.想要为家族报仇雪恨。',font=('微软雅黑',12),bd=2,command=self.player_choose_5_3)
        self.player_race_choose.place(x=200,y=400)
    def player_choose_5_1(self):
        self.Str = self.Str + 3
        self.Agi = self.Agi + 3
        self.Int = self.Int + 1
        self.Player_create_info_reload()
        self.player_choose_6()
    def player_choose_5_2(self):
        self.Str = self.Str + 2
        self.Agi = self.Agi + 2
        self.Int = self.Int + 4
        self.Player_create_info_reload()
        self.player_choose_6()
    def player_choose_5_3(self):
        self.Str = self.Str + 3
        self.Agi = self.Agi + 3
        self.Int = self.Int + 0
        self.Player_create_info_reload()
        self.player_choose_6()
    def player_choose_6(self):
        self.player_choose = tk.Canvas(self.Player_Create_set,width=750,height=740,bg=None)
        self.player_choose.place(x=500,y=0)
        self.player_choose_label = tk.Label(self.player_choose,text='从此你踏上了新的旅途！',font=('微软雅黑',14),anchor='nw',bg=None)
        self.player_choose_label.place(x=200,y=40)
        self.player_choose_label = tk.Label(self.player_choose,text='「人物初始属性设定完成！」',font=('微软雅黑',12),anchor='nw',bg=None)
        self.player_choose_label.place(x=200,y=75)
        self.player_race_choose = tk.Button(self.player_choose,text='前往蒂斯亚克大陆！',font=('微软雅黑',12),bd=3,command=self.PlayTheGameToplevel_change)
        self.player_race_choose.place(x=300,y=150)
        self.Player_file() #创建人物数据存档
#—————————————————————————————————————————————————↑↑↑↑↑创建角色系统↑↑↑↑↑——————————————————————————————————————————————————————————————————————————————————
#
#          
#
#
#
#—————————————————————————————————————————————————↓↓↓↓↓主要游戏系统↓↓↓↓↓——————————————————————————————————————————————————————————————————————————————————
    def PlayTheGame(self):
        self.PlayTheGame = tk.Toplevel(self.Player_Create_set,width=1920,height=1080)
        self.PlayTheGame.title("欢迎来到蒂斯亚克大陆！")
        self.PlayTheGame.iconbitmap('python_simplegame\\qiji.ico')
        self.PlayTheGame.attributes('-fullscreen', True)
        self.PlayTheGame.geometry("1920x1080")
        self.PlayTheGame.withdraw()
        self.PlayTheGame.bind('<Escape>', self.GameMain_shutdown)
        self.PlayTheGame_story_1()

    def PlayTheGameToplevel_change(self):
        self.Player_file_login()#读取人物数据存档
        self.PlayTheGame.deiconify()
        self.Player_Create_set.withdraw()#关闭人物创建界面
        self.win.withdraw()#关闭开始游戏界面

    def GameMain_shutdown(self,event):
        self.GameMain_shutdown_canvas = tk.Canvas(self.PlayTheGame, width= 1920, height=1080,bg=None)
        self.GameMain_shutdown_canvas.place(x=0, y=0)
        self.GameMain_shutdown_photo = tk.PhotoImage(file="python_simplegame\\mainimg\\Title_2.png")
        self.GameMain_shutdown_canvas.create_image(330,50,image=self.GameMain_shutdown_photo,anchor='nw')
        self.GameMain_shutdown_button_1 = tk.Button(self.GameMain_shutdown_canvas,bd=0,text="返回大厅",font=("微软雅黑", 22, "bold"),command=self.create_play_game_main_canvas)
        self.GameMain_shutdown_button_1.place(x=875, y=450)
        self.GameMain_shutdown_button_2 = tk.Button(self.GameMain_shutdown_canvas,bd=0,text="保存游戏",font=("微软雅黑", 22, "bold"),command=self.Player_file)
        self.GameMain_shutdown_button_2.place(x=875, y=550)
        self.GameMain_shutdown_button_3 = tk.Button(self.GameMain_shutdown_canvas,bd=0,text="读取游戏",font=("微软雅黑", 22, "bold"),command=self.Player_file_login)
        self.GameMain_shutdown_button_3.place(x=875, y=650)
        self.GameMain_shutdown_button_4 = tk.Button(self.GameMain_shutdown_canvas,bd=0,text="退出游戏",font=("微软雅黑", 22, "bold"),command=self.win.quit)
        self.GameMain_shutdown_button_4.place(x=875, y=750)
        self.GameMain_shutdown_canvas.create_text(980,1000,text="看到这个界面表示你摁ECS辣！现在是回不去你之前的界面辣！问就是我懒！",font=("微软雅黑", 20))

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    #                                                           初始剧情介绍
    def PlayTheGame_story_1(self):
        self.PlayTheGame_story = tk.Canvas(self.PlayTheGame,width=1920,height=1080,  bg=None)
        self.PlayTheGame_story.place(x=0,y=0)
        self.PlayTheGame_story.bind("<Button-1>", self.PlayTheGame_story_2)
        self.PlayTheGame_story_1 = tk.Label(self.PlayTheGame_story,text='『　蒂斯亚克历　708年4月26日  』',font=('微软雅黑',25),anchor='nw',bg=None)
        self.PlayTheGame_story_1.place(x=675,y=200)
        self.PlayTheGame_story_1 = tk.Label(self.PlayTheGame_story,text='你在一场噩梦中醒来————',font=('微软雅黑',18),anchor='nw',bg=None)
        self.PlayTheGame_story_1.place(x=800,y=320)
    def PlayTheGame_story_2(self, event):
        self.PlayTheGame_story = tk.Canvas(self.PlayTheGame,width=1920,height=1080, bg=None)
        self.PlayTheGame_story.place(x=0,y=0)
        self.PlayTheGame_story.bind("<Button-1>", self.PlayTheGame_story_3)
        self.PlayTheGame_story_2 = tk.Label(self.PlayTheGame_story,text='睁眼看到的是熟悉的天花板与握住你的手在担心你的妹妹',font=('微软雅黑',18),anchor='nw',bg=None)
        self.PlayTheGame_story_2.place(x=650,y=250)
        self.PlayTheGame_story_2 = tk.Label(self.PlayTheGame_story,text='你们是那场混沌战争的幸存者，对于经历了战争洗礼与失去家族的你来说',font=('微软雅黑',18),anchor='nw',bg=None)
        self.PlayTheGame_story_2.place(x=600,y=325)
        self.PlayTheGame_story_2 = tk.Label(self.PlayTheGame_story,text='现在唯一的目标是保护好自己的妹妹',font=('微软雅黑',18),anchor='nw',bg=None)
        self.PlayTheGame_story_2.place(x=725,y=400)
    def PlayTheGame_story_3(self, event):
        self.PlayTheGame_story = tk.Canvas(self.PlayTheGame,width=1920,height=1080, bg=None)
        self.PlayTheGame_story.place(x=0,y=0)
        self.PlayTheGame_story_3 = tk.Label(self.PlayTheGame_story,text='在你温柔地问候妹妹后',font=('微软雅黑',18),anchor='nw',bg=None)
        self.PlayTheGame_story_3.place(x=825,y=250)
        self.PlayTheGame_story_3 = tk.Label(self.PlayTheGame_story,text='你一如既往的迈出玄关前往『冒险者公会』',font=('微软雅黑',18),anchor='nw',bg=None)
        self.PlayTheGame_story_3.place(x=750,y=325)
        self.PlayTheGame_choose = tk.Button(self.PlayTheGame_story,text='加油吧……！',font=('微软雅黑',16),bd=1,command=self.create_play_game_main_canvas)
        self.PlayTheGame_choose.place(x=1050,y=400)
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    def create_play_game_main_canvas(self):
        self.play_game_main_canvas = tk.Canvas(self.PlayTheGame, width=1920, height=1080, bg=None)
        self.play_game_main_canvas.place(x=0, y=0)
        self.play_game_main_photo_0 = tk.PhotoImage(file="python_simplegame\\mainui\\游戏主题UI设计.png")
        self.play_game_main_canvas.create_image(0, 783, image=self.play_game_main_photo_0, anchor="nw")
        self.play_game_main_photo_1 = tk.PhotoImage(file="python_simplegame\\mainui\\人物.png")
        self.play_game_main_photo_2 = tk.PhotoImage(file="python_simplegame\\mainui\\装备.png")
        self.play_game_main_photo_3 = tk.PhotoImage(file="python_simplegame\\mainui\\物品.png")
        self.play_game_main_photo_4 = tk.PhotoImage(file="python_simplegame\\mainui\\任务.png")
        self.play_game_main_choose_1 = tk.Button(self.play_game_main_canvas,image=self.play_game_main_photo_1,bd=0,command=self.create_play_game_main_canvas__Characterattributes)
        self.play_game_main_choose_1.place(x=1172,y=820)
        self.play_game_main_choose_2 = tk.Button(self.play_game_main_canvas,image=self.play_game_main_photo_2,bd=0,)
        self.play_game_main_choose_2.place(x=1172,y=885)
        self.play_game_main_choose_3 = tk.Button(self.play_game_main_canvas,image=self.play_game_main_photo_3,bd=0,)
        self.play_game_main_choose_3.place(x=1172,y=950)
        self.play_game_main_choose_4 = tk.Button(self.play_game_main_canvas,image=self.play_game_main_photo_4,bd=0,)
        self.play_game_main_choose_4.place(x=1172,y=1015)
        self.play_game_main_choose_5 = tk.Button(self.play_game_main_canvas,bd=0,text="王   都【未实装】",font=("微软雅黑", 22, "bold"))
        self.play_game_main_choose_5.place(x=580,y=120)
        self.play_game_main_choose_6 = tk.Button(self.play_game_main_canvas,bd=0,text="冒险者公会【未实装】",font=("微软雅黑", 22, "bold"))
        self.play_game_main_choose_6.place(x=120,y=340)
        self.play_game_main_choose_7 = tk.Button(self.play_game_main_canvas,bd=0,text="交易市场【未实装】",font=("微软雅黑", 22, "bold"))
        self.play_game_main_choose_7.place(x=720,y=520)
        self.play_game_main_choose_8 = tk.Button(self.play_game_main_canvas,bd=0,text="前往野外",font=("微软雅黑", 22, "bold"),command=self.Map_levelchoose)
        self.play_game_main_choose_8.place(x=1450,y=120)
        self.play_game_main_choose_9 = tk.Button(self.play_game_main_canvas,bd=0,text="酒馆",font=("微软雅黑", 22, "bold"),command=self.create_play_game_main_canvas__tavern)
        self.play_game_main_choose_9.place(x=1450,y=580)
        self.create_play_game_main_canvas_playerinforeload_2()
        self.play_game_main_canvas.create_text(550, 845, text=self.name, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.play_game_main_canvas.create_text(1010, 845, text=self.Race, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.play_game_main_canvas.create_text(850, 845, text=self.Player_Level, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.play_game_main_canvas.create_text(330, 845, text=self.HP, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.play_game_main_canvas.create_text(1010, 912, text=self.Str, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.play_game_main_canvas.create_text(1010, 965, text=self.Agi, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.play_game_main_canvas.create_text(1010, 1017, text=self.Int, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.play_game_main_canvas.create_text(730, 1017, text=self.Magical_adaptabilityUP, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.play_game_main_canvas.create_text(630, 912, text=self.Attact, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.play_game_main_canvas.create_text(630, 965, text=self.Defense, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.I_label_PlayGameMain = tk.Label(self.play_game_main_canvas,text="体力值:",font=('微软雅黑',17, "bold"),anchor='nw')
        self.I_label_PlayGameMain.place(x=50,y=50)
        self.I_label_PlayGameMain = tk.Label(self.play_game_main_canvas,text=self.ps,font=('微软雅黑',17, "bold"),anchor='nw')
        self.I_label_PlayGameMain.place(x=150,y=50)
        self.I_label_PlayGameMain = tk.Label(self.play_game_main_canvas,text="/",font=('微软雅黑',17, "bold"),anchor='nw')
        self.I_label_PlayGameMain.place(x=200,y=50)
        self.I_label_PlayGameMain = tk.Label(self.play_game_main_canvas,text=self.ps_max,font=('微软雅黑',17, "bold"),anchor='nw')
        self.I_label_PlayGameMain.place(x=220,y=50)

    def Map_levelchoose(self):                                 
        self.Map_levelchoose_canvas = tk.Canvas(self.PlayTheGame, width=1920, height=775, bg=None)
        self.Map_levelchoose_canvas.place(x=-2, y=0)
        self.Map_levelchoose_1 = tk.Button(self.Map_levelchoose_canvas,text="【荒野平原】 Lv10 ",font=("微软雅黑", 22, "bold"),bd=0,command=self.Incident_order)
        self.Map_levelchoose_1.place(x=810,y=140)
        self.Map_levelchoose_2 = tk.Button(self.Map_levelchoose_canvas,text="【厄菲尔海滩】 Lv20 - 未开放",font=("微软雅黑", 22, "bold"),bd=0)
        self.Map_levelchoose_2.place(x=790,y=240)
        self.Map_levelchoose_3 = tk.Button(self.Map_levelchoose_canvas,text="【无名者洞穴】 Lv30 - 未开放",font=("微软雅黑", 22, "bold"),bd=0)
        self.Map_levelchoose_3.place(x=790,y=340)
        self.Map_levelchoose_4 = tk.Button(self.Map_levelchoose_canvas,text="【冰天雪地】 Lv40 - 未开放 ",font=("微软雅黑", 22, "bold"),bd=0)
        self.Map_levelchoose_4.place(x=800,y=440)
        self.Map_levelchoose_5 = tk.Button(self.Map_levelchoose_canvas,text="【炽焰火山】 Lv50 - 未开放",font=("微软雅黑", 22, "bold"),bd=0)
        self.Map_levelchoose_5.place(x=800,y=540)
        self.Map_levelchoose_6 = tk.Button(self.Map_levelchoose_canvas, text="【返回城镇】", font=("微软雅黑", 22, "bold"), bd=0, command=self.create_play_game_main_canvas)
        self.Map_levelchoose_6.place(x=850,y=640)


    def create_play_game_main_canvas__Characterattributes(self):
        self.create_play_game_main_canvas()                                                                  #bg="#ffca58"
        self.play_game_main_canvas__Characterattributes = tk.Canvas(self.PlayTheGame, width=1920, height=775, bg=None)
        self.play_game_main_canvas__Characterattributes.place(x=-2, y=0)
        self.play_game_main_canvasphoto__Characterattributes = tk.PhotoImage(file="python_simplegame\\mainui\\人物属性\\人物属性-介绍.png")
        self.play_game_main_canvas__Characterattributes.create_image(0, 0, image=self.play_game_main_canvasphoto__Characterattributes, anchor="nw")
        #技能点描述
        self.play_game_main_canvas__Characterattributes.create_text(520,30,text=self.Skinpoint, anchor="nw", fill="#277f00", font=("微软雅黑", 23, "bold",))
        #主属性额外加点描述
        self.play_game_main_canvas__Characterattributes.create_text(330,100,text=self.Skinpoint_str, anchor="nw", fill="#277f00", font=("微软雅黑", 23, "bold",))
        self.play_game_main_canvas__Characterattributes.create_text(330,150,text=self.Skinpoint_agi, anchor="nw", fill="#277f00", font=("微软雅黑", 23, "bold",))
        self.play_game_main_canvas__Characterattributes.create_text(330,200,text=self.Skinpoint_int, anchor="nw", fill="#277f00", font=("微软雅黑", 23, "bold",))
        #基本信息描述
        self.play_game_main_canvas__Characterattributes.create_text(165,100,text=self.Str, anchor="nw", fill="black", font=("微软雅黑", 25, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(165,150,text=self.Agi, anchor="nw", fill="black", font=("微软雅黑", 25, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(165,200,text=self.Int, anchor="nw", fill="black", font=("微软雅黑", 25, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(165,300,text=self.HP_Max, anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(500,300,text=self.Luck, anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(165,355,text=self.Attact, anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(165,405,text=self.Defense, anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        #暴击描述        
        self.play_game_main_canvas__Characterattributes.create_text(195,450,text=self.Crit_p * 1, anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(195,500,text=self.Crit_d * 100, anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(195,550,text=self.Crit_r * 100, anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(230,450,text="  %", anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(285,500,text="%", anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(230,550,text="  %", anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        #闪避描述
        self.play_game_main_canvas__Characterattributes.create_text(500,500,text=self.Sidestep_p * 1, anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(500,550,text=self.Sidestep_r * 100, anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(550,500,text=" %", anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(550,550,text=" %", anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        #增伤描述
        self.play_game_main_canvas__Characterattributes.create_text(500,350,text=self.Attact_deepen * 100, anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(500,400,text=self.Attact_deduction * 100, anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(550,350,text=" %", anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(550,400,text=" %", anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        #经验值描述
        self.play_game_main_canvas__Characterattributes.create_text(220,655,text=self.Player_now, anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(220,705,text=self.Player_need, anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        #按钮放置
        self.play_game_main_canvasphoto__Characterattributes_1 = tk.PhotoImage(file="python_simplegame\\mainui\\人物属性\\加点.png")
        self.play_game_main_choose_0 = tk.Button(self.play_game_main_canvas__Characterattributes,image=self.play_game_main_canvasphoto__Characterattributes_1,bd=0,)
        self.play_game_main_choose_0.place(x=470,y=100)
        self.play_game_main_choose_1 = tk.Button(self.play_game_main_canvas__Characterattributes,image=self.play_game_main_canvasphoto__Characterattributes_1,bd=0,)
        self.play_game_main_choose_1.place(x=470,y=150)
        self.play_game_main_choose_2 = tk.Button(self.play_game_main_canvas__Characterattributes,image=self.play_game_main_canvasphoto__Characterattributes_1,bd=0,)
        self.play_game_main_choose_2.place(x=470,y=200)
        self.play_game_main_canvasphoto__Characterattributes_2 = tk.PhotoImage(file="python_simplegame\\mainui\\人物属性\\提升等级.png")
        self.play_game_main_choose_3 = tk.Button(self.play_game_main_canvas__Characterattributes,image=self.play_game_main_canvasphoto__Characterattributes_2,bd=0,command=self.player_level)
        self.play_game_main_choose_3.place(x=1005,y=565)
        self.play_game_main_canvasphoto__Characterattributes_3 = tk.PhotoImage(file="python_simplegame\\mainui\\人物属性\\确认应用.png")
        self.play_game_main_choose_4 = tk.Button(self.play_game_main_canvas__Characterattributes,image=self.play_game_main_canvasphoto__Characterattributes_3,bd=0,command=self.create_play_game_main_canvas_playerinforeload)
        self.play_game_main_choose_4.place(x=1005,y=625)
        self.play_game_main_canvasphoto__Characterattributes_4 = tk.PhotoImage(file="python_simplegame\\mainui\\人物属性\\返回.png")
        self.play_game_main_choose_5 = tk.Button(self.play_game_main_canvas__Characterattributes,image=self.play_game_main_canvasphoto__Characterattributes_4,bd=0,command=self.create_play_game_main_canvas)
        self.play_game_main_choose_5.place(x=1005,y=685)
    
    def create_play_game_main_canvas__tavern(self):
        self.tavern_mes = messagebox.askyesno("酒馆", "您可以免费回复全部体力值，是否要继续？")
        if self.tavern_mes:
            messagebox.showinfo("酒馆","酒馆侍女为你温了一杯酒，短暂歇息后你的体力值已全部恢复。")
            self.ps = self.ps_max
            self.create_play_game_main_canvas()
        else:
            self.create_play_game_main_canvas()
    
if __name__ == "__main__":
    win = Tk()
    win.iconbitmap('python_simplegame\\qiji.ico')
    SimpleGame(win)
    win.mainloop()
