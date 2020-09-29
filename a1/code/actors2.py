from __future__ import annotations
import pygame
from typing import Optional
from settings import *

"""
Numbers set to distinguish between different objects(Used in actor_type() method)
Actor -> 0
Player -> 1
Monster -> 2
Star -> 3
Wall -> 4
Door -> 5
Key -> 6
Orb -> 7
Box -> 8

(This is just for convenience) :)
"""

class Actor:
    """
    A class to represent all the game's actors. This class includes any
    attributes/methods that every actor in the game must have.

    This is an abstract class. Only subclasses should be instantiated.

    === Public Attributes ===
    x:
        x coordinate of this actor's location on the stage
    y:
        y coordinate of this actor's location on the stage
    icon:
        the image representing this actor
    """
    x: int
    y: int
    icon: pygame.Surface

    def __init__(self, icon_file, x, y):
        """Initialize an actor with the given image <icon_file> and the
        given <x> and <y> position on the game's stage.
        """

        self.x, self.y = x, y
        self.icon = pygame.image.load(icon_file)

    def move(self, game: 'Game') -> None:
        """Move this actor by taking one step of its animation."""

        raise NotImplementedError



class Player(Actor):
    """
    A class to represent a Player in the game.
    """
    # === Private Attributes ===
    # _stars_collected:
    #       the number of stars the player has collected so far
    # _last_event:
    #       keep track of the last key the user pushed down
    # _smooth_move:
    #       represent on/off status for smooth player movement

    x: int
    y: int
    icon: pygame.Surface
    _stars_collected: int
    _last_event: Optional[int]
    _smooth_move: bool
    _door_touched:bool
    _orbs_collected: int
    key_collected: int

    def __init__(self, icon_file: str, x: int, y: int) -> None:
        """Initalize a Player with the given image <icon_file> at the position
        <x> and <y> on the stage."""

        super().__init__(icon_file, x, y)
        self._stars_collected = 0
        self._last_event = None # This is used for precise movement
        self._smooth_move = False # Turn this on for smooth movement
        self._door_touched = False
        self._orbs_collected = 0
        self.key_collected = 0

    def orb_power(self, game: 'Game'):
        for actor in game._actors:
            if self._orbs_collected >=5 and actor.actor_type()== 2:
                game.remove_actor(actor)
            else:
                continue



    def set_smooth_move(self, status: bool) -> None:
        """
        Set the <status> of whether or not the player will move smoothly.
        """

        self._smooth_move = status

    def get_star_count(self) -> int:
        """
        Return the number of stars collected.
        """

        return self._stars_collected

    def register_event(self, event: int) -> None:
        """
        Keep track of the last key <event> the user made.
        """

        self._last_event = event

    def actor_type(self):
        return 1


    def move(self, game: 'Game') -> None:
        """
        Move the player on the <game>'s stage based on keypresses.
        """

        evt = self._last_event

        if self._last_event:
            dx, dy = 0, 0
            if self._smooth_move: # Smooth movement used by the ghost level
                if game.keys_pressed[pygame.K_LEFT] or game.keys_pressed[pygame.K_a] :
                    unreachable = game.get_actor(self.x - 1, self.y)
                    if unreachable == None:
                        dx -= 1
                    else:
                        if unreachable.actor_type() == 3:
                            dx -= 1
                            game.player._stars_collected += 1
                            game.remove_actor(unreachable)
                        if unreachable.actor_type() == 7:
                            dx -= 1
                            game.player._orbs_collected += 1
                            game.remove_actor(unreachable)
                            self.orb_power(game)

                        if unreachable.actor_type() == 6:
                            dx -= 1
                            game.player.key_collected += 1
                            game.remove_actor(unreachable)



                if game.keys_pressed[pygame.K_RIGHT] or game.keys_pressed[pygame.K_d]:
                    unreachable = game.get_actor(self.x + 1, self.y)
                    if unreachable == None:
                        dx += 1
                    else:
                        if unreachable.actor_type() == 5:
                            if self._stars_collected < 5 and game._level == 0:
                                print("Door won't open unless you collect enough stars")
                            if self.key_collected < 1 and self._orbs_collected <=5 and game._level ==2:
                                print("Get key and collect 5 orbs to proceed!!!!")
                            else:
                                self._door_touched = True


                        if unreachable.actor_type() == 3:
                            dx += 1
                            game.player._stars_collected += 1
                            game.remove_actor(unreachable)

                        if unreachable.actor_type() == 7:
                            dx += 1
                            game.player._orbs_collected += 1
                            game.remove_actor(unreachable)
                            self.orb_power(game)

                        if unreachable.actor_type() == 6:
                            dx += 1
                            game.player.key_collected += 1
                            game.remove_actor(unreachable)


                if game.keys_pressed[pygame.K_UP]or game.keys_pressed[pygame.K_w]:
                    unreachable = game.get_actor(self.x , self.y -1)
                    if unreachable == None:
                        dy -= 1
                    else:
                        if unreachable.actor_type() == 3:
                            dy -= 1
                            game.player._stars_collected += 1
                            game.remove_actor(unreachable)
                        if unreachable.actor_type() == 7:
                            dy -= 1
                            game.player._orbs_collected += 1
                            game.remove_actor(unreachable)
                            self.orb_power(game)

                        if unreachable.actor_type() == 6:
                            dy -= 1
                            game.player.key_collected += 1
                            game.remove_actor(unreachable)

                if game.keys_pressed[pygame.K_DOWN]or game.keys_pressed[pygame.K_s]:
                    unreachable = game.get_actor(self.x , self.y + 1)
                    if unreachable == None:
                        dy += 1
                    else:
                        if unreachable.actor_type() == 3:
                            dy += 1
                            game.player._stars_collected += 1
                            game.remove_actor(unreachable)

                        if unreachable.actor_type() == 7:
                            dy += 1
                            game.player._orbs_collected += 1
                            game.remove_actor(unreachable)
                            self.orb_power(game)


                        if unreachable.actor_type() == 6:
                            dy += 1
                            game.player.key_collected += 1
                            game.remove_actor(unreachable)


                # TODO: (Task 0) Move over your code from A0 here; adjust

            else: # Precise movement used by the squishy monster level
                if evt == pygame.K_LEFT or evt == pygame.K_a:
                    unreachable = game.get_actor(self.x - 1, self.y)
                    if unreachable == None:
                        dx -= 1
                    elif unreachable.actor_type()==8:
                        if unreachable.be_pushed(game,dx-1,dy):
                            dx-=1

                if evt == pygame.K_RIGHT or evt == pygame.K_d:
                    unreachable = game.get_actor(self.x + 1, self.y)
                    if unreachable == None:
                        dx += 1
                    elif unreachable.actor_type()==8:
                        if unreachable.be_pushed(game,dx+1,dy):
                            dx+=1
                    elif unreachable.actor_type() == 5:
                            if game.monster_count > 0 and game._level == 1:
                                print("Door won't open unless you kill enough monsters")

                            else:
                                self._door_touched = True

                if evt == pygame.K_UP or evt == pygame.K_w:
                    unreachable = game.get_actor(self.x , self.y - 1)
                    if unreachable == None:
                        dy -= 1
                    elif unreachable.actor_type()==8:
                        if unreachable.be_pushed(game,dx,dy-1):
                            dy-=1

                if evt == pygame.K_DOWN or evt == pygame.K_s:
                    unreachable = game.get_actor(self.x , self.y + 1)
                    if unreachable == None:
                        dy += 1
                    elif unreachable.actor_type()==8:
                        if unreachable.be_pushed(game,dx,dy+1):
                            dy+=1

                self._last_event = None

            new_x, new_y = self.x + dx, self.y + dy

            # TODO: (Task 0) Move over your code from A0 here; adjust
            # i.e. Check if move is possible / if star is to be collected, etc.

            self.x, self.y = new_x, new_y

# === Classes for immobile objects === #

class Star(Actor):
    """
    A class to represent a Star in the game.
    """
    x: int
    y: int
    icon: pygame.Surface

    def move(self, game: 'Game') -> None:
        """
        A Star cannot move, so do nothing.
        """

        pass

    def actor_type(self):
        return 3

class Door(Actor):

    x: int
    y: int
    icon: pygame.Surface

    def move(self, game: 'Game') -> None:
        """
        A Star cannot move, so do nothing.
        """
        pass

    def actor_type(self):
        return 5

class Key(Actor):
    """
    A class to represent a Star in the game.
    """
    x: int
    y: int
    icon: pygame.Surface

    def move(self, game: 'Game') -> None:
        """
        A Star cannot move, so do nothing.
        """

        pass
    def actor_type(self):
        return 6





class Wall(Actor):
    """
    A class to represent a Wall in the game.
    """
    x: int
    y: int
    icon: pygame.Surface

    def actor_type(self):
        return 4

    def move(self, game: 'Game') -> None:
        """
        A Wall cannot move, so do nothing.
        """

        pass

class Orb(Actor):
    def move(self, game: 'Game') -> None:
        """
        A Star cannot move, so do nothing.
        """

        pass

    def actor_type(self):
        return 7



# === Classes for movable objects === #

# TODO: Your class for Box should go here
class Box(Actor):

    x: int
    y: int
    icon: pygame.Surface


    def be_pushed(self, game: 'Game',dx:int,dy:int) -> bool:
        block = game.get_actor(self.x + dx, self.y + dy)
        if block == None:
            self.x += dx
            self.y += dy
            return True

        elif block.actor_type() == 8:
            if block.be_pushed(game, dx, dy):
                self.x += dx
                self.y += dy
                return True
            else:
                return False

        elif block.actor_type() == 2:
            block.die(game)
            self.x += dx
            self.y += dy
            return True



    def move(self, game: 'Game') -> None:
        pass

    def actor_type(self):
        return 8




# === Classes for monsters === #

class Monster(Actor):
    """
    A class to represent monsters that kill the player upon contact.
    """
    # === Private attributes ===
    # _dx:
    #   the horizontal distance this monster will move during each step
    # _dy:
    #   the vertical distance this monster will move during each step
    # _delay:
    #   the speed the monster moves at
    # _delay_count:
    #   used to keep track of the monster's delay in speed
    x: int
    y: int
    icon: pygame.Surface
    _dx: float
    _dy: float
    _delay: int
    _delay_count: int

    def __init__(self, icon_file: str, x: int, y: int, dx: float, dy: float) -> None:
        """Initalize a monster with the given <icon_file> as its image,
        <x> and <y> as its position, and <dx> and <dy> being how much
        it moves by during each animation in the game. The monster also
        has a delay which could optionally be used to slow it down."""

        super().__init__(icon_file, x, y)
        self._dx = dx
        self._dy = dy
        self._delay = 5
        self._delay_count = 1




    def move(self, game: 'Game') -> None:
        """Move the monster by taking one step in its animation."""

        raise NotImplementedError

    def check_player_death(self, game: 'Game') -> None:
        """Make the game over if this monster has hit the player."""

        # TODO: (Task 0) Complete this method; should be similar to what was
        # done at the end of Chaser.move for A0
        player_position = game.get_player(self.x, self.y)
        if player_position != None:
            if player_position.actor_type() == 1:
                print("You lose! :( Better luck next time.")
                game._running=False


    def actor_type(self):
        return 2




class GhostMonster(Monster):
    """
    A class to represent a ghost in the game who chases the Player.
    """
    x: int
    y: int
    icon: pygame.Surface
    _dx: float
    _dy: float
    _delay: int
    _delay_count: int

    def __init__(self, icon_file: str, x: int, y: int) -> None:
        """Initalize a ghost with the given <icon_file> and <x> and <y>
        as its position."""

        # Set movement with each animation to be 0.5
        super().__init__(icon_file, x, y, 0.5, 0.5) # uses Monster.__init__

    def move(self, game: 'Game') -> None:
        """
        Move the ghost on the <game>'s screen based on the player's location.
        Check if the ghost has caught the player after each move.
        """

        if game.player.x > self.x:
            self.x += self._dx
        elif game.player.x < self.x:
            self.x -= self._dx
        elif game.player.y > self.y:
            self.y += self._dy
        elif game.player.y < self.y:
            self.y -= self._dy

        self.check_player_death(game)



class SquishyMonster(Monster):
    """
    A class to represent a monster in the game that can kill the player, or
    get squished by a box.
    """
    x: int
    y: int
    icon: pygame.Surface
    _dx: float
    _dy: float
    _delay: int
    _delay_count: int

    def __init__(self, icon_file: str, x: int, y: int) -> None:
        """Initalize a monster with the given <icon_file> and <x> and <y>
        as its position."""

        # Set movement with each animation to be 1 step
        super().__init__(icon_file, x, y, 1, 1) # uses Monster.__init__

    def move(self, game: 'Game') -> None:
        """
        Move one step, if possible. If the way is blocked, bounce back in
        the opposite direction. After each move, check if the player has been
        hit.
        """

        # TODO: Add code to make the monster bounce off of any non-player actors
        bouncer = game.get_actor(self.x+self._dx,self.y+self._dy)

        if bouncer != None:
            if bouncer.actor_type() != 1:
               self._dx = -1 * self._dx
               self._dy = -1 * self._dy


        if self._delay_count == 0: # delay the monster's movement
            self.x += self._dx
            self.y += self._dy

        self._delay_count = (self._delay_count + 1) % self._delay

        self.check_player_death(game)

    def die(self, game: 'Game') -> None:
        """Remove this monster from the <game>."""

        # TODO: Complete this method
        game.monster_count -= 1
        game.remove_actor(self)

class DragonMonster(Monster):
    """
    A class to represent a ghost in the game who chases the Player.
    """
    x: int
    y: int
    icon: pygame.Surface
    _dx: float
    _dy: float
    _delay: int
    _delay_count: int

    def __init__(self, icon_file: str, x: int, y: int) -> None:
        """Initalize a ghost with the given <icon_file> and <x> and <y>
        as its position."""

        # Set movement with each animation to be 0.5
        super().__init__(icon_file, x, y, 0.5, 0.5) # uses Monster.__init__

    def move(self, game: 'Game') -> None:

        if game.player.x > self.x:
            self.x += self._dx
        elif game.player.x < self.x:
            self.x -= self._dx
        elif game.player.y > self.y:
            self.y += self._dy
        elif game.player.y < self.y:
            self.y -= self._dy

        self.check_player_death(game)


    def die(self, game: 'Game') -> None:
        """Remove this monster from the <game>."""
        game.remove_actor(self)


