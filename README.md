# Meeseeks Box:
An interface allowing you to communicate with different large languages models (only chat-gpt supported currently) easily and allowing them to communicate with one another.

To interact with chat-gtp in the usual chat mode (plus some local commands) run 


### Examples

`gpt-ping`

![demonstration of gpt-ping](ressources/images/gpt-ping_demo.gif)
##### Finding prime numbers with rust:
![demonstration of building an running a rust program](ressources/images/run_rust_exemple.gif)
(sped up 300%)
##### Ploting graphs with python:
![ploting stock charts in seconds](ressources/images/plot_stonks.gif)
##### Latex rendring capabilities:
![latex_rendering](ressources/images/latex_rendering.gif)


## Requirements

Currently only works on Linux and MacOs 

Requires the [`glow`](https://github.com/charmbracelet/glow) program for printing 

## Installation

Start by cloning this repo

```
git clone https://github.com/AmdaUwU/meeseeks-box
cd messeeks-box
```
You can then create the virtual environment 

(with poetry)
```
poetry install
```
(poetry should be configured to create environnement locally)



                    print(f"\033[K"*2)
# Todo:
- [x] Command help
- [ ] multi-meeseeks conversation
- [x] Terminal feedback
- [ ] Add hyperlinks to run command ?
- [ ] Summon other messeks
- [x] Make glow code block *blockier* 
- [x] Implement `stream` api
- [ ] Add a method to load conversation
- [x] Add a token counter
- [ ] Add other llm
- [ ] find a way to display images
- [ ] Make fancy printing optional
- [x] Add a reset command 
- [x] Active local environment automatically 
- [x] open in markdown editor
- [ ] add command to copy code block
- [ ] Add install script and install instruction
- [x] Fix bugs on Mac

- Action mode:
    - [x] Fix bug with no `--live` flag
    - [ ] rework
    - [ ] Use the new builtin function calling api thing instead of whatever jank i had before.
- Live mode:
	- [x] make live less bugy
	- [x] implement code parsing
    - [ ] fix 'too long line' bug
    - [x] live parsing for 'action' keywords
