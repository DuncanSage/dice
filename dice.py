import random
import tkinter as tk


m = tk.Tk()
''' 
widgets are added here 
'''


def roll(y):
    result = random.randint(1, y)
    print(result)
    # return result


print('enter the maximum number')

# print(roll(int(input())))


m.title('Dice roller')
button = tk.Button(m, text='Roll', width=25, command=roll(6))
button.pack()

m.mainloop()



