stages = [ r'''
 +---+
 |   |
     |
     |
     |
     |
=========''',r'''
 +---+
 |   |
 O   |
     |
     |
     |
=========''',r'''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========''', r'''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', r'''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', r'''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', r'''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

logo = r'''
 _   _    _    _   _  ____ __  __    _    _   _
| | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
| |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
|  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
|_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_|
'''

win_logo = r'''
Y   Y  OOO  U   U    W   W  III  N   N
 Y Y  O   O U   U    W   W   I   NN  N
  Y   O   O U   U    W W W   I   N N N
  Y   O   O U   U    WW WW   I   N  NN
  Y    OOO   UUU     W   W  III  N   N
'''


lose_logo = r'''
Y   Y  OOO  U   U    L     OOO   SSSS  EEEEE
 Y Y  O   O U   U    L    O   O S     E
  Y   O   O U   U    L    O   O  SSS  EEEE
  Y   O   O U   U    L    O   O     S E
  Y    OOO   UUU     LLLL  OOO  SSSS  EEEEE
'''