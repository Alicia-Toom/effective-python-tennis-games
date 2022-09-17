# effective-python-tennis-games

The purpose of this repository is do a refactoring assignment for the course effitive python course for Teknikhögskolan in Gothenburg. 

Instruction: 
You work at a consulting company and one of your colleagues has worked for the Tennis Association. The contract is for 10 hours of work and your colleague has spent 8.5 hours on it. Unfortunately, he has now fallen ill. He says he has completed the work, and all tests pass. Your boss has asked you to take over for him. She wants you to spend an hour or so on the code so she can bill the client for the full 10 hours. She wants to tidy things up a bit and maybe make a better version. In the attached file you will find a couple of "Classes" that your colleague said do the same thing and one of them is a little better. 

We would like to do: 

1-Read the attached file and document and comment on what your colleague has already done.

2-Show what pylint score you get for both classes.

3- Create "main" or "run" that you can dem the functions that exist, you can do simulation for 3-4 different moments during match, it works well with terminal no GUI needed!

4- Create your own version of TennisGameklass, justify why you think it is better than the others. (50 points)

## 1. Commenting on files

In the file tennis_original.py you will find the original files of the assignment. 
I start commenting on files by first spliting the files into 2: tennis_game1.py and tennis_game2.py. There you will find a comment I have from what I have understood the code. 


## 2. Pylint score 

In this section, you will find a comparion of pyline score of 4 files: 

tennis_original (original): score 1.88/10
tennis_game1 (after comment): score 3.87/10
tennis_game2 (after comment): score 1.85/10
tennis_refactor (after refactoring code): score 10/10

## 3. Creating main

In each file, except the original file, you will find a main function to test the code in different moment

## 4. Refactoring code

In the file tennis_refactor you will find a new refactor code from both classes. There are a few points that have been improved.

**Medthod names** : In the new refactor file, tennis_refactor.py, I used a new name for the method called add_point_to_player and get_current_score instad of the old one called won_point and score where you can get confused and have to look into each line of the code to see what is what. 

**Variable names** : Both old classes used `p1` or `p2` score or player which make it confused whether the 'p' represent points or player. Intead, I used a full 'player' spelling for the variable and make everything follow the snake case. 

**Simplified score calculation logic** : In the score function in both old classes, the score calculatiuon section is rather confusing and long and a lot of if, and elif statement. 
I have used just one function with if, elif, and else to shorten the code and easier to understand. 

**Add type difinition to funcion arguments and return type** : The old code did not specify whether it is going to return None or Str, or int.

**Add Player class, additional to TennisGame class** : In both old classes, they did not have Player class, so I have added it for be able to reuse and extend the class in the future. 

**Thing that could be improved** : The represents a simplification of a tennis match since the code only supports a single game and does not cover the whole tennis match. In the future, in case of wanting to make the game more useful it might be worth considering having: 
    - Set class: where you calculate how many sets each player have won
    - Tirebreak class: when both players have equal games in a set (6-6) 
    - Add try and catch error incase of input a wrong type of data
    - Player are able to press continue or exit the game

## Appendix: Pylint score and their comments

### tennis_original both classes

```
PS C:\Users\alici\Documents\PycharmProjects\Pythonutvecklare med inriktning AI - PGBPYH21\effective-python-tennis-games> pylint tennis_original.py
************* Module tennis_original
tennis_original.py:9:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_original.py:15:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_original.py:19:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:27:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:29:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
tennis_original.py:31:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
tennis_original.py:37:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:57:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_original.py:63:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_original.py:67:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:69:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:71:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:76:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_original.py:80:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:82:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:84:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:86:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_original.py:90:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:92:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:94:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:96:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_original.py:99:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_original.py:100:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_original.py:102:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:104:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:106:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:108:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:112:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:114:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:116:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:118:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_original.py:121:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_original.py:124:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_original.py:127:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_original.py:133:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_original.py:137:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_original.py:141:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_original.py:144:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_original.py:145:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_original.py:148:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_original.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tennis_original.py:2:0: C0115: Missing class docstring (missing-class-docstring)
tennis_original.py:5:8: C0103: Attribute name "player1Name" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:6:8: C0103: Attribute name "player2Name" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:4:23: C0103: Argument name "player1Name" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:4:36: C0103: Argument name "player2Name" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:10:4: C0116: Missing function or method docstring (missing-function-docstring)
tennis_original.py:10:24: C0103: Argument name "playerName" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:16:4: C0116: Missing function or method docstring (missing-function-docstring)
tennis_original.py:18:8: C0103: Variable name "tempScore" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:26:12: C0103: Variable name "minusResult" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:38:20: C0103: Variable name "tempScore" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:41:20: C0103: Variable name "tempScore" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:51:0: C0115: Missing class docstring (missing-class-docstring)
tennis_original.py:53:8: C0103: Attribute name "player1Name" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:54:8: C0103: Attribute name "player2Name" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:52:23: C0103: Argument name "player1Name" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:52:36: C0103: Argument name "player2Name" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:58:4: C0116: Missing function or method docstring (missing-function-docstring)
tennis_original.py:58:24: C0103: Argument name "playerName" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:64:4: C0116: Missing function or method docstring (missing-function-docstring)
tennis_original.py:77:8: C0103: Variable name "P1res" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:78:8: C0103: Variable name "P2res" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:81:16: C0103: Variable name "P1res" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:83:16: C0103: Variable name "P1res" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:85:16: C0103: Variable name "P1res" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:87:12: C0103: Variable name "P2res" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:91:16: C0103: Variable name "P2res" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:93:16: C0103: Variable name "P2res" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:95:16: C0103: Variable name "P2res" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:97:12: C0103: Variable name "P1res" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:103:16: C0103: Variable name "P1res" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:105:16: C0103: Variable name "P1res" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:107:16: C0103: Variable name "P2res" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:109:16: C0103: Variable name "P2res" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:113:16: C0103: Variable name "P2res" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:115:16: C0103: Variable name "P2res" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:117:16: C0103: Variable name "P1res" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:119:16: C0103: Variable name "P1res" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:64:4: R0912: Too many branches (27/12) (too-many-branches)
tennis_original.py:64:4: R0915: Too many statements (60/50) (too-many-statements)
tennis_original.py:134:4: C0116: Missing function or method docstring (missing-function-docstring)
tennis_original.py:134:4: C0103: Method name "SetP1Score" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:135:12: W0612: Unused variable 'i' (unused-variable)
tennis_original.py:138:4: C0116: Missing function or method docstring (missing-function-docstring)
tennis_original.py:138:4: C0103: Method name "SetP2Score" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:139:12: W0612: Unused variable 'i' (unused-variable)
tennis_original.py:142:4: C0116: Missing function or method docstring (missing-function-docstring)
tennis_original.py:142:4: C0103: Method name "P1Score" doesn't conform to snake_case naming style (invalid-name)
tennis_original.py:146:4: C0116: Missing function or method docstring (missing-function-docstring)
tennis_original.py:146:4: C0103: Method name "P2Score" doesn't conform to snake_case naming style (invalid-name)

-----------------------------------
Your code has been rated at 1.88/10

PS C:\Users\alici\Documents\PycharmProjects\Pythonutvecklare med inriktning AI - PGBPYH21\effective-python-tennis-games> 


```

### TennisGame1

```
PS C:\Users\alici\Documents\PycharmProjects\Pythonutvecklare med inriktning AI - PGBPYH21\effective-python-tennis-games> pylint tennis_game1.py
************* Module tennis_game1
tennis_game1.py:13:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_game1.py:20:0: C0303: Trailing whitespace (trailing-whitespace)
tennis_game1.py:26:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game1.py:32:74: C0303: Trailing whitespace (trailing-whitespace)
tennis_game1.py:35:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game1.py:37:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
tennis_game1.py:39:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
tennis_game1.py:47:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game1.py:58:0: C0304: Final newline missing (missing-final-newline)
tennis_game1.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tennis_game1.py:9:8: C0103: Attribute name "player1Name" doesn't conform to snake_case naming style (invalid-name)
tennis_game1.py:10:8: C0103: Attribute name "player2Name" doesn't conform to snake_case naming style (invalid-name)
tennis_game1.py:7:23: C0103: Argument name "player1Name" doesn't conform to snake_case naming style (invalid-name)
tennis_game1.py:7:36: C0103: Argument name "player2Name" doesn't conform to snake_case naming style (invalid-name)
tennis_game1.py:14:24: C0103: Argument name "playerName" doesn't conform to snake_case naming style (invalid-name)
tennis_game1.py:24:8: C0103: Variable name "tempScore" doesn't conform to snake_case naming style (invalid-name)
tennis_game1.py:34:12: C0103: Variable name "minusResult" doesn't conform to snake_case naming style (invalid-name)
tennis_game1.py:48:20: C0103: Variable name "tempScore" doesn't conform to snake_case naming style (invalid-name)
tennis_game1.py:51:20: C0103: Variable name "tempScore" doesn't conform to snake_case naming style (invalid-name)

-----------------------------------
Your code has been rated at 3.87/10

PS C:\Users\alici\Documents\PycharmProjects\Pythonutvecklare med inriktning AI - PGBPYH21\effective-python-tennis-games>
```

### TennisGame2


```
PS C:\Users\alici\Documents\PycharmProjects\Pythonutvecklare med inriktning AI - PGBPYH21\effective-python-tennis-games> pylint tennis_game2.py   
************* Module tennis_game2
tennis_game2.py:27:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game2.py:29:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game2.py:31:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game2.py:41:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game2.py:43:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game2.py:45:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game2.py:52:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game2.py:54:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game2.py:56:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game2.py:63:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game2.py:65:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game2.py:67:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game2.py:69:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game2.py:74:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game2.py:76:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game2.py:78:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game2.py:80:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
tennis_game2.py:113:0: C0304: Final newline missing (missing-final-newline)
tennis_game2.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tennis_game2.py:10:8: C0103: Attribute name "player1Name" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:11:8: C0103: Attribute name "player2Name" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:8:23: C0103: Argument name "player1Name" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:8:36: C0103: Argument name "player2Name" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:15:24: C0103: Argument name "playerName" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:37:8: C0103: Variable name "P1res" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:38:8: C0103: Variable name "P2res" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:42:16: C0103: Variable name "P1res" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:44:16: C0103: Variable name "P1res" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:46:16: C0103: Variable name "P1res" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:48:12: C0103: Variable name "P2res" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:53:16: C0103: Variable name "P2res" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:55:16: C0103: Variable name "P2res" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:57:16: C0103: Variable name "P2res" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:59:12: C0103: Variable name "P1res" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:64:16: C0103: Variable name "P1res" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:66:16: C0103: Variable name "P1res" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:68:16: C0103: Variable name "P2res" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:70:16: C0103: Variable name "P2res" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:75:16: C0103: Variable name "P2res" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:77:16: C0103: Variable name "P2res" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:79:16: C0103: Variable name "P1res" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:81:16: C0103: Variable name "P1res" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:22:4: R0912: Too many branches (27/12) (too-many-branches)
tennis_game2.py:22:4: R0915: Too many statements (60/50) (too-many-statements)
tennis_game2.py:97:4: C0103: Method name "SetP1Score" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:99:12: W0612: Unused variable 'i' (unused-variable)
tennis_game2.py:102:4: C0103: Method name "SetP2Score" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:104:12: W0612: Unused variable 'i' (unused-variable)
tennis_game2.py:107:4: C0103: Method name "P1Score" doesn't conform to snake_case naming style (invalid-name)
tennis_game2.py:111:4: C0103: Method name "P2Score" doesn't conform to snake_case naming style (invalid-name)

------------------------------------------------------------------
Your code has been rated at 3.83/10 (previous run: 1.85/10, +1.98)

PS C:\Users\alici\Documents\PycharmProjects\Pythonutvecklare med inriktning AI - PGBPYH21\effective-python-tennis-games> 

```

### tennis_refactor.py

```
PS C:\Users\alici\Documents\PycharmProjects\Pythonutvecklare med inriktning AI - PGBPYH21\effective-python-tennis-games> pylint tennis_refactor.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

PS C:\Users\alici\Documents\PycharmProjects\Pythonutvecklare med inriktning AI - PGBPYH21\effective-python-tennis-games> 
```
