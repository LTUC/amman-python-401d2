# Lab: Game of Greed 3

## Overview

The game should now be playable - for honest players at least. Let's handle cheaters and/or confused players who are skirting the rules.

## Feature Tasks and Requirements

- Application should implement features from versions 1 and 2
- Should handle when cheating occurs.
  - Or just typos.
  - E.g. roll = `[1,3,5,2]` and user selects `1, 1, 1, 1, 1, 1`
- Should allow user to continue rolling with 6 new dice when all dice have scored in current turn.
- Handle **zilch**
  - No points for round, and round is over
- Any other questions refer to game doc or the online game or ask.

## Implementation Notes

- Review [rules of game](https://en.wikipedia.org/wiki/Dice_10000){:target="_blank"}
- Play game [online](http://www.playonlinedicegames.com/farkle){:target="_blank"}


### User Acceptance Tests

- Must pass provided unit and flow tests.

## Stretch Goals

- Identify features to add and propose idea to client.
- Identify gaps in current test suite and add tests to expose bugs.

## Configuration

Continue working in `game-of-greed` repository.

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.
