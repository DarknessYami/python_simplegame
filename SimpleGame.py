from tkinter import *
import tkinter as tk
class SimpleGame:
    HP = 100
    HP_Max = 100
    Attact = 20
    Defense = 5
    name = "未设定"
    Race = "未设定"
    Magical_adaptability = 0.0
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
    Luck = 0.0    

    def __init__(self,master):
        self.win = master
        self.win.geometry("1280x800")
        self.win.title("为美好的小暗献上祝福！ -开发版本beta-0.1-  测试ing")
        self.Player_Create_set() # 创建 Toplevel 创造人物窗口
        self.PlayTheGame()# 创建游戏主要窗口
        self.MenuGameCanvas() #创建开始界面窗口

        self.Player_create_info()
        self.player_set_start()


    # def MenuTopSet(self):    # 菜单创建
    #     self.Menu_set = tk.Menu(self.PlayTheGame)
    #     self.Menu_1 = tk.Menu(self.Menu_set, tearoff=0)
    #     self.Menu_set.add_cascade(label='菜单', menu = self.Menu_1)
    #     self.Menu_1.add_command(label='待开发')
    #     self.Menu_1.add_command(label='待开发')
    #     self.Menu_1.add_command(label='待开发')
    #     self.Menu_1.add_separator()  # 添加一条分隔线
    #     self.Menu_1.add_command(label='退出游戏', command=self.win.quit)
    #     self.Menu_2 = tk.Menu(self.Menu_set, tearoff=0)
    #     self.Menu_set.add_cascade(label='功能', menu = self.Menu_2)
    #     self.Menu_2.add_command(label='待开发')
    #     self.Menu_2.add_command(label='待开发')
    #     self.Menu_2.add_command(label='待开发')
    #     self.PlayTheGame.config(menu = self.Menu_set)
    def Player_Create_set(self):
        # 创建 Toplevel 窗口
        self.Player_Create_set = tk.Toplevel(self.win,width=1280,height=800)
        self.Player_Create_set.iconbitmap('python_simplegame\\qiji.ico')
        self.Player_Create_set.title("你正在塑造你的小人……")
        self.Player_Create_set.withdraw()
    def Player_Create(self):
        self.Player_Create_set.deiconify()
        self.win.withdraw()
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
    def Player_file(self): #创建人物数据存档
        self.Player_file = open("python_simplegame\\save\\Player_save.txt",'w') 
        self.Player_file.write(str(self.name) +'\r')    #姓名
        self.Player_file.write(str(self.Race) + '\r')   #种族
        self.Player_file.write(str(self.Magical_adaptability) + '\r')   #魔法适应程度
        self.Player_file.write(str(self.Str) + '\r')    #力量
        self.Player_file.write(str(self.Str_coefficient) + '\r')    #力量成长系数
        self.Player_file.write(str(self.Agi) + '\r')    #敏捷
        self.Player_file.write(str(self.Agi_coefficient) + '\r')    #敏捷成长系数
        self.Player_file.write(str(self.Int) +'\r')   #智力
        self.Player_file.write(str(self.Int_coefficient) +'\r') #智力成长系数
        self.Player_file.close()
    def Player_file_login(self):#读取人物数据存档
        self.Player_file_login = open("python_simplegame\\save\\Player_save.txt",'r')
        name = self.Player_file_login.readline()
        race = self.Player_file_login.readline()
        Magical_adaptability = self.Player_file_login.readline()
        Str = self.Player_file_login.readline()
        Str_coefficient = self.Player_file_login.readline()
        Agi = self.Player_file_login.readline()
        Agi_coefficient = self.Player_file_login.readline()
        Int = self.Player_file_login.readline()
        Int_coefficient = self.Player_file_login.readline()
        self.name = name
        self.Race = race
        self.Magical_adaptability = Magical_adaptability
        self.Str = Str
        self.Str_coefficient = Str_coefficient
        self.Agi = Agi
        self.Agi_coefficient = Agi_coefficient
        self.Int = Int
        self.Int_coefficient = Int_coefficient
        self.Player_file_login.close()

    def player_hp(self):#玩家血量系统
        while(True):
            self.HP_Max_up = int(self.HP_Max) + int(self.Str) * 4
            self.HP_Max_set = int(self.HP_Max_up)
            self.HPif = self.Str
            if(self.Str == self.HPif):
                break
    def player_Attact(self):#玩家攻击力系统
        while(True):
            self.Attact_UP = 0
            self.Attact_UP = int(self.Attact_UP) + int(self.Str) * 0.5
            self.Attact_set = int(self.Attact) + int(self.Attact_UP)
            self.Attactif = self.Str
            if(self.Str == self.Attactif):
                break
    def player_defense(self):#玩家防御力系统
        self.Defenseif = 0
        while(self.Defenseif != self.Agi):
            self.Defense_UP = 0
            self.Defense_UP = int(self.Defense_UP) + int(self.Agi) * 0.2
            self.Defense_set = int(self.Defense) + int(self.Defense_UP)
            self.Defenseif = self.Agi


    def player_level(self):#等级系统
        self.Player_Level_nowset = self.Player_now + self.Player_get
        self.Player_Level_needset = self.Player_need + self.Player_Level * 100
        while self.Player_Level_nowset >= self.Player_Level_needset:
            self.Player_Level += 1
            self.Player_Level_nowset = self.Player_Level_nowset - self.Player_Level_needset
            self.Player_Level_needset = self.Player_Level * 100 + self.Player_Level_needset

        #【bug】一、现在遇到了刷新属性，属性会各次叠加
        #这个是升级属性后的判定，还需要完善
    def create_play_game_main_canvas_playerinforeload(self):
        self.player_hp()
        self.HP_Max = "                     "
        self.HP_Max = self.HP_Max_set
        self.player_Attact()
        self.Attact = "                     "
        self.Attact = self.Attact_set                                                                                                                                                                                                                              
        self.player_defense()
        self.Defense = "                     "
        self.Defense = self.Defense_set
        self.create_play_game_main_canvas()
        #战斗系统
    def Fight_canvas(self):
        self.Fight_canvas = tk.Canvas(self.PlayTheGame, width=1920, height=1080, bg=None)
        self.Fight_canvas.place(x=0, y=0) 
        #小怪血条
        self.Fight_canvas_Redset = tk.Canvas(self.PlayTheGame, width=395, height=25, bg="#9c9c9c")
        self.Fight_canvas_Redset.place(x=130, y=180)                            
        self.Fight_canvas_Red = tk.Canvas(self.Fight_canvas_Redset, width=385, height=15, bg="#c4161e")
        self.Fight_canvas_Red.place(x=5, y=5)
        #人物血条
        self.Fight_canvas_Redset = tk.Canvas(self.PlayTheGame, width=395, height=25, bg="#9c9c9c")
        self.Fight_canvas_Redset.place(x=960, y=480)
        self.Fight_canvas_Green = tk.Canvas(self.Fight_canvas_Redset, width=385, height=15, bg="#277f00")
        self.Fight_canvas_Green.place(x=5, y=5)
        self.Fight_canvas.create_text(970, 405, text=self.name + "[Level:   " + str(self.Player_Level) + "  ]", anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        #人物
        self.Fight_canvas_playerimg = tk.PhotoImage(file="python_simplegame\\playerimg\\player.png")
        self.Fight_canvas.create_image(1024, 530, image=self.Fight_canvas_playerimg, anchor="nw")
        #战斗记录
        self.Fight_canvas_noteset = tk.Canvas(self.PlayTheGame, width=500, height=1030, bg="#d4d4d4")
        self.Fight_canvas_noteset.place(x=1400, y=20)  
        self.Fight_canvas_noteset.create_text(8, 8, text="战斗记录", anchor="nw", fill="black", font=("微软雅黑", 17, "bold"))
        #技能栏
        self.Fight_canvas_skillset = tk.Canvas(self.PlayTheGame, width=760, height=230, bg="#d4d4d4")
        self.Fight_canvas_skillset.place(x=620, y=820)
        self.Fight_canvas_skillchoose_0 = tk.Button(self.PlayTheGame,text="物理攻击", anchor="nw", font=("微软雅黑", 17, "bold"),bd=0,)
        self.Fight_canvas_skillchoose_0.place(x=500,y=820)     
        self.Fight_canvas_skillchoose_1 = tk.Button(self.PlayTheGame,text="魔法技能", anchor="nw", font=("微软雅黑", 17, "bold"),bd=0,)
        self.Fight_canvas_skillchoose_1.place(x=500,y=880)
        self.Fight_canvas.create_text(470, 877,text="◆",fill="black",font=("微软雅黑", 24, "bold"), anchor="nw")
        self.Fight_canvas_skillchoose_2 = tk.Button(self.PlayTheGame,text="道具", anchor="nw", font=("微软雅黑", 17, "bold"),bd=0,)
        self.Fight_canvas_skillchoose_2.place(x=520,y=940)
        self.Fight_canvas_skillchoose_3 = tk.Button(self.PlayTheGame,text="逃跑", anchor="nw", font=("微软雅黑", 17, "bold"),bd=0,)
        self.Fight_canvas_skillchoose_3.place(x=520,y=1000)
        #人物立绘 x446 y574
        self.Fight_canvas_playerimg_1 = tk.PhotoImage(file="python_simplegame\\playerimg\\player_set.png")
        self.Fight_canvas.create_image(0, 520, image=self.Fight_canvas_playerimg_1, anchor="nw")




#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#下面的代码为初始创建角色相关的代码
#Player_create_info = 左侧人物属性面板
#Player_create_info_reload = 【功能 - 更新属性】
#player_set_start = 开始创建人物按钮
#playername = 1、创建人物名称
#playername_set = 创建人物名称 - 实时映射
#player_race = 2、创建人物种族
#player_choose_1 = 3、幼年事件
#player_choose_2 = 4、少年事件
#player_choose_3 = 5、青年事件
#player_choose_4 = 6、战争爆发事件
#player_choose_5 = 7、家族血仇事件
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
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
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    def PlayTheGame(self):
        self.PlayTheGame = tk.Toplevel(self.Player_Create_set,width=1920,height=1080)
        self.PlayTheGame.title("欢迎来到蒂斯亚克大陆！")
        self.PlayTheGame.iconbitmap('python_simplegame\\qiji.ico')
        self.PlayTheGame.attributes('-fullscreen', True)
        self.PlayTheGame.withdraw()
        # self.MenuTopSet()
        self.PlayTheGame_story_1()

    def PlayTheGameToplevel_change(self):
        self.Player_file_login()#读取人物数据存档
        self.PlayTheGame.deiconify()
        self.Player_Create_set.withdraw()#关闭人物创建界面
        self.win.withdraw()#关闭开始游戏界面
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    #初始剧情介绍
    def PlayTheGame_story_1(self):#                                                  bg="#ffca58"
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
        self.play_game_main_canvas.create_text(550, 845, text=self.name, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.play_game_main_canvas.create_text(1010, 845, text=self.Race, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.play_game_main_canvas.create_text(850, 845, text=self.Player_Level, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.play_game_main_canvas.create_text(330, 845, text=self.HP, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.play_game_main_canvas.create_text(1010, 912, text=self.Str, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.play_game_main_canvas.create_text(1010, 965, text=self.Agi, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.play_game_main_canvas.create_text(1010, 1017, text=self.Int, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.play_game_main_canvas.create_text(730, 1017, text=self.Magical_adaptability, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.play_game_main_canvas.create_text(630, 912, text=self.Attact, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))
        self.play_game_main_canvas.create_text(630, 965, text=self.Defense, anchor="nw", fill="black", font=("微软雅黑", 20, "bold"))

    def Map_levelchoose(self):                                 
        self.Map_levelchoose_canvas = tk.Canvas(self.PlayTheGame, width=1920, height=775, bg=None)
        self.Map_levelchoose_canvas.place(x=-2, y=0)
        self.Map_levelchoose_1 = tk.Button(self.Map_levelchoose_canvas,text="【荒野平原】 Lv10 ",font=("微软雅黑", 22, "bold"),bd=0,command=self.Fight_canvas)
        self.Map_levelchoose_1.place(x=810,y=140)
        self.Map_levelchoose_2 = tk.Button(self.Map_levelchoose_canvas,text="【厄菲尔海滩】 Lv20 ",font=("微软雅黑", 22, "bold"),bd=0)
        self.Map_levelchoose_2.place(x=790,y=240)
        self.Map_levelchoose_3 = tk.Button(self.Map_levelchoose_canvas,text="【无名者洞穴】 Lv30 ",font=("微软雅黑", 22, "bold"),bd=0)
        self.Map_levelchoose_3.place(x=790,y=340)
        self.Map_levelchoose_4 = tk.Button(self.Map_levelchoose_canvas,text="【冰天雪地】 Lv40 ",font=("微软雅黑", 22, "bold"),bd=0)
        self.Map_levelchoose_4.place(x=800,y=440)
        self.Map_levelchoose_5 = tk.Button(self.Map_levelchoose_canvas,text="【炽焰火山】 Lv50 ",font=("微软雅黑", 22, "bold"),bd=0)
        self.Map_levelchoose_5.place(x=800,y=540)
        self.Map_levelchoose_6 = tk.Button(self.Map_levelchoose_canvas, text="【返回城镇】", font=("微软雅黑", 22, "bold"), bd=1, command=self.create_play_game_main_canvas)
        self.Map_levelchoose_6.place(x=850,y=640)

    def create_play_game_main_canvas__Characterattributes(self):
        self.create_play_game_main_canvas()                                                                  #bg="#ffca58"
        self.play_game_main_canvas__Characterattributes = tk.Canvas(self.PlayTheGame, width=1920, height=775, bg=None)
        self.play_game_main_canvas__Characterattributes.place(x=-2, y=0)
        self.play_game_main_canvasphoto__Characterattributes = tk.PhotoImage(file="python_simplegame\\mainui\\人物属性\\人物属性-介绍.png")
        self.play_game_main_canvas__Characterattributes.create_image(0, 0, image=self.play_game_main_canvasphoto__Characterattributes, anchor="nw")
        #技能点描述
        self.play_game_main_canvas__Characterattributes.create_text(520,25,text=self.Skinpoint, anchor="nw", fill="#277f00", font=("微软雅黑", 23, "bold",))
        # 主属性额外加点描述
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
        self.play_game_main_canvas__Characterattributes.create_text(195,450,text=self.Crit_p * 100, anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(195,500,text=self.Crit_d * 100, anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(195,550,text=self.Crit_r * 100, anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(230,450,text="  %", anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(285,500,text="%", anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        self.play_game_main_canvas__Characterattributes.create_text(230,550,text="  %", anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
        #闪避描述
        self.play_game_main_canvas__Characterattributes.create_text(500,500,text=self.Sidestep_p * 100, anchor="nw", fill="black", font=("微软雅黑", 23, "bold"))
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
        self.play_game_main_choose_3 = tk.Button(self.play_game_main_canvas__Characterattributes,image=self.play_game_main_canvasphoto__Characterattributes_2,bd=0,)
        self.play_game_main_choose_3.place(x=1005,y=565)
        self.play_game_main_canvasphoto__Characterattributes_3 = tk.PhotoImage(file="python_simplegame\\mainui\\人物属性\\确认应用.png")
        self.play_game_main_choose_4 = tk.Button(self.play_game_main_canvas__Characterattributes,image=self.play_game_main_canvasphoto__Characterattributes_3,bd=0,command=self.create_play_game_main_canvas_playerinforeload)
        self.play_game_main_choose_4.place(x=1005,y=625)
        self.play_game_main_canvasphoto__Characterattributes_4 = tk.PhotoImage(file="python_simplegame\\mainui\\人物属性\\返回.png")
        self.play_game_main_choose_5 = tk.Button(self.play_game_main_canvas__Characterattributes,image=self.play_game_main_canvasphoto__Characterattributes_4,bd=0,command=self.create_play_game_main_canvas)
        self.play_game_main_choose_5.place(x=1005,y=685)

if __name__ == "__main__":
    win = Tk()
    win.iconbitmap('python_simplegame\\qiji.ico')
    SimpleGame(win)
    win.mainloop()
