#coding:gbk
"""
����Ŀ�꣺�±�һ���� ���RPSLS��Ϸ
���ߣ������ 
"""

import random
print()
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
player_choice=input()
def name_to_number(name):#����Ϸ�����Ӧ����ͬ������
	if name=="ʯͷ" or name=="rock":
		return 0
	elif name=="ʷ����" or name=="Spock":
		return 1
	elif name=="��" or name=="paper":
		return 2
	elif name=="����" or name=="lizard":
		return 3
	elif name=="����" or name=="scissors":
		return 4
	else:
		return 5
	

def number_to_name(number):#������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
	if number==0:
		return ("ʯͷ" or "rock")
	elif number==1:
		return ("ʷ����" or "Spock")
	elif number==2:
		return ("��" or "paper")
	elif number==3:
		return ("����" or "lizard")
	else:
		return ("����" or "scissors")
		
			
	
def rpsls(player_choice):#�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
	player_choice_number=name_to_number(player_choice)	
	comp_num=random.randint(0,4)
	com_choice=number_to_name(comp_num)	
	if player_choice_number==5:
		print("Error: No Correct Name")
	else:
		print(player_choice_number,comp_num)
		print("�������ѡ��Ϊ:%s"%com_choice)
		if player_choice_number==4 and comp_num==2:    
			print("��Ӯ��")
		elif player_choice_number==2 and comp_num==0: 
			print("��Ӯ��")
		elif player_choice_number==0 and comp_num==4: 
			print("��Ӯ��")
		elif player_choice_number==0 and comp_num==3 :
			print("��Ӯ��")
		elif player_choice_number==3 and comp_num==1:
			print("��Ӯ��")
		elif player_choice_number==1 and comp_num==4:    
			print("��Ӯ��")
		elif player_choice_number==4 and comp_num==3:    
			print("��Ӯ��")
		elif player_choice_number==3 and comp_num==2:    
			print("��Ӯ��")
		elif player_choice_number==2 and comp_num==1:    
			print("��Ӯ��")
		elif player_choice_number==1 and comp_num==0:    
			print("��Ӯ��")
		elif player_choice_number==2 and comp_num==4:              
			print("�����Ӯ��")
		elif player_choice_number==0 and comp_num==2:
			print("�����Ӯ��")
		elif player_choice_number==4 and comp_num==0:
			print("�����Ӯ��")
		elif player_choice_number==3 and comp_num==0:
			print("�����Ӯ��")
		elif player_choice_number==1 and comp_num==3:
			print("�����Ӯ��")
		elif player_choice_number==4 and comp_num==1:    
			print("�����Ӯ��")
		elif player_choice_number==3 and comp_num==4:    
			print("�����Ӯ��")
		elif player_choice_number==2 and comp_num==3:    
			print("�����Ӯ��")
		elif player_choice_number==1 and comp_num==2:    
			print("�����Ӯ��")
		elif player_choice_number==1 and comp_num==0:    
			print("�����Ӯ��")
		else:
			print("���ͼ��������һ����")
print()		
rpsls(player_choice)
	
		
