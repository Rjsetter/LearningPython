#_*_ encoding:utf-8 _*_
#Word Jumble猜词游戏
import random

#创建单词序列
WORDS = ['happy', 'population', 'easy', 'tough', 'difficult', 'middle', 'continue', 'answer', 'game', 'position']

#start the game
print(
      """
			欢迎参加单词游戏
		把字母组合成一个正确的单词	
      """)
#标志量，确定是否继续游戏
Flag = True
while Flag:
	#从单词序列WORDS中随机挑出一个单词
	word = random.choice(WORDS)
	#判断变量
	correct = word
	#创建乱序单词
	jumble = ''
	while word:
		#随机取单词中的字母的位置
		position = random.randrange(len(word))
		#将随机取出的字母添加到变序的单词i中
		jumble += word[position]
		#将取出的字母从原单词中取出
		word = word[:position] + word[(position+1):] 
	print("----------------------------------------")
	print("乱序后的单词：", jumble)
	guess = input("please input your guess word:")
	while guess != correct or guess =="":
		flag = input("猜错了，是否继续？(Y/N)")
		if flag == 'N' or flag == 'n':
			break	
		else:
			guess = input("请继续猜：")
		print("----------------------------------------")
	node = input("是否还想再玩一次？Y/N：")
	if node == 'N' or node =='n':
		Flag = False
		print("欢迎下次再玩！")








