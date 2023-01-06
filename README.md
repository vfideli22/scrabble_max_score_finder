# scrabble_max_score_finder
Problem arose post-D&D, where we were intrigued about the optimal placement of our character names on a Scrabble board.


**Problem:**
Who gains the most scrabble points if you can place your name anywhere on the board? And where would this be?

**Assumptions:** (with method and problem)
- No restriction on maximum number of letters (though Kascorin with 8 letters is achievable if you build on top of an existing letter in that row; everyone else has names <= 7 letters long)
- By symmetry, horizontal searches are the same as vertical searches
- Top half of the board is symmetrical with bottom half, so search was restricted to the first half of the rows, including the centre (start) row

**Results:**
- See below (spoilered so you read this first hehe)
Fig 1) First bit of text is a summary on the number of points each name scores
Fig 2) The images show where on the board would be best for your name
Fig 3) Each text array shows the number of points your name would achieve if you placed your name horizontally, start from the top left corner

**Discussion:**
- Kascorin is, of course, the *best* name :innocent:
- A good point earlier was raised: "Isn't the triple word just the best in all cases?" 
  - Here we see that interestingly, Orville and Dorothy make use of the two double words on either end to trump the triple word. 
  - Furthermore, Ozman and Kyvir's high scores only works in this specific triple word since the Z and Y were pretty clutch, latching onto the double letter!
- This is acc super cool and I'm high-key happy I've done this hahaha

**Methods:**
- see scrabble.py
