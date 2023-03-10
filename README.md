# scrabble_max_score_finder
Problem arose post-D&D, where we were intrigued about the optimal placement of our character names on a Scrabble board.
(So I coded this just for fun :))

**Problem:**
Who gains the most scrabble points if you can place your name anywhere on the board? And where would this be?

**Assumptions:** (with method and problem)
- No restriction on maximum number of letters (though Kascorin with 8 letters is achievable if you build on top of an existing letter in that row; everyone else has names <= 7 letters long)
- By symmetry, horizontal searches are the same as vertical searches
- Top half of the board is symmetrical with bottom half, so search was restricted to the first half of the rows, including the centre (start) row

**Results:**

Fig 1) First bit of text is a summary on the number of points each name scores

Fig 2) Each text array shows the number of points your name would achieve if you placed your name horizontally, start from the top left corner

~~Fig 3) The images show where on the board would be best for your name~~

Fig 4) Heatmap showing scrabble board top half layout. Numbers show special tiles of board (0, 1, 2, 3, 4: normal, double letter, triple letter, double word, triple word). Each cell indicates how many points the name would get if it started on that square and was placed horizontally. Darker colour means more points.

**Discussion:**
- Kascorin is, of course, the *best* name :innocent:
- A good point earlier was raised: "Isn't the triple word just the best in all cases?" 
  - Here we see that interestingly, Orville and Dorothy make use of the two double words on either end of their word to trump the triple word. 
  - Furthermore, Ozman and Kyvir's high scores only work in this specific triple word since the Z and Y were pretty clutch, latching onto the double letter!
- This is acc super cool and I'm high-key happy I've done this hahaha

**Methods:**
- see scrabble.py
