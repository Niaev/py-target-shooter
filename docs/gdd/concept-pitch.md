# Py Target Shooter - Game Desin Concept and Pitch 

## High Level Design

### Concept

Shoot on targets with your mouse, earn points, get achievements, find secrets, and do your best, before the timer is over and you loose it all.

### Genre 

Single-player, 2D point-and-click shooter.

### Target Audience

Gamers of all ages willing to play indie and fun games; Mobile players also of all ages willing to play a free-to-play arcade-like experience with no ads and microtransactions.

### Unique Selling Points

Free-to-play; indie-made; no ads; no microtransactions; open-source and moddable.

## Product Design

### Player Experience and Game POV

The player is the shooter, represented by a cursor driven corss hair, against a concrete-grey wall that targets may appear and disappear. The more targets he shoots, more points he gets.

### Visual and Audio Style

Execution time generated pixel art and 16-bit audio design should create an experience similar to retro games like Super Mario Bros. and Duck Hunt, but with a way more simpler art.

### Game World Fiction

There is no world or fiction. Just targets to shoot.

### Monetization

The game is free-to-play, with no microtransactions or ads. So no monetization method.

### Platform, Technology, and Scope

PC only; 2D; PyGame only with no image files; One dev team; A couple months to conclude; Major risks? Only failing and loosing time, but it won't happen since I will learn a lot from it.

## Detailed & Game Systems Design

### Core Loops

The game loop updated every state of every object inside the game, be it the player's crosshair, targets, point counter, misses counter and timer. The change of state can be change of scale, color, content, position, opacity and if it is even on the screen or not.

The game loop is engaging since it has a local leaderbords to compare player's past tries, a timer and misses limits to motivate the player to improve under pressure, achievements and secrets willing to be found.

### Objectives and Progression

Player starts at the menu screen, being able to choose to play or other in-game options such as credits screen and configurations. By selecting to play, the player can check out the achievements already achieved and select the game mode. There are two game modes, the endless mode in which you loose by missing three targets and the normal mode in which you have decreasing time and can loose by missing only one target, which make your points go zero. The progression is made by showing the player his past tries and achievements.

### Game Systems

I don't know what it is.

### Interactivity

I don't know about that also.