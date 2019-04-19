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
    def __init__(self, title, options, text, nums, special, specialTitle, error, errordesc):
        self.title = title
        self.options = options
        self.text = text
        self.nums = nums
        self.special = special
        self.specialTitle = specialTitle
        self.error = error
        self.errordesc = errordesc

title = Color(Back.GREEN, Fore.WHITE, Style.BRIGHT)
option = Color(Back.BLACK, Fore.GREEN, Style.BRIGHT)
text = Color(Back.BLACK, Fore.WHITE, Style.NORMAL)
num = Color(Back.BLACK, Fore.WHITE, Style.BRIGHT)
special = Color(Back.BLACK, Fore.CYAN, Style.NORMAL)
specialTitle = Color(Back.CYAN, Fore.WHITE, Style.BRIGHT)
error = Color(Back.RED, Fore.RED, Style.BRIGHT)
errordesc = Color(Back.BLACK, Fore.RED, Style.NORMAL)

CS = ColorScheme(title, option, text, num, special, specialTitle, error, errordesc)

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

def displayError(error, CS):
    setColor(CS.error)
    print("\nERROR:", end='')
    setColor(CS.errordesc)
    print('', e)
    unsetColor()
    

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
        while True:
            clear(sclear, clearcmd)
            printTitle("Formulas", CS)
            printOptions({"[1]" : "Medium velocity", "[2]" : "Distance travelled", "[3]" : "Mass to newtons", "[Back]" : ''}, CS)
            inp = input("> ")

            if (inp == '1'):
                # Medium velocity
                clear(sclear, clearcmd)
                printSTitle("Medium velocity", CS)

                # Starting time
                setColor(CS.text)
                print("\nStarting time", end=' ')
                setColor(CS.special)
                print("(secs)", end='')
                setColor(CS.text)
                t1 = Decimal(input(": "))

                # Finishing time
                setColor(CS.text)
                print("\nFinishing time", end=' ')
                setColor(CS.special)
                print("(secs)", end='')
                setColor(CS.text)
                t2 = Decimal(input(": "))

                # Starting distance
                setColor(CS.text)
                print("\nStarting distance", end=' ')
                setColor(CS.special)
                print("(m)", end='')
                setColor(CS.text)
                S1 = Decimal(input(": "))

                # Finishing distance
                setColor(CS.text)
                print("\nFinishing distance", end=' ')
                setColor(CS.special)
                print("(m)", end='')
                setColor(CS.text)
                S2 = Decimal(input(": "))

                mv = mVelocity(S1, S2, t1, t2)
                print("\nMedium velocity:", mv, "m/s\n")

                enterToContinue()
                break

            elif (inp == '2'):
                # Distance travelled
                clear(sclear, clearcmd)
                break

            elif (inp == '3'):
                # Mass to newtons
                clear(sclear, clearcmd)
                printSTitle("Mass to newtons", CS)
                while True:
                    try:
                        m = coloredInput("\nMass (kg): ", CS)
                        a = coloredInput("Acceleration (m/s²): ", CS)
                        break
                    except Exception as e:
                        displayError(e, CS)
                n = m*a
                coloredDisplay("\nForce (N): ", n, CS)
                coloredFormula({ str(m) : " x ", str(a) : " = ", str(n) : 'N'}, CS)
                enterToContinue()
                break

            elif (inp.lower() == 'back'):
                break

    elif (inp == '2'):
        # Convert unit
        while True:
            clear(sclear, clearcmd)
            printTitle("Unity conversion", CS)
            printOptions({"[1]" : "Km/h to m/s", "[2]" : "M/s to km/h", "[3]" : "Mph to km/h", "[4]" : "Km/h to mph", "[5]" : "Mph to m/s", "[6]" : "M/s to mph", "[Back]" : ''}, CS)

            try:
                inp = input("> ")
            except Exception as e:
                displayError(e, CS)

            unit1 = 'ERROR'
            unit2 = 'ERROR'
            multi = Decimal(0)
            div = False

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
                unit1 = "Mph"
                unit2 = "km/h"
                div = True
            elif (inp == '4'):
                multi = Decimal(1.609344)
                unit1 = "Km/h"
                unit2 = "mph"
                div = False
            elif (inp == '5'):
                multi = Decimal(0.44704)
                unit1 = "M/s"
                unit2 = "Mph"
                div = True
            elif (inp == '6'):
                multi = Decimal(0.44704)
                unit1 = "Mph"
                unit2 = "m/s"
                div = False
                break
            elif (inp.lower() == 'back'):
                break
            else:
                continue
            break

        clear(sclear, clearcmd)
        printSTitle(str(unit1 + ' to ' + unit2), CS)
        while True:
            try:
                setColor(CS.special)
                print('\n' + unit1 + ': ', end='')
                setColor(CS.nums)
                uv1 = Decimal(input())
                unsetColor()
                break
            except Exception as e:
                displayError(e, CS)
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
                while True:
                    try:
                        getcontext().prec = (int(input("\nDecimal precision: ")) + 1)
                        break
                    except Exception as e:
                        displayError(e, CS)
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
