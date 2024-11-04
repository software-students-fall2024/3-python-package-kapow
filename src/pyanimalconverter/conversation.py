import os
import convert
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
        if(navigation=="convert"):
            os.system('clear');
            print(talk("Ribbit, ok, what number do you want to convert?","I want to convert a number!"));
            validUnit = True;
            while(True):
                convertFrom = input("Enter the number with units (e.g. 1 kg, 5 kg) you want to convert: ");
                try:
                    convertFrom_num = Q_(convertFrom);
                    fromUnit = ureg.parse_expression(convertFrom.split(" ")[1])
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
                            finalAnswer = convert.convert(convertFrom_num.magnitude, convertFrom_num.units, convertTo)
                            print('good')
                        except Exception as e:
                            os.system('clear');
                            print(e);
                            print(talk("I can't interpret this unit. Please give me another unit type or retype!"));
                            continue;
                        else:
                            os.system('clear')
                            print(talk(f"{finalAnswer.magnitude} {finalAnswer.units}"));
                            break;
                    break;
            menuInput = input("Continue? (Y/N): ")
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
        # if(menuInput == "N"):
        #     break

askAnimal();