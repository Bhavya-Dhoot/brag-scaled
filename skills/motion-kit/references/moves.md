# Moves

Every move is a pure function of time: given `u` (seconds since the move began) it returns
a style. No timers, no CSS transitions, so any frame can be rendered alone and in any order.

Helpers used below (they are in every reference engine):

```js
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const seg = (t, a, b) => clamp((t - a) / (b - a));               // 0..1 progress between two times
const eo = x => 1 - Math.pow(1 - x, 3);                           // ease out: fast, then settles
const eio = x => x < .5 ? 4*x*x*x : 1 - Math.pow(-2*x + 2, 3) / 2; // ease in and out: for travel
const spring = x => x <= 0 ? 0 : 1 - Math.exp(-x * 8) * Math.cos(x * 20);   // overshoots, then settles
const bump = x => x <= 0 || x >= 1 ? 0 : Math.sin(x * Math.PI);  // 0 -> 1 -> 0, for a pulse
```

## Entrances

| Move | Looks like | Time | Formula |
|---|---|---|---|
| rise | fades in while moving up a little | 0.4 s | `opacity = p; translateY((1 - eo(p)) * 30px)` |
| pop | scales up from nothing with an overshoot | 0.4 s | `scale(spring(u * 1.15))` |
| slam / stamp | arrives too big and lands hard | 0.14 s | `scale(2.3 - 1.3 * eo(clamp(u / .14)))`, with a thud |
| slide-in | comes in from the side | 0.3 s | `translateX((1 - eo(p)) * 320px)`, add a little skew for speed |
| stretch | grows from a flat line | 0.3 s | `scaleY(.08 + .92 * eo(p))`, origin at the baseline |
| blur-in | blurry to sharp | 0.5 s | `filter: blur((1 - p) * 18px)`; costly per frame, use on one element |
| typewriter | text types itself | 0.03 s a letter | monospace: `width = round(n * p) ch`; other type: `clip-path: inset(0 (1-p)*100% 0 0)` |
| draw-on | a line draws itself | 0.3-0.7 s | `pathLength=1; stroke-dasharray: 1 1; stroke-dashoffset = 1 - eo(p)` |
| wipe | a block of colour grows from one edge | 0.35 s | `scaleX(eo(p))`, origin at that edge |

## Proof

| Move | Looks like | Time | Formula |
|---|---|---|---|
| count-up | a number rolls to its value | 0.7-1.0 s | `round(from + (to - from) * eo(p))`; start it on the spoken number |
| bar fill | a progress bar fills | 0.6-1.0 s | `width = eio(p) * 100%`, with a rising tick every 0.1 s |
| tick | a box gets its check | 0.22 s | draw-on for the check, `scale(1 + bump(u / .28) * .35)` on the box |
| badge flip | a label turns over into its opposite | 0.28 s | old `scaleY(1 - 2p)` for `p < .5`, new `scaleY(2p - 1)` after |
| strike-through | a claim is crossed out | 0.4 s | draw-on of a marker line that follows the cursor |
| compare | two values, one marked | 0.4 s | the odd one shakes `sin(u * 60) * 5 * (1 - u / .4)` and changes colour |

## The cursor acts

| Move | Looks like | Time | Formula |
|---|---|---|---|
| travel | the cursor crosses the frame | 0.4-0.7 s | `eio` between two points; start it while the camera is still moving |
| hover-lift | a button rises as the cursor arrives | 0.2 s | `translate(-3px, -3px)` and a deeper offset shadow |
| press | a button sinks on the click | 0.2 s | `translate(4px, 4px) * bump(u / .2)`, shadow shrinks; a ring spreads from the cursor |
| drag and drop | an object follows the cursor into a target | 0.5-0.7 s | while held: `left = cursor.x - grab.x`, tilt 4 degrees, bigger shadow; on release the target pulses |
| hold-to-fill | a bar fills while the button is held | 1-3 s | progress is `seg(t, down, up)`; the button stays in its pressed state |
| slider scrub | a knob dragged back and forth, values answering live | 1.5 s | drive everything from the knob position; overshoot and come back once so it reads as a hand |
| toggle | a switch flips | 0.2 s | knob `left` eased, track colour changes at the halfway point |

## Camera and space

| Move | Looks like | Time | Formula |
|---|---|---|---|
| fly-to | the camera moves to a tile | 0.55-0.75 s | interpolate centre with `eio`, zoom geometrically: `z0 * (z1 / z0) ** p` |
| punch-in | the whole frame jumps closer | 0.28 s | `scale(1 + bump(u / .28) * .045)` on the accent word |
| push | a slow move in while a line is read | the whole hold | `scale(1 + .05 * seg(t, t0, t1))` |
| dive | one world rushes past, the next settles | 0.5 s | old: `scale(1 + 4.2 * p * p)`, fading late; new: `scale(1.28 - .28 * eo(p))` underneath |
| reframe | a full-screen panel shrinks into a card while something new appears | 0.6 s | animate the panel's rect with `eio`; bring the new element in at `p > .5` |
| shockwave | a ring spreads from a click across the frame | 0.9 s | a circle growing with `eo(p)`, opacity `1 - p`; tiles jolt as it passes |

## Reward

| Move | Looks like | Time | Formula |
|---|---|---|---|
| done flash | a finished tile swells and gains a coloured ring | 0.45 s | `scale(1 + bump(u / .45) * .03)`, ring from 5 to 12 px and back |
| pip fill | one step of a "3 of 5" counter fills | 0.35 s | colour change with `scale(1 + bump(u / .35) * .5)` |
| confetti | a small burst from the finished thing | 1.5 s | 16-20 squares: `x = vx * u * (1 - .25u)`, `y = vy * u + 900 * u * u`, fade after 1 s |
| fly-chip | a value leaves a document and lands in a table | 0.3 s | lerp start to end with `eo`, lift `sin(p * pi) * 26px` on the way |
| beat pulse | finished things nod on the beat | each beat | `bump(((t - t0) / beat - i * .5) % 4 / .6) * .014` added to scale |
