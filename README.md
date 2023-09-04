# Top Trumps 06/07 Footballers Simulator

Hello there, welcome to my 2nd program on Python, this time I've gone for a text based top-trumps style simulator based on 2000s
era footballers, specifically the 06/07 season. I was a big fan growing up of all the great ballers from this period: Ronaldinho,
Zidane, Thierry Henry etc., as well as some of the great teams of this period, AC Milan, Real Madrid, Barcelona etc., so thought
I'd try and pay tribute to them via this game.

# How to play

If you've never played Top Trumps before, not to worry, I'll try and explain the gist of it here. Normally in a pack of Top Trumps
there are about 24 to 30 cards, each with their own stats and values, some being higher in one field and lesser in others, so there
should be a good balance between the cards. In this game I've created a Card class with 6 different categories: Attack, Defence,
Physicality, Stamina, Speed and Technique, the stats I've graded on a scale of 1-99, 99 being the highest value of course. So a player
like Ronaldinho in his prime, would have a pretty high score for Technique but not so much for Defence; whereas a player like John Terry
would have high stats for Defence and Physicality but not so much for Attack; it should all balance out.

I've created the stats for over 200 players for the game; these include all your pros and all-stars of the era but also some more
'cult heroes' of the era, players like Jimmy Bullard, Tony Hibbert, Bobby Zamora etc. For every game, 20 cards are drawn randomly
from the pack so there should be the right balance of players in both the player's hand and the computer's hand.

The rules are simple, the player is shown their card and is then asked to enter a number from 1-6; 1 for Attack, 2 for Defence and so on etc.
The player should always aim for whichever is the highest stat on the card. So for example the player has drawn Paolo Maldini, his Defence
stat is pretty high so the player should go for that. After the player has selected their stat, you get to see the card that the computer has
selected, and if the statistic the player has selected happens to be higher than that of the computer's, the player 'wins' that card and it 
is added to the player's hand.

The aim of the game is to empty the computer's hand, so they have 0 cards left. Of course this can also work the other way, if the player's stat is lower
than the computer's, it is then the computer's turn to select cards. As is the case with Top Trumps in real life, you can often be on the verge of winning
and somehow lose 5-6 hands in a row, putting the opponent right back into the game.

The code so far has been fairly solid, maybe with time I'd like to add a proper HUD, rather than having it just text-based for now. Hopefully
you enjoy this little game and any feedback would be welcome!
