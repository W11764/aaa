#coding:gbk
"""
程序目标：新编一程序， 完成RPSLS游戏
作者：王娅文 
"""

import random
print()
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
player_choice=input()
def name_to_number(name):#将游戏对象对应到不同的整数
	if name=="石头" or name=="rock":
		return 0
	elif name=="史波克" or name=="Spock":
		return 1
	elif name=="布" or name=="paper":
		return 2
	elif name=="蜥蜴" or name=="lizard":
		return 3
	elif name=="剪刀" or name=="scissors":
		return 4
	else:
		return 5
	

def number_to_name(number):#将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
	if number==0:
		return ("石头" or "rock")
	elif number==1:
		return ("史波克" or "Spock")
	elif number==2:
		return ("布" or "paper")
	elif number==3:
		return ("蜥蜴" or "lizard")
	else:
		return ("剪刀" or "scissors")
		
			
	
def rpsls(player_choice):#用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
	player_choice_number=name_to_number(player_choice)	
	comp_num=random.randint(0,4)
	com_choice=number_to_name(comp_num)	
	if player_choice_number==5:
		print("Error: No Correct Name")
	else:
		print(player_choice_number,comp_num)
		print("计算机的选择为:%s"%com_choice)
		if player_choice_number==4 and comp_num==2:    
			print("您赢了")
		elif player_choice_number==2 and comp_num==0: 
			print("您赢了")
		elif player_choice_number==0 and comp_num==4: 
			print("您赢了")
		elif player_choice_number==0 and comp_num==3 :
			print("您赢了")
		elif player_choice_number==3 and comp_num==1:
			print("您赢了")
		elif player_choice_number==1 and comp_num==4:    
			print("您赢了")
		elif player_choice_number==4 and comp_num==3:    
			print("您赢了")
		elif player_choice_number==3 and comp_num==2:    
			print("您赢了")
		elif player_choice_number==2 and comp_num==1:    
			print("您赢了")
		elif player_choice_number==1 and comp_num==0:    
			print("您赢了")
		elif player_choice_number==2 and comp_num==4:              
			print("计算机赢了")
		elif player_choice_number==0 and comp_num==2:
			print("计算机赢了")
		elif player_choice_number==4 and comp_num==0:
			print("计算机赢了")
		elif player_choice_number==3 and comp_num==0:
			print("计算机赢了")
		elif player_choice_number==1 and comp_num==3:
			print("计算机赢了")
		elif player_choice_number==4 and comp_num==1:    
			print("计算机赢了")
		elif player_choice_number==3 and comp_num==4:    
			print("计算机赢了")
		elif player_choice_number==2 and comp_num==3:    
			print("计算机赢了")
		elif player_choice_number==1 and comp_num==2:    
			print("计算机赢了")
		elif player_choice_number==1 and comp_num==0:    
			print("计算机赢了")
		else:
			print("您和计算机出的一样呢")
print()		
rpsls(player_choice)
	
		
