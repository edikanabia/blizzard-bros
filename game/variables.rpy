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

#region image and transition config variables

define config.layers = ['master', 'background', 'character', 'cg', 'transient', 'screens', 'overlay']
define config.tag_layer = {"bg":"background", "emmett":"character", "cg":"cg"}

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



#endregion motion transforms



#region Sound

$ renpy.music.register_channel("ambience", "sfx", loop=True, tight=True, buffer_queue=True)

#region SFX

#endregion SFX

#region music

#endregion music

#endregion Sound



#region characters
define em = Character("Emmett", image="emmett")
define wb = Character("Werebeast")
define fl = Character("Falo", image="falo")
define narrator = Character(what_italic=True, color="#E7C275") #italics, specify color if so desired

#endregion characters

#region images
#characters
image emmett = "images/emNeutral.png"
image emmett neutral = "images/emNeutral.png"
image emmett happy = "images/emHappy.png"
image emmett thinking = "images/emThink.png"
image emmett pensive = "images/emThoughtful.png"
image emmett gentle = "images/emSmile.png"

#backgrounds
image bg white = Solid("#fff")

#CGs

#endregion images



