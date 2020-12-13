# Lab: Numpy Arrays

## Overview

Today we'll be constructing chess boards like it's 1980. No prebuilt images just the power of arrays and pixel art.

## Feature Tasks and Requirements

Your job is to render out chess boards with red and blue queens on them.

Chess board is an 8 by 8 grid of alternating black and white squares. The queens are red and blue squares.

Each board will have one red and one blue queen at different coordinates. In addition to displaying the board you'll need to identify if the queens are "under attack" based on their coordinates.

## Implementation Notes

### User Acceptance Tests

- queens on same row should be "under attack"
- queens on same column should be "under attack"
- queens on same diagonal should be "under attack"
- queens with any other coordinates should NOT be "under attack"

**NOTE:** Include `assert` statements directly in your notebook verifying the behavior above.

## Configuration

Use `poetry` to create `chess-board` project.

**NOTE:** do NOT use `poetry new` for this project. If you did use new command the easiest thing is to delete the folder and start again with instructions below.

- $ mkdir chess-board
- $ cd chess-board
- $ poetry init -n
- $ poetry add numpy matplotlib jupyterlab
- $ poetry shell
- $ touch chess_board.ipynb

> open chess-board folder in vscode

> open chess_board.ipynb and VS Code Jupyter Server should start

Use the `chess-board` folder as the root of your project's git repository.

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.
