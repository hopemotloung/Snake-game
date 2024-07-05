import tkinter
import random

#main window setup
win = tkinter.Tk()
win.title("Dope Snake Game!")
win.resizable(False,False)

#for storing of X and Y coordinates
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#25px
ROWS = 25
COLS = 25
TILE = 25

WIN_HEIGHT = TILE * COLS
WIN_WIDTH = TILE * ROWS

#Game Screen
canvas = tkinter.Canvas(win, bg= "white", height=WIN_HEIGHT, width=WIN_WIDTH )
canvas.pack()
win.update()

#Main start of the game
snake = Tile(5*TILE, 5*TILE) #ONE TILE (SNAKES HEAD)
food = Tile(10*TILE,10*TILE)
#to store snakes body
snake_body = []
#speed
speedX = 0
speedY = 0
game_over = False
score = 0


def move():
    global snake, food, game_over, snake_body, score

    if game_over:
        return
    
    if snake.x < 0 or snake.x >= WIN_WIDTH or snake.y < 0 or snake.y >= WIN_HEIGHT:
        game_over = True
        return
    
    for tile in snake_body:
        if snake.x == tile.x and snake.y == tile.y:
            game_over = True
            return

    #collosion check
    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS-1) * TILE
        food.y = random.randint(0, ROWS-1) * TILE
        score += 1

    #to merge the body to move with the head
    for i in range(len(snake_body)-1, -1, -1):
        tiles = snake_body[i]
        if i == 0:
            tiles.x = snake.x
            tiles.y = snake.y
        else:
            prev_tile = snake_body[i-1]
            tiles.x = prev_tile.x
            tiles.y = prev_tile.y

    #move snake
    snake.x += (speedX * TILE)/2
    snake.y += (speedY * TILE)/2

def direction(e):# "e" is for event
    print(e)
    print(e.keysym)
    global speedX, speedY, game_over

    if game_over:
        return

    if e.keysym == "Up" and speedY != 1:
        speedY = -1
        speedX = 0
    elif e.keysym == "Down" and speedY != -1:
        speedX = 0
        speedY = 1
    elif e.keysym == "Left" and speedX != 1:
        speedY = 0
        speedX = -1
    elif e.keysym == "Right" and speedX != -1:
        speedX = 1
        speedY = 0
    

def draw():
    global snake, food, snake_body, game_over, scores
    move()

    #to delete trail
    canvas.delete("all")

    #making of the food
    canvas.create_oval(food.x, food.y, food.x + TILE, food.y + TILE, fill="red")
    #making of the snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE, snake.y + TILE, fill="black")
    
    #creating body after collosion
    for tiles in snake_body:
        canvas.create_rectangle(tiles.x, tiles.y, tiles.x + TILE, tiles.y + TILE, fill="black")
    
     #writing when game is over
    if game_over:
        canvas.create_text(WIN_WIDTH/2, WIN_HEIGHT/2, font="Arial 20", text= f"Game Over!! \nYour Score: {score}", fill="red")
    else:
        canvas.create_text(30, 20, font="Arial 10", text=f"Score: {score}", fill="black")
    #to loop the rectangle
    win.after(100, draw)#to happen every 100ms

draw()


win.bind("<KeyRelease>", direction)#similar to event listener of JavaScript





win.mainloop()