# PythonChallengeDayNineTen
from Repl.it

## Nomad Academy Python challenge Day 6
Using this boilerplate, build a program that:

### criteria
Using this boilerplate we are going to build a mini clone of the Hacker News Website using the Hacker News Search API and Flask.

- The website should have the following routes:
   - /
   - /?order_by=new
   - /?order_by=popular
   - /＜id＞

- Implement a fake DB like the one we make on the video #4.6 so 'new' and 'popular' can load faster.
- The template should reflect the current order_by selection.
- The main page "/" should by default order_by popular
- There should be a link to each of the stories to go and see the comments.

clues
- If a comment does not have an author it means it has been deleted.
- To render the comment text, use the safe tag from Flask.
- Don't worry about the CSS, I have included a .css file on the boilerplate that will style the default HTML elements, just use \<header> \<section> \<div>\<h1> etc and it will automatically look nice.
- The API has a limit of 10,000 requests per hour so don't go crazy and you will be alright.
