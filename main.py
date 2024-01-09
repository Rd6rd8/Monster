import certifi
from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField
from kivymd.uix.selectioncontrol import MDCheckbox
import threading
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition, NoTransition
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDIconButton,MDRectangleFlatButton,MDRoundFlatIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.metrics import dp, sp
from kivy.properties import ObjectProperty,ListProperty
from datetime import datetime
import os
import json
import random

def find_key_by_value(dictionary, target_value):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            nested_result = find_key_by_value(value, target_value)
            if nested_result is not None:
                return key
        elif value == target_value:
            return key
    return None
def error (self,text,title):
        dialog = MDDialog(
            title=  title,
            text= text,
            buttons=[ 
            MDRectangleFlatButton(
            text= "[color=ffffff][b]Okay[/b][/color]",
         on_release=lambda instance: dialog.dismiss()  ,
            font_size = '18sp',
            md_bg_color= (33/255,150/255,243/255,1))
            ]
        )
        dialog.open()

def coin (self,value):
    custom = '/storage/emulated/0/.Monster : NewCard/Game Data/Monstercarddata.rd6p'
    with open(custom, 'r') as file:
        data = json.load(file)
        if data:
            coin = data.get('Rohit',int(00))
            diamond = data.get('Shubham',int(00))
            rank = data.get('Suraj',int(00))
            ranks=decode(rank)
            diamonds=decode(diamond)
            coins = decode(coin)
            if value =='detail':
                self.manager.get_screen(value).ids.coin_label.text = f'  {str(coins)}'
                self.manager.get_screen(value).ids.diamond_label.text = f'  {str(diamonds)}'
            elif value =='odetail':
                self.manager.get_screen(value).ids.coin_label.text = f'  {str(coins)}'
                self.manager.get_screen(value).ids.diamond_label.text = f'  {str(diamonds)}'
            elif value =='other':
                self.manager.get_screen(value).ids.coin_label.text = f'  {str(coins)}'
                self.manager.get_screen(value).ids.diamond_label.text = f'  {str(diamonds)}'
            elif value =='itemdetail':
                self.manager.get_screen(value).ids.coin_label.text = f'  {str(coins)}'
                self.manager.get_screen(value).ids.diamond_label.text = f'  {str(diamonds)}'
            else:
                self.manager.get_screen(value).ids.coin_label.text = str(coins)
                self.manager.get_screen(value).ids.diamond_label.text = str(diamonds)

my_list = ['+#!', '#/!', '*?!', '#_!', '*!', '&!', '?!', '%@!', '@*!', '@?!']

def encode(value):
    try:
        user_input = value

        new_list = []
        for digit in user_input:
            index = int(digit)
            if 0 <= index < len(my_list):
                new_list.append(my_list[index])
        separators = ['@#', '(@)']
        separator_list = [random.choice(separators) for _ in range(len(new_list) - 1)]
        joined_list = ''.join(item + sep for item, sep in zip(new_list, separator_list)) + new_list[-1]
        return joined_list
    except Exception as e:
        return f"Encoding Error: {str(e)}"
def decode(jned_list):
    joined_list = str(jned_list)
    separated_items = joined_list.split('@#')
    separated_items = [item.split('(@)') for item in separated_items]
    replaced_list = []
    for items in separated_items:
        for item in items:
            index = my_list.index(item)
            replaced_list.append(str(index))
    num_value = int("".join(replaced_list))
    return num_value
    

class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = FadeTransition(duration=1)

    def switch_screen(self, name):
        if self.current == 'first':
            self.transition = FadeTransition(duration=1)
        else:
            self.transition = NoTransition()
        self.current = name
class MonsterApp(MDApp):
    my_dict = {
  "Volter": {
    "type": "Electric",
    "price": "15000/1500",
    "attacks": ["Thunderbolt", "Quick Attack", "Iron Tail", "Volt Tackle", "Thunder Punch", "Thunder Wave", "Shock Wave", "Thunder Shock", "Thunder Fang", "Thunder Clap", "Charge Beam", "Thunder", "Zap Cannon", "Wild Charge", "Thunderstorm", "Electro Ball", "Bolt Strike", "Spark", "Discharge", "Lightning Strike", "Thunderstrike"],
    "code": "123456",
    "rank": [55, 72, 80, 92, 105, 120, 125, 130, 150, 160, 167, 175, 180, 198, 200],
    "level": 48
  },
  "Volteron": {
    "type": "Electric",
    "price": "16000/1600",
    "attacks": ["Thunderbolt", "Quick Attack", "Thunder Punch", "Volt Tackle", "Thunder", "Agility", "Charge Beam", "Thunder Wave", "Thunder Shock", "Zap Cannon", "Wild Charge", "Shock Wave", "Thunder Fang", "Thunder Clap", "Thunderstorm", "Electro Ball", "Bolt Strike", "Spark", "Discharge", "Lightning Strike", "Thunderstrike"],
    "code": "185456",
    "rank": [50, 60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 135, 140, 150, 160, 170, 180, 190, 200],
    "level": 53
  },
  "Rianchi": {
    "type": "Fighting",
    "price": "3500/350",
    "attacks": ["Attack", "Force Palm", "Blaze Kick", "Aura Sphere", "Extreme Speed", "Power-Up Punch", "Brick Break", "Counter", "High Jump Kick", "Dynamic Punch", "Circle Throw", "Superpower", "Karate Chop", "Vital Throw", "Revenge", "Submission", "Double Kick", "Mega Punch", "Mach Punch", "Strength", "Cross Chop", "Smelling Salt", "Focus Punch"],
    "code": "193456",
    "rank": [55, 60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 130, 135, 140, 150, 160, 175, 185, 190, 200],
    "level": 42
  },
"Recomer": {
    "type": "Steel",
    "price": "5500/550",
    "attacks": ["Force Palm", "Close Combat", "Dragon Pulse", "Flash Cannon", "Aura Sphere", "Power-Up Punch", "Metal Claw", "Iron Head", "Metal Burst", "Gyro Ball", "Heavy Slam", "Meteor Mash", "Comet Punch", "Bullet Punch", "Meteor Hammer", "Dynamic Punch", "Mach Punch", "Bullet Seed", "Seed Bomb", "Frenzy Plant", "Petal Blizzard", "Solar Beam", "Vine Whip", "Razor Leaf"],
    "code": "123356",
    "rank": [55, 65, 70, 75, 80, 90, 100, 105, 120, 125, 130, 135, 140, 140, 150, 160, 160, 165, 175, 180, 200],
    "level": 58
  },
  "Silpander": {
    "type": "Fire",
    "price": "2000/200",
    "attacks": ["Ember", "Flamethrower", "Fire Spin", "Fire Blast", "Inferno", "Heat Wave", "Lava Plume", "Eruption", "Mystical Fire", "Flare Blitz", "Blaze Kick", "Fire Pledge", "Overheat", "Flame Charge", "Flame Wheel", "Will-O-Wisp", "Sacred Fire", "Burn Up", "Sunny Day", "Fire Fang", "Fire Lash", "Fire Punch", "Firespin", "Blast Burn"],
    "code": "123656",
    "rank": [50, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 130, 140, 150, 160, 170, 180, 200],
    "level": 43
  },
  "Ustomenger": {
    "type": "Fire",
    "price": "4000/400",
    "attacks": ["Flamethrower", "Dragon Claw", "Earthquake", "Fire Blast", "Air Slash", "Wing Attack", "Air Cutter", "Sky Attack", "Hurricane", "Aerial Ace", "Twister", "Acrobatics", "Roost", "Steel Wing", "Brave Bird", "Punishment", "Mirror Move", "Fly", "Sky Drop", "Defog", "Peck", "Drill Peck", "Pluck", "Peck"],
    "code": "123956",
    "rank": [60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 155, 160, 180, 200],
    "level": 52
  },
"Vitti": {
    "type": "Grass",
    "price": "2000/200",
    "attacks": ["Tackle", "Vine Whip", "Razor Leaf", "Solar Beam", "Absorb", "Energy Ball", "Giga Drain", "Leaf Storm", "Frenzy Plant", "Leech Seed", "Bullet Seed", "Seed Bomb", "Synthesis", "Leaf Tornado", "Leaf Blade", "Grass Knot", "Solar Blade", "Mega Drain", "Power Whip", "Leafage", "Cotton Spore", "Cotton Guard", "Cotton Spore", "Cotton Guard"],
    "code": "190456",
    "rank": [60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 200],
    "level": 46
  },
  "Brutesaur": {
    "type": "Grass",
    "price": "4000/400",
    "attacks": ["Vine Whip", "Razor Leaf", "Solar Beam", "Sludge Bomb", "Earthquake", "Hyper Beam", "Giga Drain", "Seed Bomb", "Leaf Tornado", "Leech Seed", "Mega Drain", "Frenzy Plant", "Leaf Storm", "Leaf Blade", "Grass Knot", "Solar Blade", "Bullet Seed", "Synthesis", "Cotton Spore", "Cotton Guard", "Power Whip", "Leafage", "Cotton Spore", "Cotton Guard"],
    "code": "124456",
    "rank": [60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 200],
    "level": 55
  },
    "Durny": {
    "type": "Water",
    "price": "1600/160",
    "attacks": ["Tackle", "Water Gun", "Surf", "Hydro Pump", "Bite", "Aqua Jet", "Aqua Tail", "Muddy Water", "Soak", "Scald", "Bubble Beam", "Water Pulse", "Brine", "Aqua Ring", "Rain Dance", "Aqua Ring", "Water Sport", "Toxic", "Whirlpool", "Water Gun", "Waterfall", "Dive", "Whirlpool", "Water Gun"],
    "code": "103456",
    "rank": [50, 60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 130, 135, 140, 150, 160, 170, 180, 200],
    "level": 57
  },
  "Deadmine": {
    "type": "Water",
    "price": "2500/250",
    "attacks": ["Water Gun", "Surf", "Hydro Pump", "Ice Beam", "Blizzard", "Bite", "Aqua Jet", "Aqua Tail", "Muddy Water", "Soak", "Scald", "Bubble Beam", "Water Pulse", "Brine", "Aqua Ring", "Rain Dance", "Aqua Ring", "Water Sport", "Toxic", "Whirlpool", "Water Gun", "Waterfall", "Dive", "Whirlpool", "Water Gun"],
    "code": "127456",
    "rank": [60, 75, 80, 85, 90, 95, 100, 105, 110, 120, 130, 140, 150, 160, 170, 180, 200, 250],
    "level": 48
  },
  "Blaster": {
    "type": "Water",
    "price": "5500/550",
    "attacks": ["Water Gun", "Hydro Pump", "Ice Beam", "Blizzard", "Earthquake", "Hyper Beam", "Flash Cannon", "Magnet Bomb", "Metal Sound", "Mirror Shot", "Lock-On", "Zap Cannon", "Metal Burst", "Gyro Ball", "Shift Gear", "Gear Grind", "Recycle", "Discharge", "Sonic Boom", "Spark", "Thunder", "Charge Beam", "Magnet Rise", "Electric Terrain", "Parabolic Charge"],
    "code": "100456",
    "rank": [60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 140, 150, 160, 170, 180, 200],
    "level": 42
  },
  "Omit": {
    "type": "Stone",
    "price": "1600/160",
    "attacks": ["Rock Throw", "Earthquake", "Stone Edge", "Iron Tail", "Smack Down", "Stone Edge", "Rock Slide", "Rock Blast", "Rock Tomb", "Rock Wrecker", "Wide Guard", "Power Gem", "Meteor Mash", "Ancient Power", "Head Smash", "Diamond Storm", "Stone Edge", "Rock Slide", "Smack Down", "Rock Blast", "Rock Tomb", "Rock Wrecker", "Wide Guard", "Power Gem", "Meteor Mash"],
    "code": "103056",
    "rank": [60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 130, 135, 140, 150, 160, 170, 180, 200],
    "level": 53
  },
  "Rhidon": {
    "type": "Stone",
    "price": "2800/280",
    "attacks": ["Mud-Slap", "Stone Edge", "Earthquake", "Megahorn", "Rock Slide", "Avalanche", "Stone Edge", "Rock Blast", "Rock Tomb", "Rock Wrecker", "Wide Guard", "Power Gem", "Meteor Mash", "Ancient Power", "Head Smash", "Diamond Storm", "Mud-Slap", "Stone Edge", "Rock Slide", "Smack Down", "Rock Blast", "Rock Tomb", "Rock Wrecker", "Wide Guard", "Power Gem", "Meteor Mash"],
    "code": "103406",
    "rank": [50, 55, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 130, 135, 140, 150, 160, 170, 180, 190],
    "level": 59
  },
  "Ridamon": {
    "type": "Dragon",
    "price": "6000/600",
    "attacks": ["Dragon Tail", "Crunch", "Stone Edge", "Iron Tail", "Earthquake", "Heavy Slam", "Meteor Mash", "Bullet Punch", "Dragon Claw", "Iron Head", "Flash Cannon", "Gyro Ball", "Zap Cannon", "Lock-On", "Metal Burst", "Mirror Shot", "Metal Sound", "Flash Cannon", "Magnet Bomb", "Hyper Beam", "Tri Attack", "Charge Beam", "Metal Sound", "Mirror Shot", "Lock-On"],
    "code": "103450",
    "rank": [55, 60, 75, 80, 90, 95, 100, 105, 110, 115, 120, 130, 135, 140, 150, 160, 170, 175, 180, 190, 200],
    "level": 44
  },
"Flystuck": {
    "type": "Air",
    "price": "1700/170",
    "attacks": ["Air Slash", "Solar Beam", "Leaf Blade", "Razor Leaf", "Hurricane", "Tailwind", "Sky Attack", "Sky Drop", "Defog", "Peck", "Drill Peck", "Pluck", "Pluck", "Brave Bird", "Acrobatics", "Roost", "Punishment", "Mirror Move", "Fly", "Sky Drop", "Air Cutter", "Wing Attack", "Fly", "Twister", "Aerial Ace", "Astonish"],
    "code": "101456",
    "rank": [50, 60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 150, 160, 165, 170, 190, 200],
    "level": 55
  },
  "Airone": {
    "type": "Grass",
    "price": "2400/240",
    "attacks": ["Razor Leaf", "Leaf Storm", "Giga Drain", "Hydro Pump", "Solar Beam", "Leech Seed", "Bullet Seed", "Seed Bomb", "Frenzy Plant", "Leaf Tornado", "Leaf Blade", "Grass Knot", "Solar Blade", "Synthesis", "Cotton Spore", "Cotton Guard", "Power Whip", "Leafage", "Cotton Spore", "Cotton Guard", "Cotton Spore", "Cotton Guard", "Leafage", "Cotton Spore"],
    "code": "103426",
    "rank": [55, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200],
    "level": 42
  },
  "Dronestar": {
    "type": "Water",
    "price": "5000/500",
    "attacks": ["Aqua Tail", "Blizzard", "Surf", "Hydro Pump", "Leaf Blade", "Razor Leaf", "Ice Beam", "Hyper Beam", "Solar Beam", "Aqua Jet", "Hydro Cannon", "Muddy Water", "Water Pulse", "Aqua Ring", "Rain Dance", "Aqua Ring", "Water Sport", "Toxic", "Whirlpool", "Water Gun", "Waterfall", "Dive", "Whirlpool", "Water Gun"],
    "code": "103556",
    "rank": [60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200],
    "level": 46
  },
  "Monkar": {
    "type": "Fighting",
    "price": "2000/200",
    "attacks": ["Astonish", "Brick Break", "Mud Bomb", "Dynamic Punch", "Cross Chop", "Low Kick", "Karate Chop", "Focus Energy", "Seismic Toss", "Vital Throw", "Wake-Up Slap", "Foresight", "Revenge", "Submission", "Double Kick", "Mega Punch", "Counter", "Mega Kick", "Heavy Slam", "Focus Punch", "Drain Punch", "High Jump Kick", "Smelling Salt", "Rolling Kick", "Comet Punch"],
    "code": "103356",
    "rank": [60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200],
    "level": 58
  },
  "Connie": {
    "type": "Poison",
    "price": "4000/400",
    "attacks": ["Poison Jab", "Sludge Bomb", "Dynamic Punch", "Mud Bomb", "Brick Break", "Fighting-type", "Drain Punch", "High Jump Kick", "Smelling Salt", "Rolling Kick", "Comet Punch", "Bullet Punch", "Mach Punch", "Karate Chop", "Double Kick", "Mega Punch", "Counter", "Revenge", "Foresight", "Vital Throw", "Wake-Up Slap", "Seismic Toss", "Focus Energy", "Cross Chop", "Low Kick", "Triple Kick"],
    "code": "104456",
    "rank": [60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200],
    "level": 49
  },
  "Enic": {
    "type": "Grass",
    "price": "1800/180",
    "attacks": ["Quick Attack", "Pound", "Absorb", "Energy Ball", "Leech Seed", "Mega Drain", "Bullet Seed", "Solar Blade", "Seed Bomb", "Frenzy Plant", "Leaf Tornado", "Leaf Blade", "Grass Knot", "Solar Blade", "Synthesis", "Cotton Spore", "Cotton Guard", "Power Whip", "Leafage", "Cotton Spore", "Cotton Guard", "Cotton Spore", "Cotton Guard", "Leafage", "Cotton Spore"],
    "code": "109456",
    "rank": [60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200],
    "level": 57
  },
  "Eniger": {
    "type": "Grass",
    "price": "2500/250",
    "attacks": ["Bullet Seed", "Energy Ball", "Leaf Blade", "Leaf Storm", "Frenzy Plant", "Energy Ball", "Solar Blade", "Synthesis", "Cotton Spore", "Cotton Guard", "Power Whip", "Leafage", "Cotton Spore", "Cotton Guard", "Cotton Spore", "Cotton Guard", "Leafage", "Cotton Spore", "Cotton Guard", "Cotton Spore", "Cotton Guard", "Leafage", "Cotton Spore", "Cotton Guard"],
    "code": "903456",
    "rank": [60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200],
    "level": 53
  },
  "Endiron": {
    "type": "Grass",
    "price": "6000/600",
    "attacks": ["Leaf Blade", "Solar Beam", "Frenzy Plant", "Energy Ball", "Dragon Pulse", "Earthquake", "Heavy Slam", "Meteor Mash", "Bullet Punch", "Iron Head", "Metal Burst", "Gyro Ball", "Flash Cannon", "Lock-On", "Zap Cannon", "Mirror Shot", "Metal Sound", "Metal Burst", "Hyper Beam", "Tri Attack", "Charge Beam", "Metal Sound", "Mirror Shot", "Lock-On", "Flash Cannon"],
    "code": "103156",
    "rank": [60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200],
    "level": 44
  },
  "Jueter": {
    "type": "Normal",
    "price": "2000/200",
    "attacks": ["Lick", "Headbutt", "Body Slam", "Zen Headbutt", "Psyshock", "Extrasensory", "Psybeam", "Future Sight", "Telekinesis", "Miracle Eye", "Disarming Voice", "Stored Power", "Synchronoise", "Psycho Cut", "Zen Headbutt", "Headbutt", "Iron Tail", "Tackle", "Take Down", "Double-Edge", "Giga Impact", "Rollout", "Zen Headbutt", "Headbutt", "Iron Tail"],
    "code": "100406",
    "rank": [60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200],
    "level": 60
  },
  "Spiker": {
    "type": "Normal",
    "price": "2900/290",
    "attacks": ["Scratch", "Tackle", "Pound", "Hyper Beam", "Shadow Claw", "Dark Pulse", "Payback", "Foul Play", "Thief", "Snatch", "Torment", "Embargo", "Punishment", "Taunt", "Dark Pulse", "Hone Claws", "Bite", "Sucker Punch", "Crunch", "Pursuit", "Punishment", "Thief", "Nasty Plot", "Memento"],
    "code": "103759",
    "rank": [60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200],
    "level": 47
  },
  "Jushteron": {
    "type": "Normal",
    "price": "6000/600",
    "attacks": ["Lick", "Headbutt", "Hyper Beam", "Psychic", "Giga Impact", "Rollout", "Zen Headbutt", "Rock Slide", "Rock Tomb", "Rock Blast", "Rock Polish", "Stealth Rock", "Head Smash", "Power Gem", "Rock Climb", "Wide Guard", "Metal Sound", "Meteor Beam", "Meteor Mash", "ice Crash", "Ice Spear", "Ice Shard", "Ice Fang"],
    "code": "100400",
    "rank": [55, 60, 65, 70, 72, 80, 90, 92, 105, 120, 130, 140, 150, 160, 167, 175, 180, 190, 198, 200],
    "level": 56
  },
"MegaEndiron": {
        "type": "Grass", 'price': '16000/1600', "code": "103756",
        "attacks": ["Leaf Blade", "Solar Beam", "Frenzy Plant", "Energy Ball", "Dragon Pulse", "Earthquake", "Heavy Slam", "Meteor Mash", "Bullet Punch", "Iron Head", "Metal Burst", "Gyro Ball", "Flash Cannon", "Lock-On", "Zap Cannon", "Mirror Shot", "Metal Sound", "Metal Burst", "Hyper Beam", "Tri Attack", "Charge Beam", "Metal Sound", "Mirror Shot", "Lock-On", "Flash Cannon"],
        "rank": [60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200],
        "level": 40
    },
    "MegaRidamon": {
        "type": "Dragon", 'price': '15000/1500', "code": "103459",
        "attacks": ["Dragon Tail", "Crunch", "Stone Edge", "Iron Tail", "Earthquake", "Heavy Slam", "Meteor Mash", "Bullet Punch", "Dragon Claw", "Iron Head", "Flash Cannon", "Gyro Ball", "Zap Cannon", "Lock-On", "Metal Burst", "Mirror Shot", "Metal Sound", "Flash Cannon", "Magnet Bomb", "Hyper Beam", "Tri Attack", "Charge Beam", "Metal Sound", "Mirror Shot", "Lock-On"],
        "rank": [55, 60, 75, 80, 90, 95, 100, 105, 110, 115, 120, 130, 135, 140, 150, 160, 170, 175, 180, 190, 200],
        "level": 50
    },
    "MegaRecomer": {
        "type": "Steel", 'price': '16000/1600', "code": "100000",
        "attacks": ["Force Palm", "Close Combat", "Dragon Pulse", "Flash Cannon", "Aura Sphere", "Power-Up Punch", "Metal Claw", "Iron Head", "Metal Burst", "Gyro Ball", "Heavy Slam", "Meteor Mash", "Comet Punch", "Bullet Punch", "Meteor Hammer", "Dynamic Punch", "Mach Punch", "Bullet Seed", "Seed Bomb", "Frenzy Plant", "Petal Blizzard", "Solar Beam", "Vine Whip", "Razor Leaf"],
        "rank": [55, 65, 70, 75, 80, 90, 100, 105, 120, 125, 130, 135, 140, 140, 150, 160, 160, 165, 175, 180, 200],
        "level": 60
    },
    "MegaDronestar": {
        "type": "Water", 'price': '18000/1800', "code": "109496",
        "attacks": ["Aqua Tail", "Blizzard", "Surf", "Hydro Pump", "Leaf Blade", "Razor Leaf", "Ice Beam", "Hyper Beam", "Solar Beam", "Aqua Jet", "Hydro Cannon", "Muddy Water", "Water Pulse", "Aqua Ring", "Rain Dance", "Aqua Ring", "Water Sport", "Toxic", "Whirlpool", "Water Gun", "Waterfall", "Dive", "Whirlpool", "Water Gun"],
        "rank": [60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200],
        "level": 40
    },
    "MegaJushteron": {
        "type": "Normal", 'price': '14000/1400', "code": "108756",
        "attacks": ["Lick", "Headbutt", "Hyper Beam", "Psychic", "Giga Impact", "Rollout", "Zen Headbutt", "Rock Slide", "Rock Tomb", "Rock Blast", "Rock Polish", "Stealth Rock", "Head Smash", "Power Gem", "Rock Climb", "Wide Guard", "Metal Sound", "Meteor Beam", "Meteor Mash", "Ice Crash", "Ice Spear", "Ice Shard", "Ice Fang"],
        "rank": [55, 60, 70, 80, 85, 90, 95, 100, 105, 110, 115, 120, 130, 135, 140, 145, 150, 160, 165, 170, 175, 200],
        "level": 50
    },
  "GmaxVoltron": {
    "type": "Electric",
    "price": "18000/1800",
    "code": "103956",
    "attacks": ["Thunderbolt", "Quick Attack", "Iron Tail", "Volt Tackle", "Thunder Punch", "Thunder Wave", "Shock Wave", "Thunder Shock", "Thunder Fang", "Thunder Clap", "Charge Beam", "Thunder", "Zap Cannon", "Wild Charge", "Thunderstorm", "Electro Ball", "Bolt Strike", "Spark", "Discharge", "Lightning Strike", "Thunderstrike"],
    "rank": [55, 72, 80, 92, 105, 120, 125, 130, 150, 160, 167, 175, 180, 198, 200],
    "level": 41
  },
  "GmaxUstomenger": {
    "type": "Fire",
    "price": "15000/1500",
    "code": "103656",
    "attacks": ["Flamethrower", "Dragon Claw", "Earthquake", "Fire Blast", "Air Slash", "Wing Attack", "Air Cutter", "Sky Attack", "Hurricane", "Aerial Ace", "Twister", "Acrobatics", "Roost", "Steel Wing", "Brave Bird", "Punishment", "Mirror Move", "Fly", "Sky Drop", "Defog", "Drill Peck", "Pluck", "Peck"],
    "rank": [60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 155, 160, 180, 200],
    "level": 49
  },
  "GmaxBrutesaur": {
    "type": "Grass",
    "price": "14000/1400",
    "code": "109056",
    "attacks": ["Vine Whip", "Razor Leaf", "Solar Beam", "Sludge Bomb", "Earthquake", "Hyper Beam", "Giga Drain", "Seed Bomb", "Leaf Tornado", "Leech Seed", "Mega Drain", "Frenzy Plant", "Leaf Storm", "Leaf Blade", "Grass Knot", "Solar Blade", "Bullet Seed", "Synthesis", "Cotton Guard", "Cotton Spore", "Cotton Guard", "Cotton Spore", "Cotton Guard"],
    "rank": [55, 60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200],
    "level": 53
  },
  "GmaxConnie": {
    "type": "Steel",
    "price": "20000/2000",
    "code": "103406",
    "attacks": ["Metal Burst", "Mirror Shot", "Metal Sound", "Flash Cannon", "Steel Beam", "Iron Tail", "Metal Claw", "Iron Head", "Meteor Mash", "Bullet Punch", "Steel Wing", "Iron Defense", "Heavy Slam", "Meteor Hammer", "Iron Bash", "Metal Burst", "Metal Sound", "Mirror Shot", "Lock-On", "Flash Cannon", "Magnet Bomb", "Hyper Beam", "Tri Attack"],
    "rank": [55, 65, 75, 80, 90, 100, 105, 120, 125, 130, 140, 145, 150, 160, 170, 175, 180, 190, 195, 200],
    "level": 58
  },
  "GmaxBlaster": {
    "type": "Water",
    "price": "20000/2000",
    "code": "104056",
    "attacks": ["Hydro Pump", "Surf", "Aqua Tail", "Muddy Water", "Water Pulse", "Bubble Beam", "Brine", "Aqua Ring", "Rain Dance", "Toxic", "Whirlpool", "Waterfall", "Dive", "Aqua Jet", "Aqua Ring", "Water Sport", "Blizzard", "Ice Beam", "Ice Fang", "Ice Punch", "Ice Shard", "Icicle Spear", "Avalanche", "Frost Breath", "Freeze-Dry"],
    "rank": [60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 200],
    "level": 55
  },

    "Spark": {
        "description": "Use Spark to shake up your opponent's strategy. When you use Spark, your opponent's G-Max and M-Evolve Cards won't work, sending them away for a while, leaving your opponent in a bit of a fix.",
        "price": "8000/800",
        "code": "456789"
    },
    "Joto": {
        "description": "Joto gives your Monster Cards extra endurance. It cuts the damage they take in half when you're using it, making your Monster Cards a lot tougher in battles.",
        "price": "8500/850",
        "code": "567890"
    },
    "Mary": {
        "description": "Mary is a sneaky card. It forces your opponent to swap their Active Card, messing up their plans in battles and giving you an unexpected upper hand.",
        "price": "9000/900",
        "code": "678901"
    },
    "Adena": {
        "description": "Adena helps you peek at your opponent's Monster Card's health. This helps you understand your opponent's strengths and weaknesses in battles.",
        "price": "7000/700",
        "code": "789012"
    },
    "Kodar": {
        "description": "Kodar gives you a quick pause to think. You get 5 seconds to plan and make smarter moves in battles, giving you a valuable moment to come up with a winning strategy.",
        "price": "7500/750",
        "code": "890123"
    },
    "Maira": {
        "description": "Maira is a trickster card. It lets you cancel out your opponent's Ability Card, stopping them from using their current card abilities in battles and giving you an edge.",
        "price": "9000/900",
        "code": "901234"
    }}
                    
    card = {
    "Potion": {
        "description": "Potions are your Monster Cards' healing tools. When a Monster Card is too tired or damaged to keep battling, using a Potion restores its energy and health, getting it ready for another fight.",
        "price": "400/40",
        "code": "123456"
    },
    "Card Bag": {
        "description": "The Card Bag is like an extra closet for your Monster Cards. It allows you to keep more Monster Cards, so you can collect and save more of your favorites without worrying about running out of space.",
        "price": "200/20",
        "code": "234567"
    },
    "Item Bag": {
        "description": "The Item Bag helps you carry more stuff in your adventures. It's like a magical backpack that lets you store more items you find during the game - like extra energy boosts or helpful tools for battles.",
        "price": "100/10",
        "code": "345678"
    },
    "Fire Energy": {
        "description": "Fire Energy makes your Monster Cards stronger in battles. It helps them throw powerful fire attacks, making them extra hot and strong when they're in the fighting arena.",
        "price": "10/1",
        "code": "456789"
    },
    "Water Energy": {
        "description": "Water Energy gives your Monster Cards extra power in battles. It's like a blast of water power that helps them hit harder and smarter in a battle.",
        "price": "10/1",
        "code": "567890"
    },
    "Stone Energy": {
        "description": "Stone Energy toughens your Monster Cards, making their attacks rock-solid. It's like giving them super strength to deal heavy, powerful hits in battles.",
        "price": "10/1",
        "code": "678901"
    },
    "Steel Energy": {
        "description": "Steel Energy gives your Monster Cards a strong advantage in battles. It helps them attack more fiercely, like a tough shield making their moves more forceful.",
        "price": "10/1",
        "code": "789012"
    },
    "Grass Energy": {
        "description": "Grass Energy makes your Monster Cards extra strong in battles. It's like a shot of nature's power that helps them deliver strong attacks in battles.",
        "price": "10/1",
        "code": "890123"
    },
    "Air Energy": {
        "description": "Air Energy gives your Monster Cards the ability to launch powerful aerial attacks. They soar high, dealing strong blows to opponents in battles.",
        "price": "10/1",
        "code": "901234"
    },
    "Poison Energy": {
        "description": "Poison Energy helps your Monster Cards launch toxic attacks. It's like poisoning the opponent, making their attacks more venomous and dangerous in battles.",
        "price": "10/1",
        "code": "192345"
    },
    "Electric Energy": {
        "description": "Electric Energy electrifies your Monster Cards, giving them the power to shock opponents in battles. It's like a lightning strike, giving them shocking power.",
        "price": "10/1",
        "code": "127456"
    },
    "Fighting Energy": {
        "description": "Fighting Energy strengthens your Monster Cards' attack skills. It helps them land strong physical hits, making their attacks more powerful in battles.",
        "price": "10/1",
        "code": "234567"
    },
    "Dragon Energy": {
        "description": "Dragon Energy gives your Monster Cards the strength of dragons. It helps them unleash powerful dragon-type attacks, making them extremely fierce in battles.",
        "price": "10/1",
        "code": "345678"
    }
}
    type_icon_mapping = {
        "Fire" : "/storage/emulated/0/Monster _ New Card/Assests/Item/Fire Energy.png",
        'Water':"/storage/emulated/0/Monster _ New Card/Assests/Item/Water Energy.png",
        'Stone': "/storage/emulated/0/Monster _ New Card/Assests/Item/Stone Energy.png",
        'Steel':"/storage/emulated/0/Monster _ New Card/Assests/Item/Steel Energy.png",
        'Grass':"/storage/emulated/0/Monster _ New Card/Assests/Item/Grass Energy.png",
        'Air':"/storage/emulated/0/Monster _ New Card/Assests/Item/Air Energy.png",
        'Poison':"/storage/emulated/0/Monster _ New Card/Assests/Item/Poison Energy.png",
        'Electric':"/storage/emulated/0/Monster _ New Card/Assests/Item/Electric Energy.png",
        'Fighting':"/storage/emulated/0/Monster _ New Card/Assests/Item/Fighting Energy.png",
        'Dragon':"/storage/emulated/0/Monster _ New Card/Assests/Item/Dragon Energy.png"
        }
    coinrup = '10500'
    diamo = '300'
    def csub(self,num,value,*arg):
        custom = '/storage/emulated/0/.Monster : NewCard/Game Data/Monstercarddata.rd6p'
        title = arg[0]
        with open(custom, 'r') as file:
            data = json.load(file)
            if title in self.my_dict:
                code = self.my_dict[title]['code']
                en = encode(code)
                data['Rupee'].append(en)
                with open(custom, 'w') as file:
                    json.dump(data, file,indent = 2) 
            elif title in self.card:
                code = self.card[title]['code']
                en = encode(code)
                data['Dear'].append(en)
                with open(custom, 'w') as file:
                    json.dump(data, file,indent = 2) 
            if data:
                 coin = data.get('Rohit',int(00))
                 coinr= decode(coin)
                 coins = int(coinr)
            if coins >= num:
                newcoin = coins - num
                coinle = encode(str(newcoin))
                data['Rohit'] = coinle 
                with open(custom, 'w') as file:
                    json.dump(data, file,indent = 2)
                if value == 'detail':
                    self.strng.get_screen(value).ids.coin_label.text =f'  {str(newcoin)}'
                elif value == 'other':
                    self.strng.get_screen(value).ids.coin_label.text =f'  {str(newcoin)}'
                else:
                    self.strng.get_screen(value).ids.coin_label.text = str(newcoin)
                return error(self,'You have got a something in Bag','Successful')
            else :
                return error(self,'You have no enough money','Something went wrong')
            
                
            
    def dsub(self,num,value,*arg):
        custom = '/storage/emulated/0/.Monster : NewCard/Game Data/Monstercarddata.rd6p'
        title = arg[0]
        with open(custom, 'r') as file:
            data = json.load(file)
            if title in self.my_dict:
                code = self.my_dict[title]['code']
                en = encode(code)
                data['Rupee'].append(en)
                with open(custom, 'w') as file:
                    json.dump(data, file,indent = 2) 
            elif title in self.card:
                code = self.card[title]['code']
                en = encode(code)
                data['Dear'].append(en)
                with open(custom, 'w') as file:
                    json.dump(data, file,indent = 2) 
            if data:
                 coin = data.get('Shubham',int(00))
                 coinr= decode(coin)
                 coins = int(coinr)
            if coins >= num:
                newcoin = coins - num
                coinle = encode(str(newcoin))
                data['Shubham'] = coinle
                with open(custom, 'w') as file:
                    json.dump(data, file,indent = 2) 
                if value == 'detail':
                    self.strng.get_screen(value).ids.diamond_label.text =f'  {str(newcoin)}'
                    
                elif value == 'other':
                    self.strng.get_screen(value).ids.diamond_label.text =f'  {str(newcoin)}'
                else:
                     self.strng.get_screen(value).ids.diamond_label.text = str(newcoin)
                return error(self,'You have got a Monster Card','Successful')
                
                
            else :
                 return error(self,'You have no enough diamond','Something went wrong')
            
                
            

    def exit (self):
        exit()   
    def buyd(self, title):
        if title in self.card :
            s = self.card[title]['price']
            if '/' in s:
                t = s.split('/')
                self.coinrup = t[0]
                self.diamo = t[1]
        if title in self.my_dict :
            s = self.my_dict[title]['price']
            if '/' in s:
                t = s.split('/')
                self.coinrup = t[0]
                self.diamo = t[1]
            
        dbutton = MDRoundFlatIconButton(
            text= f'[color=ffffff][b] {self.diamo} [/b][/color]'
           , icon = "/storage/emulated/0/Monster _ New Card/Assests/Rdiamond.png"
        ,    icon_size ='22dp',
        on_press = lambda x: self.dsub(int(self.diamo),'store',title),
            font_size = '18sp',
            md_bg_color= (33/255,150/255,243/255,1))
        coinbutton = MDRoundFlatIconButton(
            text= f'[color=ffffff][b] {self.coinrup}[/b][/color]'
           , icon = "/storage/emulated/0/Monster _ New Card/Assests/Scoin.png"
        ,    icon_size ='22dp',
            font_size = '18sp',
            on_press = lambda x: self.csub(int(self.coinrup),'store',title),
            md_bg_color= (0.1294117647,0.5882352941,0.9529411765,1)) 
        dialog = MDDialog(
            title=title,
            text='By which way do you like',
            buttons=[coinbutton,
                MDIconButton(
                    icon ='close-circle',
                    on_release=lambda instance: dialog.dismiss()
                ),
                dbutton
            ]
        )
        dialog.open()
    def build(self):
        self.strng = Manager()        
        self.strng.add_widget(First(name='first'))      
        self.strng.add_widget(Check(name='check'))
        self.strng.add_widget(Load(name='load'))
        self.strng.add_widget(Signup(name='signup'))
        return self.strng
    def transition_to_detail(self, scren, image_source, card_name):
        try:
            detail_screen = self.root.get_screen(scren)
            detail_screen.details(image_source, card_name)
            self.root.current = scren
        except Exception as e:
            app = App.get_running_app()
            detail_screen = self.root.get_screen('itemdetail')
            detail_screen.details(image_source, card_name)
            self.root.current = 'itemdetail'  
    def change (self,screen):
        if screen == 'first':
            self.strng.transition = FadeTransition(duration=1)
        else:
            self.strng.transition = NoTransition()
        self.strng.current = screen
    def add_other_screens(self):
        Builder.load_file('main.kv')
        self.strng. add_widget(ItemDetail(name='itemdetail'))
        self.strng.add_widget(Otherdetail(name='other'))
        self.strng.add_widget(Home(name='home'))
        self.strng.add_widget(Profile(name='profile'))
        self.strng.add_widget(Bag(name='bag'))
        self.strng.add_widget(Detail(name='detail'))
        self.strng.add_widget(ODetail(name='odetail'))
        self.strng.add_widget(Card(name='card'))
        self.strng.add_widget(Store(name='store'))    
class First(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.My_CallBack,5)
        

        img = Image(source="/storage/emulated/0/Monster _ New Card/Assests/Bg.png", allow_stretch = True)
        icon_button = MDIconButton(opacity=1, icon="/storage/emulated/0/Monster _ New Card/Assests/Rd6rd.png", pos_hint={'center_x': 0.5, 'center_y': 0.5},icon_size="400sp")

        self.add_widget(img)
        self.add_widget(icon_button)
        
    def My_CallBack(self, dt):
        self.manager.switch_screen('check')
        self.manager.get_screen('check').done()

class Check(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        img = Image(source="/storage/emulated/0/Monster _ New Card/Assests/Bg.png", allow_stretch=True)
        icon_button = MDIconButton(id="icon_button", icon="/storage/emulated/0/Monster _ New Card/Assests/Logo.png", pos_hint={'center_x': 0.5, 'center_y': 0.7544}, size_hint=(None, None), icon_size="400sp")
        self.progress_bar = ProgressBar(value=0, max=100, pos_hint={'center_x': 0.5, 'center_y': 0.2}, size_hint_x=.9, size_hint_y=1.0)
        label = Label(text="© 2023 Shubham. All rights reserved.", pos_hint={'center_y': 0.15, 'center_x': 0.5}, bold=True, italic=True, font_size='20dp')

        self.add_widget(img)
        self.add_widget(icon_button)
        self.add_widget(self.progress_bar)
        self.add_widget(label)
    
    def done(self):
        self.progress_value = 0
        max_progress = 1000

        Clock.schedule_interval(self.update_progress, .001)  

    def update_progress(self, dt):
        self.progress_value += 1
        self.progress_bar.value = self.progress_value

        if self.progress_value >= self.progress_bar.max:
            Clock.unschedule(self.update_progress)  
            self.check_file_exists()

    def check_file_exists(self):
        custom = '/storage/emulated/0//.Monster : NewCard/Game Data/Monstercarddata.rd6p'
        if os.path.exists(custom):
            app = App.get_running_app()
            app.change('load')
        else:
            self.change_to_signup()

    def change_to_signup(self):
        app = App.get_running_app()
        app.change('signup')

class Signup(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        img = Image(source="/storage/emulated/0/Monster _ New Card/Assests/Bg.png", allow_stretch=True)
        step2 = MDCard(orientation='vertical', padding='20dp', size_hint=(0.9, 0.6), pos_hint={'center_x': 0.5, 'center_y': 0.5}, md_bg_color=(1, 1, 1, 0.5))

        layout = MDBoxLayout(orientation='vertical', spacing='10dp', padding=['1dp', '1dp', '1dp', '35dp'])

        self.gamename = MDTextField(hint_text="Game Name", helper_text="Enter your game name", helper_text_mode="on_error", required=True, pos_hint={'center_x': 0.5, 'center_y': 0.3}, icon_left="gamepad")

        gender_layout = MDGridLayout(rows=1, spacing='150dp', padding=['40dp', '90dp', '1dp', '170dp'])
        self.boycheck = MDCheckbox(group='gender', id='boycheck', size_hint=(None, None), size=('48dp', '48dp'))
        self.girlcheck = MDCheckbox(group='gender', id='girlcheck', size_hint=(None, None), size=('48dp', '48dp'))
        gender_layout.add_widget(self.boycheck)
        gender_layout.add_widget(self.girlcheck)

        icon_layout = MDGridLayout(rows=1, spacing='65dp', padding=['1dp', '-80dp', '1dp', '1dp'])
        boy_icon = MDIconButton(icon='/storage/emulated/0/Monster _ New Card/Assests/Boy.png', icon_size='100sp', size_hint=(None, None), size=('48dp', '48dp'), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        girl_icon = MDIconButton(icon='/storage/emulated/0/Monster _ New Card/Assests/Girl.png', icon_size='100sp', size_hint=(None, None), size=('48dp', '48dp'))
        icon_layout.add_widget(boy_icon)
        icon_layout.add_widget(girl_icon)

        terms_layout = MDGridLayout(cols=2, spacing='2dp', padding=['1dp', '50dp', '1dp', '100dp'])
        self.term = MDCheckbox(id='term', size_hint=(None, None), size=('30dp', '30dp'))
        terms_label = Label(text='I accept all terms and conditions.', font_size='15dp')
        terms_layout.add_widget(self.term)
        terms_layout.add_widget(terms_label)

        privacy_layout = MDGridLayout(cols=2, spacing='2dp', padding=['1dp', '10dp', '1dp', '150dp'])
        self.privacy = MDCheckbox(id='privacy', size_hint=(None, None), size=('30dp', '30dp'))
        policy_label = Label(text='I accept all privacy and policy.', font_size='15dp')
        privacy_layout.add_widget(self.privacy)
        privacy_layout.add_widget(policy_label)

        create_account_button = MDRectangleFlatButton(text="Create Account with Google", text_color=(1, 241/255, 0, 1), line_color=(1, 241/255, 0, 1), line_width=dp(1.5), font_size=sp(15), pos_hint={'center_x': 0.5, 'center_y': 0.3}, on_press=self.create)

        layout.add_widget(self.gamename)
        layout.add_widget(gender_layout)
        layout.add_widget(icon_layout)
        layout.add_widget(terms_layout)
        layout.add_widget(privacy_layout)
        layout.add_widget(create_account_button)

        step2.add_widget(layout)
        self.add_widget(img)
        self.add_widget(step2)
    def show_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda instance: dialog.dismiss()
                )
            ]
        )
        dialog.open()
    def update_datetime(self):
        now = datetime.now()
        formatted_datetime = now.strftime("%m/%d/%Y %I:%M:%S %p")
        return formatted_datetime
    def create(self, instance):
        game = self.gamename.text
        b = self.boycheck
        g = self.girlcheck
        t = self.term
        p = self.privacy
        scoin = '68889'
        rd = '66700'
        rank = '10000'
        hat = '00'
        ok = '00'
        tc = '00'
        jj = '01'
        lvl = encode(jj)
        card = encode(tc)
        coin = encode(scoin)
        dai = encode(rd)
        won = encode(ok)
        bat = encode(hat)
        ran = encode(rank)
    
        if len(game) >= 5:
            if b.active or g.active:
                if p.active and t.active:
                    data = {
                        "Gamename": game,
                        'Gender': 'boy' if b.active else 'girl',
                        'started': self.update_datetime(),
                        'Rohit': coin,
                        'Shubham': dai,
                        'Dear': [],  # item
                        'Suraj': ran,
                        'Rupee': [],  # moster
                        'hat': bat,
                        'rat': won,
                        'tp': card,
                        'pa': lvl
                    }
    
                    json_data = json.dumps(data, indent=2)
                    base_path = '/storage/emulated/0/'
                    folder_name = ".Monster : NewCard"
                    subfolder_name = "Game Data"
                    file_name = "Monstercarddata.rd6p"  
                    folder_path = os.path.join(base_path, folder_name)
                    subfolder_path = os.path.join(folder_path, subfolder_name)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    if not os.path.exists(subfolder_path):
                        os.makedirs(subfolder_path)
            
                    file_path = os.path.join(subfolder_path, file_name)
            
                    with open(file_path, 'w') as file:
                        file.write(json_data)
                    self.manager.switch_screen('load')
                else:
                    self.show_dialog("Account Error", "Please confirm our condition and policy. And must read carefully")
            else:
                self.show_dialog("Account Error", "Please select one gender.")
        else:
            self.show_dialog("Account Error", "Ensure that Gamename is more than 5 characters.")

class Load(Screen):
    def on_enter (self):
        self.ok()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        img = Image(source="/storage/emulated/0/Monster _ New Card/Assests/Load2.png", allow_stretch=True)
        self.loadbar = ProgressBar(value=0, max=100, pos_hint={'center_x': 0.5, 'center_y': 0.150009}, size_hint_x=0.9, size_hint_y=1.0)

        self.add_widget(img)
        self.add_widget(self.loadbar)
    def ok (self):
        self.progress_value = 0
        max_progress = 100

        def update_progress(dt):
            if self.progress_value == 40:
                app = App.get_running_app()
                loading_thread = threading.Thread(target=app.add_other_screens())
                loading_thread.start()
            if self.progress_value < max_progress:
                self.progress_value += 1
                self.loadbar.value = self.progress_value
            else:
                Clock.unschedule(update_progress)
                app = App.get_running_app()
                app.change('store')

        Clock.schedule_interval(update_progress,.01)          
class Home(Screen):
    def on_enter(self):
        coin(self,'home')
        avatar = self.ids.Avatar
        av = self.ch()
        avatar.source = av
    def ch(self):       
        custom = '/storage/emulated/0//.Monster : NewCard/Game Data/Monstercarddata.rd6p'
        with open(custom, 'r') as file:
            data = json.load(file)
        if data:
            gender = data.get('Gender', '')
            if gender == 'boy':
                return '/storage/emulated/0/Monster _ New Card/Assests/Boy.png'
            else:
                return '/storage/emulated/0/Monster _ New Card/Assests/Girl.png'
class Profile(Screen):
    def on_enter(self):
        custom = '/storage/emulated/0//.Monster : NewCard/Game Data/Monstercarddata.rd6p'
        coin(self,'profile')
        with open(custom, 'r') as file:
            data = json.load(file)
        if data:
            g = data.get('Gamename')
            l= decode(data.get('pa'))
            d = data.get('Gender')
            r = decode (data.get('Suraj'))
            s = data.get('started')
            p = decode(data.get('tp'))
            tb =decode( data.get('hat'))
            tw = decode(data.get('rat'))
                
            lv = self.ids.Lvl
            lv.text =f'lvl {l}'
            about = self.ids.game
            about.text = f'''Name      :      {g}

Gender      :      {d}

Started      :      {s}

Total PokeCard      :      {p}

Total Battel      :      {tb}

Total Won      :      {tw}'''
        avatar = self.ids.Avatar
        av = self.ch()
        avatar.source = av
    def ch(self):       
        custom = '/storage/emulated/0//.Monster : NewCard/Game Data/Monstercarddata.rd6p'
        with open(custom, 'r') as file:
            data = json.load(file)
        if data:
            gender = data.get('Gender', '')
            if gender == 'boy':
                return '/storage/emulated/0/Monster _ New Card/Assests/Boy.png'
            else:
                return '/storage/emulated/0/Monster _ New Card/Assests/Girl.png'
            
class ODetail(Screen):
    ok = 'g'
    def on_leave(self):
        self.ids.typer.clear_widgets()
    def on_pre_enter (self):
        coin(self,'odetail')
    def __init__(self, **kwargs):
        super(ODetail, self).__init__(**kwargs)
        self.type1 = MDIconButton (icon = "",icon_size = '40sp')
        self.type2 = MDIconButton (icon ="",icon_size = '40sp')
        self.typer = self.ids.typer
    def details (self,image,name):  
        self.ok = name
        app = App.get_running_app()
        self.ids.image.source = image
        self.ids.name.text = name
        if name in app.my_dict:
            attacks = app.my_dict[name]['attacks']
            ranks = app.my_dict[name]['rank']
            monster_type = app.my_dict[name]['type']
            self.update_type_icons(monster_type)
            for attack,rank in zip(attacks,ranks):
                rp_power_text = '\n' +str(rank)
                attack_text = '\n' +attack
                new_item = MyListItem(rp_power_text=rp_power_text, attack_text=attack_text)
                self.ids.list_layout.add_widget(new_item)
               
    def update_type_icons(self, monster_type):
        app = App.get_running_app()
        if '/' in monster_type:
            type_list = monster_type.split('/')
            if type_list[0] in app.type_icon_mapping:
                self.type1.icon = app.type_icon_mapping[type_list[0]]
                self.typer.add_widget(self.type1)
            if type_list[1] in app.type_icon_mapping:
                self.type2.icon= app.type_icon_mapping[type_list[1]]
                self.typer.add_widget(self.type2)
            else:
                self.type2.icon= ""
                
        else:
            if monster_type in app.type_icon_mapping:
                self.type1.icon = app.type_icon_mapping[monster_type]
                self.typer.add_widget(self.type1)
                self.type2.icon = ""        
class Bag(Screen):
    def on_pre_enter(self):
        crd = self.ids.ne
        coin(self, 'bag')
        crd.clear_widgets()
        custom = '/storage/emulated/0/.Monster : NewCard/Game Data/Monstercarddata.rd6p'
        with open(custom, 'r') as file:
            data = json.load(file)
            if data:
                c = data.get('Dear')
                for s in range(len(c)):
                    d = decode(c[int(s)])
                    app = App.get_running_app()
                    result_key = find_key_by_value(app.card, str(d))
                    st = str(result_key)
                    cads = BagCard(
                    t = 'itemdetail',
                        name=st,
                        image=f'/storage/emulated/0/Monster _ New Card/Assests/Item/{st}.png'
                    )
                    crd.add_widget(cads)
class BagCard(MDCard):
    def __init__(self, name='', image='', t='odetail',**kwargs):
        super(BagCard, self).__init__(**kwargs)
        self.name = name
        self.image = image
        self.font = '20dp'
        self.t = t
        self.sip_x = 130
        self.sip_y = 90
        
class Card(Screen):
    def on_pre_enter(self):
        card = self.ids.ne
        coin(self, 'card')
        card.clear_widgets()
        custom = '/storage/emulated/0/.Monster : NewCard/Game Data/Monstercarddata.rd6p'
        with open(custom, 'r') as file:
            data = json.load(file)
            if data:
                c = data.get('Rupee')
                for s in range(len(c)):
                    d = decode(c[int(s)])
                    app = App.get_running_app()
                    result_key = find_key_by_value(app.my_dict, str(d))
                    st = str(result_key)
                    cads = BagCard(
                        name=st,
                        image=f'/storage/emulated/0/Monster _ New Card/Assests/Pokemon card/{st}.png'
                    )
                    card.add_widget(cads)
class Detail(Screen):
    ok = 'g'
    def on_leave(self):
        self.ids.typer.clear_widgets()
    def on_pre_enter (self):
        coin(self,'detail')
    def __init__(self, **kwargs):
        super(Detail, self).__init__(**kwargs)
        self.type1 = MDIconButton (icon = "",icon_size = '40sp')
        self.type2 = MDIconButton (icon ="",icon_size = '40sp')
        self.typer = self.ids.typer
    def details (self,image,name):  
        self.ok = name
        app = App.get_running_app()
        self.ids.image.source = image
        self.ids.name.text = name
        if name in app.my_dict:
            attacks = app.my_dict[name]['attacks']
            ranks = app.my_dict[name]['rank']
            self.ids.rp.text = f"RP : {app.my_dict[name]['level']}"
            monster_type = app.my_dict[name]['type']
            set= app.my_dict[name]['price']
            if '/' in set :
                t = set.split('/')
                self.ids.cp.text =f'[color=ffffff][b]    {t[0]}    [/b][/color]'
                self.ids.dp.text = f'[color=ffffff][b]      {t[1]}      [/b][/color]'
            self.update_type_icons(monster_type)
            for attack,rank in zip(attacks,ranks):
                rp_power_text = '\n' +str(rank)
                attack_text = '\n' +attack
                new_item = MyListItem(rp_power_text=rp_power_text, attack_text=attack_text)
                self.ids.list_layout.add_widget(new_item)
    def update_type_icons(self, monster_type):
        app = App.get_running_app()
        if '/' in monster_type:
            type_list = monster_type.split('/')
            if type_list[0] in app.type_icon_mapping:
                self.type1.icon = app.type_icon_mapping[type_list[0]]
                self.typer.add_widget(self.type1)
            if type_list[1] in app.type_icon_mapping:
                self.type2.icon= app.type_icon_mapping[type_list[1]]
                self.typer.add_widget(self.type2)
            else:
                self.type2.icon= ""
                
        else:
            if monster_type in app.type_icon_mapping:
                self.type1.icon = app.type_icon_mapping[monster_type]
                self.typer.add_widget(self.type1)
                self.type2.icon = ""

class MyListItem(BoxLayout):
    def __init__(self, rp_power_text, attack_text, **kwargs):
        super(MyListItem, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.spacing = 40
        attack_label = Label(text=attack_text, font_size='20dp',color=(33/255,150/255,243/255,1))
        rp_power_label = Label(text=rp_power_text, font_size='20dp',color=(33/255,150/255,243/255,1))
        
        self.add_widget(attack_label)
        self.add_widget(rp_power_label)
        
        
class Store(Screen):
    def on_pre_enter (self):
        coin(self,'store')
class Otherdetail(Screen):
    ok = 't'
    def on_pre_enter (self):
        coin(self,'other')    
    def details (self,image,name):  
        self.ids.image.source = image
        self.ids.name.text = name    
        self.ok = name
        app = App.get_running_app()
        if name in app.card:
            attacks = app.card[name]['description']
            self.ids.about.text = attacks
            price = app.card[name]['price']
            if '/' in price :
                set = price.split('/')
                self.ids.pc.text = f'[color=ffffff][b]     {set[0]}     [/b][/color]'
                self.ids.pd.text = f'[color=ffffff][b]     {set[1]}     [/b][/color]'
        elif name in app.my_dict :
            attacks = app.my_dict[name]['description']
            self.ids.about.text = attacks
            price = app.my_dict[name]['price']
            if '/' in price :
                set = price.split('/')
                self.ids.pc.text = f'[color=ffffff][b]     {set[0]}     [/b][/color]'
                self.ids.pd.text = f'[color=ffffff][b]     {set[1]}     [/b][/color]'
class ItemDetail (Screen):
    ok = 't'
    def on_pre_enter (self):
        coin(self,'itemdetail')    
    def __init__(self, **kwargs):
        super(ItemDetail, self).__init__(**kwargs)
        ic = MDIconButton(
        icon = 'arrow-left-circle'    ,
        pos_hint ={'center_x': 0.1, 'center_y': 0.95}    ,
        icon_size = '40dp',
        on_press = self.Gunn)
        self.add_widget(ic)
    def Gunn (self,hh):
        app = App.get_running_app()
        if self.ok in {'Kodar', 'Maria', 'Mary', 'Spark', 'Joto', 'Jeda', 'Dika', 'Adena'}:
            return app.change('card')
        else:
            return app.change('bag') 
    def details (self,image,name):  
        app = App.get_running_app()
        self.ids.image.source = image
        self.ids.name.text = name    
        self.ok = name
        if name in app.card:
            attacks = app.card[name]['description']
            self.ids.about.text = attacks
        else:
            attacks = app.my_dict[name]['description']
            self.ids.about.text = attacks  
if __name__ == '__main__':
    MonsterApp().run()