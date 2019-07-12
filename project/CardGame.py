# Card Game

from tkinter import*
from tkinter.colorchooser import*
import tkinter.font as font
import random


''' HalliGalli(할리갈리) Rule
    : 카드는 모두 56장이다. 1개짜리 5장, 2개짜리3장, 3개짜리 3장, 4개짜리 2장, 5개짜리 1장
      과일은 바나나, 딸기, 라임(키위), 자두(체리)로 총 네 종류이다.
      만약 상대방과 나의 카드의 과일 종류가 같고 개수의 합이 5개이면 종을 빨리 누르는 사람이 이기는 형식이다.
      본 게임에서는 상대방이 컴퓨터이므로 해당 조건을 만족할 경우 일정시간에 안에 눌르면 이기도록 설정하였다.'''


class CardGame:
    def __init__(self, r):
       
        # 배경 설정
        self.s = Frame(r, height = 530, width = 750, bg = "white", cursor = "hand2")
        self.s.pack()

        photo1 = PhotoImage(file = "HalliGalli_Bell_image.png")
        photo2 = PhotoImage(file = "HalliGalli_Card_BackGround.png")
        photo3 = PhotoImage(file = "HalliGalli_Card_BackGround2.png")

        menu = Button(self.s, text = "Menu", cursor = "hand2", bg = "white")
        bell = Button(self.s, cursor = "hand2", bg = "white", image = photo1, command = lambda : self.CardController())
        card_background = Button(self.s, cursor = "hand2", image = photo2, command = lambda : self.UserCardController())
        card_background2 = Label(self.s, cursor = "hand2", image = photo3)
        bell.image = photo1
        card_background.image = photo2
        card_background2.image = photo3
        
        menu.place(x = 710, y = 1)
        bell.place(x = 600, y = 150)
        card_background.place(x = 320, y = 370)
        card_background2.place(x = 320, y = 1)

        self.UserCardController_counter = 0
        count_window1 = Label(self.s, text = "내 카드 수 : ", cursor = "hand2", bg = "white", font = "Times 28 bold italic")
        count_window2 = Label(self.s, text = "적 카드 수 : ", cursor = "hand2", bg = "white", font = "Times 28 bold italic")
        count_window1.place(x = 10, y = 240)
        count_window2.place(x = 10, y = 180)

        # 카드 이미지 파일
        
        strawberry1 = PhotoImage(file = "HalliGalli_Card_Strawberry1.png")
        strawberry2 = PhotoImage(file = "HalliGalli_Card_Strawberry2.png")
        strawberry3 = PhotoImage(file = "HalliGalli_Card_Strawberry3.png")
        strawberry4 = PhotoImage(file = "HalliGalli_Card_Strawberry4.png")
        strawberry5 = PhotoImage(file = "HalliGalli_Card_Strawberry5.png")
        
        banana1 = PhotoImage(file = "HalliGalli_Card_Banana1.png")
        banana2 = PhotoImage(file = "HalliGalli_Card_Banana2.png")
        banana3 = PhotoImage(file = "HalliGalli_Card_Banana3.png")
        banana4 = PhotoImage(file = "HalliGalli_Card_Banana4.png")
        banana5 = PhotoImage(file = "HalliGalli_Card_Banana5.png")
        
        kiwi1 = PhotoImage(file = "HalliGalli_Card_Kiwi1.png")
        kiwi2 = PhotoImage(file = "HalliGalli_Card_Kiwi2.png")
        kiwi3 = PhotoImage(file = "HalliGalli_Card_Kiwi3.png")
        kiwi4 = PhotoImage(file = "HalliGalli_Card_Kiwi4.png")
        kiwi5 = PhotoImage(file = "HalliGalli_Card_Kiwi5.png")

        plum1 = PhotoImage(file = "HalliGalli_Card_Plum1.png")
        plum2 = PhotoImage(file = "HalliGalli_Card_Plum2.png")
        plum3 = PhotoImage(file = "HalliGalli_Card_Plum3.png")
        plum4 = PhotoImage(file = "HalliGalli_Card_Plum4.png")
        plum5 = PhotoImage(file = "HalliGalli_Card_Plum5.png")
        

        # 카드 이미지 맞추기
        
        self.card = []
        
        self.Strawberry1 = Label(self.s, cursor = "hand2", image = strawberry1)
        self.Strawberry2 = Label(self.s, cursor = "hand2", image = strawberry2)
        self.Strawberry3 = Label(self.s, cursor = "hand2", image = strawberry3)
        self.Strawberry4 = Label(self.s, cursor = "hand2", image = strawberry4)
        self.Strawberry5 = Label(self.s, cursor = "hand2", image = strawberry5)
        self.Strawberry1.image = strawberry1
        self.Strawberry2.image = strawberry2
        self.Strawberry3.image = strawberry3
        self.Strawberry4.image = strawberry4
        self.Strawberry5.image = strawberry5

        self.Banana1 = Label(self.s, cursor = "hand2", image = banana1)
        self.Banana2 = Label(self.s, cursor = "hand2", image = banana2)
        self.Banana3 = Label(self.s, cursor = "hand2", image = banana3)
        self.Banana4 = Label(self.s, cursor = "hand2", image = banana4)
        self.Banana5 = Label(self.s, cursor = "hand2", image = banana5)
        self.Banana1.image = banana1
        self.Banana2.image = banana2
        self.Banana3.image = banana3
        self.Banana4.image = banana4
        self.Banana5.image = banana5

        self.Kiwi1 = Label(self.s, cursor = "hand2", image = kiwi1)
        self.Kiwi2 = Label(self.s, cursor = "hand2", image = kiwi2)
        self.Kiwi3 = Label(self.s, cursor = "hand2", image = kiwi3)
        self.Kiwi4 = Label(self.s, cursor = "hand2", image = kiwi4)
        self.Kiwi5 = Label(self.s, cursor = "hand2", image = kiwi5)
        self.Kiwi1.image = kiwi1
        self.Kiwi2.image = kiwi2
        self.Kiwi3.image = kiwi3
        self.Kiwi4.image = kiwi4
        self.Kiwi5.image = kiwi5

        self.Plum1 = Label(self.s, cursor = "hand2", image = plum1)
        self.Plum2 = Label(self.s, cursor = "hand2", image = plum2)
        self.Plum3 = Label(self.s, cursor = "hand2", image = plum3)
        self.Plum4 = Label(self.s, cursor = "hand2", image = plum4)
        self.Plum5 = Label(self.s, cursor = "hand2", image = plum5)
        self.Plum1.image = plum1
        self.Plum2.image = plum2
        self.Plum3.image = plum3
        self.Plum4.image = plum4
        self.Plum5.image = plum5


        self.card.append(self.Strawberry1)
        self.card.append(self.Strawberry2)
        self.card.append(self.Strawberry3)
        self.card.append(self.Strawberry4)
        self.card.append(self.Strawberry5)

        self.card.append(self.Banana1)
        self.card.append(self.Banana2)
        self.card.append(self.Banana3)
        self.card.append(self.Banana4)
        self.card.append(self.Banana5)

        self.card.append(self.Kiwi1)
        self.card.append(self.Kiwi2)
        self.card.append(self.Kiwi3)
        self.card.append(self.Kiwi4)
        self.card.append(self.Kiwi5)

        self.card.append(self.Plum1)
        self.card.append(self.Plum2)
        self.card.append(self.Plum3)
        self.card.append(self.Plum4)
        self.card.append(self.Plum5)

        # 카드 56장 만들기(1개짜리 5장, 2개짜리3장, 3개짜리 3장, 4개짜리 2장, 5개짜리 1장)

        i = 5
        o = 0
        p = 0
        self.cards = []
        for a in range(i):
            self.cards.append(self.card[o])
            self.cards.append(self.card[o + 5])
            self.cards.append(self.card[o + 10])
            self.cards.append(self.card[o + 15])
        for b in range(i - 3):
            for c in range(i - 2):
                self.cards.append(self.card[o + 1])
                self.cards.append(self.card[o + 6])
                self.cards.append(self.card[o + 11])
                self.cards.append(self.card[o + 16])
            o += 1
    
        for d in range(i - 3):
            self.cards.append(self.card[p + 3])
            self.cards.append(self.card[p + 8])
            self.cards.append(self.card[p + 13])
            self.cards.append(self.card[p + 18])
        for e in range(i - 4):
            self.cards.append(self.card[p + 4])
            self.cards.append(self.card[p + 9])
            self.cards.append(self.card[p + 14])
            self.cards.append(self.card[p + 19])

        # 사용자와 컴퓨터 카드 섞기
        
        random.shuffle(self.cards) # 카드 섞기

        self.usercards = self.cards[0:27] # 총 28장의 사용자 카드
        self.computercards = self.cards[28:55] # 총 28장의 컴퓨터 카드


        # 카드게임의 규칙을 설정하는 리스트(True값)

        self.true_strawberry = [self.Strawberry1, self.Strawberry2, self.Strawberry3, self.Strawberry4, self.Strawberry5]
        self.true_banana = [self.Banana1, self.Banana2, self.Banana3, self.Banana4, self.Banana5]
        self.true_kiwi = [self.Kiwi1, self.Kiwi2, self.Kiwi3, self.Kiwi4, self.Kiwi5]
        self.true_plum = [self.Plum1, self.Plum2, self.Plum3, self.Plum4, self.Plum5]
        
        self.true_strawberry1 = [self.Strawberry1, self.Strawberry4]
        self.true_strawberry2 = [self.Strawberry2, self.Strawberry3]

        self.true_banana1 = [self.Banana1, self.Banana4]
        self.true_banana2 = [self.Banana2, self.Banana3]

        self.true_kiwi1 = [self.Kiwi1, self.Kiwi4]
        self.true_kiwi2 = [self.Kiwi2, self.Kiwi3]

        self.true_plum1 = [self.Plum1, self.Plum4]
        self.true_plum2 = [self.Plum2, self.Plum3]

        self.true = [self.Strawberry5, self.Banana5, self.Kiwi5, self.Plum5]


        
    def UserCardController(self):  # 사용자의 카드 뽑기 및 전반적인 카드 값을 조정하는 함수

        # 사용자와 컴퓨터 카드 수 확인

        self.usercards_number = len(self.usercards) - 2
        self.computercards_number = len(self.computercards) - 2
        
            
        # 사용자 카드 뽑기


        if self.UserCardController_counter >= 1:
            self.randomcard1.place(x = 2000, y = 2000)
            self.usercards.remove(self.randomcard1) # 카드 사용 후 카드 제거
            
        
        self.randomcard1 = random.choice(self.usercards)
        self.randomcard1.place(x = 320, y = 225)
        
        # 사용자 카드 수 표시
        
        count_window2_number = Label(self.s, text = self.usercards_number, cursor = "hand2", bg = "white", font = "Times 28 bold italic")
        count_window2_number.place(x = 220, y = 240)

        
        # 컴퓨터에게 턴을 넘기기(ComputerCardController 함수 실행)
        
        time = random.randrange(100,1500)
        self.s.after(time, self.ComputerCardController) # 0.1 ~ 1.5초 사이에 랜덤으로 함수 실행


    def ComputerCardController(self): # 컴퓨터의 카드 뽑기 및 전반적인 카드 값을 조정하는 함수
      

        # 컴퓨터 카드 뽑기


        if self.UserCardController_counter >= 1:
            self.randomcard2.place(x = 2000, y = 2000)
            self.computercards.remove(self.randomcard2) # 카드 사용 후 카드 제거
    
        
        self.randomcard2 = random.choice(self.computercards)
        self.randomcard2.place(x = 320, y = 70)

        self.UserCardController_counter += 1

        if self.UserCardController_counter == 27: 
            self.draw()
            
        # 컴퓨터 카드 수 표시
        
        count_window2_number = Label(self.s, text = self.computercards_number, cursor = "hand2", bg = "white", font = "Times 28 bold italic")
        count_window2_number.place(x = 220, y = 180)
        
        

    def CardController(self): # 사용자와 컴퓨터의 카드를 분석하여 참인지 거짓인지 알아내는 함수

        if self.UserCardController_counter >= 1:
            if self.randomcard1 in self.true_strawberry and self.randomcard2 in self.true_strawberry:
                if self.randomcard1 == self.true_strawberry1[0] and self.randomcard2 == self.true_strawberry1[1] or self.randomcard1 == self.true_strawberry1[1] and self.randomcard2 == self.true_strawberry1[0]:
                    self.win()

                if self.randomcard1 == self.true_strawberry2[0] and self.randomcard2 == self.true_strawberry2[1] or self.randomcard1 == self.true_strawberry2[1] and self.randomcard2 == self.true_strawberry2[0]:
                    self.win()

                if self.randomcard1 == self.true[0] or self.randomcard2 == self.true[0]:
                    self.lose()

                
            elif self.randomcard1 in self.true_banana and self.randomcard2 in self.true_banana:
                if self.randomcard1 == self.true_banana1[0] and self.randomcard2 == self.true_banana1[1] or self.randomcard1 == self.true_banana1[1] and self.randomcard2 == self.true_banana1[0]:
                    self.win()

                if self.randomcard1 == self.true_banana2[0] and self.randomcard2 == self.true_banana2[1] or self.randomcard1 == self.true_banana2[1] and self.randomcard2 == self.true_banana2[0]:
                    self.win()

                if self.randomcard1 == self.true[1] or self.randomcard2 == self.true[1]:
                    self.lose()

            elif self.randomcard1 in self.true_kiwi and self.randomcard2 in self.true_kiwi:
                if self.randomcard1 == self.true_kiwi1[0] and self.randomcard2 == self.true_kiwi1[1] or self.randomcard1 == self.true_kiwi1[1] and self.randomcard2 == self.true_kiwi1[0]:
                    self.win()

                if self.randomcard1 == self.true_kiwi2[0] and self.randomcard2 == self.true_kiwi2[1] or self.randomcard1 == self.true_kiwi2[1] and self.randomcard2 == self.true_kiwi2[0]:
                    self.win()

                if self.randomcard1 == self.true[2] or self.randomcard2 == self.true[2]:
                    self.lose()

            elif self.randomcard1 in self.true_plum and self.randomcard2 in self.true_plum:
                if self.randomcard1 == self.true_plum1[0] and self.randomcard2 == self.true_plum1[1] or self.randomcard1 == self.true_plum1[1] and self.randomcard2 == self.true_plum1[0]:
                    self.win()

                if self.randomcard1 == self.true_plum2[0] and self.randomcard2 == self.true_plum2[1] or self.randomcard1 == self.true_plum2[1] and self.randomcard2 == self.true_plum2[0]:
                    self.win()

                if self.randomcard1 == self.true[3] or self.randomcard2 == self.true[3]:
                    self.lose()

            elif self.randomcard1 in self.true or self.randomcard2 in self.true:
                self.win()
                
            else:
                self.lose()

        else:
            self.mistake()

    def mistake(self):

        self.mistake_message = Toplevel()
        self.mistake_message.wm_title('에러!')
        self.f = Frame(self.win_message, height = 250, width = 350, bg = "white", cursor = "hand2")
        self.f.pack()
        
        self.photo4 = PhotoImage(file = "mistake_image.png")
        self.Mistake_image = Label(self.f, cursor = "hand2", image = self.photo4)
        self.Mistake_image.image = self.photo4
        self.Mistake_image.place(x = 45, y = 0)

        self.message_mistake = Label(self.f, cursor = "hand2", bg = "white", text = "카드를 뽑지 않았습니다!", font = "Times 14 bold italic")
        self.message_mistake.place(x = 70, y = 190)

        self.mistake_message.mainloop



    def win(self):
        self.win_message = Toplevel()
        self.win_message.wm_title('게임결과')
        self.f = Frame(self.win_message, height = 250, width = 350, bg = "white", cursor = "hand2")
        self.f.pack()
        
        self.photo5 = PhotoImage(file = "win_image.png")
        self.Win_image = Label(self.f, cursor = "hand2", image = self.photo5)
        self.Win_image.image = self.photo5
        self.Win_image.place(x = 23, y = 0)

        self.message_win = Label(self.f, cursor = "hand2", bg = "white", text = "이겼습니다!", font = "Times 14 bold italic")
        self.message_win.place(x = 130, y = 195)

        self.win_message.mainloop

        self.reload()
        

    def lose(self):
        self.lose_message = Toplevel()
        self.lose_message.wm_title('게임결과')
        self.f = Frame(self.lose_message, height = 250, width = 350, bg = "white", cursor = "hand2")
        self.f.pack()
        
        self.photo6 = PhotoImage(file = "lose_image.png")
        self.Lose_image = Label(self.f, cursor = "hand2", image = self.photo6)
        self.Lose_image.image = self.photo6
        self.Lose_image.place(x = 65, y = 10)

        self.message_lose = Label(self.f, cursor = "hand2", bg = "white", text = "실수하셨습니다 ㅠㅠ", font = "Times 14 bold italic")
        self.message_lose.place(x = 80, y = 190)

        self.lose_message.mainloop
        

    def draw(self):
        self.draw_message = Toplevel()
        self.draw_message.wm_title('게임결과')
        self.f = Frame(self.draw_message, height = 250, width = 350, bg = "white", cursor = "hand2")
        self.f.pack()
        
        self.photo7 = PhotoImage(file = "draw_image.png")
        self.Draw_image = Label(self.f, cursor = "hand2", image = self.photo7)
        self.Draw_image.image = self.photo7
        self.Draw_image.place(x = 65, y = 10)

        self.message_draw = Label(self.f, cursor = "hand2", bg = "white", text = "무승부!", font = "Times 14 bold italic")
        self.message_draw.place(x = 140, y = 200)

        self.draw_message.mainloop

        self.reload()

    def reload(self): # 다시 카드를 섞고 재생성하기

        # 기존의 카드 제거

        self.randomcard1.place(x = 2000, y = 2000) # 사용자 카드 제거
        self.randomcard2.place(x = 2000, y = 2000) # 컴퓨터 카드 제거
        
        random.shuffle(self.cards) # 카드 섞기

        self.usercards = self.cards[0:27] # 사용자 카드 초기화
        self.computercards = self.cards[28:55] # 컴퓨터 카드 초기화

        self.UserCardController_counter = 0 # 다시 카운트 수 0으로 초기화해주기 
        




        

window = Tk()
window.wm_title('CardGame')
gamecenter = CardGame(window)
window.mainloop
