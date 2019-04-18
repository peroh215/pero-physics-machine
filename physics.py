#/usr/bin/env python

print("\nStarting program...")

from decimal import *
from os import system as sys
from platform import system
from colorama import init, Fore, Back, Style

# Color-related
init(autoreset=False) # Initialize colorama

class Color():
    def __init__(self, background, foreground, style):
        self.background = background
        self.foreground = foreground
        self.style = style

class ColorScheme():
    def __init__(self, title, options, text, nums, special, specialTitle):
        self.title = title
        self.options = options
        self.text = text
        self.nums = nums
        self.special = special
        self.specialTitle = specialTitle

title = Color(Back.GREEN, Fore.WHITE, Style.BRIGHT)
option = Color(Back.BLACK, Fore.GREEN, Style.BRIGHT)
text = Color(Back.BLACK, Fore.WHITE, Style.NORMAL)
num = Color(Back.BLACK, Fore.WHITE, Style.BRIGHT)
special = Color(Back.BLACK, Fore.CYAN, Style.NORMAL)
specialTitle = Color(Back.CYAN, Fore.WHITE, Style.BRIGHT)

CS = ColorScheme(title, option, text, num, special, specialTitle)

def setColor(color):
    print(color.background + color.foreground + color.style, end='')

def unsetColor():
    print(Style.RESET_ALL, end='')

def printColored(text, color):
    setColor(color)
    print(text, end='')
    unsetColor()

# Funcs
mVelocity = lambda S1, S2, t1, t2 : (S2 - S1) / (t2 - t1)
mAcceleration = lambda v1, v2, t1, t2 : (v2 - v1) / (t2 - t1)
distanceTraveled = lambda v1, v2, t1, t2 : (v2 - v1) * (t2 - t1)

def clear(sclear, clearcmd):
    if (sclear == True):
        sys(clearcmd)
    else:
        print('\n', end='')

def printTitle(title, cs):
    setColor(cs.title)
    print(title, end='\n')
    unsetColor()

def printSTitle(title, cs):
    setColor(cs.specialTitle)
    print(title, end='\n')
    unsetColor()

def printOptions(options, cs, pre=''):
    print(pre)
    for option, desc in options.items():
        setColor(cs.options)
        print(option, end=' ')
        setColor(cs.text)
        print(desc + '\n')
    unsetColor()

def coloredInput(prompt, CS):
    setColor(CS.special)
    print(prompt, end='')
    setColor(CS.nums)
    i = Decimal(input())
    unsetColor()
    return i

def coloredDisplay(text, data, CS):
    setColor(CS.special)
    print(str(text), end='')
    setColor(CS.nums)
    print(str(data), end='')

def coloredFormula(formula, CS):
    setColor(CS.special)
    print(" (", end='')
    for num, operation in formula.items():
        setColor(CS.nums)
        print(str(num), end='')
        setColor(CS.special)
        print(str(operation), end='')
    print(')')

def enterToContinue():
    unsetColor()
    print("\nPress", end=' ')
    setColor(CS.special)
    print("ENTER", end=' ')
    unsetColor()
    print("to continue...", end='')
    input()

# Setup
sclear = True
clearcmd = ''
osystem = system()
print(osystem, "detected")
if ("windows" in str(osystem).lower()): clearcmd = "cls"
elif ("linux" in str(osystem).lower()): clearcmd = "clear"
else: 
    print("ERROR: System doesn't support terminal cleaning")
    sclear = False

getcontext().prec = 16 # Decimal precision

# Main
while True:
    clear(sclear, clearcmd)
    printTitle("Pero's Physics Machine (PPM)", CS)
    unsetColor()
    printOptions({'[1]' : 'Formulas', '[2]' : 'Convert unit', '[3]' : 'Settings', '[Exit]' : ''}, CS)
    
    inp = input("> ")

    if (inp == '1'):
        # Velocity
        clear(sclear, clearcmd)
        printTitle("Formulas", CS)
        printOptions({"[1]" : "Medium velocity", "[2]" : "Distance travelled", "[3]" : "Mass to newtons", "[Back]" : ''}, CS)
        inp = input("> ")

        if (inp == '1'):
            # Medium velocity
            clear(sclear, clearcmd)
            t1 = Decimal(input("\nStarting time (secs): "))
            t2 = Decimal(input("\nFinishing time (secs): "))
            S1 = Decimal(input("\nStarting distance (m): "))
            S2 = Decimal(input("\nFinishing distance (m): "))
            mv = mVelocity(S1, S2, t1, t2)
            print("\nMedium velocity:", mv, "m/s\n")

        elif (inp == '2'):
            # Distance travelled
            clear(sclear, clearcmd)

        elif (inp == '3'):
            # Mass to newtons
            clear(sclear, clearcmd)
            printSTitle("Mass to newtons", CS)
            m = coloredInput("\nMass (kg): ", CS)
            a = coloredInput("Acceleration (m/s²): ", CS)
            n = m*a

            coloredDisplay("\nForce (N): ", n, CS)
            coloredFormula({ str(m) : " x ", str(a) : " = ", str(n) : 'N'}, CS)
            enterToContinue()

        elif (inp.lower() == 'back'):
            continue

    elif (inp == '2'):
        # Convert unit
        clear(sclear, clearcmd)
        printTitle("Unity conversion", CS)
        printOptions({"[1]" : "Km/h to m/s", "[2]" : "M/s to km/h", "[3]" : "Mph to km/h", "[4]" : "Km/h to mph", "[5]" : "Mph to m/s", "[6]" : "M/s to mph", "[Back]" : ''}, CS)

        unit1 = 'ERROR'
        multi = Decimal(0)
        div = False
        inp = input("> ")

        if (inp == '1'):
            multi = Decimal(3.6)
            unit1 = "Km/h"
            unit2 = "m/s"
            div = True
        elif (inp == '2'):
            multi = Decimal(3.6)
            unit1 = "M/s"
            unit2 = "km/h"
            div = False
        elif (inp == '3'):
            multi = Decimal(1.609344)
            unit1 = "Km/h"
            unit2 = "mph"
            div = True
        elif (inp == '4'):
            multi = Decimal(1.609344)
            unit1 = "Mph"
            unit2 = "km/h"
            div = False
        elif (inp == '5'):
            multi = Decimal(0.44704)
            unit1 = "Mph"
            unit2 = "m/s"
            div = True
        elif (inp == '6'):
            multi = Decimal(0.44704)
            unit1 = "Mph"
            unit2 = "m/s"
            div = False
        elif (inp.lower() == 'back'):
            continue

        clear(sclear, clearcmd)
        printSTitle(str(unit1 + ' to ' + unit2), CS)
        setColor(CS.special)
        print('\n' + unit1 + ': ', end='')
        setColor(CS.nums)
        uv1 = Decimal(input())
        unsetColor()

        t = 0
        if (div == False): t = uv1 * multi
        else: t = uv1 / multi

        #clear(sclear, clearcmd)
        print('\n', end='')
        setColor(CS.nums)
        print(uv1, end=' ')
        setColor(CS.special)
        print(unit1, end='')
        setColor(CS.special)
        print(" = ", end='')
        setColor(CS.nums)
        print(t, end=' ')
        setColor(CS.special)
        print(unit2)
        unsetColor()

        enterToContinue()

    elif (inp == '3'):
        while True:
            clear(sclear, clearcmd)
            printTitle("Settings", CS)
            setColor(CS.options)
            print("\n[1]", end=' ')
            setColor(CS.text)
            print("Decimal precision:", end=' ')
            setColor(CS.nums)
            print(getcontext().prec - 1)
            setColor(CS.options)
            print("\n[2]", end=' ')
            setColor(CS.text)
            print("Terminal cleaning:", end=' ')
            setColor(CS.nums)
            print(sclear)
            setColor(CS.options)
            print("\n[Back]")
            setColor(CS.text)
            inp = input("\n> ")

            if (inp == '1'):
                # Decimal precision
                getcontext().prec = (int(input("\nDecimal precision: ")) + 1)
            elif (inp == '2'):
                # Terminal cleaning
                while True:
                    print("\nTerminal cleaning:", end=' ')
                    setColor(CS.nums)
                    inp = input()
                    unsetColor()
                    if (inp.lower() == "true"):
                        sclear = True
                        break
                    elif (inp.lower() == "false"):
                        sclear = False
                        break
                    else:
                        print("Invalid value, use \"True\" or \"False\"")
                        continue
            elif (inp.lower() == 'back'):
                break
                continue

    elif (inp.lower() == 'exit'):
        exit(0)
