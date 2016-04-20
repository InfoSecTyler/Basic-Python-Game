'''
Created by: Tyler Linne
Coded in part as a Treehouse Project
Date: 4-20-16
'''

import random


class Combat:
  dodge_limit = 6
  attack_limit = 6
  
  def dodge(self):
    roll = random.randint(1, self.dodge_limit)
    if roll > 9:
      print("LIMIT BREAK!")
    return roll > 4
  
  def attack(self):
    roll = random.randint(1, self.attack_limit)
    if roll > 9:
      print("LIMIT BREAK!")
    return roll > 4
