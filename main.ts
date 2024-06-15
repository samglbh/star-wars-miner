namespace SpriteKind {
    export const arrow = SpriteKind.create()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(img`
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
        `)
    direction = "up"
    if (!(tiles.tileAtLocationEquals(mySprite.tilemapLocation().getNeighboringLocation(CollisionDirection.Top), assets.tile`myTile16`))) {
        tiles.setTileAt(mySprite.tilemapLocation(), assets.tile`myTile15`)
        tiles.setWallAt(mySprite.tilemapLocation().getNeighboringLocation(CollisionDirection.Top), false)
    }
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    for (let index = 0; index < randint(0, 10); index++) {
        music.play(music.createSoundEffect(WaveShape.Sine, 5000, 1801, 255, 255, 5000, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
        tiles.placeOnRandomTile(mySprite2, assets.tile`myTile1`)
        tiles.setTileAt(mySprite2.tilemapLocation(), assets.tile`myTile18`)
        tiles.placeOnTile(mySprite, mySprite2.tilemapLocation())
    }
})
function song () {
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Double)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(392, music.beat(BeatFraction.Double)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(349, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Eighth))
    music.play(music.tonePlayable(330, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Eighth))
    music.play(music.tonePlayable(294, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(523, music.beat(BeatFraction.Double)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(392, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(349, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Eighth))
    music.play(music.tonePlayable(330, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Eighth))
    music.play(music.tonePlayable(294, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(523, music.beat(BeatFraction.Double)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(392, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Eighth))
    music.play(music.tonePlayable(349, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Eighth))
    music.play(music.tonePlayable(330, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Eighth))
    music.play(music.tonePlayable(294, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Double)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(196, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Breve))
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile3`, function (sprite, location) {
    info.changeScoreBy(1)
    tiles.setTileAt(location, assets.tile`myTile16`)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(img`
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
        `)
    direction = "down"
    if (!(tiles.tileAtLocationEquals(mySprite.tilemapLocation().getNeighboringLocation(CollisionDirection.Bottom), assets.tile`myTile16`))) {
        tiles.setWallAt(mySprite.tilemapLocation().getNeighboringLocation(CollisionDirection.Bottom), false)
        tiles.setTileAt(mySprite.tilemapLocation(), assets.tile`myTile15`)
    }
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(img`
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
        `)
    direction = "right"
    if (!(tiles.tileAtLocationEquals(mySprite.tilemapLocation().getNeighboringLocation(CollisionDirection.Right), assets.tile`myTile16`))) {
        tiles.setWallAt(mySprite.tilemapLocation().getNeighboringLocation(CollisionDirection.Right), false)
        tiles.setTileAt(mySprite.tilemapLocation(), assets.tile`myTile14`)
    }
})
function song_and_jar_jar () {
    game.setDialogCursor(img`
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
        `)
    song()
    game.showLongText("JAR JAR BINKS: \"Mesa welcomen yousa tada STAR WARS MINER!!!\"", DialogLayout.Bottom)
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    music.setVolume(100)
    music.stopAllSounds()
    if (direction == "left") {
        projectile = sprites.createProjectileFromSprite(img`
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
            `, mySprite, -200, 0)
        music.play(music.createSoundEffect(WaveShape.Sawtooth, 5000, 1, 255, 0, 300, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), music.PlaybackMode.InBackground)
    } else if (direction == "right") {
        projectile = sprites.createProjectileFromSprite(img`
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
            `, mySprite, 200, 0)
        music.play(music.createSoundEffect(WaveShape.Sawtooth, 5000, 1, 255, 0, 300, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), music.PlaybackMode.InBackground)
    } else if (direction == "up") {
        projectile = sprites.createProjectileFromSprite(img`
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
            `, mySprite, 0, -200)
        music.play(music.createSoundEffect(WaveShape.Sawtooth, 5000, 1, 255, 0, 300, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), music.PlaybackMode.InBackground)
    } else if (direction == "down") {
        projectile = sprites.createProjectileFromSprite(img`
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
            `, mySprite, 0, 200)
        music.play(music.createSoundEffect(WaveShape.Sawtooth, 5000, 1, 255, 0, 300, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), music.PlaybackMode.InBackground)
    }
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(img`
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
        `)
    direction = "left"
    if (!(tiles.tileAtLocationEquals(mySprite.tilemapLocation().getNeighboringLocation(CollisionDirection.Left), assets.tile`myTile16`))) {
        tiles.setWallAt(mySprite.tilemapLocation().getNeighboringLocation(CollisionDirection.Left), false)
        tiles.setTileAt(mySprite.tilemapLocation(), assets.tile`myTile14`)
    }
})
function start () {
    mySprite2 = sprites.create(img`
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
        `, SpriteKind.Player)
    mySprite = sprites.create(img`
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
        `, SpriteKind.Player)
    tiles.setCurrentTilemap(tilemap`level2`)
    tiles.placeOnRandomTile(mySprite, assets.tile`myTile6`)
    scene.cameraFollowSprite(mySprite)
    direction = "left"
    controller.moveSprite(mySprite, 50, 50)
    info.setScore(0)
}
let projectile: Sprite = null
let mySprite2: Sprite = null
let direction = ""
let mySprite: Sprite = null
song_and_jar_jar()
start()
