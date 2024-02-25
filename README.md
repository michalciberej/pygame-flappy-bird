<h1 style="text-align:center">FLAPPY BIRD CLONE</h1>

<p style="text-align:center">This is my final project for cs50. I recreated Flappy bird and added few features.</p>

## FEATURES

- Leaderboard
- Extra lives

## HOW TO USE

### Open as .exe

- You can download this repository as zip, unzip the folder and then navigate to dist folder where you can find main.exe. By opening this file, the game should start.

  <p style="color:lightgray">NOTE: Game was bundled on Linux (debian distribution) and pyinstaller docs say that the game works only on same system that bundled it. So might not work on Windows or MacOS without additional bundeling.</p>

### Open from terminal

1. Clone the repository.

```
$ git clone https://github.com/michalciberej/pygame-flappy-bird.git
```

2. Move to cloned directory.

```
$ cd pygame-flappy-bird
```

3. Install dependencies

```
$ pip install -r requirements.txt
```

4. Start the game.

```
$ python3 main.py
```

## Project explanation

[Link to video demo](https://youtu.be/ylYbhq_L4dY)

### Description

I would start by saying that I have separated all the code into main.py and multiple modules in './data'.

### assests.py

Special file for assets imports. Images get loaded into variables and then are imported from other files.

### variables.py

File for global variables.

### helpers.py

File for bigger functions.

- <b>quit_game</b> - Function tells pygame to close the window if the cross in top right corner is pressed.
- <b>spawn_pipes_coins</b> - Function takes 4 arguments - pipes_group, pipes_spawn_timer, and coins_group. Function takes care of spawning pipes on right side of screen. It randomly calculates gaps between top and bottom pipe, gaps between couples of pipes. It adds new pipes and coin to groups when pipe_spawn_timer reaches 0. Decreminates pipe_spawn_timer and returns it. Later in main function groups are rendered to screen.
- <b>make_bird_immune</b> - This function takes 1 argument - bird. It sets bird.immunity to True so makes the bird immune to colisions with pipes. After it starts nonblocking Timer function which sets bird.immunity back to False after 5 seconds.
- <b>check_colisions</b> - This function takes 4 arguments - bird, pipes, ground and coins. Function on every call checks for colisions between bird and pipes, ground and coins and sets boolean result into variables. After conditionaly calls make_bird_immune function, adds coins to bird object, or sets bird.alive to false.
- <b>place_in_middle</b> - This function takes 1 argument - image. It calculates exact middle of screen and return x and y coordinates.

### classes.py

File for all class definitions. Every class has <b>\_\_init\_\_</b> and <b>update</b> method.

- <b>\_\_init**</b> - This method takes 0 or more arguments. Depends how the object is intended to be instanciate. E.g. Ground.\_\_init** takes x and y arguments. It then sets its image then it gets Rect from that image and after it sets place on the screen of object to x and y.

- <b>update</b> - This method takes 0 or 1 arguments. Depends how the object is intended to be updated. E.g. Ground.update takes no arguments. It updates Ground.x on every call by -1 and if Ground.x is less or equal to negative size of window it kills this object. Bird.update takes 1 argument - user_input and on every call it conditionaly checks if user_input is space it increments Bird.velocity which makes the bird tilt on the screen. This method also updates bird images. On every call it adds 1 to bird.image_index divide it by 10 and conditionaly change bird.image to image from BIRD_IMAGES list and lastly reset image_index if is more or equal to 30.

### main.py

This is the main file where the 2 main functions main and menu are.

- <b>menu</b> - This is the function that runs when you run the game and before you start the main loop. First global variable game_paused is declared and if gane_paused is True then while loop runs. In loop first quit_game function is called, window is filled with white color then images of background, ground, bird and gamestart logo are staticly rendered on the screen. After that on every iteration it waits on user input and if user input is key space then calls the main function and updates game_paused variable to True. Only thing left is to call the pygame.display.update function that must be called.

- <b>main</b> - This is the main game loop. First global variable game_paused is declared then ground group, bird group, pipes group and coins group are declared. Lastly before the game loop starts more variables user_name that gets name of current os profile, data_sent, leaderboard and player_scores are declared. Main loop runs and first calls quit_game, after that local variable passed is set to False, this function represents fact if pipe already passed bird. Window is filled with white color abd background image is rendered on the screen, user input is gathered. If ground group length is less or equal to 2 add another ground object to make fluid moving ground. After that all pipes, ground, bird and coins are rendered with their current attributes. After check_colisions is run, next if bird is alive update all groups of objects except bird, also small for loop checks if any pipe has passed attribute set to true set passed variable also to True. If bird is not alive, user_name and score is sent to database and first 10 highest scores is fetched from database and data_sent is set to True to deny any other data sending/fetching. Leaderboard data is then stored in list and rendered on the screen with gameover image aswell. At the end of this condition is laso reset condition, if user_input is key r then call the main fucntion again and break out of the main loop. Score and coins are rendered on the screen, bird is updated and pipes_spawn is updated by calling spawn_pipes_coins. Lastly maximum of 60 frames per second is sent and pygame.display.update is called.
