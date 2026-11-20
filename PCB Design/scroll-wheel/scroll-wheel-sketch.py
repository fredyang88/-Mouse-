from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

OUT = Path(__file__).parent
ink = '#24313b'
muted = '#647580'
blue = '#23689b'
orange = '#ba5b20'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                     'text.color': ink, 'axes.labelcolor': ink,
                     'svg.fonttype': 'none'})
fig = plt.figure(figsize=(13, 8.5), facecolor='white')
gs = fig.add_gridspec(1, 2, width_ratios=[1.35, 1], left=.045,
                      right=.97, bottom=.23, top=.85, wspace=.12)
ax = fig.add_subplot(gs[0, 0])
ax.set_aspect('equal')
ax.set_xlim(-6.7, 8.0)
ax.set_ylim(-3.5, 13.2)
ax.axis('off')

def line(a, b, color=ink, lw=1.2, ls='-'):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=lw, ls=ls)

def vdim(x, y0, y1, text, color=ink, side='left', size=11):
    ax.annotate('', xy=(x,y1), xytext=(x,y0),
                arrowprops=dict(arrowstyle='<->', color=color, lw=1.1,
                                shrinkA=0, shrinkB=0))
    ax.text(x + (-.20 if side=='left' else .20), (y0+y1)/2,
            text, ha='right' if side=='left' else 'left', va='center',
            color=color, fontsize=size)

# Common mounting datum and shell floor. Offset deliberately unscaled.
ax.add_patch(Rectangle((-3.25,-.55), 7.45,.55, facecolor='#e2e9ed',
                       edgecolor=ink, lw=1.3, hatch='///'))
line((-5.2,0), (6.7,0), muted, 1, '-.')
ax.text(.4, -.90, 'PCB / common mounting plane: z = 0', ha='center', fontsize=10)
ax.add_patch(Rectangle((-3.25,-2.75),7.45,.55,facecolor='#edf0f2',edgecolor=ink,lw=1.3))
ax.text(.4,-3.18,'Inner shell floor', ha='center', fontsize=10)
vdim(5.2,-2.2,0,'s',muted,side='right')
line((4.2,-2.2),(5.5,-2.2),muted,.8)

# Generic switch outline: body proportions are illustrative, not part dimensions.
ax.add_patch(Rectangle((-1.65,0),3.3,4.65,facecolor='#f0f3f4',edgecolor=ink,lw=1.5))
ax.add_patch(Rectangle((-.65,4.65),1.3,2.05,facecolor='#f9e8dc',edgecolor=orange,lw=1.5))
ax.text(0,2.4,'Middle-click\nswitch',ha='center',va='center')
line((-.9,7.3),(.9,7.3),muted,1.3,'--')
line((-.9,6.7),(.9,6.7),orange,2)

# Only the contact collar/axle feature is shown, not outer scroll wheel diameter.
ax.add_patch(Circle((0,9),2.3,facecolor='#e8f1f7',edgecolor=blue,lw=2))
ax.add_patch(Circle((0,9),.28,facecolor='white',edgecolor=blue,lw=1))
line((-3.1,9),(5.2,9),muted,.85,'-.')
line((0,6.2),(0,11.9),muted,.85,'-.')
ax.plot(0,6.7,'o',color=orange,ms=5)
ax.text(0,12.25,'CONTACT-END SECTION',ha='center',fontsize=11,fontweight='medium')
ax.text(0,11.65,'Contact collar / axle feature: Ø4.6 mm',ha='center',fontsize=10)
ax.annotate('Axle centre',xy=(0,9),xytext=(3.15,10.3),fontsize=10,
            arrowprops=dict(arrowstyle='-',color=muted,lw=.8))

# Nominal geometry dimensions.
line((-4.1,0),(-3.3,0),muted,.8)
line((-4.1,9),(-2.5,9),muted,.8)
vdim(-3.8,0,9,'9.0 mm',blue)
line((.1,6.7),(4.3,6.7),orange,.8)
line((.1,9),(4.3,9),muted,.8)
vdim(4.0,6.7,9,'R2.3',blue,side='right',size=10)
vdim(6.4,0,6.7,'6.7 mm\n±0.2*',orange,side='left')
ax.annotate('Contact surface at rest',xy=(.1,6.7),xytext=(-6.1,5.65),
            fontsize=10,color=orange,
            arrowprops=dict(arrowstyle='-',color=orange,lw=.8))

# Separate enlarged illustration of preload, kept symbolic.
bx=fig.add_subplot(gs[0,1])
bx.set_xlim(0,10)
bx.set_ylim(0,12)
bx.axis('off')
bx.text(0,11.8,'SWITCH HEIGHT & PRELOAD',fontsize=12,fontweight='medium')
bx.text(0,10.8,'Dashed: free, uncompressed actuator',fontsize=10,color=muted)
bx.text(0,10.1,'Solid: actuator touching collar at rest',fontsize=10,color=orange)
bx.plot([.3,9.2],[1.6,1.6],color=muted,lw=1)
bx.add_patch(Rectangle((2.5,1.6),3.0,4.0,facecolor='#f0f3f4',edgecolor=ink,lw=1.5))
bx.add_patch(Rectangle((3.45,5.6),1.1,1.6,facecolor='#f9e8dc',edgecolor=orange,lw=1.5))
bx.plot([3.1,4.9],[8.3,8.3],ls='--',color=muted,lw=1.3)
bx.plot([3.1,4.9],[7.2,7.2],color=orange,lw=2)
bx.annotate('',xy=(6.2,8.3),xytext=(6.2,7.2),
            arrowprops=dict(arrowstyle='<->',color=ink,lw=1.1,shrinkA=0,shrinkB=0))
bx.plot([4.95,6.4],[8.3,8.3],color=muted,lw=.8,ls='--')
bx.plot([4.95,6.4],[7.2,7.2],color=orange,lw=.8)
bx.text(6.55,7.75,'c = preload\ncompression',va='center',fontsize=10)
bx.annotate('',xy=(1.3,7.2),xytext=(1.3,1.6),
            arrowprops=dict(arrowstyle='<->',color=orange,lw=1.1,shrinkA=0,shrinkB=0))
bx.text(1.08,4.4,'6.7 mm',rotation=90,ha='right',va='center',color=orange)
bx.text(4,1.1,'Switch mounting plane',ha='center',fontsize=10)
bx.text(.3,.15,'Preload inset exaggerated; c is not specified.',fontsize=10,color=muted)

fig.text(.06,.95,'Scroll-wheel / middle-click height sketch',fontsize=19,fontweight='medium')
fig.text(.06,.906,'Nominal geometry from your measurements • all dimensions in mm • schematic only',
         fontsize=11,color=muted)
fig.text(.06,.18,'Contact height = 9.0 − (4.6 ÷ 2) = 6.7 mm',fontsize=14,color=orange)
fig.text(.06,.132,'Same mounting plane: free switch height = 6.7 + c',fontsize=12)
fig.text(.06,.092,'Above inner shell floor: contact height = s + 6.7; free actuator height = s + 6.7 + c',fontsize=11)
fig.text(.06,.047,'* ±0.2 mm is your estimated geometric allowance, not switch travel. If c = 0, contact is just touching.',
         fontsize=10,color=muted)
fig.savefig(OUT/'scroll-wheel-height-sketch.png',dpi=180,facecolor='white')
fig.savefig(OUT/'scroll-wheel-height-sketch.svg',facecolor='white')
print(OUT/'scroll-wheel-height-sketch.png')
