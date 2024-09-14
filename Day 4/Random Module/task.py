import random
from random import choice

# code for adding and using module
# print(f"area of a circle is {5 * 5 * my_module.pi}")

# import my_module
#
# random_int = random.randint(0,2)
# print(random_int)
#
# random_float = round(random.random()*10,2)
# print(random_float)
#
# random_float = round(random.uniform(1,10))
# print(random_float)

print("Lets flip a coin\n")
print('''
               ,,==="""""""===,,
           ,==""' |\ |   /\   `""==,
        ,="'|\    | \|  /__\   /\  `"=,
      /"    |,"\  |  | /'  `\ /  )     "
    /"  ,"  |                 `\/    /|  "
   /'  |   ,                       /",|   `
  /'   ",/"                           |    `
 /'      I=I=I               ,d8ba,___      `
/'     I=8=8=8=I_I_          88888P"""       `
|   xXXXXXXXXXXXXXXXxIxx    ,888"             |
| ~XXXXXXXXXXXXXXX~-~-~-~-~ d888~-~-~-~-~-~-~ |
| ~-~-~-~-~-~-~-~-,aad888ba,8888,-~-~-~-~-~-~ |
| ~-~-~-~-~-~-,ad888888888888888b-~-~-~-~-~-~ |˳
\ ~-~-~-~-~,ad8888888888888888888-~-~-~-~-~-~ /
`\ -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~- /'
 `\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,-,~~~~~ /'
  `\    /"\         1 9 9 4        \ /\    /'
   `\  "\,/'                   |\   `\ `  /'
     "\      /""\   |    |     |,'\     /"
       `"=,_ \__/   |__  |__   |    ,="'  
          `""=,__             __,=""'     
               ``""=========""''
''')

var = random.randint(1,2)

if var == 1:
    print("It's a Heads")
else:
    print("It's a Tail")

