import re,sys
old=open('Syntea Case Study.html',encoding='utf-8').read()
t=open('v2/src/template.html',encoding='utf-8').read()
def cut(s,a,b,inc_b=False):
    i=s.index(a); j=s.index(b,i+len(a)); return s[i:j+(len(b) if inc_b else 0)]
css = cut(old,'/* prototype chrome */','/* say hi */') \
    + cut(old,'/* Teams product UI (light, 2024) */','/* assumption matrix */') \
    + cut(old,'/* lean canvas on the DPS template */','/* lean canvas */')
# drop the old .scen-desc etc fine; drop old assumption-matrix leftovers none
evo = cut(old,'      <div class="evo" id="evo">','      <h3 style="margin-top:24px">The click dummy')
evo = evo.replace('Client tenant','IU Group')
proto = cut(old,'      <div class="proto-wrap">','      <div class="annot">')
annot = cut(old,'      <div class="annot">','    </div></div>\n  </div>\n</section>\n\n<section id="outcome">')
lean = cut(old,'<figure class="lean">','</figure>',True)
lean = re.sub(r'src="data:image/webp;base64,[^"]+"','src="lean-canvas.webp"',lean)
flow = cut(old,'<div class="flowchart"','</div>\n\n      <h3>How research shaped',False)
flow = flow.replace('style="display:block;min-width:760px"','style="display:block;min-width:640px"')
scripts = re.findall(r'<script>.*?</script>',old,re.S)
js=[x for x in scripts if 'var LOGO' in x or "getElementById('evo')" in x]
assert len(js)==2, len(js)
t=(t.replace('{{REUSED_CSS}}',css).replace('{{EVO_HTML}}',evo).replace('{{PROTO_HTML}}',proto+annot)
    .replace('{{LEAN}}',lean).replace('{{FLOW}}',flow).replace('{{REUSED_JS}}','\n'.join(js)))
assert '{{' not in t
open('v2/Syntea_Case_Study_v2.html','w',encoding='utf-8').write(t)
print(len(t))
