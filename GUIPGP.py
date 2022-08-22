#!/usr/bin/env python
# coding: utf-8
# %%
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QTextEdit
from PyQt5.QtWidgets import QDialog, QMessageBox, QLCDNumber, QRadioButton, QLineEdit
from PyQt5.QtGui import QPixmap, QIntValidator, QFont
import PyQt5.QtCore
from PyQt5 import uic
from ipynb.fs.full.PaiGowEvaluator_NoJoker import *
from ipynb.fs.full.PaiGowPVP import *
import sys
import random

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        #load the ui file
        uic.loadUi("deck_2.ui", self)
        self.setWindowTitle("Press Deal New")
        

        
        
        #define our widgets
        
        
        self.dealer_top_1_label = self.findChild(QLabel, "dealer_top_1")
        self.dealer_top_2_label = self.findChild(QLabel, "dealer_top_2")
        
        self.dealer_bottom_1_label = self.findChild(QLabel, "dealer_bottom_1")
        self.dealer_bottom_2_label = self.findChild(QLabel, "dealer_bottom_2")
        self.dealer_bottom_3_label = self.findChild(QLabel, "dealer_bottom_3")
        self.dealer_bottom_4_label = self.findChild(QLabel, "dealer_bottom_4")
        self.dealer_bottom_5_label = self.findChild(QLabel, "dealer_bottom_5")
        
        
        self.player_top_1_label = self.findChild(QLabel, "player_top_1")
        self.player_top_2_label = self.findChild(QLabel, "player_top_2")
        
        self.player_bottom_1_label = self.findChild(QLabel, "player_bottom_1")
        self.player_bottom_2_label = self.findChild(QLabel, "player_bottom_2")
        self.player_bottom_3_label = self.findChild(QLabel, "player_bottom_3")
        self.player_bottom_4_label = self.findChild(QLabel, "player_bottom_4")
        self.player_bottom_5_label = self.findChild(QLabel, "player_bottom_5")
        
        self.payout_player_1 = self.findChild(QLabel, "payout_player_1")
        self.payout_player_2 = self.findChild(QLabel, "payout_player_2")
        self.payout_player_3 = self.findChild(QLabel, "payout_player_3")
        self.payout_player_4 = self.findChild(QLabel, "payout_player_4")
        self.payout_player_5 = self.findChild(QLabel, "payout_player_5")
        self.payout_player_6 = self.findChild(QLabel, "payout_player_6")
        
        self.payout_dealer_1 = self.findChild(QLabel, "payout_dealer_1")
        self.payout_dealer_2 = self.findChild(QLabel, "payout_dealer_2")
        self.payout_dealer_3 = self.findChild(QLabel, "payout_dealer_3")
        self.payout_dealer_4 = self.findChild(QLabel, "payout_dealer_4")
        self.payout_dealer_5 = self.findChild(QLabel, "payout_dealer_5")
        self.payout_dealer_6 = self.findChild(QLabel, "payout_dealer_6")
        
        self.payout_tie = self.findChild(QLabel, "payout_tie")
        self.win_loss_banner = self.findChild(QLabel, "win_loss_banner")
        
        
        self.deal_button = self.findChild(QPushButton, "deal_new")
        self.next_button = self.findChild(QPushButton, "next_hand")
        self.bet_button = self.findChild(QPushButton, "bet_button")
        
        self.casino_score = self.findChild(QLCDNumber, "casino_wins")
        self.player_score = self.findChild(QLCDNumber, "player_wins")
        self.player_balance = self.findChild(QLCDNumber, "player_balance")
        
        self.player_by_1 = self.findChild(QRadioButton, "player_by_1")
        self.player_by_2 = self.findChild(QRadioButton, "player_by_2")
        self.player_by_3 = self.findChild(QRadioButton, "player_by_3")
        self.player_by_4 = self.findChild(QRadioButton, "player_by_4")
        self.player_by_5 = self.findChild(QRadioButton, "player_by_5")
        self.player_by_6 = self.findChild(QRadioButton, "player_by_6")
        
        self.dealer_by_1 = self.findChild(QRadioButton, "dealer_by_1")
        self.dealer_by_2 = self.findChild(QRadioButton, "dealer_by_2")
        self.dealer_by_3 = self.findChild(QRadioButton, "dealer_by_3")
        self.dealer_by_4 = self.findChild(QRadioButton, "dealer_by_4")
        self.dealer_by_5 = self.findChild(QRadioButton, "dealer_by_5")
        self.dealer_by_6 = self.findChild(QRadioButton, "dealer_by_6")
        
        self.tie = self.findChild(QRadioButton, "tie")
        
        self.bet_size = self.findChild(QLineEdit, "betsize")
        self.bet_size.setPlaceholderText('Type in Bet Here')
        
        global player_balance
        player_balance = 100
        onlyInt = QIntValidator()
        self.player_balance.display(player_balance)
        onlyInt.setRange(0, 100)
        self.bet_size.setValidator(onlyInt)
        
        
        
        #click buttons
        self.deal_button.clicked.connect(self.deal)
        self.next_button.clicked.connect(self.next_)
        self.bet_button.clicked.connect(self.bet)
        
        
        
        
        #show the app
        self.show()
        
    def get_png(self, card):
        suits_dict = {'♠': 'spades', '♥': 'hearts', '♦': 'diamonds', '♣': 'clubs' }    
        nums_dict =  {2: 2, 3: 3, 4: 4, 5: 5, 6: 6,
                      7: 7, 8: 8, 9: 9, 10: 10, 'J': 'jack', 
                      'Q': 'queen', 'K': 'king', 'A': 'ace'}
        
        return '{}_of_{}.png'.format(nums_dict[card[0]], suits_dict[card[1]])
        
    def deal(self):
        global player_balance
        if player_balance > 0:
            hierarchy_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
            suits = ['♠', '♦', '♥', '♣']
            cards = [(x,y) for x in hierarchy_values for y in suits]
            random.shuffle(cards)
            self.setWindowTitle("Make your bets!")
            self.win_loss_banner.setText('Paytable reflects a $5 wager')
            global ordered_player_payouts
            ordered_player_payouts = [self.player_by_6, self.player_by_5, self.player_by_4, self.player_by_3,
                                      self.player_by_2, self.player_by_1, self.tie, self.dealer_by_1, 
                                      self.dealer_by_2,self.dealer_by_3, self.dealer_by_4, self.dealer_by_5, 
                                      self.dealer_by_6]


            self.bet_button.setEnabled(True)
            for button in ordered_player_payouts:
                button.setCheckable(True)

            dealt_cards = []
            for i in range(7):
                dealt_cards.append(cards.pop(0))
            global dealer_hand 
            dealer_hand = evaluate_seven(dealt_cards)

            global player_cards
            player_cards = []
            for j in range(8):
                player_cards.append(cards[7*j: 7 * (j+1)])


            global hands_dealt
            hands_dealt = 0

            global dealer_wins
            global player_wins

            dealer_wins = 0
            player_wins = 0

            self.casino_score.display(dealer_wins)
            self.player_score.display(player_wins)


            self.dealer_top_1_label.setPixmap(QPixmap(f'images/{self.get_png(dealer_hand[1][0])}'))
            self.dealer_top_2_label.setPixmap(QPixmap(f'images/{self.get_png(dealer_hand[1][1])}'))

            self.dealer_bottom_1_label.setPixmap(QPixmap(f'images/{self.get_png(dealer_hand[0][0])}'))
            self.dealer_bottom_2_label.setPixmap(QPixmap(f'images/{self.get_png(dealer_hand[0][1])}'))
            self.dealer_bottom_3_label.setPixmap(QPixmap(f'images/{self.get_png(dealer_hand[0][2])}'))
            self.dealer_bottom_4_label.setPixmap(QPixmap(f'images/{self.get_png(dealer_hand[0][3])}'))
            self.dealer_bottom_5_label.setPixmap(QPixmap(f'images/{self.get_png(dealer_hand[0][4])}'))

            self.player_top_1_label.setPixmap(QPixmap(f'images/back.png'))
            self.player_top_2_label.setPixmap(QPixmap(f'images/back.png'))

            self.player_bottom_1_label.setPixmap(QPixmap(f'images/back.png'))
            self.player_bottom_2_label.setPixmap(QPixmap(f'images/back.png'))
            self.player_bottom_3_label.setPixmap(QPixmap(f'images/back.png'))
            self.player_bottom_4_label.setPixmap(QPixmap(f'images/back.png'))
            self.player_bottom_5_label.setPixmap(QPixmap(f'images/back.png'))


            global payouts 
            payouts = get_payouts(dealt_cards)
            self.payout_player_6.setText(str(payouts[1][0]))
            self.payout_player_5.setText(str(payouts[1][1]))
            self.payout_player_4.setText(str(payouts[1][2]))
            self.payout_player_3.setText(str(payouts[1][3]))
            self.payout_player_2.setText(str(payouts[1][4]))
            self.payout_player_1.setText(str(payouts[1][5]))

            self.payout_dealer_6.setText(str(payouts[1][12]))
            self.payout_dealer_5.setText(str(payouts[1][11]))
            self.payout_dealer_4.setText(str(payouts[1][10]))
            self.payout_dealer_3.setText(str(payouts[1][9]))
            self.payout_dealer_2.setText(str(payouts[1][8]))
            self.payout_dealer_1.setText(str(payouts[1][7]))

            self.payout_tie.setText(str(payouts[1][6]))
        else:
            self.setWindowTitle("No Money, No BacGow")
        
    def bet(self):
        
        global hands_dealt
        global player_balance
        global payouts
        global selection
        global player_prediction
        selection = []
        
        if hands_dealt == 0:
            global ordered_player_payouts


            onlyInt = QIntValidator()
            onlyInt.setRange(0, player_balance)
            self.bet_size.setValidator(onlyInt)
            player_balance -= int(self.bet_size.text())
            self.player_balance.display(player_balance)
            for button in ordered_player_payouts:
                #button.setCheckable(False)
                if button.isChecked():
                    selection.append(1)
                else:
                    selection.append(0)
            print(selection)
            print(ordered_player_payouts[selection.index(1)])
            self.bet_button.setEnabled(False)
            
            player_prediction = list(range(-6,7))[selection.index(1)]
            
            
            
        else:
            pass
        
        
    def next_(self):
        
        global player_cards
        global hands_dealt
        global dealer_wins
        global player_wins
        global dealer_hand
        global player_prediction
        global payouts
        global player_balance

        self.setWindowTitle("next card")
        
        
        if hands_dealt < 6:
            self.setWindowTitle("Hand " + str(9 - len(player_cards)))
            
            curr_hand = player_cards.pop(0)
            
            player_hand = best_hand_against_dealer(dealer_hand[0], dealer_hand[1], curr_hand)
            hand_score = face_dealer(dealer_hand[0], dealer_hand[1], curr_hand)

            self.player_top_1_label.setPixmap(QPixmap(f'images/{self.get_png(player_hand[1][0])}'))
            self.player_top_2_label.setPixmap(QPixmap(f'images/{self.get_png(player_hand[1][1])}'))

            self.player_bottom_1_label.setPixmap(QPixmap(f'images/{self.get_png(player_hand[0][0])}'))
            self.player_bottom_2_label.setPixmap(QPixmap(f'images/{self.get_png(player_hand[0][1])}'))
            self.player_bottom_3_label.setPixmap(QPixmap(f'images/{self.get_png(player_hand[0][2])}'))
            self.player_bottom_4_label.setPixmap(QPixmap(f'images/{self.get_png(player_hand[0][3])}'))
            self.player_bottom_5_label.setPixmap(QPixmap(f'images/{self.get_png(player_hand[0][4])}'))
            hands_dealt +=1
            
            
            if hand_score == 2:
                player_wins +=1
            elif hand_score == 0:
                dealer_wins += 1
            
            self.casino_score.display(dealer_wins)
            self.player_score.display(player_wins)
        
        else:
            self.setWindowTitle("Out of cards! Hit the deal button to start a new round!")
            if dealer_wins - player_wins == player_prediction:
                player_balance += bet_size * payouts[player_prediction] / 5
                self.win_loss_banner.setText('Congrats! You won $' +str(bet_size * payouts[player_prediction] / 5))
            else:
                self.win_loss_banner.setText('Better luck next time...')
                



        
        
UI.evaluate_seven = evaluate_seven   
UI.face_dealer = face_dealer
UI.best_hand_against_dealer = best_hand_against_dealer
UI.get_payouts = get_payouts
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()


