import turtle as trtl
import random
trtl.register_shape("mushroom.gif") 
trtl.register_shape("flower.gif") 
trtl.register_shape("star.gif") 
trtl.register_shape("bobomb.gif")
trtl.register_shape("egg.gif") 
trtl.register_shape("goomba.gif") 
trtl.register_shape("bowser.gif")
trtl.register_shape("coin.gif") 
trtl.register_shape("luigi.gif")
trtl.register_shape("phonto.gif")
legend = trtl.Turtle()
legend.hideturtle()
legend.shape("phonto.gif")
legend.penup()
legend.goto(295,-215)
messanger= trtl.Turtle()
messanger.hideturtle()
messanger.speed(0)
wn = trtl.Screen()
wn.listen()
which_card = 0
betpen = trtl.Turtle()
betpen.hideturtle()
betpen.speed(0)
card1 = trtl.Turtle()
card1.penup()
card1.hideturtle()
coin_pic = trtl.Turtle()
coin_pic.penup()
coin_pic.hideturtle()
coin_pic.shape("coin.gif")
card2 = trtl.Turtle()
card2.penup()
card2.hideturtle()
card3 = trtl.Turtle()
card3.penup()
card3.hideturtle()
ecard1 = trtl.Turtle()
ecard1.penup()
ecard1.hideturtle()
ecard2 = trtl.Turtle()
ecard2.penup()
ecard2.hideturtle()
ecard3 = trtl.Turtle()
ecard3.penup()
ecard3.hideturtle()
decoy1 = trtl.Turtle()
decoy1.penup()
decoy1.hideturtle()
decoy1.shape("luigi.gif")
decoy2 = trtl.Turtle()
decoy2.penup()
decoy2.hideturtle()
decoy2.shape("luigi.gif")
decoy3 = trtl.Turtle()
decoy3.penup()
decoy3.hideturtle()
decoy3.shape("luigi.gif")
drawer = trtl.Turtle()
pen2 = trtl.Turtle()
pen2.hideturtle()
pen2.pencolor('black')
pen2.fillcolor('blue')
legend.showturtle()
mushroom_value = 0
flower_value = 0
star_value = 0
bobomb_value = 0
egg_value = 0
goomba_value = 0
bowser_value = 0
coins = 10
betted_coins = 0
holding_list = ["Mushroom", "Flower", "Star", "Bobomb", "Egg", "Goomba", "Bowser"]
card_list = ["Mushroom", "Flower", "Star", "Bobomb", "Egg", "Goomba", "Bowser"]
eholding_list = ["Mushroom", "Flower", "Star", "Bobomb", "Egg", "Goomba"]
ecard_list = ["Mushroom", "Flower", "Star", "Bobomb", "Egg", "Goomba"]
def field():
    drawer.speed(0)
    drawer.penup()
    drawer.goto(-215,-350)
    drawer.pendown()
    drawer.left(90)
    drawer.forward(175)
    drawer.right(90)
    drawer.forward(125)
    drawer.right(90)
    drawer.forward(175)
    drawer.penup()
    drawer.setheading(0)
    drawer.goto(-63,-350)
    drawer.pendown()
    drawer.left(90)
    drawer.forward(175)
    drawer.right(90)
    drawer.forward(125)
    drawer.right(90)
    drawer.forward(175)
    drawer.penup()
    drawer.setheading(0)
    drawer.goto(88,-350)
    drawer.pendown()
    drawer.left(90)
    drawer.forward(175)
    drawer.right(90)
    drawer.forward(125)
    drawer.right(90)
    drawer.forward(175)
    drawer.penup()
    drawer.setheading(0)
    drawer.goto(-215,350)
    drawer.pendown()
    drawer.right(90)
    drawer.forward(175)
    drawer.left(90)
    drawer.forward(125)
    drawer.left(90)
    drawer.forward(175)
    drawer.penup()
    drawer.setheading(0)
    drawer.goto(-63,350)
    drawer.pendown()
    drawer.right(90)
    drawer.forward(175)
    drawer.left(90)
    drawer.forward(125)
    drawer.left(90)
    drawer.forward(175)
    drawer.penup()
    drawer.setheading(0)
    drawer.goto(88,350)
    drawer.pendown()
    drawer.right(90)
    drawer.forward(175)
    drawer.left(90)
    drawer.forward(125)
    drawer.left(90)
    drawer.forward(175)
def draw(card, list):
    global which_card
    global card1_value
    global card2_value
    global card3_value
    global ecard1_value
    global ecard2_value
    global ecard3_value
    which_card += 1
    balance_list = ["Mushroom", "Flower", "Star"]
    balancer = random.choice(balance_list)
    list.append(balancer)
    select = random.choice(list)
    list.remove(select)
    try:
        list.remove(balancer)
    except:
        drawer.setheading(0)
    if (select == "Mushroom"):
        card.shape("mushroom.gif")
        if (which_card == 1):
           card1_value = "Mushroom"
        elif (which_card == 2):
           card2_value = "Mushroom"
        elif (which_card == 3):
           card3_value = "Mushroom"
        elif (which_card == 4):
           ecard1_value = "Mushroom"
        elif (which_card == 5):
           ecard2_value = "Mushroom"
        elif (which_card == 6):
           ecard3_value = "Mushroom"
    elif (select == "Flower"):
        card.shape("flower.gif")
        if (which_card == 1):
           card1_value = "Flower"
        elif (which_card == 2):
           card2_value = "Flower"
        elif (which_card == 3):
           card3_value = "Flower"
        elif (which_card == 4):
           ecard1_value = "Flower"
        elif (which_card == 5):
           ecard2_value = "Flower"
        elif (which_card == 6):
           ecard3_value = "Flower"
    elif (select == "Star"):
        card.shape("star.gif")
        if (which_card == 1):
           card1_value = "Star"
        elif (which_card == 2):
           card2_value = "Star"
        elif (which_card == 3):
           card3_value = "Star"
        elif (which_card == 4):
           ecard1_value = "Star"
        elif (which_card == 5):
           ecard2_value = "Star"
        elif (which_card == 6):
           ecard3_value = "Star"
    elif (select == "Bobomb"):
        card.shape("bobomb.gif")
        if (which_card == 1):
           card1_value = "Bobomb"
        elif (which_card == 2):
           card2_value = "Bobomb"
        elif (which_card == 3):
           card3_value = "Bobomb"
        elif (which_card == 4):
           ecard1_value = "Bobomb"
        elif (which_card == 5):
           ecard2_value = "Bobomb"
        elif (which_card == 6):
           ecard3_value = "Bobomb"
    elif (select == "Egg"):
        card.shape("egg.gif")
        if (which_card == 1):
           card1_value = "Egg"
        elif (which_card == 2):
           card2_value = "Egg"
        elif (which_card == 3):
           card3_value = "Egg"
        elif (which_card == 4):
           ecard1_value = "Egg"
        elif (which_card == 5):
           ecard2_value = "Egg"
        elif (which_card == 6):
           ecard3_value = "Egg"
    elif (select == "Goomba"):
        card.shape("goomba.gif")
        if (which_card == 1):
           card1_value = "Goomba"
        elif (which_card == 2):
           card2_value = "Goomba"
        elif (which_card == 3):
           card3_value = "Goomba"
        elif (which_card == 4):
           ecard1_value = "Goomba"
        elif (which_card == 5):
           ecard2_value = "Goomba"
        elif (which_card == 6):
           ecard3_value = "Goomba"
    else:
        card.shape("bowser.gif")
        if (which_card == 1):
           card1_value = "Bowser"
        elif (which_card == 2):
           card2_value = "Bowser"
        elif (which_card == 3):
           card3_value = "Bowser"
        elif (which_card == 4):
           ecard1_value = "Bowser"
        elif (which_card == 5):
           ecard2_value = "Bowser"
        elif (which_card == 6):
           ecard3_value = "Bowser"
def mushroom():
    global mushroom_value
    mushroom_choices = [1, 2, 3]
    mushroom_value = random.choice(mushroom_choices)
def flower():
    global flower_value
    flower_choices = [4, 5, 6]
    flower_value = random.choice(flower_choices)
def star():
    global star_value
    star_choices = [7, 8, 9]
    star_value = random.choice(star_choices)
def goomba():
    global goomba_value
    goomba_choices = [-1, -2, -3]
    goomba_value = random.choice(goomba_choices)
def bobomb():
    global bobomb_value
    bobomb_choices = [1.25, 1.5, 1.75]
    bobomb_value = random.choice(bobomb_choices)
def egg():
    global egg_value
    egg_choices = [0, 5, 10]
    egg_value = random.choice(egg_choices)
def bowser():
    global bowser_value
    bowser_value = 999
Button2_x = 250
Button2_y = -25
Button2Length = 100
Button2Width = 75
def draw_cont(pen2, message = 'Continue'):
    pen2.penup()
    pen2.begin_fill()
    pen2.goto(Button2_x, Button2_y)
    pen2.goto(Button2_x + Button2Length, Button2_y)
    pen2.goto(Button2_x + Button2Length, Button2_y + Button2Width)
    pen2.goto(Button2_x, Button2_y + Button2Width)
    pen2.goto(Button2_x, Button2_y)
    pen2.end_fill()
    pen2.goto(Button2_x + 12, Button2_y + 23)
    pen2.write(message, font = ('Arial', 15, 'normal'))
cont_count = 0
player_score = 0
enemy_score = 0
def cont(v,w):
    global coins
    global betted_coins
    if (betted_coins == 0):
        coin()
    global cont_count
    cont_count = cont_count + 1
    if Button2_x <= v <= Button2_x + Button2Length:
        if Button2_y <= w <= Button2_y + Button2Width:
            global which_card
            global card_list
            global ecard_list
            global holding_list
            global eholding_list
            global pow_list
            global card1_value
            global card2_value
            global card3_value
            global ecard1_value
            global ecard2_value
            global ecard3_value
            global replace_count
            global player_score
            global enemy_score
            if (cont_count == 1):
                messanger.clear()
                messanger.penup()
                messanger.goto(-180,0)
                messanger.pendown()
                messanger.write("Want to swap a card? Click continue next!", font = ('Arial', 15, 'normal'))
                wn.onkeypress(replace1, "1")
                wn.onkeypress(replace2, "2")
                wn.onkeypress(replace3, "3")
            elif (cont_count == 2):
                ecard1.showturtle()
                ecard2.showturtle()
                ecard3.showturtle()
                if (card1_value == "Mushroom"):
                    mushroom()
                    card1_value = mushroom_value
                elif (card1_value == "Flower"):
                    flower()
                    card1_value = flower_value
                elif (card1_value == "Star"):
                    star()
                    card1_value = star_value
                elif (card1_value == "Bobomb"):
                    bobomb()
                    card1_value = bobomb_value
                elif (card1_value == "Egg"):
                    egg()
                    card1_value = egg_value
                elif (card1_value == "Goomba"):
                    goomba()
                    card1_value = goomba_value
                elif (card1_value == "Bowser"):
                    bowser()
                    card1_value = bowser_value
                if (card2_value == "Mushroom"):
                    mushroom()
                    card2_value = mushroom_value
                elif (card2_value == "Flower"):
                    flower()
                    card2_value = flower_value
                elif (card2_value == "Star"):
                    star()
                    card2_value = star_value
                elif (card2_value == "Bobomb"):
                    bobomb()
                    card2_value = bobomb_value
                elif (card2_value == "Egg"):
                    egg()
                    card2_value = egg_value
                elif (card2_value == "Goomba"):
                    goomba()
                    card2_value = goomba_value
                elif (card2_value == "Bowser"):
                    bowser()
                    card2_value = bowser_value
                if (card3_value == "Mushroom"):
                    mushroom()
                    card3_value = mushroom_value
                elif (card3_value == "Flower"):
                    flower()
                    card3_value = flower_value
                elif (card3_value == "Star"):
                    star()
                    card3_value = star_value
                elif (card3_value == "Bobomb"):
                    bobomb()
                    card3_value = bobomb_value
                elif (card3_value == "Egg"):
                    egg()
                    card3_value = egg_value
                elif (card3_value == "Goomba"):
                    goomba()
                    card3_value = goomba_value
                elif (card3_value == "Bowser"):
                    bowser()
                    card3_value = bowser_value
                if (ecard1_value == "Mushroom"):
                    mushroom()
                    ecard1_value = mushroom_value
                elif (ecard1_value == "Flower"):
                    flower()
                    ecard1_value = flower_value
                elif (ecard1_value == "Star"):
                    star()
                    ecard1_value = star_value
                elif (ecard1_value == "Bobomb"):
                    bobomb()
                    ecard1_value = bobomb_value
                elif (ecard1_value == "Egg"):
                    egg()
                    ecard1_value = egg_value
                elif (ecard1_value == "Goomba"):
                    goomba()
                    ecard1_value = goomba_value
                if (ecard2_value == "Mushroom"):
                    mushroom()
                    ecard2_value = mushroom_value
                elif (ecard2_value == "Flower"):
                    flower()
                    ecard2_value = flower_value
                elif (ecard2_value == "Star"):
                    star()
                    ecard2_value = star_value
                elif (ecard2_value == "Bobomb"):
                    bobomb()
                    ecard2_value = bobomb_value
                elif (ecard2_value == "Egg"):
                    egg()
                    ecard2_value = egg_value
                elif (ecard2_value == "Goomba"):
                    goomba()
                    ecard2_value = goomba_value
                if (ecard3_value == "Mushroom"):
                    mushroom()
                    ecard3_value = mushroom_value
                elif (ecard3_value == "Flower"):
                    flower()
                    ecard3_value = flower_value
                elif (ecard3_value == "Star"):
                    star()
                    ecard3_value = star_value
                elif (ecard3_value == "Bobomb"):
                    bobomb()
                    ecard3_value = bobomb_value
                elif (ecard3_value == "Egg"):
                    egg()
                    ecard3_value = egg_value
                elif (ecard3_value == "Goomba"):
                    goomba()
                    ecard3_value = goomba_value
                if (card1_value == 1.25) or (card1_value == 1.5) or (card1_value == 1.75):
                    player_score = (card2_value + card3_value) * card1_value
                    player_score = int(player_score)
                    if (player_score < 0):
                        player_score = 0
                elif (card2_value == 1.25) or (card2_value == 1.5) or (card2_value == 1.75):
                    player_score = (card1_value + card3_value) * card2_value
                    player_score = int(player_score)
                    if (player_score < 0):
                        player_score = 0
                elif (card3_value == 1.25) or (card3_value == 1.5) or (card3_value == 1.75):
                    player_score = (card2_value + card1_value) * card3_value
                    player_score = int(player_score)
                    if (player_score < 0):
                        player_score = 0
                else:
                    player_score = card1_value + card2_value + card3_value
                    player_score = int(player_score)
                    if (player_score < 0):
                        player_score = 0
                if (ecard1_value == 1.25) or (ecard1_value == 1.5) or (ecard1_value == 1.75):
                    enemy_score = (ecard2_value + ecard3_value) * ecard1_value
                    enemy_score = int(enemy_score)
                    if (enemy_score < 0):
                        enemy_score = 0
                elif (ecard2_value == 1.25) or (ecard2_value == 1.5) or (ecard2_value == 1.75):
                    enemy_score = (ecard1_value + ecard3_value) * ecard2_value
                    enemy_score = int(enemy_score)
                    if (enemy_score < 0):
                        enemy_score = 0
                elif (ecard3_value == 1.25) or (ecard3_value == 1.5) or (ecard3_value == 1.75):
                    enemy_score = (ecard2_value + ecard1_value) * ecard3_value
                    enemy_score = int(enemy_score)
                    if (enemy_score < 0):
                        enemy_score = 0
                else:
                    enemy_score = ecard1_value + ecard2_value + ecard3_value
                    enemy_score = int(enemy_score)
                    if (enemy_score < 0):
                        enemy_score = 0
                messanger.clear()
                messanger.penup()    
                messanger.goto(-160,-140)
                messanger.pendown()
                messanger.write(str(card1_value), font = ('Arial', 15, 'normal'))
                messanger.penup()    
                messanger.goto(-10,-140)
                messanger.pendown()
                messanger.write(str(card2_value), font = ('Arial', 15, 'normal'))
                messanger.penup()    
                messanger.goto(140,-140)
                messanger.pendown()
                messanger.write(str(card3_value), font = ('Arial', 15, 'normal'))
                messanger.penup()    
                messanger.goto(-160,140)
                messanger.pendown()
                messanger.write(str(ecard1_value), font = ('Arial', 15, 'normal'))
                messanger.penup()    
                messanger.goto(-10,140)
                messanger.pendown()
                messanger.write(str(ecard2_value), font = ('Arial', 15, 'normal'))
                messanger.penup()    
                messanger.goto(140,140)
                messanger.pendown()
                messanger.write(str(ecard3_value), font = ('Arial', 15, 'normal'))
                messanger.penup()    
                messanger.goto(-10,-75)
                messanger.pendown()
                messanger.write(str(player_score), font = ('Arial', 15, 'normal'))
                messanger.penup()    
                messanger.goto(-10,75)
                messanger.pendown()
                messanger.write(str(enemy_score), font = ('Arial', 15, 'normal'))
                if (player_score > 16) and (enemy_score > 16):
                    messanger.penup()
                    messanger.goto(-25,0)
                    messanger.pendown()
                    messanger.write("Draw!", font = ('Arial', 15, 'normal'))
                    coins = coins + betted_coins
                    betted_coins = 0
                    betpen.clear()
                    betpen.penup()
                    betpen.goto(-321,-75)
                    betpen.pendown()
                    betpen.write("Coins: " + str(coins), font = ('Arial', 15, 'normal'))
                    betpen.up()
                    betpen.goto(-321,75)
                    betpen.down()
                    betpen.write("Bet: " + str(betted_coins), font = ('Arial', 15, 'normal'))
                elif (player_score == enemy_score):
                    messanger.penup()
                    messanger.goto(-25,0)
                    messanger.pendown()
                    messanger.write("Draw!", font = ('Arial', 15, 'normal'))
                    coins = coins + betted_coins
                    betted_coins = 0
                    betpen.clear()
                    betpen.penup()
                    betpen.goto(-321,-75)
                    betpen.pendown()
                    betpen.write("Coins: " + str(coins), font = ('Arial', 15, 'normal'))
                    betpen.up()
                    betpen.goto(-321,75)
                    betpen.down()
                    betpen.write("Bet: " + str(betted_coins), font = ('Arial', 15, 'normal'))
                elif (player_score > enemy_score) and (player_score <= 16):
                    messanger.penup()
                    messanger.goto(-35,0)
                    messanger.pendown()
                    messanger.write("You win!", font = ('Arial', 15, 'normal')) 
                    coins = coins + betted_coins + betted_coins
                    betted_coins = 0
                    betpen.clear()
                    betpen.penup()
                    betpen.goto(-321,-75)
                    betpen.pendown()
                    betpen.write("Coins: " + str(coins), font = ('Arial', 15, 'normal'))
                    betpen.up()
                    betpen.goto(-321,75)
                    betpen.down()
                    betpen.write("Bet: " + str(betted_coins), font = ('Arial', 15, 'normal'))
                elif (player_score < enemy_score) and (enemy_score <= 16):  
                    messanger.penup()
                    messanger.goto(-35,0)
                    messanger.pendown()
                    messanger.write("You lose!", font = ('Arial', 15, 'normal')) 
                    coins = coins
                    betted_coins = 0
                    betpen.clear()
                    betpen.penup()
                    betpen.goto(-321,-75)
                    betpen.pendown()
                    betpen.write("Coins: " + str(coins), font = ('Arial', 15, 'normal'))
                    betpen.up()
                    betpen.goto(-321,75)
                    betpen.down()
                    betpen.write("Bet: " + str(betted_coins), font = ('Arial', 15, 'normal'))
                elif (player_score >= 17):
                    messanger.penup()
                    messanger.goto(-35,0)
                    messanger.pendown()
                    messanger.write("You lose!", font = ('Arial', 15, 'normal')) 
                    coins = coins
                    betted_coins = 0 
                    betpen.clear()
                    betpen.penup()
                    betpen.goto(-321,-75)
                    betpen.pendown()
                    betpen.write("Coins: " + str(coins), font = ('Arial', 15, 'normal'))
                    betpen.up()
                    betpen.goto(-321,75)
                    betpen.down()
                    betpen.write("Bet: " + str(betted_coins), font = ('Arial', 15, 'normal'))
                elif (enemy_score >= 17):
                    messanger.penup()
                    messanger.goto(-35,0)
                    messanger.pendown()
                    messanger.write("You win!", font = ('Arial', 15, 'normal')) 
                    coins = coins + betted_coins + betted_coins
                    betted_coins = 0
                    betpen.clear()
                    betpen.penup()
                    betpen.goto(-321,-75)
                    betpen.pendown()
                    betpen.write("Coins: " + str(coins), font = ('Arial', 15, 'normal'))
                    betpen.up()
                    betpen.goto(-321,75)
                    betpen.down()
                    betpen.write("Bet: " + str(betted_coins), font = ('Arial', 15, 'normal'))
            elif (cont_count == 3):
                if (coins > 99):
                    messanger.clear()
                    betpen.clear()
                    drawer.clear()
                    coin_pic.hideturtle()
                    pen2.clear()
                    card1.hideturtle()
                    card2.hideturtle()
                    card3.hideturtle()
                    ecard1.hideturtle()
                    ecard2.hideturtle()
                    ecard3.hideturtle()
                    decoy1.hideturtle()
                    decoy2.hideturtle()
                    decoy3.hideturtle()
                    legend.hideturtle()
                    wn.bgcolor("lime")
                    messanger.penup()
                    messanger.goto(-160,0)
                    messanger.pendown()
                    messanger.write("Congratulations, you hit the jackpot!", font = ('Arial', 15, 'normal'))
                    messanger.speed(1)
                    messanger.penup()
                    messanger.goto(777,777)
                    quit()
                elif (coins == 0):
                    messanger.clear()
                    betpen.clear()
                    drawer.clear()
                    coin_pic.hideturtle()
                    pen2.clear()
                    card1.hideturtle()
                    card2.hideturtle()
                    card3.hideturtle()
                    ecard1.hideturtle()
                    ecard2.hideturtle()
                    ecard3.hideturtle()
                    decoy1.hideturtle()
                    decoy2.hideturtle()
                    decoy3.hideturtle()
                    legend.hideturtle()
                    wn.bgcolor("red")
                    messanger.penup()
                    messanger.goto(-160,0)
                    messanger.pendown()
                    messanger.write("Uh oh, you're out of money! It's over...", font = ('Arial', 15, 'normal'))
                    messanger.speed(1)
                    messanger.penup()
                    messanger.goto(777,777)
                    quit()
                else:
                    cont_count = 0
                    which_card = 0
                    holding_list = ["Mushroom", "Flower", "Star", "Bobomb", "Egg", "Goomba", "Bowser"]
                    card_list = ["Mushroom", "Flower", "Star", "Bobomb", "Egg", "Goomba", "Bowser"]
                    eholding_list = ["Mushroom", "Flower", "Star", "Bobomb", "Egg", "Goomba"]
                    ecard_list = ["Mushroom", "Flower", "Star", "Bobomb", "Egg", "Goomba"]
                    pow_list = ["Mushroom", "Flower", "Star", "Goomba", "Egg"]
                    replace_count = 0
                    card1_value = 0
                    card2_value = 0
                    card3_value = 0
                    ecard1_value = 0
                    ecard2_value = 0
                    ecard3_value = 0
                    messanger.clear()
                    card1.hideturtle()
                    card2.hideturtle()
                    card3.hideturtle()
                    ecard1.hideturtle()
                    ecard2.hideturtle()
                    ecard3.hideturtle()
                    run()
pow_list = ["Mushroom", "Flower", "Star", "Goomba", "Egg"]
replace_count = 0
def replace1():
    global replace_count
    global card1_value
    if (cont_count == 1):
        if (replace_count == 0):
            replacement = random.choice(pow_list)
            if (replacement == "Mushroom"):
                card1.shape("mushroom.gif")
                card1_value = "Mushroom"
            elif (replacement == "Flower"):
                card1.shape("flower.gif")
                card1_value = "Flower"
            elif (replacement == "Star"):
                card1.shape("star.gif")
                card1_value = "Star"
            elif (replacement == "Egg"):
                card1.shape("egg.gif")
                card1_value = "Egg"
            elif (replacement == "Goomba"):
                card1.shape("goomba.gif")
                card1_value = "Goomba"
        else:
            messanger.penup()
            messanger.goto(-150,0)
            messanger.pendown()
            messanger.clear()
            messanger.write("Only 1 swap allowed, press continue!", font = ('Arial', 15, 'normal'))
        replace_count = replace_count + 1
def replace2():
    global replace_count
    global card2_value
    if (cont_count == 1):
        if (replace_count == 0):
            replacement = random.choice(pow_list)
            if (replacement == "Mushroom"):
                card2.shape("mushroom.gif")
                card2_value = "Mushroom"
            elif (replacement == "Flower"):
                card2.shape("flower.gif")
                card2_value = "Flower"
            elif (replacement == "Star"):
                card2.shape("star.gif")
                card2_value = "Star"
            elif (replacement == "Egg"):
                card2.shape("egg.gif")
                card2_value = "Egg"
            elif (replacement == "Goomba"):
                card2.shape("goomba.gif")
                card2_value = "Goomba"
        else:
            messanger.penup()
            messanger.goto(-170,0)
            messanger.pendown()
            messanger.clear()
            messanger.write("Only 1 swap allowed, press continue!", font = ('Arial', 15, 'normal'))
        replace_count = replace_count + 1
def replace3():
    global replace_count
    global card3_value
    if (cont_count == 1):
        if (replace_count == 0):
            replacement = random.choice(pow_list)
            if (replacement == "Mushroom"):
                card3.shape("mushroom.gif")
                card3_value = "Mushroom"
            elif (replacement == "Flower"):
                card3.shape("flower.gif")
                card3_value = "Flower"
            elif (replacement == "Star"):
                card3.shape("star.gif")
                card3_value = "Star"
            elif (replacement == "Egg"):
                card3.shape("egg.gif")
                card3_value = "Egg"
            elif (replacement == "Goomba"):
                card3.shape("goomba.gif")
                card3_value = "Goomba"
        else:
            messanger.penup()
            messanger.goto(-170,0)
            messanger.pendown()
            messanger.clear()
            messanger.write("Only 1 swap allowed, press continue!", font = ('Arial', 15, 'normal'))
        replace_count = replace_count + 1
def run():
    global card_list
    global ecard_list
    draw(card1, card_list)
    draw(card2, card_list)
    draw(card3, card_list)
    card_list = holding_list
    draw(ecard1, ecard_list)
    draw(ecard2, ecard_list)
    draw(ecard3, ecard_list)
    ecard_list = eholding_list
    coin_pic.goto(-290,15)
    coin_pic.showturtle()
    card1.goto(-150,-250)
    card2.goto(0,-250)
    card3.goto(150,-250)
    ecard1.goto(-150,250)
    ecard2.goto(0,250)
    ecard3.goto(150,250)
    decoy1.goto(-150,250)
    decoy2.goto(0,250)
    decoy3.goto(150,250)
    card1.showturtle()
    card2.showturtle()
    card3.showturtle()
    decoy1.showturtle()
    decoy2.showturtle()
    decoy3.showturtle()
    messanger.hideturtle()
    messanger.penup()
    messanger.goto(-150,0)
    messanger.pendown()
    betpen.hideturtle()
    betpen.penup()
    betpen.goto(-321,-75)
    betpen.pendown()
    messanger.write("Choose amount of coins to bet!", font = ('Arial', 15, 'normal'))
    betpen.write("Coins: " + str(coins), font = ('Arial', 15, 'normal'))
    betpen.up()
    betpen.goto(-321,75)
    betpen.down()
    betpen.write("Bet: " + str(betted_coins), font = ('Arial', 15, 'normal'))
def coin():
    global coins
    global betted_coins
    if (cont_count == 0) and (coins > 0):
        coins -= 1
        betted_coins += 1
        betpen.clear()
        betpen.penup()
        betpen.goto(-321,-75)
        betpen.pendown()
        betpen.write("Coins: " + str(coins), font = ('Arial', 15, 'normal'))
        betpen.up()
        betpen.goto(-321,75)
        betpen.down()
        betpen.write("Bet: " + str(betted_coins), font = ('Arial', 15, 'normal'))
    else:
        betpen.penup()
field()
draw_cont(pen2)
run()
wn.onkeypress(coin,"c")
trtl.onscreenclick(cont)
wn.mainloop()
