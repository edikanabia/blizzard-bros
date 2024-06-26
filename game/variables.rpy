#Script to initialize all characters, images, music, sfx, vfx. Initialization should be used for constants,
#and variables that are set should not be changed.

define newFade = Fade(0.3, 0.2, 0.3) #test

#screenshake effect
init:

    python:
        
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

        Shake = renpy.curry(_Shake)
    #

define shake = Shake((0,0,0,0),1.0, dist=15)

#beep voice character callback
init python:
    def beep_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "slow_done":
            renpy.sound.play("audio/sfx/menu_ctc.ogg", "sound", loop=False)


#region image and transition config variables

define config.layers = ['master', 'background', 'character', 'cg', 'transient', 'screens', 'overlay']
define config.tag_layer = {"bg":"background", "emmett":"character", "falo":"character", "cg":"cg"}

transform fade_to_alpha_fast(old_widget, new_widget):
    old_widget
    linear 0.15 alpha 0.0
    new_widget
    linear 0.15 alpha 1.0

define config.say_attribute_transition = ComposeTransition(trans=dissolve, before=fade_to_alpha_fast)
define config.say_attribute_transition_layer = "character"

#endregion config variables



#region user-defined transitions

#endregion user-defined transitions

#region static transforms
transform left_edge:
    align (0.05, 1.0)
    yalign 1.0

transform person_a:
    xalign 0.15
    yalign 1.0

transform person_b:
    xalign 0.3
    yalign 1.0

transform person_c:
    xalign 0.5
    yalign 1.0

transform person_d:
    xalign 0.7
    yalign 1.0

transform person_e:
    xalign 0.82
    yalign 1.0

transform right_edge:
    xalign 0.95
    yalign 1.0



#endregion static transforms

#region motion transforms
transform move_to_offscreenleft:
    linear 0.8 offscreenleft

transform move_to_left_edge:
    linear 0.8 left_edge

transform move_to_person_a:
    linear 0.8 person_a

transform move_to_person_b:
    linear 0.8 person_b

transform move_to_person_c:
    linear 0.8 person_c

transform move_to_person_d:
    linear 0.8 person_d

transform move_to_person_e:
    linear 0.8 person_e

transform move_to_right_edge:
    linear 0.8 right_edge

transform move_to_offscreenright:
    linear 0.8 offscreenright



#endregion motion transforms

#region ctcanim
image ctc_indicator:
    "gui/click_to_continue_indicator.png"
    align (0.79, 0.925)
      
    parallel:
        ease_bounce 0.5 yalign 0.92
        ease_bounce 0.5 yalign 0.925

    
    repeat
    


#endregion ctcanim



#region Sound

init python:
    renpy.music.register_channel("ambience", "sfx", loop=True, tight=True, buffer_queue=True)
    renpy.music.register_channel("foley","sfx", loop=False)

#region SFX oneshots
define audio.growl = "audio/sfx/beast_growl.ogg"
define audio.blanket = "audio/sfx/blanket.ogg"
define audio.creak = "audio/sfx/door_creak.ogg"
define audio.door_open = "audio/sfx/door_open.ogg"
define audio.door_shut = "audio/sfx/door_shut.ogg"
define audio.walk = "audio/sfx/footsteps_slow(reverb).ogg"
define audio.monster = "audio/sfx/ominous_shuffling.ogg"
define audio.paper = "audio/sfx/paper.ogg"
define audio.knock = "audio/sfx/slow_knock.ogg"
define audio.panic_knock = "audio/sfx/panicked_knock.ogg"
define audio.sizzle = "audio/sfx/sizzle.ogg"



#endregion SFX oneshots

#region SFX ambience
define audio.fireplace = "audio/sfx/ambience_fireplace.ogg"
define audio.wind = "audio/sfx/wind.ogg"
define audio.noise = "audio/sfx/ambience_noise.ogg"

#endregion SFX ambience


#region music

define audio.haunting = "audio/bgm/haunting.ogg"
define audio.meeting ="audio/bgm/meeting.ogg"
define audio.emmett1 = "audio/bgm/emmett_intro.ogg"
define audio.emmett2 = "audio/bgm/emmett_loop.ogg"
define audio.imgsong1 = "audio/bgm/(instr)escape_intro.ogg"
define audio.imgsong2 = "audio/bgm/(instr)escape_loop.ogg"
define audio.falomotif = "<from 0.0 to 15.4>audio/bgm/haunting.ogg"
define audio.emmettmotif = "audio/bgm/emmett_motif.ogg"
define audio.imgsongbeat = "audio/bgm/escape_beat.ogg"

#endregion music

#endregion Sound



#region characters
define em = Character("Emmett", image="emmett", ctc="ctc_indicator", ctc_position="fixed", callback=beep_voice)
define wb = Character("Werebeast", ctc="ctc_indicator", ctc_position="fixed", callback=beep_voice)
define fl = Character("Falo", image="falo", ctc="ctc_indicator", ctc_position="fixed", callback=beep_voice)
define narrator = Character(what_font="LibreBaskerville-Italic.ttf", what_color="#f3d491", ctc="ctc_indicator", ctc_position="fixed", callback=beep_voice) 
define journal = Character(kind=nvl_narrator, what_color="#362c1f", what_outlines=[(0, None, 0, 0)], what_font="fonts/blzee.ttf")

#endregion characters

#region images
#characters
image emmett = "images/emNeutral.png"
image emmett neutral = "images/emNeutral.png"
image emmett happy = "images/emHappy.png"
image emmett thinking = "images/emThink.png"
image emmett pensive = "images/emThoughtful.png"
image emmett gentle = "images/emSmile.png"

image falo = "images/flNeutral.png"
image falo neutral = "images/flNeutral.png"
image falo happy = "images/flSmile.png"
image falo thinking = "images/flThink.png"

#backgrounds
image bg white = Solid("#fff")
image bg black = Solid("#000")
image bg fireplace day = "images/BGFireplaceDay.png"
image bg fireplace night = "images/BGFireplaceNight.png"
image bg window snow = "images/BGWindowSnow.png"
image bg window clear = "images/BGWindowClear.png"

#CGs
image bg one = "images/CG1.png"
image bg two = "images/CG2.png"
image bg three = "images/CG3.png"
image bg four = "images/CG4.png"

#endregion images




