
# coding: utf-8

# In[ ]:


import random
dic = {'banana':'香蕉', 'pineapple':'鳳梨','apple':'蘋果', 'peach':'桃子'}
message = '\n1.新增單字，2.查詢單字，3.單字練習，4.顯示所有單字，5.刪除單字，6.結束程式：'
choice = 9

def funcAdd(word):
    if word in dic == False:
        chi = input('請輸入中文意思：')
        dic[word] = chi
    else:
        print('單字已存在，是否要更改其意思？')
        if int(input('1.是，2.否：')) == 1:
            chi = input('請輸入中文意思：')
            dic[word] = chi

def funcFind(word):
    if word in dic:
        chi = dic[word]
        print(word + ':' , chi)
    else:
        print("查詢的單字'" + word + "'不存在！是否要新增單字？")
        if int(input('1.是，2.否：')) == 1:
            funcAdd(word)          
    
def funcPrac():
    eng = random.choice(list(dic.keys()))
    chi = dic[eng]
    ans = input("請輸入'" + chi + "'的英文：")
    if ans == eng: print('答對了！')
    else: print('答錯了！正確答案為：', eng)
    
def funcViewAll():
    for eng, chi in dic.items():
        print(eng, chi)

def funcDel():
    funcViewAll()
    word = input('請輸入要刪除的單字：')
    for eng, chi in dic.items():
        if word == chi:
            del dic[eng]
            return
        elif word == eng:
            del dic[eng]
            return
    print('刪除失敗！')
        
        
while(choice != 6):
    print(message)
    choice = input('請輸入1-6：')
    if choice.isdigit() == True:
        choice = int(choice)
        if choice == 1: funcAdd(input('請輸入要增加的英文單字：'))
        elif choice == 2: funcFind(input('請輸入要查詢的英文單字：'))
        elif choice == 3: funcPrac()
        elif choice == 4: funcViewAll()
        elif choice == 5: funcDel()
        elif choice == 6: break
        else: print('暫無此功能！')
    else:
        print('輸入的不是數字！請重新輸入！')
    
print('Thanks! See you next time!')

