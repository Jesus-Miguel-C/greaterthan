@namespace
class SpriteKind:
    Cherry = SpriteKind.create()
projectile: Sprite = None
mySprite: Sprite = None

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    otherSprite.destroy()
    if info.score() > 5:
        mySprite.say_text("Too many cherries")
sprites.on_overlap(SpriteKind.player, SpriteKind.Cherry, on_on_overlap)

mySprite = sprites.create(img("""
        . . . . . . 5 . 5 . . . . . . .
        . . . . . f 5 5 5 f f . . . . .
        . . . . f 1 5 2 5 1 6 f . . . .
        . . . f 1 6 6 6 6 6 1 6 f . . .
        . . . f 6 6 f f f f 6 1 f . . .
        . . . f 6 f f d d f f 6 f . . .
        . . f 6 f d f d d f d f 6 f . .
        . . f 6 f d 3 d d 3 d f 6 f . .
        . . f 6 6 f d d d d f 6 6 f . .
        . f 6 6 f 3 f f f f 3 f 6 6 f .
        . . f f d 3 5 3 3 5 3 d f f . .
        . . f d d f 3 5 5 3 f d d f . .
        . . . f f 3 3 3 3 3 3 f f . . .
        . . . f 3 3 5 3 3 5 3 3 f . . .
        . . . f f f f f f f f f f . . .
        . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
mySprite.set_stay_in_screen(True)
game.splash("Collect 5 cherries")

def on_update_interval():
    global projectile
    projectile = sprites.create_projectile(img("""
            . . . . . . . . . . . 6 6 6 6 6
            . . . . . . . . . 6 6 7 7 7 7 8
            . . . . . . 8 8 8 7 7 8 8 6 8 8
            . . e e e e c 6 6 8 8 . 8 7 8 .
            . e 2 5 4 2 e c 8 . . . 6 7 8 .
            e 2 4 2 2 2 2 2 c . . . 6 7 8 .
            e 2 2 2 2 2 2 2 c . . . 8 6 8 .
            e 2 e e 2 2 2 2 e e e e c 6 8 .
            c 2 e e 2 2 2 2 e 2 5 4 2 c 8 .
            . c 2 e e e 2 e 2 4 2 2 2 2 c .
            . . c 2 2 2 e e 2 2 2 2 2 2 2 e
            . . . e c c e c 2 2 2 2 2 2 2 e
            . . . . . . . c 2 e e 2 2 e 2 c
            . . . . . . . c e e e e e e 2 c
            . . . . . . . . c e 2 2 2 2 c .
            . . . . . . . . . c c c c c . .
        """),
        randint(-30, 30),
        randint(-30, 30),
        SpriteKind.Cherry)
game.on_update_interval(500, on_update_interval)