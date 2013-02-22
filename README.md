## Tips

1. How to Run
  * setup virtual env
  * pip install -r requirement.txt
  * python manage.py runserver
2. RESTful APIs can be accessed via http://127.0.0.1:8000/api/v1/fruit/1/ 

## Note

1. the RESTful APIs are just for demo, and didn't include the auth
2. unittests can be found at salad_machine/tests.py
3. Run python manage.py test salad_machine to make testing

## Spec

Fruit Salad Machine
Design a system for allowing users to create fruit salads given a random basket of fruit.

The server maintains a set of "specs" for fruit basket designs. A spec consisting of a list of fruits and properties for selection. Each fruit has the following properties:

name (e.g. apple)
percent_chance_to_include (e.g. 30%)
min_quantity
max_quantity
A client may request a fruit basket from the server at which point the server should generate a new random basket, by first selecting a spec and then generating a unique basket from that spec. The client can specify which spec to use (eg like a level in a game)

The client then allows the user to select which fruits and quantities of each fruit to include in the salad, and sends the salad data to the server.

The server must validate that the user had adequate quantities in their given basket to create the given salad (ie to stop the client cheating)

So a scenario may look like this:

client => request a basket for level 1
server picks the spec for level 1
generates a random basket based on the spec (rules, chance, etc)
returns the list of fruit (eg 10 fruit)

client displays 10 fruit
allows user to pick - say 5 of these
user hits "submit" and sends back the shortlist of 5 picked fruit
client [ level ] [ fruit selection] => server

server validates that the fruit selected would be possible to generate for the defined level

the full spec maybe a lot to implement, please limit to a reasonable amount of time at your end, and let us know how many hours spent.
for example, you could skip the html page to "pick fruit" and just write example tests for each of the URLs.
or skip the validation part if you feel that will be hugely complex mathematically (is this combination possible from this set of rules? is different than just generating a set from the same rules)

Further requirements:

The system should be developed with Python 2.7.x.
The system should be backed by a persistent datastore
The system should provide a REST API to the client.
The system should have unit tests.
Preferable:
For our final app we are planning to use:

Flask, Mysql, deploy on dotcloud, sqlAlchemy ORM mapper. so even if mongo or other maybe your favorite for this simple task something closer to the above stack would be a better reference for us.
Provide as much (or as little) design detail and code as you feel is necessary.
