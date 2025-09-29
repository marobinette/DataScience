# Data Science 1 - HW 3

**Date:** September 26, 2025  
**Course:** CSYS 5870, Fall 2025  

-----

## Question 1: Revisiting a Previous Visualization 

## Question 2: Causal Statements

**Statement 1:** "There are certain groups of people that don't take vaccines and don't take any pills and have no autism." - Donald Trump

% https://q.uiver.app/#q=WzAsNCxbMCwwLCJcXHRleHR7Q2VydGFpbiBHcm91cHN9Il0sWzEsMCwiXFx0ZXh0e05vIFZhY2NpbmVzfSJdLFswLDEsIlxcdGV4dHtObyBQaWxsc30iXSxbMSwxLCJcXHRleHR7Tm8gQXV0aXNtfSJdLFswLDEsIiIsMCx7InN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRvdHRlZCJ9fX1dLFswLDIsIiIsMCx7InN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRvdHRlZCJ9fX1dLFsyLDNdLFsxLDNdXQ==
\[\begin{tikzcd}
	{\text{Certain Groups}} & {\text{No Vaccines}} \\
	{\text{No Pills}} & {\text{No Autism}}
	\arrow[dotted, from=1-1, to=1-2]
	\arrow[dotted, from=1-1, to=2-1]
	\arrow[from=1-2, to=2-2]
	\arrow[from=2-1, to=2-2]
\end{tikzcd}\]

**Statement 2:** "Evidence suggests acetaminophen use in pregnant women, especially late in pregnancy, may cause long-term neurological effects in their children." - [The White House](https://www.whitehouse.gov/articles/2025/09/fact-evidence-suggests-link-between-acetaminophen-autism/)

Loading diagram...



Lightness:
Sync label/edge colours:
Preset:
LaTeX:(None)
Diagram:
Keyboard shortcuts⌘/
General
Dismiss errors, and panels;
Cancel modification or movement;
Hide focus point;
Deselect, and dequeue cells	esc
Import tikz-cd	⌘I
Export to LaTeX	⌘E
Navigation
Pan view	Scroll
Enable mouse panning	ctrl,alt
Enable touch panning	Long press
Enable mouse zooming	⇧
Move focus point	←,↑,↓,→
Select next queued cell	⇥
Select previous queued cell	⇧⇥
Select / deselect object	S
Select cells	;
Toggle cell selection	'
Modification
Focus / defocus label input	↵
Create object, and connect to selection	        
Move selected objects	B
Change source	,
Change target	.
Create arrows from selection	/
Copy	⌘C
Cut	⌘X
Paste	⌘V
Styling
Reverse arrows	R
Flip arrows	E
Flip labels	F
Left-align labels	V
Centre-align labels	C
Over-align labels	X
Modify label position	I
Modify offset	O
Modify curve	K
Modify radius	N
Modify length	L (hold ⇧ to shorten symmetrically)
Modify level	M
Modify style	D
Display as arrow	A
Display as adjunction	J
Display as pullback/pushout	P (press again to switch corner style)
Modify label colour	Y
Modify arrow colour	U
Toolbar
Save diagram in URL	⌘S
Undo	⌘Z
Redo	⇧⌘Z
Select all	⌘A
Select connected components	⇧⌘C
Deselect all	⇧⌘A
Delete	⌫,del
Centre view	G
Zoom out	⌘-
Zoom in	⌘=
Toggle grid	H
Toggle help	⇧⌘H
Export
Toggle diagram centring	C
Toggle ampersand replacement	A
Toggle cramped spacing	R
Toggle fixed size	F
About
quiver is a modern, graphical editor for commutative and pasting diagrams, capable of rendering high-quality diagrams for screen viewing, and exporting to LaTeX via tikz-cd.

Creating and modifying diagrams with quiver is orders of magnitude faster than writing the equivalent LaTeX by hand and, with a little experience, competes with pen-and-paper.

The editor is open source and may be found on GitHub. If you would like to request a feature, or want to report an issue, you can do so here.

You can follow quiver on Mastodon or Twitter for updates on new features.

Thanks to
S. C. Steenkamp, for helpful discussions regarding the aesthetic rendering of arrows.
AndréC, for the custom TikZ style for curves of a fixed height.
Nathan Corbyn, for adding the ability to export embeddable diagrams to HTML.
Paolo Brasolin, for adding offline support.
Carl Davidson, for discussing and prototyping loop rendering.
Everyone who has improved quiver by reporting issues or suggesting improvements.
Created by varkor.
Welcome
quiver is a modern, graphical editor for commutative and pasting diagrams, capable of rendering high-quality diagrams for screen viewing, and exporting to LaTeX via tikz-cd.

quiver is intended to be intuitive to use and easy to pick up. Here are a few tips to help you get started:

Click and drag to create new arrows: the source and target objects will be created automatically.
Double-click to create a new object.
Edit labels with the input bar at the bottom of the screen.
Click and drag the empty space around a object to move it around.
Hold Shift (⇧) to select multiple cells to edit them simultaneously.
Get started
Remember to include \usepackage{quiver} in your LaTeX preamble. You can install the package through CTAN, or open quiver.sty in a new tab to copy-and-paste.updated on 2025-07-05
% https://q.uiver.app/#q=WzAsNCxbMCwwLCJcXHRleHR7TWF0ZXJuYWwgSGVhbHRofSJdLFsxLDAsIlxcdGV4dHtBY2V0YW1pbm9waGVuIFVzZX0iXSxbMSwxLCJcXHRleHR7UGFpbi9JbmZsYW1tYXRpb259Il0sWzEsMiwiXFx0ZXh0e05ldXJvbG9naWNhbCBFZmZlY3RzfSJdLFswLDFdLFsxLDJdLFsyLDNdXQ==
\[\begin{tikzcd}
	{\text{Maternal Health}} & {\text{Acetaminophen Use}} \\
	& {\text{Pain/Inflammation}} \\
	& {\text{Neurological Effects}}
	\arrow[from=1-1, to=1-2]
	\arrow[from=1-2, to=2-2]
	\arrow[from=2-2, to=3-2]
\end{tikzcd}\]


**Statement 3:** "Marvel is better than DC because they have less stereotypical superhero ideas like The Thing versus Superman. The Thing's powers can impede him. They stop him from living a normal life because of his rock-like skin and monstrous appearance, but Superman has all the benefits of being a superhero - speed, superhuman strength, but none of the downsides."



