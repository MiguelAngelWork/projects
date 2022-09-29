from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo",12,5,50)
michelangelo.show_stats()
jack_sparrow = Pirate("Jack Sparrow",15,2,70)

jack_sparrow.show_stats()
# michelangelo.attack(jack_sparrow)
jack_sparrow.attack(michelangelo)

michelangelo.show_stats()
# jack_sparrow.show_stats()

