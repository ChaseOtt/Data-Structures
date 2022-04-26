{% include nav.html %}

# Chase O Create Task
[Link to Video](https://www.loom.com/share/b05b26bd4e1142fdbe575dbc5dbe5c99)

- [Task Page](Create_task)



# 3. A
## i. Describes the overall purpose of the program

The purpose of the program is to emulate the game known as Simon says. 
## ii. Describes what functionality of the program is demonstrated in the video
The functionality shown in the video is that when you load up the program there are four boxes that flash at random. You must press them in the correct order otherwise you lose.

## iii. Describes the input and output of the program demonstrated in the video

The input is when you click on one of the four buttons. The output is if you get it right there is a new color added to the sequence however if you get it wrong the game ends.


# 3. B

## i. The first program code segment must show how data have been stored in the list.
```
const panels = [
            topLeft,
            topRight,
            bottomLeft,
            bottomRight
        ];
```
## ii. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose.
```
 const panels = [
            topLeft,
            topRight,
            bottomLeft,
            bottomRight
        ];
        return panels[parseInt(Math.random() * panels.length)];
    };
```
## iii. Identify the name of the list being used in this response
The name of the list is called panels.
## iv. Describes what the data contained in the list represent in your program
The data contained in the program is which square it is, the top left, top right, bottom left, or bottom right. So the position of the square that is chosen
## v. Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently if you did not use the list
The list is what allows the program to repeat the same sequence if a player gets it correct



# 3. C
## i. The first program code segment must be a student-developed procedure that:
Defines the procedure’s name and return type (if necessary)
Contains and uses one or more parameters that have an effect on the functionality of the procedure
Implements an algorithm that includes sequencing, selection, and iteration
Sequencing: 
```
  const sequence = [getRandomPanel()];
    let sequenceToGuess = [...sequence];

...

    const panelClicked = panelClicked => {
        if (!canClick) return;
        const expectedPanel = sequenceToGuess.shift();
        if (expectedPanel === panelClicked) {
```
Selection:
```
  const panelClicked = panelClicked => {
        if (!canClick) return;
        const expectedPanel = sequenceToGuess.shift();
        if (expectedPanel === panelClicked) {
            if (sequenceToGuess.length === 0) {
                //new round
                sequence.push(getRandomPanel());
                sequenceToGuess = [...sequence];
                startFlashing();
            }
        } else {
            //end game
            alert("Game Over");
        }
    };
```
Iteration:
```
 const sequence = [getRandomPanel()];
    let sequenceToGuess = [...sequence];

...

   sequence.push(getRandomPanel());
   sequenceToGuess = [...sequence];
   startFlashing();
```
## ii. The second program code segment must show where your student-developed procedure is being called in your program.
```
<div>
    <div onclick="panelClicked(event.currentTarget)" class="panel top-left-panel"></div>
    <div onclick="panelClicked(event.currentTarget)" class="panel top-right-panel"></div>
</div>
<div>
    <div onclick="panelClicked(event.currentTarget)" class="panel bottom-left-panel"></div>
    <div onclick="panelClicked(event.currentTarget)" class="panel bottom-right-panel"></div>
</div>
  const panelClicked = panelClicked => {
        if (!canClick) return;
        const expectedPanel = sequenceToGuess.shift();
        if (expectedPanel === panelClicked) {
```
## iii. Describes in general what the identified procedure does and how it contributes to the overall functionality of the program
It finds out if the color that the player clicked corresponds with the color that the computer randomly chose.
## iv. Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.

panelClicked starts off with the panel being clicked by the human. This then leads to the algorithm checking if the panel(s) clicked by the user are the same as the ones that the computer generated 

# 3. D

## i. Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute.

First Call:
```
     const getRandomPanel = () => {
        const panels = [
            topLeft,
            topRight,
            bottomLeft,
            bottomRight
        ];
        return panels[parseInt(Math.random() * panels.length)];
    };

    const sequence = [getRandomPanel()];
    let sequenceToGuess = [...sequence];
...
    //new round
    sequence.push(getRandomPanel());
                sequenceToGuess = [...sequence];
                startFlashing();
            }
```
Second Call:
```
<div>
    <div onclick="panelClicked(event.currentTarget)" class="panel top-left-panel"></div>
    <div onclick="panelClicked(event.currentTarget)" class="panel top-right-panel"></div>
</div>
<div>
    <div onclick="panelClicked(event.currentTarget)" class="panel bottom-left-panel"></div>
    <div onclick="panelClicked(event.currentTarget)" class="panel bottom-right-panel"></div>
</div>

...

 const panelClicked = panelClicked => {
        if (!canClick) return;
        const expectedPanel = sequenceToGuess.shift();
        if (expectedPanel === panelClicked) {
            if (sequenceToGuess.length === 0) {
                //new round
                sequence.push(getRandomPanel());
                sequenceToGuess = [...sequence];
                startFlashing();
            }
        } else {
            //end game
            alert("Game Over");
        }
    };


```
## ii. Describes what condition(s) is being tested by each call to the procedure
The first call tests if the player guessed sequence is the same as the computer-generated one

The second call tests if the colors guessed by the player are the same as the computer-generated ones

## iii. Identifies the result of each call
The result of the first call is that it adds a random panel to the previous sequence using math.random after this the new sequence is used as the one the player must guess

The result of the second call is linking the 4 boxes with different colors to the algorithm. It allows the program to detect if it has been clicked.


