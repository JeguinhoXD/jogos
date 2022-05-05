class Personagem:
  def __init__(self, name, hp, atk, defs): #self representa a Classe "Personagem". Os demais são parametros de entrada
    self.name = name #Como se estivessemos criando uma nova váriavel dentro do self, ou seja, deste personagem em si.
    self.hp = hp
    self.atk = atk
    self.defs = defs

def Attack(attacker, defender):
  defender.hp -= attacker.atk
  print(attacker.name + " atingiu " + defender.name + " com um golpe de: " + str(attacker.atk) + 
        " de poder! \n" + defender.name + " tem agora " + str(defender.hp) + " de vida \n")

hero = Personagem("Gustavo", 45, 9, 34)
vilain = Personagem("thanos", 50, 35, 31)


while hero.hp > 0 and vilain.hp > 0:
  Attack(hero, vilain)
  if vilain.hp <= 0:
    break
  Attack(vilain, hero)
