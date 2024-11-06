import os
from pint import UnitRegistry
import pyanimalconverter.convert as convert

ureg = UnitRegistry()
Q_ = ureg.Quantity

def talk(rightText="",leftText=""):
    one_speechBubbleTop = '''
                                            ----------------------------------
    '''
    one_speechBubbleBottom = '''
                                            ---   _---------------------------
                                              / _/
                                             //
    '''
    middleText = f'''
              {leftText}                                   {rightText}
    '''
    both_speechBubbleTop = '''
        -----------------------------       ----------------------------------
    '''
    both_speechBubbleBottom = '''
        ----_   ---------------------       ---   _---------------------------
            \\ _\\                              / _/
                \\                           //
    '''
    animal = '''
                        _           _ 
            __   ___.--'_`.       .'_`--.___   __
            ( _`.'. -   'o` )     ( 'o`   - .`.'_ )
            _\\.'_'      _.-'       `-._      `_`./_
            ( \\`. )    //\\`           '/\\    ( .'/ )
             \\_`-'`---'\\__,         ,__//`---'`-'_/
              \\`        `-\\           /-'        '/
               `                                 '   
    '''
    if(leftText==""):
        return one_speechBubbleTop + middleText + one_speechBubbleBottom + animal
    else:
        return both_speechBubbleTop + middleText + both_speechBubbleBottom + animal

def askAnimal():
    navigation = "menu";
    while(True):
        os.system('clear');
        if(navigation=="menu"):
            print(talk("Ribbit, what do you want?"))
            menuInput = input("I want to (CONVERT/COMPARE) some numbers: ").upper()
            print(menuInput);
            if(menuInput=="CONVERT"):
                navigation="convert";
            elif(menuInput=="COMPARE"):
                navigation="compare";
        if(navigation=="convert"):
            os.system('clear');
            print(talk("Ribbit, ok, what number do you want to convert?","I want to convert a number!"));
            while(True):
                convertFrom = input("Enter the number with units (e.g. 1 kg, 5 kg) you want to convert (or MENU to cancel): ");
                if "MENU" or "menu" in convertFrom:
                    navigation="menu";
                    break;
                try:
                    convertFrom_num = Q_(convertFrom);
                    fromUnit = ureg.parse_expression(convertFrom.split(" ")[1])
                    fromUnit_two = convertFrom.split(" ")[1]
                except Exception as e:
                    os.system('clear');
                    print(e);
                    print(talk("I don't understand, please tell me a number with the right format - ribbit!"));
                    continue;
                else:
                    os.system('clear');
                    print(convertFrom_num.magnitude);
                    print(convertFrom_num.units);
                    print(talk("What do you want to convert this number to?",f"{convertFrom_num.magnitude} {convertFrom_num.units}"))
                    while(True):
                        try:
                            convertTo = input("Enter unit type (e.g. kg, cm, lb): ")
                            # print(convert.convert(convertFrom_num.magnitude, "km", "meter"))
                            finalAnswer = convert.convert(convertFrom_num.magnitude, fromUnit_two, convertTo)
                        except Exception as e:
                            os.system('clear');
                            print(e);
                            print(talk("I can't interpret this unit. Please give me another unit type or retype!"));
                            continue;
                        else:
                            os.system('clear')
                            print(talk(f"{finalAnswer} {convertTo}"));
                            break;
                    menuInput = input("Ask the frog to convert another number? (Y/N): ")
                    if(menuInput == "N"):
                        navigation="menu"
                        break
                    else:
                        os.system('clear')
                        print(talk("Ribbit, ok.. what number?","'Scuse me, can you convert another number?"));

                    
        #     if(menuInput == "N"):
        #         break
        #             print("Unit is not valid!", file=sys.stderr)
        #             print(talk(rightText="I can't understand that Ribbit."))
        #         else:
        #             os.system('clear');
        #             print(talk("Ribbit. Ok seems doable. Which unit would you like to convert to?", "I want to convert " + convertFrom))
        #             convertTo = input("Enter the unit to convert to: ")
        #             try:
        #                 toUnit = ureg.parse_expression(convertTo)
        #             except Exception:
        #                 print("Unit is not valid!", file=sys.stderr)
        #                 print(talk(rightText="I can't understand that Ribbit. Try again."))
        #             else:
        #                 result = convert.convert(convertFrom_num, fromUnit, toUnit)
        #                 print(talk("The answer is " + result,"What's the result?"))
        #                 cont = input("Enter to continue: ")
        #                 break;
                        
        # menuInput = input("Continue? (Y/N): ")
        if(menuInput == "compare"):
            os.system('clear')
            print(talk("What's the first number?"));
            while(True):
                compareFirst = input("Enter a number with units (e.g. 1 kg, 5 kg) you want to compare: ");
                if "MENU" or "menu" in compareFirst:
                    navigation="menu";
                    break;
                try:
                    compareFirst_num = Q_(compareFirst);
                    compareFirst_unit = convertFrom.split(" ")[1]
                except Exception as e:
                    os.system('clear');
                    print(e);
                    print(talk("I don't understand, please tell me a number with the right format - ribbit!"));
                    continue;
                else:
                    os.system('clear');
                    print(talk(f"What number do you want me to compare {compareFirst} with?",f"{compareFirst_num.magnitude} {compareFirst_num.units}"))
                    while(True):
                        try:
                            compareSecond = input("Enter a number with units (e.g. 1 kg, 5 kg) you want to compare with: ")
                            compareSecond_num = Q_(compareSecond);  # just to check if user input in the right format
                            compareSecond_unit = compareSecond.split(" ")[1]    # to extract the unit from the original input str
                            # print(convert.convert(convertFrom_num.magnitude, "km", "meter"))
                            finalAnswer = convert.compare(compareFirst_num.magnitude, compareSecond_num.magnitude, compareFirst_unit, compareSecond_unit)
                        except Exception as e:
                            os.system('clear');
                            print(e);
                            print(talk("I can't interpret this unit. Please give me another unit type or retype!"));
                            continue;
                        else:
                            os.system('clear')
                            print(talk("CODE TO BE WRITTEN")); # TODO: say which number (in its original pre-conversion form) is bigger
                            break;
                    menuInput = input("Ask the frog to compare more numbers? (Y/N): ")
                    if(menuInput == "N"):
                        navigation="menu"
                        break
                    else:
                        os.system('clear')
                        print(talk("Ribbit, ok.. what number?","'Scuse me, can you compare some other numbers?"));


askAnimal();