from tkinter import *
import tkinter as tk

#蜘蛛
def zhizhu(self):
    self.M_HP = 50
    self.M_Damage = 10
    self.M_Defense = 3
    self.M_name = "蜘蛛 [Lv1]"
    self.M_Crit_p = 0.0              #暴击概率
    self.M_Crit_d = 1.5              #暴击伤害  
    self.M_Crit_r = 0.0              #暴击抵抗
    self.M_Sidestep_p = 0.0          #闪避概率
    self.M_Sidestep_r = 0.0          #闪避抵抗
    self.M_Damage_deepen = 0.0       #伤害加深
    self.M_Damage_deduction = 0.0    #伤害减免
    self.M_Luck = 0.0  
#巨型蜘蛛【boss】
def boss_zhizhu(self):
    self.M_HP = 150
    self.M_Damage = 30
    self.M_Defense = 10
    self.M_name = "巨型蜘蛛 [Lv8]"
    self.M_Crit_p = 0.0              #暴击概率
    self.M_Crit_d = 1.5              #暴击伤害  
    self.M_Crit_r = 0.0              #暴击抵抗
    self.M_Sidestep_p = 0.0          #闪避概率
    self.M_Sidestep_r = 0.0          #闪避抵抗
    self.M_Damage_deepen = 0.0       #伤害加深
    self.M_Damage_deduction = 0.0    #伤害减免
    self.M_Luck = 5.0
#恐狼
def konglang(self):
    self.M_HP = 70
    self.M_Damage = 20
    self.M_Defense = 5
    self.M_name = "恐狼 [Lv3]"
    self.M_Crit_p = 0.0              #暴击概率
    self.M_Crit_d = 1.5              #暴击伤害  
    self.M_Crit_r = 0.0              #暴击抵抗
    self.M_Sidestep_p = 0.0          #闪避概率
    self.M_Sidestep_r = 0.0          #闪避抵抗
    self.M_Damage_deepen = 0.0       #伤害加深
    self.M_Damage_deduction = 0.0    #伤害减免
    self.M_Luck = 0.0
#恐狼领袖【boss】
def boss_konglang(self):
    self.M_HP = 170
    self.M_Damage = 40
    self.M_Defense = 10
    self.M_name = "恐狼领袖 [Lv9]"
    self.M_Crit_p = 0.0              #暴击概率
    self.M_Crit_d = 1.5              #暴击伤害  
    self.M_Crit_r = 0.0              #暴击抵抗
    self.M_Sidestep_p = 0.0          #闪避概率
    self.M_Sidestep_r = 0.0          #闪避抵抗
    self.M_Damage_deepen = 0.0       #伤害加深
    self.M_Damage_deduction = 0.0    #伤害减免
    self.M_Luck = 5.0
#哥布林斥候
def gebulinchihou(self):
    self.M_HP = 100
    self.M_Damage = 25
    self.M_Defense = 8
    self.M_name = "哥布林斥候 [Lv6]"
    self.M_Crit_p = 0.0              #暴击概率
    self.M_Crit_d = 1.5              #暴击伤害  
    self.M_Crit_r = 0.0              #暴击抵抗
    self.M_Sidestep_p = 0.0          #闪避概率
    self.M_Sidestep_r = 0.0          #闪避抵抗
    self.M_Damage_deepen = 0.0       #伤害加深
    self.M_Damage_deduction = 0.0    #伤害减免
    self.M_Luck = 0.0
#哥布林队长【boss】
def gebulinchihou(self):
    self.M_HP = 200
    self.M_Damage = 50
    self.M_Defense = 12
    self.M_name = "哥布林队长 [Lv10]"
    self.M_Crit_p = 0.0              #暴击概率
    self.M_Crit_d = 1.5              #暴击伤害  
    self.M_Crit_r = 0.0              #暴击抵抗
    self.M_Sidestep_p = 0.0          #闪避概率
    self.M_Sidestep_r = 0.0          #闪避抵抗
    self.M_Damage_deepen = 0.0       #伤害加深
    self.M_Damage_deduction = 0.0    #伤害减免
    self.M_Luck = 5.0