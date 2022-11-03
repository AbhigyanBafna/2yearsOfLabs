/* Statements -
Appu is an elephant.
An elephant is a mammal.
A mammal is a vertebrate.
Elephants are herbivores.
All herbivores eat grass.
Vertebrates have Spinal cord.
Appu is a mascot of Asian Games.
Some vertebrates stand.
Tappu is an elephant.
*/

elephant(appu).
elephant(tappu).
mammal(X) :- elephant(X).
vertebrate(Y) :- mammal(Y).
herbivore(Z) :- elephant(Z).
eat(P, grass) :- herbivore(P).
have(Q, spinal-cord) :- vertebrate(Q).
mascotOfAsianGames(appu).
stand(S) :- vertebrate(S).