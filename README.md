# Bot-Clean-Hackerrank
Can solve the "Bot Clean" challenge on hackerrank with the partially observable board.

## Thoughts on Future Improvement

The algorithm to search for new dirt could likely be improved. Currently it moves towards 'd' spots, or towards unmapped spots if no 'd' spots are found. However, this means that it is biased towards cleaning the 'd' spots as opposed to mapping the board. A more efficient pattern may involve a more consistent search of the board interspersed with the cleaning task.
