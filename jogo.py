import random

class Personagem():
  def __init__(self, n, hp, spells):
    self.name = n
    self.health = hp
    self.spells = spells

class Spell():
  def __init__(self, n, dmg):
    self.name = n
    self.damage = dmg

def CastSpell(attacker, defender):
  rSpellIndex = random.randint(0, len(attacker.spells)-1) #Randomiza um valor de 0 até o tamanho da lista
  spell = attacker.spells[rSpellIndex] #Pega a spell da lista, baseado no valor randomizado

  print(attacker.name + " usou a habilidade: " + spell.name)

  defender.health -= spell.damage #Remove o dano da spell da vida do personagem

  print(defender.name + " foi atingido com " + str(spell.damage) + " de dano")
  print(defender.name + " está agora com " + str(defender.health) + " de vida")


heroSpells = [Spell("choque fantasmagorico", 100), Spell("trindade onipotente", 800), Spell("choque fantasmagorico", 100)]
enemySpells = [Spell("golpe fantastico", 100), Spell("destruidor de almas",200), Spell("ataque especial",250)]

hero = Personagem("Jethacu", 1000, heroSpells)
enemy = Personagem("noiado", 30, enemySpells)


while(hero.health > 0 and enemy.health > 0):
  print("")
  CastSpell(hero, enemy)
  if(enemy.health <= 0): break
  print("")
  CastSpell(enemy, hero)
