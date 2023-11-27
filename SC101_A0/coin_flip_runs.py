"""
File: coin_flip_runs.py
Name: 吳宇韻
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	This is a program that runs coin flips.
	"""
	print("Let's flip a coin!")

	num_run = int(input("Number of runs: "))

	ans = ""
	count = 0

	while count < num_run:
		r1 = r.choice(["T", "L"])
		r2 = r.choice(["T", "L"])
		ans += r1 + r2
		if r1 == r2:
			count += 1
			while True:
				r3 = r.choice(["T", "L"])
				ans += r3
				if r3 != r2:
					break
	print(ans, end="")

# 	問題1：要終止程式前的最後ㄧ個字母（與前面的不同），仍然會顯示出來，
# 	已有試過for i in range，把 i != num_run -1 的表達式還是寫錯
# 	問題2：比完ㄧ二，當第三個要跟前ㄧ個開始比的時候我的程式有錯誤還是沒辦法找出

#   1. flip
#   2. 檢查是否為連續區間, 來決定count是否可以加, ture(是還在連續區間）false (不在連續區間）
#   3. 定義連續區間，如何定義？ㄧ開始沒有flip時都還沒有被定義，當第ㄧ次flip時怎辦？要找出初始值，
is_in_a_row = False
last_char =  " "

while count < num_run:
	if last_char != r1 and is_in_a_row:
		is_in_a_row = False

	if last_char == r1:
		is_in_a_row = True
#    以後想到這個 用布林直 開關


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
