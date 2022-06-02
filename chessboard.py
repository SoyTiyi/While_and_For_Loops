def print_chessboard(chessboard):
    for row in chessboard:
        text = "["
        for item in row:
            text += item + ","
        text = text[:-1]+"]"
        print(text)

def change_color(color):
    if(color == "B"):
        return "W"
    else:
        return "B"

def draw_chessboard():
    chessboard = []
    color = "W"
    for i in range(8):
        row = []
        for j in range(8):
            row.append(color)
            color = change_color(color)
        color = change_color(color)
        chessboard.append(row)
    print_chessboard(chessboard)

def main():
    draw_chessboard()

if __name__ == "__main__":
    main()
