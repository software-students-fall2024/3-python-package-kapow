import os

def talk(leftText="",rightText=""):
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
            \ _\                              / _/
                \\                           //
    '''
    animal = '''
                        _           _ 
            __   ___.--'_`.       .'_`--.___   __
            ( _`.'. -   'o` )     ( 'o`   - .`.'_ )
            _\.'_'      _.-'       `-._      `_`./_
            ( \`. )    //\`           '/\\    ( .'/ )
             \_`-'`---'\\__,         ,__//`---'`-'_/
              \`        `-\           /-'        '/
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
            print(talk("","Ribbit, what do you want?"))
        
        menuInput = input("I want to (CONVERT/COMPARE) some numbers: ")
        print(menuInput);
        menuInput = input("Continue? (Y/N): ")
        if(menuInput == "N"):
            break

askAnimal();