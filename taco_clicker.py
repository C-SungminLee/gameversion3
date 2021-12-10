#################
### Importing ###
#################
import random as rand
import turtle as trtl
import winsound
from threading import Event
wn = trtl.Screen()
wn.setup(580,449)

# Menu shapes
wn.addshape("menu.gif")
wn.addshape("menuhelp.gif")
wn.addshape("menuplay.gif")
wn.addshape("menutaco.gif")
wn.addshape("arrow.gif")
wn.addshape("arrowleft.gif")

# Game Sprites
wn.addshape("taco.gif")
wn.addshape("burrito.gif")
wn.addshape("buttonunpressed.gif")
wn.addshape("buttonpressed.gif")
wn.addshape("fork.gif")
wn.addshape("background.gif")
# Autoclicker Sprites
wn.addshape("tabasco.gif")
wn.addshape("bbq_sauce.gif")
wn.addshape("ketchup.gif")
wn.addshape("mayonnaise.gif")
wn.addshape("soy_sauce.gif")
# Timer images
wn.addshape("timer0.gif")
wn.addshape("timer1.gif")
wn.addshape("timer2.gif")
wn.addshape("timer3.gif")
wn.addshape("timer4.gif")
wn.addshape("timer5.gif")
wn.addshape("timer6.gif")

##################
### Game Setup ###
##################
rectCors = ((-10,20),(10,20),(10,-20),(-10,-20))
wn.register_shape('rectangle',rectCors)
score = 0

# math problems and answers for burrito lootbox
math_problems = ["1 + 1 = ?","84 / 4 = ?","5 * 25 = ?","3^4 = ?","9 ^ 1/2 = ?","6 * 2 = ?", "50 / 10 = ?","Solve for x. 9((3x+6)/3) = 0"]
math_anwers = ["2", "21", "125","81","3", "12", "5", "-2"]

# Score Writer
score_writer = trtl.Turtle()
score_writer.speed(0)
score_writer.penup()
score_writer.hideturtle()
score_writer.setposition(-450, -250)
score_writer.pendown()
# Font
font_setup = ("Arial", "15", "normal")

# Taco per click upgrade Button
button = trtl.Turtle()
button.speed(0)
button.penup()
button.setposition(-510, 118)

# Burrito math loot box
burrito = trtl.Turtle()
burrito.hideturtle()
burrito.speed(0)
burrito.shape("burrito.gif")
burrito.penup()
global burritovalue
burritovalue = False

# Score rate
score_rate = 1
upgrade_cost = (score_rate*3)**2

rate = trtl.Turtle()
rate.speed(0)
rate.penup()
rate.hideturtle()
rate.setposition(-450, -230)
rate.pendown()

# Score rate upgrade text
next = trtl.Turtle()
next.color("moccasin")
next.speed(0)
next.penup()
next.hideturtle()
next.setposition(-550, 180)
next.pendown()

# Taco
taco = trtl.Turtle()
taco.hideturtle()
score = 0
taco.shape("taco.gif")
taco.speed(0)
taco.penup() 
taco.setposition(-190, -150)

font_setup = ("Arial", "15", "normal")

# TPS writer
tps = trtl.Turtle()
tps.hideturtle()
tps.penup()
tps.speed(0)
tps.pencolor("white")
tps.setposition(-580, 210)
tps.write("Current tacos per second: 0")
tacos_per_second = 0
def tps_update():
  tps.clear()
  tps.write("Current tacos per second: "+str(tacos_per_second))

#update the amount of tacos
def update_score(amount):
  global tutorialmode, tutorialnumber
  if tutorialmode == True and tutorialnumber == 0:
    arrow.clear()
    score_writer.clear()
    score_writer.write("1 tacos", font = font_setup)
    arrow.setposition(-540, -235)
    arrow.shape("arrow.gif")
    arrow.showturtle()
    arrow.stamp()
    arrow.hideturtle()
    arrow.setposition(-590, -240)
    arrow.write("This is your score, you use",font = ("Arial", "8", "italic"))
    arrow.setposition(-590, -255)
    arrow.write("your score to buy upgrades",font = ("Arial", "8", "italic"))
    tutorialnumber = 1
  elif tutorialmode == True and tutorialnumber == 1:
    arrow.clear()
    arrow.setposition(-540, -210)
    arrow.showturtle()
    arrow.stamp()
    arrow.hideturtle()
    arrow.setposition(-590, -215)
    arrow.write("This is your cps, the amount",font = ("Arial", "8", "italic"))
    arrow.setposition(-590, -225)
    arrow.write("of tacos you get per click",font = ("Arial", "8", "italic"))
    tutorialnumber = 2
  elif tutorialmode == True and tutorialnumber == 2:
    arrow.clear()
    arrow.setposition(-350, 110)
    arrow.shape("arrowleft.gif")
    arrow.showturtle()
    arrow.stamp()
    arrow.hideturtle()
    arrow.setposition(-400,115)
    arrow.write("This is the upgrade button, ",font = ("Arial", "8", "italic"))
    arrow.setposition(-400,105)
    arrow.write("you press it to upgade your cps",font = ("Arial", "8", "italic"))
    tutorialnumber = 3
  elif tutorialmode == True and tutorialnumber == 3:
    arrow.clear()
    arrow.setposition(-375, 180)
    arrow.showturtle()
    arrow.stamp()
    arrow.hideturtle()
    arrow.setposition(-425,190)
    arrow.write("This is the cost, when you",font = ("Arial", "8", "italic"))
    arrow.setposition(-425,180)
    arrow.write("press the button the cost is ",font = ("Arial", "8", "italic"))
    arrow.setposition(-425,170)
    arrow.write("subtracted from your score",font = ("Arial", "8", "italic"))
    tutorialnumber = 4
  elif tutorialmode == True and tutorialnumber == 4:
    arrow.clear()
    arrow.setposition(180, 130)
    arrow.shape("arrow.gif")
    arrow.showturtle()
    arrow.stamp()
    arrow.hideturtle()
    arrow.setposition(100,130)
    arrow.write("These are the autoclickers, ",font = ("Arial", "8", "italic"))
    arrow.setposition(100,120)
    arrow.write("they automatically add score ",font = ("Arial", "8", "italic"))
    arrow.setposition(100,110)
    arrow.write("per timer",font = ("Arial", "8", "italic"))
    tutorialnumber = 5
  elif tutorialmode == True and tutorialnumber == 5:
    arrow.clear()
    arrow.setposition(180, 130)
    
    arrow.showturtle()
    arrow.stamp()
    arrow.hideturtle()
    arrow.setposition(100,130)
    arrow.write("The # next to the oz is ",font = ("Arial", "8", "italic"))
    arrow.setposition(100,120)
    arrow.write("the score that is being ",font = ("Arial", "8", "italic"))
    arrow.setposition(100,110)
    arrow.write("added for the multiplier",font = ("Arial", "8", "italic"))
    tutorialnumber = 6

  elif tutorialmode == True and tutorialnumber == 6:
    arrow.clear()
    arrow.setposition(180, 130)
    arrow.showturtle()
    arrow.stamp()
    arrow.hideturtle()
    arrow.setposition(100,130)
    arrow.write("Tobasco has a 1 multiplier, ",font = ("Arial", "8", "italic"))
    arrow.setposition(100,120)
    arrow.write("bbq sauce has a 30 multiplier, ",font = ("Arial", "8", "italic"))
    arrow.setposition(100,110)
    arrow.write("ketchup has a 150 multiplier",font = ("Arial", "8", "italic"))
    tutorialnumber = 7
  elif tutorialmode == True and tutorialnumber == 7:
    arrow.clear()
    arrow.setposition(180, 130)
    arrow.showturtle()
    arrow.stamp()
    arrow.hideturtle()
    arrow.setposition(100,125)
    arrow.write("mayonnaise has a 2000 multiplier, ",font = ("Arial", "7", "italic"))
    arrow.setposition(100,115)
    arrow.write("and soy sauce has a 10000 multiplier. ",font = ("Arial", "7", "italic"))
    tutorialnumber = 8

  elif tutorialmode == True and tutorialnumber == 8:
    arrow.clear()
    arrow.setposition(180, 130)
    arrow.showturtle()
    arrow.stamp()
    arrow.hideturtle()
    arrow.setposition(100,130)
    arrow.write("Next to the autoclikcers there ",font = ("Arial", "8", "italic"))
    arrow.setposition(100,120)
    arrow.write("are timers, when the timers fill ",font = ("Arial", "8", "italic"))
    arrow.setposition(100,110)
    arrow.write("the autoclicker adds to the score.",font = ("Arial", "7", "italic"))
    
    tutorialnumber = 9

  elif tutorialmode == True and tutorialnumber == 9:
    arrow.clear()
    arrow.setposition(180, 130)
    arrow.showturtle()
    arrow.stamp()
    arrow.hideturtle()
    arrow.setposition(100,120)
    arrow.write("Thats the Game! ",font = ("Arial", "15", "italic"))    
    tutorialnumber = 10

  elif tutorialmode == True and tutorialnumber == 10:
    arrow.clear()
    tutorialmode = False
    tutorialnumber = 0
    
    help.showturtle()
    start_button.showturtle()
    textwriter.showturtle()


    wn.setup(580,449)
    wn.bgpic("menu.gif")
    
    taco.hideturtle()
    score_writer.clear()
    next.clear()
    rate.clear()
    tabasco.hideturtle()
    bbq_sauce.hideturtle()
    ketchup.hideturtle()
    mayonnaise.hideturtle()
    soy_sauce.hideturtle()



  else:
    global score
    score_writer.clear()
    score += amount
    score_writer.write(str(score) + " tacos", font = font_setup)


###################
### Menu Screen ###
###################

global tutorialmode
tutorialmode = False
global tutorialnumber
tutorialnumber = 0
textwriter = trtl.Turtle()
textwriter.showturtle()
textwriter.speed(0)
textwriter.pu()
textwriter.shape("menutaco.gif")
textwriter.setposition(0,100)

wn.bgpic("menu.gif")
game_start = False
start_button = trtl.Turtle()
start_button.speed(0)
start_button.penup()
start_button.shape("menuplay.gif")


help = trtl.Turtle()
help.showturtle()
help.pu()
help.speed(0)
help.shape("menuhelp.gif")
help.setposition(0, -100)

arrow = trtl.Turtle()
arrow.speed(0)
arrow.hideturtle()
arrow.pu()
arrow.shape("arrow.gif")

def start_game(x, y):
  global game_start

  help.hideturtle()
  textwriter.hideturtle()
  wn.setup(1200,700)
  wn.bgpic("background.gif")
  game_start = True
  start_button.hideturtle()
  taco.showturtle()
  score_writer.write(str(score) + " tacos", font = font_setup)
  
  taco.shape("taco.gif")
  button.shape("buttonunpressed.gif")
  next.write("Next upgrade: " + str(upgrade_cost) + " tacos",font = ("Arial", "7", "italic"))
  rate.write("tacos per click: " + str(score_rate))
  tabasco.showturtle()
  bbq_sauce.showturtle()
  ketchup.showturtle()
  mayonnaise.showturtle()
  soy_sauce.showturtle()
  winsound.PlaySound("gamemusic.wav", winsound.SND_ASYNC)
  wn.ontimer(countdown, rand.randint(30000,120000))


  


def tutorial(x,y):
  winsound.PlaySound("btsmusic.wav", winsound.SND_ASYNC)
  global tutorialmode
  tutorialmode = True
  help.hideturtle()
  textwriter.hideturtle()
  wn.setup(1200,700)
  wn.bgpic("background.gif")
  start_button.hideturtle()
  taco.showturtle()
  score_writer.write(str(score) + " tacos", font = font_setup)
  
  taco.shape("taco.gif")
  button.shape("buttonunpressed.gif")
  next.write("Next upgrade: 1",font = ("Arial", "7", "italic"))
  rate.write("tacos per click: 1")
  tabasco.showturtle()
  bbq_sauce.showturtle()
  ketchup.showturtle()
  mayonnaise.showturtle()
  soy_sauce.showturtle()
  
  arrow.setposition(0, -150)
  arrow.shape("arrowleft.gif")
  arrow.showturtle()
  arrow.stamp()
  arrow.hideturtle()
  arrow.setposition(-50, -140)
  arrow.color("white")
  arrow.write("Press the Taco to",font = ("Arial", "10", "italic"))
  arrow.setposition(-50, -160)
  arrow.write("increase your score",font = ("Arial", "10", "italic"))
  





start_button.onclick(start_game)
help.onclick(tutorial)


####################
### Autoclickers ###
####################

# sauces
tabasco = trtl.Turtle()
tabasco.hideturtle()
bbq_sauce = trtl.Turtle()
bbq_sauce.hideturtle()
ketchup = trtl.Turtle()
ketchup.hideturtle()
mayonnaise = trtl.Turtle()
mayonnaise.hideturtle()
soy_sauce = trtl.Turtle()
soy_sauce.hideturtle()

# sauce text writers
tabasco_writer = trtl.Turtle()
bbq_sauce_writer = trtl.Turtle()
ketchup_writer = trtl.Turtle()
mayonnaise_writer = trtl.Turtle()
soy_sauce_writer = trtl.Turtle()

sauce_list = [tabasco, tabasco_writer, bbq_sauce, bbq_sauce_writer, ketchup, ketchup_writer, mayonnaise, mayonnaise_writer, soy_sauce, soy_sauce_writer]
for sauce in sauce_list:
  sauce.penup()
  sauce.speed(0)

# Menu writer
sauce_font = ("Times New Roman", "17", "italic")
menu_writer = trtl.Turtle()
menu_writer.penup()
menu_writer.speed(0)
menu_writer.hideturtle()
menu_item_list = ["-  TABASCO  -", "-  BBQ SAUCE  -", "-  KETCHUP  -", "-  MAYONNAISE  -", "-  SOY SAUCE  -"]
menu_item_coords = [(310, 145), (310, 55), (310, -35), (310, -125), (310, -215)]
for i in range(5):
  menu_writer.setposition(menu_item_coords[i])
  menu_writer.write(menu_item_list[i], font = sauce_font)

#-----tabasco-----
tabasco_delay = 5
tabasco_tacos = 1
tabasco.setposition(285, 130)
tabasco.shape("tabasco.gif")
tabasco_amount = 0
tabasco_cost = 2
tabasco_bought = False

def buy_tabasco(x, y):
  global tabasco_amount, score, tabasco_cost, tacos_per_second, tabasco_bought, ttimer_on
  if score >= tabasco_cost:
    tabasco_amount += 1
    score -= tabasco_cost
    update_score(0)
    tabasco_cost = 2 * (round(1.15**tabasco_amount)+tabasco_amount)
    update_tabasco()
    tacos_per_second += 0.2
    tps_update()
    if tabasco_bought == False:
      tabasco_bought = True
      ttimer_on = True
      timer()

# tabasco writer
tabasco_writer.hideturtle()
tabasco_writer.setposition(310, 120)
tabasco_writer.write("0 oz. of Tabasco", font = font_setup)
tabasco_writer.setposition(310, 100)
tabasco_writer.write("Current cost: " + str(tabasco_cost) + " tacos")

def update_tabasco():
  global tabasco_amount
  tabasco_writer.clear()
  tabasco_writer.setposition(310, 120)
  tabasco_writer.write(str(tabasco_amount) + " oz. of Tabasco", font = font_setup)
  tabasco_writer.setposition(310, 100)
  tabasco_writer.write("Current cost: " + str(tabasco_cost) + " tacos")


#-----bbq sauce-----
bbq_sauce_delay = 3
bbq_sauce_tacos = 30
bbq_sauce.setposition(285, 40)
bbq_sauce.shape("bbq_sauce.gif")
bbq_sauce_amount = 0
bbq_sauce_cost = 1000
bbq_sauce_bought = False

def buy_bbq_sauce(x, y):
  global bbq_sauce_amount, score, bbq_sauce_cost, tacos_per_second, bbq_sauce_bought, btimer_on
  if score >= bbq_sauce_cost:
    bbq_sauce_amount += 1
    score -= bbq_sauce_cost
    update_score(0)
    bbq_sauce_cost = 1000 + 100*(round(1.15**bbq_sauce_amount)+bbq_sauce_amount)
    update_bbq_sauce()
    tacos_per_second += 10
    tps_update()
    if bbq_sauce_bought == False:
      bbq_sauce_bought = True
      btimer_on = True

# bbq_sauce writer
bbq_sauce_writer.hideturtle()
bbq_sauce_writer.setposition(310, 30)
bbq_sauce_writer.write("0 oz. of BBQ Sauce", font = font_setup)
bbq_sauce_writer.setposition(310, 10)
bbq_sauce_writer.write("Current cost: " + str(bbq_sauce_cost) + " tacos")

def update_bbq_sauce():
  global bbq_sauce_amount
  bbq_sauce_writer.clear()
  bbq_sauce_writer.setposition(310, 30)
  bbq_sauce_writer.write(str(bbq_sauce_amount) + " oz. of BBQ Sauce", font = font_setup)
  bbq_sauce_writer.setposition(310, 10)
  bbq_sauce_writer.write("Current cost: " + str(bbq_sauce_cost) + " tacos")

#-----ketchup-----
ketchup_delay = 1
ketchup_tacos = 150
ketchup.setposition(285, -50)
ketchup.shape("ketchup.gif")
ketchup_amount = 0
ketchup_cost = 11000
ketchup_bought = False

def buy_ketchup(x, y):
  global ketchup_amount, score, ketchup_cost, tacos_per_second, ketchup_bought, ktimer_on
  if score >= ketchup_cost:
    ketchup_amount += 1
    score -= ketchup_cost
    update_score(0)
    ketchup_cost = 11000 + 1000*(round(1.15**ketchup_amount)+ketchup_amount)
    update_ketchup()
    tacos_per_second += 150
    tps_update()
    if ketchup_bought == False:
      ketchup_bought = True
      ktimer_on = True

# ketchup writer
ketchup_writer.hideturtle()
ketchup_writer.setposition(310, -60)
ketchup_writer.write("0 oz. of Ketchup", font = font_setup)
ketchup_writer.setposition(310, -80)
ketchup_writer.write("Current cost: " + str(ketchup_cost) + " tacos")

def update_ketchup():
  global ketchup_amount
  ketchup_writer.clear()
  ketchup_writer.setposition(310, -60)
  ketchup_writer.write(str(ketchup_amount) + " oz. of Ketchup", font = font_setup)
  ketchup_writer.setposition(310, -80)
  ketchup_writer.write("Current cost: " + str(ketchup_cost) + " tacos")


#-----mayonnaise-----
mayonnaise_delay = 1
mayonnaise_tacos = 2000
mayonnaise.setposition(285, -140)
mayonnaise.shape("mayonnaise.gif")
mayonnaise_amount = 0
mayonnaise_cost = 120000
mayonnaise_bought = False

def buy_mayonnaise(x, y):
  global mayonnaise_amount, score, mayonnaise_cost, tacos_per_second, mayonnaise_bought, mtimer_on
  if score >= mayonnaise_cost:
    mayonnaise_amount += 1
    score -= mayonnaise_cost
    update_score(0)
    mayonnaise_cost = 120000 + 10000*(round(1.15**mayonnaise_amount)+mayonnaise_amount)
    update_mayonnaise()
    tacos_per_second += 2000
    tps_update()
    if mayonnaise_bought == False:
      mayonnaise_bought = True
      mtimer_on = True

# mayonnaise writer
mayonnaise_writer.hideturtle()
mayonnaise_writer.setposition(310, -150)
mayonnaise_writer.write("0 oz. of mayonnaise", font = font_setup)
mayonnaise_writer.setposition(310, -170)
mayonnaise_writer.write("Current cost: " + str(mayonnaise_cost) + " tacos")

def update_mayonnaise():
  global mayonnaise_amount
  mayonnaise_writer.clear()
  mayonnaise_writer.setposition(310, -150)
  mayonnaise_writer.write(str(mayonnaise_amount) + " oz. of mayonnaise", font = font_setup)
  mayonnaise_writer.setposition(310, -170)
  mayonnaise_writer.write("Current cost: " + str(mayonnaise_cost) + " tacos")


#-----soy sauce-----
soy_sauce_delay = 1
soy_sauce_tacos = 10000
soy_sauce.setposition(285, -230)
soy_sauce.shape("soy_sauce.gif")
soy_sauce_amount = 0
soy_sauce_cost = 1300000
soy_sauce_bought = False

def buy_soy_sauce(x, y):
  global soy_sauce_amount, score, soy_sauce_cost, tacos_per_second, soy_sauce_bought, stimer_on
  if score >= soy_sauce_cost:
    soy_sauce_amount += 1
    score -= soy_sauce_cost
    update_score(0)
    soy_sauce_cost = 1300000 + 100000*(round(1.15**soy_sauce_amount)+soy_sauce_amount)
    update_soy_sauce()
    tacos_per_second += 1300000
    tps_update()
    if soy_sauce_bought == False:
      soy_sauce_bought = True
      stimer_on = True

# soy_sauce writer
soy_sauce_writer.hideturtle()
soy_sauce_writer.setposition(310, -240)
soy_sauce_writer.write("0 oz. of Soy Sauce", font = font_setup)
soy_sauce_writer.setposition(310, -260)
soy_sauce_writer.write("Current cost: " + str(soy_sauce_cost) + " tacos")

def update_soy_sauce():
  global soy_sauce_amount
  soy_sauce_writer.clear()
  soy_sauce_writer.setposition(310, -240)
  soy_sauce_writer.write(str(soy_sauce_amount) + " oz. of Soy Sauce", font = font_setup)
  soy_sauce_writer.setposition(310, -260)
  soy_sauce_writer.write("Current cost: " + str(soy_sauce_cost) + " tacos")


#############
### Timer ###
#############
# Timers for tabasco, bbq, ketchup, mayo, and soy sauce
ttimer = trtl.Turtle()
btimer = trtl.Turtle()
ktimer = trtl.Turtle()
mtimer = trtl.Turtle()
stimer = trtl.Turtle()
timer_list = [ttimer, btimer, ktimer, mtimer, stimer]
for timer in timer_list:
  timer.speed(0)
  timer.penup()
  timer.shape("timer0.gif")
  timer.setposition(550, 130 - 90*timer_list.index(timer))

# variables to check if a certain sauce is activated
ttimer_on = False
btimer_on = False
ktimer_on = False
mtimer_on = False
stimer_on = False

# functions to shorten code for 1 second sauces
def one_second(sauce_timer):
  sauce_timer.shape("timer0.gif")
  one_second_image(sauce_timer)

def one_second_image(sauce_timer):
  wn.ontimer(sauce_timer.shape("timer6.gif"), 1)

# checking which timers are on
def timer_check():
  if ttimer_on == True: 
    if level == 1: ttimer.shape("timer1.gif")
    elif level == 2: ttimer.shape("timer2.gif")
    elif level == 3: ttimer.shape("timer3.gif")
    elif level == 4: ttimer.shape("timer4.gif")
    elif level == 5: ttimer.shape("timer5.gif")
    elif level == 6: ttimer.shape("timer6.gif"), update_score(tabasco_amount*tabasco_tacos)
  if btimer_on == True: 
    if level == 1 or level == 4: btimer.shape("timer2.gif")
    elif level == 2 or level == 5: btimer.shape("timer4.gif")
    elif level == 3 or level == 6: btimer.shape("timer6.gif"), update_score(bbq_sauce_amount*bbq_sauce_tacos)
  if ktimer_on == True: update_score(ketchup_amount*ketchup_tacos), one_second(ktimer)
  if mtimer_on == True: update_score(mayonnaise_amount*mayonnaise_tacos), one_second(mtimer)
  if stimer_on == True: update_score(soy_sauce_amount*soy_sauce_tacos), one_second(stimer)

# timer system
level = 1
def timer():
  global level
  if level == 1:
    timer_check()
    level = level + 1
    wn.ontimer(timer, 1000)

  elif level == 2:
    timer_check()
    level = level + 1
    wn.ontimer(timer, 1000)

  elif level == 3:
    timer_check()
    level = level + 1
    wn.ontimer(timer, 1000)

  elif level == 4:
    timer_check()
    level = level + 1
    wn.ontimer(timer, 1000)

  elif level == 5:
    timer_check()
    level = level + 1
    wn.ontimer(timer, 1000)

  elif level == 6:
    timer_check()
    level = 1
    wn.ontimer(timer, 1000)

########################
### Burrito Loot Box ###
########################
global checkvalue
checkvalue = False

def check():
  global burritovalue
  if burritovalue != True:
    hideturtle()
    burritovalue = False
  else:
    global checkvalue
    checkvalue = True
    burrito.showturtle()

def countdown():
  burrito.setposition(rand.randint(-300, 90), rand.randint(50, 120))
  burrito.showturtle()
  wn.ontimer(check, rand.randint(30000,120000))

def hideturtle():
  burrito.hideturtle()
  wn.ontimer(countdown, rand.randint(30000,120000))

#When the taco is clicked increase the score
def taco_click(x, y):
  update_score(score_rate)

#When the burrito is clicked ask a random math question
def burrito_click(x, y):
  global burritovalue
  burritovalue = True
  lootbox()

#Asking the random math question
def lootbox():
  number = rand.randint(0,len(math_problems)-1)  
  answer = wn.textinput("Problem","What is " + str(math_problems[number]))
  while answer != math_anwers[number]:
    answer = wn.textinput("Problem","Try again what is " + (math_problems[number]))
  else:
    if score_rate <= 7:
      update_score(rand.randint(50,150))
    elif score_rate >= 8 and score_rate <= 14:
      update_score(rand.randint(200,350))
    elif score_rate >= 15 and score_rate <= 20:
      update_score(rand.randint(1000,2000))
    elif score_rate >= 21 and score_rate <= 30:
      update_score(rand.randint(3000,4500))
    burrito.hideturtle()
    if checkvalue != False:
      wn.ontimer(countdown, rand.randint(30000,120000))
    
  
######################
### Upgrade Button ###
######################
#When the button is clicked upgrade
def button_click(x, y):
  upgrade() 

#Updgrade the rate of tacos per click
def upgrade():
  global score_rate
  global score
  global upgrade_cost
  if score >= upgrade_cost:
    button.shape("buttonpressed.gif")
    score_rate += 1
    rate.clear()
    rate.write("Tacos per click: " + str(score_rate))
    score -= upgrade_cost
    score_writer.clear()
    score_writer.write(str(score) + " tacos", font = font_setup)
    upgrade_cost = (score_rate*3)**2

    next.clear()
    next.write("Next upgrade: " + str(upgrade_cost) + " tacos",font = ("Arial", "7", "italic"))
    button.shape("buttonunpressed.gif")


#-----click detection-----
tabasco.onclick(buy_tabasco)
bbq_sauce.onclick(buy_bbq_sauce)
ketchup.onclick(buy_ketchup)
mayonnaise.onclick(buy_mayonnaise)
soy_sauce.onclick(buy_soy_sauce)
burrito.onclick(burrito_click)
button.onclick(button_click)
taco.onclick(taco_click)


wn.listen()
wn.mainloop()
