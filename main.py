from datafile import resources,MENU
from os import system
# TODO 1:ask user what it wants?
quater, nickel, dime, penny=.25, .05, .1,.01
latte_cost,es_cost,capa_cost=MENU['latte']['cost'],MENU['espresso']['cost'],MENU['cappuccino']['cost']


es_water,latte_water,capu_water=MENU['espresso']['ingredients']['water'],MENU['latte']['ingredients']['water'],MENU['cappuccino']['ingredients']['water']
latte_milk,capu_milk=MENU['latte']['ingredients']['milk'],MENU['cappuccino']['ingredients']['milk']
es_coffee,latte_coffee,capu_coffee=MENU['espresso']['ingredients']['coffee'],MENU['latte']['ingredients']['coffee'],MENU['cappuccino']['ingredients']['coffee']
cup_sale=0
order = input("What do u want(1.espresso,2.latte,3.cappuccino:  )").lower()
while order=='report'or order=='1' or order=='2'or order=='3'or order=='sales':

# TODO 2:print report when user types the report after repeat 1
    water,milk,coffee = resources['water'],resources['milk'],resources['coffee']
    if order == 'report':
        print(f"water = ",water,"\n milk = ",milk, "\ncoffee = ",coffee)
        order = input("What do u want(1.espresso,2.latte,3.cappuccino:  )").lower()
        continue
#todo 3: check resources are sufficient,ask for coins: , if yes check coins are sufficient
#espresso order
    elif order =='1' or order =='espresso':
        if water >= es_water and coffee>= es_coffee:
            quater = float(input("enter quater: "))
            dime=float(input("enter dime: "))
            nickel = float(input("enter nickel: "))
            penny= float(input("enter penny: "))
            if quater / 4>=es_cost or nickel / 20>=es_cost or dime / 10>=es_cost or penny / 100>=es_cost:
                print(f"transaction successfull: \n enjoy you order: espresso")
                resources['water']=resources['water']-es_water
                resources['coffee']=resources['coffee']-es_coffee
                cup_sale+=1
                order = input("What do u want(1.espresso,2.latte,3.cappuccino:  )").lower()
                continue
            else:
                print("Not enough money espresso for :$1.5 ")
                order = input("What do u want(1.espresso,2.latte,3.cappuccino:  )").lower()
                continue
        else:
            print("not enough resources")
            order = input("What do u want(1.espresso,2.latte,3.cappuccino:  )").lower()
            continue
#latte
    elif order =='2' or order =='latte':
        if water >= latte_water and coffee>= latte_coffee and milk >=latte_milk:
            quater = float(input("enter quater: "))
            dime=float(input("enter dime: "))
            nickel = float(input("enter nickel: "))
            penny= float(input("enter penny: "))
            if quater / 4>=latte_cost or nickel / 20>=latte_cost or dime / 10>=latte_cost or penny / 100>=latte_cost:
                print(f"transaction successfull: \n enjoy you order: latte")
                resources['water']=resources['water']-latte_water
                resources['coffee']=resources['coffee']-latte_coffee
                resources['milk'] = resources['milk'] - latte_milk
                cup_sale+=1
                order = input("What do u want(1.espresso,2.latte,3.cappuccino:  )").lower()
                continue
            else:
                print("Not enough money espresso for :$1.5 ")
                order = input("What do u want(1.espresso,2.latte,3.cappuccino:  )").lower()
                continue
        else:
            print("not enough resources")
            order = input("What do u want(1.espresso,2.latte,3.cappuccino:  )").lower()
            continue
#cappuccino
    elif order == '3' or order == 'cappuccino':
        if water >= capu_water and coffee>= capu_coffee and milk >=capu_milk:
            quater = float(input("enter quater: "))
            dime=float(input("enter dime: "))
            nickel = float(input("enter nickel: "))
            penny= float(input("enter penny: "))
            if quater / 4>=capa_cost or nickel / 20>=capa_cost or dime / 10>=capa_cost or penny / 100>=capa_cost:
                print(f"transaction successfull: \n enjoy you order: cappuccino")
                resources['water']=resources['water']-capu_water
                resources['coffee']=resources['coffee']-capu_coffee
                resources['milk'] = resources['milk'] - capu_milk
                cup_sale+=1
                order = input("What do u want(1.espresso,2.latte,3.cappuccino:  )").lower()
                continue
            else:
                print("Not enough money espresso for :$1.5 ")
                order = input("What do u want(1.espresso,2.latte,3.cappuccino:  )").lower()
                continue
        else:
            print("not enough resources")
            order = input("What do u want(1.espresso,2.latte,3.cappuccino:  )").lower()
            continue
#sales report
    elif order=='sales':
        print("total sales:",cup_sale)
        order = input("What do u want(1.espresso,2.latte,3.cappuccino:  )").lower()
        continue
    else:
        order = input("What do u want(1.espresso,2.latte,3.cappuccino:  )").lower()
        continue


# TODO 4:print transaction successfull , return refund , serve coffee .
