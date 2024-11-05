from tkinter import *


window = Tk()

window.title("TicTacToe App")
window.geometry("400x400")


frame = Frame(window)
frame.pack()

# global variables
player1 = 'X'
player2 = 'O'
curr_player = player1
end_game = False


def button_press(num):
    char = ""
    global curr_player
    global end_game

    if curr_player == player1:
        char = player1
    else:
        char = player2

    if not end_game:
        if num == 1 and button1.cget('text') == tic_char:
            button1.config(text=char)
        if num == 2 and button2.cget('text') == tic_char:
            button2.config(text=char)
        if num == 3 and button3.cget('text') == tic_char:
            button3.config(text=char)
        if num == 4 and button4.cget('text') == tic_char:
            button4.config(text=char)
        if num == 5 and button5.cget('text') == tic_char:
            button5.config(text=char)
        if num == 6 and button6.cget('text') == tic_char:
            button6.config(text=char)
        if num == 7 and button7.cget('text') == tic_char:
            button7.config(text=char)
        if num == 8 and button8.cget('text') == tic_char:
            button8.config(text=char)
        if num == 9 and button9.cget('text') == tic_char:
            button9.config(text=char)

        if not check_win():
            if curr_player == player2:
                curr_player = player1
            else:
                curr_player = player2


def check_win():
    global end_game
    # horizontal check
    if button1.cget("text") == button2.cget("text") == button3.cget("text") and button1.cget("text") != tic_char:
        result.config(text=f"{button1.cget('text')} won!", font=('calibre', 50, 'bold'))
        end_game = True
        return False
    elif button4.cget("text") == button5.cget("text") == button6.cget("text") and button4.cget("text") != tic_char:
        result.config(text=f"{button4.cget('text')} won!", font=('calibre', 50, 'bold'))
        end_game = True
        return False
    elif button7.cget("text") == button8.cget("text") == button9.cget("text") and button7.cget("text") != tic_char:
        result.config(text=f"{button7.cget('text')} won!", font=('calibre', 50, 'bold'))
        end_game = True
        return False
    # vertical check
    elif button1.cget("text") == button4.cget("text") == button7.cget("text") and button1.cget("text") != tic_char:
        result.config(text=f"{button1.cget('text')} won!", font=('calibre', 50, 'bold'))
        end_game = True
        return False
    elif button2.cget("text") == button5.cget("text") == button8.cget("text") and button2.cget("text") != tic_char:
        result.config(text=f"{button3.cget('text')} won!", font=('calibre', 50, 'bold'))
        end_game = True
        return False
    elif button3.cget("text") == button6.cget("text") == button9.cget("text") and button3.cget("text") != tic_char:
        result.config(text=f"{button3.cget('text')} won!", font=('calibre', 50, 'bold'))
        end_game = True
        return False
    # diagonal check
    elif button1.cget("text") == button5.cget("text") == button9.cget("text") and button1.cget("text") != tic_char:
        result.config(text=f"{button1.cget('text')} won!", font=('calibre', 50, 'bold'))
        end_game = True
        return False
    elif button3.cget("text") == button5.cget("text") == button7.cget("text") and button3.cget("text") != tic_char:
        result.config(text=f"{button3.cget('text')} won!", font=('calibre', 50, 'bold'))
        end_game = True

    return  end_game


if __name__ == "__main__":
    tic_char = " "

    banner = Label(frame, text="Welcome to\nTicTac App", height=4, width=10, font=20)
    banner.grid(row=0, column=1)

    button1 = Button(frame, text=tic_char, height=4, width=9, font=35,
                     command=lambda: button_press(1))
    button1.grid(row=2, column=0)

    button2 = Button(frame, text=tic_char, height=4, width=9, font=35,
                     command=lambda: button_press(2))
    button2.grid(row=2, column=1)

    button3 = Button(frame, text=tic_char, height=4, width=9, font=35,
                     command=lambda: button_press(3))
    button3.grid(row=2, column=2)

    button4 = Button(frame, text=tic_char, height=4, width=9, font=35,
                     command=lambda: button_press(4))
    button4.grid(row=3, column=0)

    button5 = Button(frame, text=tic_char, height=4, width=9, font=35,
                     command=lambda: button_press(5))
    button5.grid(row=3, column=1)

    button6 = Button(frame, text=tic_char, height=4, width=9, font=35,
                     command=lambda: button_press(6))
    button6.grid(row=3, column=2)

    button7 = Button(frame, text=tic_char, height=4, width=9, font=35,
                     command=lambda: button_press(7))
    button7.grid(row=4, column=0)

    button8 = Button(frame, text=tic_char, height=4, width=9, font=35,
                     command=lambda: button_press(8))
    button8.grid(row=4, column=1)

    button9 = Button(frame, text=tic_char, height=4, width=9, font=35,
                     command=lambda: button_press(9))
    button9.grid(row=4, column=2)

    result = Label(frame, text="", fg="White")
    result.grid(row=5, column=1)

window.mainloop()
