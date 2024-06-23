# second scene
label scene_two:
    scene bg black
    "Coming back to ground floor, the howling wind persists from outside."
    play foley wind
    scene bg window snow
    with dissolve
    "Even if I hadn't looked outside, I could tell that the blizzard is still raging on."
    "I doubt it's going to let up within the next day; I'm effectively trapped here until it subsides."
    stop ambience fadeout 0.7
    "That's what I get for letting curiosity get the better of me. However I did see with my own eyes that this mansion is not completely abandoned."
    scene bg fireplace night
    with fade

    play ambience fireplace fadein 0.2
    "It didn't take me long to find a fireplace I could settle next to for the night, however admittedly, I did get slightly...distracted."
    "No one is around to care if I snooped around, and I doubt the occupant downstairs minds either."
    play music emmettmotif

    "I settle down next to the fireplace, using magic to light up the logs."
    "I start to read over the documents I've gathered around the mansion..."
    show emmett
    em "This one looks like a journal entry."
    em "Maybe I'll be lucky and this can give some insight to what happened here..."
    journal "Hopefully this will not be the last time I am able to write. I am done working for this family. I did not come to this conclusion lightly, as I have worked for them for Lord knows how long. Frankly, I regret not leaving when the child was infected... but I stayed out of loyalty to her, as I had seen her grow up. Probably a bit naive in hindsight. I stayed and tried to help but instead watched everyone turn. You can't even call this a plague, this is- something else."
    show emmett thinking
    em "Hm, it seems like a curse went around this mansion. But what was the cause of it?"
    em "Maybe this list of names and room numbers are the people who were affected by this magic." 
    em "So it wasn't just the family but it looks like the mansion staff were cursed too…"
    journal "When word got out that the child turned, about half of the staff dropped overnight. The kitchen was a mess. My comrades wrapped any food that they could carry on their backs in spare linens from the washroom-"
    "The bottom of the entry has been eaten by moths, lost to time."
    show emmett pensive
    em "I was right! They did look like they left in a hurry. But there's still a lot that's not fitting here."
    "I look at another letter I found earlier, which was near the front door of the mansion. I crack open the wax seal and unfold it."
    nvl clear
    journal "Leave now. There was a reason why those who turned were left behind."
    show emmett neutral
    stop music fadeout 0.3
    em "…They were abandoned?"
    "I look over from across the house, where I can see the door to the basement."
    show emmett pensive
    em "Well, it looks like he has a lot of explaining to do tomorrow."
    stop ambience fadeout 1.0
    jump scene_three
    return

# fourth scene (Stara.rpy has third scene)
label scene_four:
    
    scene bg fireplace day
    with fade
    play ambience fireplace fadein 0.3
    "I must have scraped this mansion from top to bottom, and there are barely any scraps of wood left for kindling."
    show emmett thinking
    em "That's strange… I could have sworn that there would have been more bones laying around based on our talk this morning…"
    em "There are less corpses than the names of people who were cursed…"
    em "And comparing the dates of the letters up to now, the werebeast would have starved to death- but he didn't!"
    show emmett pensive
    em "He is not trapped here, as I am able to come and go as I please- he can too."
    hide emmett
    scene bg four
    with fade
    play foley walk
    "I walk back into the basement, with less kindling this time. The Werebeast is staring at the flames with his back to me."
    play music emmett1 noloop
    queue music emmett2
    wb "Have you ever taken something back that was stolen from you?"
    em "Well, I did find out that some of my tools were stolen the other day."
    em "But then I realized that whomever took them probably needed them a lot more than I did at that moment."
    em "I was able to buy some new ones at a little shop one town over from here."
    "The Werebeast is silent, only the sounds of the wood crackling in the fire can be heard."
    wb "It feels like before I even took this form I had to find a way to survive."
    wb "…I wish I did not have to eat them."
    em "So let's say that you did eat all of those people-"
    "He quickly turns to me, head craining at an almost unnatural angle."
    wb "I did."
    em "No you did not. There are no hidden bodies stored anywhere within this mansion."
    em "I've swept it from top to bottom, gathering firewood. You think it just appeared out of thin air?"
    em "And you haven't eaten me yet, and you won't."
    wb "…"
    wb "But I cursed all of them… and who's to say that I won't do that to you too."
    em "You haven't done that yet either."
    em "You can't change the past, but you can come with me."
    wb "And do what? I'd better use as the last piece of furniture in this mansion."
    em "Come with me anyways."
    wb "I-"
    em "You can't just sit here and wallow for all eternity about what you should have done." 
    em "That was your old life, and there's nothing you can do to change it."
    em "There's no one here to stop you. It would be like starting over."
    "I set the firewood down and start to put the tools back in my bag."
    em "I'll let you think about it. Once the blizzard dies down, I'll be leaving. You're welcome to join me."
    "I leave the Werebeast alone in the basement, as the flames reduce to a simmer."
    stop music fadeout 1.0
    stop ambience fadeout 0.5
    jump scene_final
    return

