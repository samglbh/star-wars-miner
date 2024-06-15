@namespace
class SpriteKind:
    arrow = SpriteKind.create()

def on_up_pressed():
    global direction
    mySprite.set_image(img("""
        . . . . . . . . . . 
                . . . . . . . . . . 
                c c f f f . . . . . 
                c b f b b c c c c . 
                c c b b b f c c c b 
                . c c b b f c c c b 
                . . c c b c c c c . 
                . . . c c c . . . . 
                . . . . . . . . . . 
                . . . . . . . . . .
    """))
    direction = "up"
    if not (tiles.tile_at_location_equals(mySprite.tilemap_location().get_neighboring_location(CollisionDirection.TOP),
        assets.tile("""
            myTile16
        """))):
        tiles.set_tile_at(mySprite.tilemap_location(),
            assets.tile("""
                myTile15
            """))
        tiles.set_wall_at(mySprite.tilemap_location().get_neighboring_location(CollisionDirection.TOP),
            False)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    global mySprite2
    mySprite2 = sprites.create(img("""
            . . . . f f f f f f . . . . . . 
                    . . . f c f b b b b f f . . . . 
                    . . f c c c f b b b b f f . . . 
                    . . f b b b b f f b b b f . . . 
                    . f b c c c c b b f f f f . . . 
                    . f c b f f f f c c c b f . . . 
                    . f f f b b b f f f f f f f . . 
                    . f b b d d 8 1 e d d b f f . . 
                    . . f b 1 1 8 8 d 1 d b b f . . 
                    . . . f 1 1 1 1 d b b b f . . . 
                    . . . f b d d d b b f f . . . . 
                    . . . f c c c b 1 1 a . . . . . 
                    . . . f c c c b 1 1 b . . . . . 
                    . . . f 4 4 d f b b f . . . . . 
                    . . . . f f f f f f . . . . . . 
                    . . . . . . f f f . . . . . . .
        """),
        SpriteKind.player)
    for index in range(randint(0, 10)):
        tiles.place_on_random_tile(mySprite2, assets.tile("""
            myTile1
        """))
        tiles.set_tile_at(mySprite2.tilemap_location(),
            assets.tile("""
                myTile18
            """))
        tiles.place_on_tile(mySprite, mySprite2.tilemap_location())
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def song():
    music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(392, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(349, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play(music.tone_playable(330, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play(music.tone_playable(294, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(523, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(349, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play(music.tone_playable(330, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play(music.tone_playable(294, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(523, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play(music.tone_playable(349, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play(music.tone_playable(330, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play(music.tone_playable(294, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(196, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.BREVE))

def on_a_pressed():
    global projectile
    music.stop_all_sounds()
    if direction == "left":
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . 2 3 3 3 2 2 2 . . . . . 
                            . . . 2 3 1 1 1 1 1 3 3 2 2 2 . 
                            . . . 2 1 1 1 1 1 1 1 1 1 1 1 . 
                            . . . 2 3 1 1 1 1 1 3 3 2 2 2 . 
                            . . . . 2 3 3 3 3 2 2 . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            -200,
            0)
        music.play(music.create_sound_effect(WaveShape.SAWTOOTH,
                5000,
                1,
                255,
                0,
                300,
                SoundExpressionEffect.WARBLE,
                InterpolationCurve.LOGARITHMIC),
            music.PlaybackMode.IN_BACKGROUND)
    elif direction == "right":
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . 2 2 3 3 3 3 2 . . . . 
                            . 2 2 2 3 3 1 1 1 1 1 3 2 . . . 
                            . 1 1 1 1 1 1 1 1 1 1 1 2 . . . 
                            . 2 2 2 3 3 1 1 1 1 1 3 2 . . . 
                            . . . . . 2 2 2 3 3 3 2 . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            200,
            0)
        music.play(music.create_sound_effect(WaveShape.SAWTOOTH,
                5000,
                1,
                255,
                0,
                300,
                SoundExpressionEffect.WARBLE,
                InterpolationCurve.LOGARITHMIC),
            music.PlaybackMode.IN_BACKGROUND)
    elif direction == "up":
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . 2 2 2 . . . . . . . 
                            . . . . . 2 3 1 3 2 . . . . . . 
                            . . . . . 3 1 1 1 3 . . . . . . 
                            . . . . . 3 1 1 1 3 . . . . . . 
                            . . . . . 3 1 1 1 3 . . . . . . 
                            . . . . . 3 1 1 1 2 . . . . . . 
                            . . . . . 2 1 1 1 2 . . . . . . 
                            . . . . . 2 3 1 3 2 . . . . . . 
                            . . . . . . 3 1 3 . . . . . . . 
                            . . . . . . 2 1 2 . . . . . . . 
                            . . . . . . 2 1 2 . . . . . . . 
                            . . . . . . 2 1 2 . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            0,
            -200)
        music.play(music.create_sound_effect(WaveShape.SAWTOOTH,
                5000,
                1,
                255,
                0,
                300,
                SoundExpressionEffect.WARBLE,
                InterpolationCurve.LOGARITHMIC),
            music.PlaybackMode.IN_BACKGROUND)
    elif direction == "down":
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . 2 1 2 . . . . . . 
                            . . . . . . . 2 1 2 . . . . . . 
                            . . . . . . . 2 1 2 . . . . . . 
                            . . . . . . . 3 1 3 . . . . . . 
                            . . . . . . 2 3 1 3 2 . . . . . 
                            . . . . . . 2 1 1 1 2 . . . . . 
                            . . . . . . 2 1 1 1 3 . . . . . 
                            . . . . . . 3 1 1 1 3 . . . . . 
                            . . . . . . 3 1 1 1 3 . . . . . 
                            . . . . . . 3 1 1 1 3 . . . . . 
                            . . . . . . 2 3 1 3 2 . . . . . 
                            . . . . . . . 2 2 2 . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            0,
            200)
        music.play(music.create_sound_effect(WaveShape.SAWTOOTH,
                5000,
                1,
                255,
                0,
                300,
                SoundExpressionEffect.WARBLE,
                InterpolationCurve.LOGARITHMIC),
            music.PlaybackMode.IN_BACKGROUND)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite, location):
    info.change_score_by(1)
    tiles.set_tile_at(location, assets.tile("""
        myTile16
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile3
    """),
    on_overlap_tile)

def on_down_pressed():
    global direction
    mySprite.set_image(img("""
        . . . . . . . . . . 
                . . . . . . . . . . 
                . . . c c c . . . . 
                . . c c b c c c c . 
                . c c b b f c c c b 
                c c b b b f c c c b 
                c b f b b c c c c . 
                c c f f f . . . . . 
                . . . . . . . . . . 
                . . . . . . . . . .
    """))
    direction = "down"
    if not (tiles.tile_at_location_equals(mySprite.tilemap_location().get_neighboring_location(CollisionDirection.BOTTOM),
        assets.tile("""
            myTile16
        """))):
        tiles.set_wall_at(mySprite.tilemap_location().get_neighboring_location(CollisionDirection.BOTTOM),
            False)
        tiles.set_tile_at(mySprite.tilemap_location(),
            assets.tile("""
                myTile15
            """))
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_right_pressed():
    global direction
    mySprite.set_image(img("""
        . . . . . c c c . . 
                . . . . c c b c . . 
                . . . c c b f f . . 
                . . c c b b b f . . 
                . . c b b b b f . . 
                . . c c f f c . . . 
                . . . c c c c . . . 
                . . . c c c c . . . 
                . . . c c c c . . . 
                . . . . b b . . . .
    """))
    direction = "right"
    if not (tiles.tile_at_location_equals(mySprite.tilemap_location().get_neighboring_location(CollisionDirection.RIGHT),
        assets.tile("""
            myTile16
        """))):
        tiles.set_wall_at(mySprite.tilemap_location().get_neighboring_location(CollisionDirection.RIGHT),
            False)
        tiles.set_tile_at(mySprite.tilemap_location(),
            assets.tile("""
                myTile14
            """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def song_and_jar_jar():
    game.set_dialog_cursor(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . f 1 . . . . f 1 . . . . 
                . . . . f f . . . . f f . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . f . . . . f . . . . . 
                . . . . . . f f f f . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    song()
    game.show_long_text("JAR JAR BINKS: \"Mesa welcomen yousa tada STAR WARS MINER!!!\"",
        DialogLayout.BOTTOM)

def on_left_pressed():
    global direction
    mySprite.set_image(img("""
        . . c c c . . . . . 
                . . c b c c . . . . 
                . . f f b c c . . . 
                . . f b b b c c . . 
                . . f b b b b c . . 
                . . . c f f c c . . 
                . . . c c c c . . . 
                . . . c c c c . . . 
                . . . c c c c . . . 
                . . . . b b . . . .
    """))
    direction = "left"
    if not (tiles.tile_at_location_equals(mySprite.tilemap_location().get_neighboring_location(CollisionDirection.LEFT),
        assets.tile("""
            myTile16
        """))):
        tiles.set_wall_at(mySprite.tilemap_location().get_neighboring_location(CollisionDirection.LEFT),
            False)
        tiles.set_tile_at(mySprite.tilemap_location(),
            assets.tile("""
                myTile14
            """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def start():
    global mySprite, direction
    mySprite = sprites.create(img("""
            . . c c c . . . . . 
                    . . c b c c . . . . 
                    . . f f b c c . . . 
                    . . f b b b c c . . 
                    . . f b b b b c . . 
                    . . . c f f c c . . 
                    . . . c c c c . . . 
                    . . . c c c c . . . 
                    . . . c c c c . . . 
                    . . . . b b . . . .
        """),
        SpriteKind.player)
    tiles.set_current_tilemap(tilemap("""
        level2
    """))
    tiles.place_on_random_tile(mySprite, assets.tile("""
        myTile6
    """))
    scene.camera_follow_sprite(mySprite)
    direction = "left"
    controller.move_sprite(mySprite, 50, 50)
    info.set_score(0)
projectile: Sprite = None
mySprite2: Sprite = None
direction = ""
mySprite: Sprite = None
song_and_jar_jar()
start()