# Игра в крестики-нолики

from tkinter import *

root = Tk()
root.title('Игра')
label = Label(width=20, text='Крестики-Нолики', font=('Arial', 12, "bold"))
label.grid(row=0, column=1, columnspan=3, sticky='nsew')

user = 'X'
game = True
field = []


def create_board(root):
    for row in range(1, 4):
        line = []
        for col in range(1, 4):
            button = Button(root, text=' ', width=5, height=2,
                            font=('Verdana', 25, 'bold'), bg='gainsboro',
                            command=lambda x=row, y=col: click(x, y))
            button.grid(row=row, column=col, sticky='nsew')
            line.append(button)
        field.append(line)
    new_button = Button(root, text='NewGame',
                        command=new_game, font=('Arial', 8, 'bold'))
    new_button.grid(row=4, column=1, columnspan=1, sticky='nsew')
    exit_button = Button(
        root, text='Exit', command=root.destroy, font=('Arial', 8, 'bold'))
    exit_button.grid(row=4, column=3, columnspan=3, sticky='nsew')


def new_game():
    global game, user
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'gainsboro'
    game = True
    user = 'X'


def click(row, col):
    global user, game
    if game and field[row - 1][col - 1]['text'] == ' ':
        field[row - 1][col - 1]['text'] = user
        check_win(user)
        user = 'O' if user == 'X' else 'X'


def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)


def check_line(a1, a2, a3, smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'green4'
        global game
        game = False


if __name__ == '__main__':
    create_board(root)
    root.mainloop()
