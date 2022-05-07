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
  rSpellIndex = random.randint(0, len(attacker.spells)-1) >
  spell = attacker.spells[rSpellIndex] #Pega a spell da li>

  print(attacker.name + " usou a habilidade: " + spell.nam>

  defender.health -= spell.damage #Remove o dano da spell >

  print(defender.name + " foi atingido com " + str(spell.d>
  print(defender.name + " está agora com " + str(defender.>


heroSpells = [Spell("choque fantasmagorico", 100), Spell(">
enemySpells = [Spell("golpe fantastico", 100), Spell("dest>
