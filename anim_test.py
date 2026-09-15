import ui

window = ui.NewWindow()
screen = window.screen

run = True

ting = ui.Rect(screen, 350, 250, 50, 50, (255,255,255))
window.create_anim(ting, ting.pos, (700, 300), 1)
window.animate()

while run:
    window.NextFrame()