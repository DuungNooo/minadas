"""Render a top-down block-plan SVG from the actual generated map commands.

This is a block-layout preview, not a screenshot from Minecraft.
"""
from pathlib import Path
import html
import build_map

def colour(block):
    if 'air'==block:return '#111827'
    for word,value in [('water','#387aaf'),('ice','#9bd8ef'),('snow','#e5f4fb'),('quartz','#ede8da'),('diorite','#c8c9c4'),('grass','#6c965b'),('moss','#607b48'),('leaves','#477b56'),('cherry','#d7a4bb'),('dark_oak','#694a3c'),('spruce','#967456'),('oak','#b39970'),('nether','#622f3b'),('blackstone','#39334b'),('obsidian','#443657'),('basalt','#535460'),('deepslate','#454c59'),('copper','#ac7353'),('glowstone','#ffca66'),('lantern','#a7eddb'),('redstone','#d24b50'),('magma','#c97440'),('glass','#e8b166'),('bookshelf','#976c4b'),('plank','#b89667'),('stone','#83909c'),('brick','#9f8582'),('terracotta','#9777b1'),('target','#dd665b')]:
        if word in block:return value
    return '#a8a49c'

def main():
    panels=[]
    for i,area in enumerate(build_map.AREAS):
        m=build_map.Map(*area);build_map.build(m)
        grid={}
        for cmd in m.commands:
            parts=cmd.split()
            if parts[0]=='fill':
                x1,y1,z1,x2,y2,z2=map(int,parts[1:7]);raw=parts[7]
            elif parts[0]=='setblock':
                x1,y1,z1=map(int,parts[1:4]);x2,y2,z2=x1,y1,z1;raw=parts[4]
            else:raise ValueError(cmd)
            block=raw.split(':',1)[1].split('[')[0].split('{')[0]
            for x in range(x1,x2+1):
                for z in range(z1,z2+1):
                    col=grid.setdefault((x-m.cx,z-m.cz),{})
                    for y in range(y1,y2+1):
                        if block=='air':col.pop(y,None)
                        else:col[y]=block
        ox=22+(i%4)*248;oy=104+(i//4)*270
        panels.append(f'<g transform="translate({ox},{oy})"><rect x="-8" y="-32" width="240" height="252" rx="12" fill="#182235"/>')
        panels.append(f'<text x="4" y="-12" fill="#f4f6fb" font-size="13">{i+1:02} · {html.escape(m.title)}</text>')
        for (x,z),column in grid.items():
            if not column:continue
            block=column[max(column)];px=(x+35)*3;py=(z+35)*3
            panels.append(f'<rect x="{px}" y="{py}" width="3.1" height="3.1" fill="{colour(block)}"/>')
        panels.append('<circle cx="105" cy="45" r="4" fill="#ff5c82" stroke="white"/>')
        panels.append(f'<text x="4" y="235" fill="#9caec6" font-size="11">X {m.cx} · Z {m.cz} · fantasia:campaign</text></g>')
    text='<svg xmlns="http://www.w3.org/2000/svg" width="1008" height="920" viewBox="0 0 1008 920"><rect width="100%" height="100%" fill="#0d1523"/><g font-family="Noto Sans CJK KR, sans-serif"><text x="24" y="39" fill="#f2dfab" font-size="28" font-weight="bold">FANTASIA · 균열의 왕</text><text x="26" y="66" fill="#a8b7cd" font-size="13">11개 구역 · 실제 생성 블록의 평면도 · 분홍 점: 도착 지점 · 게임 화면 캡처 아님</text>'+''.join(panels)+'</g></svg>'
    out=Path(__file__).resolve().parents[1]/'artifacts/map_preview.svg';out.parent.mkdir(exist_ok=True);out.write_text(text)
    print(out)

if __name__=='__main__':main()
