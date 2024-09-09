#Enums
from enum import Enum

class State(Enum): #State word can be any word we use
  INACTIVE = 0
  ACTIVE = 1

print(State.ACTIVE)
print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'])

print(list(State)) #list the values of the State

print(len(State))