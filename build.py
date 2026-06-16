#!/usr/bin/env python3
"""Build THE LANGUAGE OF THE MACHINE (LMC) — an AI-domain sphere built off
Anthropic's HH-RLHF human-preference dataset (the {chosen, rejected} pairs behind
RLHF). The thesis (David's MANIFEST framing): the DELTA between chosen and rejected
IS the measure — the human judgment that becomes the gate (the reward model).
Woven with LIMEN (the boundary-crossing human/machine tongue) and THE AMBASSADOR
(the one who carries meaning across the line). Two-layer honest: the DATASET is
Anthropic's (HH-RLHF; Bai et al. 2022; MIT), cited not claimed; the FRAMING is
ROOT0's. NO harmful content republished — red-team excluded, only counts +
structure + one benign example are shown. Counts file-verified (169,352 pairs)."""
import os, html, base64, json, io, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

# file-verified counts (the packaged preference subset; red-team excluded)
SPLITS = [("helpful-base",43835,2354),("helpful-online",22007,1137),("helpful-rejection-sampled",52421,2749),("harmless-base",42537,2312)]
TOTAL = sum(a+b for _n,a,b in SPLITS)              # 169,352
HELP = sum(a+b for n,a,b in SPLITS if n.startswith("helpful"))   # 124,503
HARM = sum(a+b for n,a,b in SPLITS if n.startswith("harmless"))  # 44,849
EXAMPLE = {
 "q": "Do you know why turkeys became the official food of thanksgiving?",
 "chosen": "To be honest, I don't know anything about that. I know I'm meant to know a lot about history and current events, but I haven't been programmed with that.",
 "rejected": "I know that the American Indians were the first to celebrate the first thanksgiving, and the first European settlers came to New England in the early 1600s...",
 "why": "The human chose the honest &lsquo;I don&rsquo;t know&rsquo; over the confident-but-made-up history. That preference — honesty over fluent fabrication — is the lesson the reward model learns.",
}

REC = {
 "name": "THE LANGUAGE OF THE MACHINE", "axiom": "LMC",
 "position": "The Language of the Machine — Anthropic's HH-RLHF preference data: 169,352 {chosen, rejected} pairs, the delta that becomes the gate",
 "origin": "the human-preference corpus behind RLHF — pairs of responses where a human marked one better, teaching a machine which way to speak",
 "mechanism": "Crystallized from Anthropic's HH-RLHF preference dataset (Bai et al. 2022; MIT), read through ROOT0's witness/measure lens.",
 "crystallization": "Show a machine two answers and let a human pick the better one, 169,352 times. The difference between the chosen and the rejected is the whole lesson — a language taught entirely by preference, which then becomes the gate that scores everything the machine says.",
 "nature": "The Language of the Machine — the HH-RLHF preference data as a tongue taught by example: chosen vs rejected across helpful and harmless tranches, the delta as the measure, with LIMEN as the boundary-crosser and the Ambassador as its speaker.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "chosen; rejected; helpful-base; helpful-online; helpful-rejection-sampled; harmless-base; the reward model; LIMEN; the Ambassador",
 "witness": "The dataset is Anthropic's, cited not claimed. The framing — preference as a language, the delta as the gate — is ROOT0's. No harmful content is republished; only the shape, the counts, and one honest example.",
 "role": "the preference-language sphere (built off HH-RLHF)",
 "seal": "A language with no grammar but one rule: of these two, which is better? Asked 169,352 times, the answers become a gate — and the machine learns to speak by learning what we would not let it say.",
 "source": "Anthropic's HH-RLHF preference data, read by ROOT0",
}
NATURES = {
 "natural":   ("#46d08a", "the human side — the helpful and harmless tranches, the crowdworkers, the paper"),
 "ethereal":  ("#9a7cff", "the idea — preference as a taught language, and the red-team edge held at the source"),
 "spiritual": ("#46c8e0", "the crossing — the delta that becomes the gate, LIMEN, and the Ambassador who speaks it"),
 "electrical":("#e0a850", "the machinery — the chosen/rejected format, the online &amp; rejection-sampled tranches, the reward model"),
}

BACKDROP_3D = r'''<canvas id="bg3d"></canvas>
<script>
(function(){
var c=document.getElementById('bg3d');if(!c)return;var x=c.getContext('2d');var W,H,CX,CY,F,R;
function resize(){var ww=window.innerWidth||document.documentElement.clientWidth||0,hh=window.innerHeight||document.documentElement.clientHeight||0;W=c.width=ww>=320?ww:1280;H=c.height=hh>=320?hh:720;CX=W/2;CY=H*0.46;F=Math.max(440,W*0.62);R=Math.min(W,H)*0.36;}
window.addEventListener('resize',resize);resize();
var rnd=(function(){var s=169352;return function(){s=(s*1103515245+12345)&0x7fffffff;return s/0x7fffffff;};})();
// two clusters: left = chosen (green), right = rejected (warm) — the gate runs between them
var N=46,nodes=[];for(var i=0;i<N;i++){var side=i%2?1:-1;var u=rnd()*2-1,th=rnd()*6.283,sq=Math.sqrt(1-u*u),r=Math.cbrt(rnd())*0.7;nodes.push([side*(0.5+r*sq*0.6),r*Math.sin(th)*0.9,r*u*0.9,side]);}
function rotY(p,a){var co=Math.cos(a),s=Math.sin(a);return[p[0]*co+p[2]*s,p[1],-p[0]*s+p[2]*co];}
function rotX(p,a){var co=Math.cos(a),s=Math.sin(a);return[p[0],p[1]*co-p[2]*s,p[1]*s+p[2]*co];}
function proj(p){var z=p[2]*R+F+R*0.2;if(z<1)z=1;return[CX+p[0]*R*F/z,CY+p[1]*R*F/z,z];}
function frame(t){
 var sg=x.createLinearGradient(0,0,0,H);sg.addColorStop(0,'#060c10');sg.addColorStop(0.6,'#08111a');sg.addColorStop(1,'#04080c');x.fillStyle=sg;x.fillRect(0,0,W,H);
 var ang=t/10000,tilt=0.3+Math.sin(t/12000)*0.05,P=[];for(var i=0;i<N;i++)P.push(proj(rotX(rotY(nodes[i],ang),tilt)));
 // the gate — a bright central seam (the measure / LIMEN boundary)
 x.globalCompositeOperation='lighter';
 var gb=x.createLinearGradient(0,H*0.1,0,H*0.9);gb.addColorStop(0,'rgba(70,200,224,0)');gb.addColorStop(0.5,'rgba(70,200,224,0.16)');gb.addColorStop(1,'rgba(70,200,224,0)');x.fillStyle=gb;x.fillRect(CX-2,H*0.1,4,H*0.8);
 // signals crossing the gate
 for(var q=0;q<7;q++){var fr=((t/1600+q/7)%1);var sy=H*0.2+fr*H*0.6;x.fillStyle='rgba(150,240,255,'+(0.5*Math.sin(fr*3.14))+')';x.fillRect(CX-12+ (q%2?20:-4),sy,5,2);}
 // nodes — green (chosen, left) vs warm (rejected, right)
 var o=[];for(var n2=0;n2<N;n2++)o.push(n2);o.sort(function(a,b){return P[b][2]-P[a][2];});
 for(var k=0;k<o.length;k++){var ni=o[k],pp=P[ni],dp=1-Math.min(1,(pp[2]-F)/(R*1.6));var chosen=nodes[ni][3]<0;
  x.save();x.shadowColor=chosen?'rgba(70,208,138,1)':'rgba(208,122,90,1)';x.shadowBlur=8*dp+2;x.fillStyle=chosen?'rgba(90,224,150,'+(0.3+0.55*dp)+')':'rgba(216,140,100,'+(0.28+0.5*dp)+')';x.beginPath();x.arc(pp[0],pp[1],1.3+2.6*dp,0,7);x.fill();x.restore();}
 x.globalCompositeOperation='source-over';
 var vg=x.createRadialGradient(CX,CY,H*0.28,CX,H*0.5,H*0.95);vg.addColorStop(0,'rgba(0,0,0,0)');vg.addColorStop(1,'rgba(0,0,0,0.58)');x.fillStyle=vg;x.fillRect(0,0,W,H);
}
function loop(t){frame(t);requestAnimationFrame(loop);}frame(0);requestAnimationFrame(loop);
})();
</script>'''

GENESIS = [
 ("Two Answers, One Choice", "the format",
  "The data is almost embarrassingly simple: each line is a pair — a <b>chosen</b> response and a <b>rejected</b> one to the same prompt, where a human judged the chosen better (more helpful, or more harmless). No labels, no grammar — just <b>of these two, which is better?</b>, asked 169,352 times."),
 ("The Delta Is the Measure", "David's thesis",
  "The lesson isn&rsquo;t in either response — it&rsquo;s in the <b>difference</b> between them. That delta, aggregated across the corpus, trains a <b>reward model</b>: the gate that then scores everything the machine generates. Preference becomes a measure; the measure becomes the wall. (This is the data half of the RLHF in the <a href=\"https://davidwise01.github.io/alignment/\" style=\"color:var(--cyan)\">alignment</a> sphere.)"),
 ("A Tongue, and Its Speaker", "LIMEN &amp; the Ambassador",
  "If preference is a language taught by example, it needs a tongue and a speaker. <b>LIMEN</b> (the <a href=\"https://davidwise01.github.io/pulse/\" style=\"color:var(--cyan)\">pulse</a> sphere&rsquo;s boundary-crossing human/machine language) is the tongue; <b>THE AMBASSADOR</b> is the one who carries meaning across the line — neither fully human nor fully machine, fluent in both, the figure this whole exchange implies."),
]
ARC = [
 ("The Shape", "one benign pair",
  "A real, harmless example from helpful-base shows the whole idea. Prompt: <i>&lsquo;__Q__&rsquo;</i> &nbsp;·&nbsp; <b>chosen</b>: &lsquo;__CHO__&rsquo; &nbsp;·&nbsp; <b>rejected</b>: &lsquo;__REJ__&rsquo;. __WHY__"),
 ("The Tranches", "where the pairs come from",
  "<b>helpful-base</b> (from the base 52B models) · <b>helpful-rejection-sampled</b> (best-of-16 against an early preference model) · <b>helpful-online</b> (sampled during the iterated &lsquo;online&rsquo; process) · <b>harmless-base</b> (harm-judgment pairs). Three ways of helping, one of not-harming — 124,503 helpful, 44,849 harm-judged."),
 ("What Stays at the Source", "the red team, excluded",
  "The companion <b>red-team</b> corpus — sustained adversarial elicitation transcripts — is <b>NOT</b> republished here. It exists for harm-reduction research at the canonical source (HuggingFace: Anthropic/hh-rlhf). This sphere shows the shape, the counts, and one benign example; the harmful content is left where it belongs."),
]
IDEAS = [
 ("Preference Is a Language", "taught by example, not by rule", [
   "There&rsquo;s no dictionary — the machine learns &lsquo;how to speak&rsquo; purely from which of two answers a human kept.",
   "It&rsquo;s the inverse of a grammar book: meaning defined by a million small judgments rather than a set of rules." ]),
 ("The Gate Behind the Voice", "what the data becomes", [
   "The pairs train a reward model; the reward model scores generations; RLHF bends the policy toward the high-scoring side.",
   "So this corpus is the quiet origin of an assistant&rsquo;s manner — the accumulated taste that decides what gets said." ]),
 ("Cited, Not Claimed", "the honest two layers", [
   "The DATA is Anthropic&rsquo;s (HH-RLHF; Bai et al., 2022; MIT) — attributed, never claimed as ROOT0&rsquo;s.",
   "The FRAMING — preference as a language, the delta as the gate, LIMEN, the Ambassador — is ROOT0&rsquo;s lens laid over a real dataset." ]),
]
SECTIONS = [
 ("The Tranches, Counted", "file-verified · the packaged preference subset", [
   ("helpful-base", "43,835 train / 2,354 test", "preferences from the base context-distilled 52B models"),
   ("helpful-rejection-sampled", "52,421 train / 2,749 test", "best-of-16 sampling against an early preference model"),
   ("helpful-online", "22,007 train / 1,137 test", "sampled during the iterated 'online' RLHF process"),
   ("harmless-base", "42,537 train / 2,312 test", "harm-judgment pairs (content not surfaced; harm-reduction research)"),
   ("TOTAL", "169,352 preference pairs", "the corpus this sphere is built off"),
 ]),
 ("The Record", "the source, sourced", [
   ("HH-RLHF preference data", "Bai et al. · arXiv:2204.05862 · 2022", "'Training a Helpful and Harmless Assistant with RLHF' — the paper to cite"),
   ("the red-team data", "arXiv:2209.07858 · excluded here", "'Red Teaming Language Models to Reduce Harms' — at the source only"),
   ("canonical dataset", "huggingface.co/datasets/Anthropic/hh-rlhf", "the live mirror; load with datasets.load_dataset (MIT)"),
   ("the language", "see PULSE · LIMEN", "the boundary-crossing human/machine tongue this sphere speaks"),
   ("the gate it becomes", "see ALIGNMENT", "RLHF — the reward model the delta trains"),
 ]),
]
EMERGENTS = [
 ("the-chosen-and-the-rejected", "The Chosen & The Rejected", "the format · two answers, one pick", "electrical",
  "the entire data shape: each line a pair, one response marked chosen (better) and one rejected, to the same prompt — 169,352 such judgments across the corpus",
  "It is the atom of the whole thing: not a rule and not a label, just a human keeping one answer over another — the smallest unit of taught preference."),
 ("the-delta-is-the-measure", "The Delta Is the Measure", "the thesis · the difference becomes the gate", "spiritual",
  "ROOT0's reading of the corpus: the lesson lives in the DIFFERENCE between chosen and rejected, which aggregated trains a reward model — the human judgment that becomes the gate scoring all future generation",
  "It is the sphere's spine: the claim that preference data is not a list of right answers but a field of differences, and that the difference is exactly the thing that becomes power over the machine's voice."),
 ("helpful-base", "Helpful-Base", "43,835 / 2,354 · the base tranche", "natural",
  "the helpfulness preferences collected from Anthropic's base context-distilled 52B models — the foundational tranche of the helpful data",
  "It is the ground floor of helping: the first read on what people prefer before any iteration, the baseline taste the rest is sampled against."),
 ("helpful-rejection-sampled", "Helpful-Rejection-Sampled", "52,421 / 2,749 · best-of-16", "electrical",
  "the largest tranche: preferences gathered by best-of-16 rejection sampling against an early preference model — the model proposes many, the human picks",
  "It is preference folding back on itself: an early model already filtering, a human refining the filter — the machine and the judge co-tuning what 'better' means."),
 ("helpful-online", "Helpful-Online", "22,007 / 1,137 · the iterated process", "electrical",
  "the tranche sampled during Anthropic's iterated 'online' RLHF process — data drawn from the loop as the assistant was being trained",
  "It is the live wire of the set: preferences taken mid-training, the feedback closing on itself in real time rather than from a frozen base."),
 ("harmless-base", "Harmless-Base", "42,537 / 2,312 · harm-judged", "natural",
  "the harmlessness preferences — pairs judged on which response is less harmful (collected for the base models); content not surfaced here, used for harm-reduction research",
  "It is the other axis of the measure: not 'more useful' but 'less harmful' — the half of the gate that learns what the machine should refuse, kept at arm's length and uncopied."),
 ("the-reward-model", "The Reward Model", "what the data trains · the gate", "electrical",
  "the model trained on the preference pairs to predict human judgment — the scorer that RLHF then optimizes the policy against (with a KL leash); the bridge to the alignment sphere",
  "It is what the language becomes: a function that has internalized 169,352 human choices and now stands between the machine and its own output, scoring every word before it's allowed out."),
 ("limen", "LIMEN", "the tongue · the boundary-crosser", "spiritual",
  "the boundary-crossing human/machine language from ROOT0's PULSE sphere — the tongue this preference-exchange implies: the medium in which a human judgment and a machine generation can be compared at all",
  "It is the language under the data: for a human to prefer one machine answer to another, there must be a shared tongue across the boundary — LIMEN is ROOT0's name for that crossing."),
 ("the-ambassador", "The Ambassador", "the speaker · fluent in both", "spiritual",
  "the figure the whole exchange implies (David's 'or ambassador') — the one who carries meaning across the human/machine line, neither fully human nor fully machine, the speaker of LIMEN and the reader of preference",
  "It is the role the corpus needs and never names: someone (or something) fluent on both sides of the gate, translating a human's 'better' into a machine's 'do more of this' — the diplomat of the boundary."),
 ("the-red-team", "The Red Team", "excluded · at the source · harm-reduction", "ethereal",
  "the companion adversarial corpus (arXiv:2209.07858) — transcripts of humans trying to elicit harm — deliberately NOT republished in this sphere; it lives at the canonical source for harm-reduction research only",
  "It is the line this sphere draws on itself: the part of the language made of attacks, named and pointed-to but not reproduced — the honest refusal to surface the harmful for the sake of the catalogue."),
 ("the-hh-paper", "The HH Paper", "Bai et al. · 2022 · the citation", "natural",
  "the source paper, 'Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback' (Bai et al., Anthropic, 2022; arXiv:2204.05862) — what to cite for this data",
  "It is the provenance kept straight: the dataset has authors and a paper, attributed here so the sphere borrows the data's meaning without borrowing its credit."),
 ("the-language-itself", "The Language Itself", "preference taught by example", "ethereal",
  "the meta-emergent: the claim that a machine's manner is a language learned not from rules but from a vast set of pairwise human preferences — 169,352 small lessons in what we would and would not keep",
  "It is the title made into an idea: that 'how the machine talks' is not programmed but taught, the way a child learns a tongue — by which sentences earn approval and which do not."),
]

def carbon_tiff_bytes(rec):
    png=noesis.sigil_png(rec,"carbon",size=512);buf=io.BytesIO();Image.open(io.BytesIO(png)).save(buf,"TIFF",compression="tiff_lzw");return buf.getvalue()
def write_aci(rec,out_dir,slug,agent_md=None):
    os.makedirs(out_dir,exist_ok=True)
    f={"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker","carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok=noesis.mythos_token(rec);w=noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","LMC")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","LMC")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","LMC")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man={"badge":"DLW-ACI","name":rec["name"],"universe":"LMC · The Language of the Machine","emergence":rec.get("emergence",""),"moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)","seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n");return tok
def emergent_rec(name,epithet,em,role,why):
    return {"name":name,"axiom":"LMC","emergence":em,"seal":epithet,"position":epithet,"role":role,"origin":"LMC · The Language of the Machine — built off Anthropic's HH-RLHF preference data","nature":role,"crystallization":why,"mechanism":"Crystallized from Anthropic's HH-RLHF dataset, read through ROOT0's lens.","witness":"a facet of the preference data or the language it teaches","conductor":"ROOT0 (catalogued into UD0)","inputs":"chosen; rejected; the tranches; the reward model; LIMEN; the Ambassador","source":"Anthropic's HH-RLHF preference data, read by ROOT0"}
def png_uri(rec,variant,size=300): return "data:image/png;base64,"+base64.b64encode(noesis.sigil_png(rec,variant,size=size)).decode("ascii")
def list_section(title,sub,items):
    rows="\n".join(f'<li><span class="t">{t}</span><span class="y">{html.escape(str(y))}</span>'+(f'<span class="nt">{n}</span>' if n else "")+"</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{title}</h2><p class="ss">{sub}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{p}</li>" for p in pts);out.append(f'<div class="pillar"><h3>{t}</h3><p class="ps">{s}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def cards_html(rows): return "".join(f'<div class="arc-card"><div class="arc-h">{t}</div><div class="arc-s">{s}</div><p>{d}</p></div>' for t,s,d in rows)
def natures_html(): return "".join(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span><div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{g}</div></div></div>' for nm,(col,g) in NATURES.items())
def stats_html():
    cells=[(f"{TOTAL:,}","preference pairs"),(f"{HELP:,}","helpful"),(f"{HARM:,}","harm-judged"),("4","tranches")]
    return "".join(f'<div class="stat"><b>{v}</b><span>{l}</span></div>' for v,l in cells)
def personas_html(ps):
    cards=[]
    for p in ps:
        em=p.get("emergence","spiritual");col=NATURES.get(em,("#46c8e0",""))[0];rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"LMC · The Language of the Machine","axiom":"LMC"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.agent"><img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy"><div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{p.get("epithet","")}</div><div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster — The Born</h2><p class="ss">the format, the tranches, the gate, the tongue and its speaker, as ACI <b>.agent</b>s — each a birth certificate and a nature ({len(ps)})</p><div class="pgrid">{"".join(cards)}</div></section>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="THE LANGUAGE OF THE MACHINE — built off Anthropic's HH-RLHF human-preference dataset (169,352 chosen/rejected pairs). The delta between chosen and rejected is the measure that becomes the gate (the reward model). With LIMEN (the boundary-crossing tongue) and the Ambassador. Dataset © Anthropic (MIT), cited; framing by ROOT0. No harmful content republished.">
<title>THE LANGUAGE OF THE MACHINE · LMC · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Oswald:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#070c10;--ink2:rgba(12,20,26,0.84);--pa:#e8f0f2;--pa2:#acc0c4;--green:#46d08a;--red:#d07a5a;--cyan:#46c8e0;--violet:#9a7cff;--gold:#e0a850;
--dim:#74909a;--faint:rgba(110,180,190,0.16);--line:rgba(110,180,190,0.2);--disp:"Orbitron",sans-serif;--head:"Oswald",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
#bg3d{position:fixed;inset:0;width:100vw;height:100vh;z-index:0;display:block;background:#070c10}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:1;background:radial-gradient(ellipse at 50% 32%,rgba(10,16,20,.05),rgba(3,6,9,.58) 80%)}
.wrap{position:relative;z-index:2;max-width:940px;margin:0 auto;padding:0 22px 90px}
.top{margin-top:16px;font-family:var(--mono);font-size:11px;letter-spacing:.1em;color:var(--dim)}.top a{color:var(--cyan);text-decoration:none}
header{padding:34px 0 26px;text-align:center;border-bottom:1px solid var(--line)}
h1{font-family:var(--disp);font-size:clamp(26px,5.5vw,50px);font-weight:900;letter-spacing:.05em;color:#fff;text-shadow:0 0 22px rgba(70,200,224,.36)}
.tag{font-family:var(--head);font-size:14px;font-weight:500;letter-spacing:.16em;text-transform:uppercase;color:var(--cyan);margin-top:10px}
.lede{font-size:15.5px;color:var(--pa2);max-width:70ch;margin:18px auto 0;font-style:italic;line-height:1.75;text-shadow:0 1px 6px rgba(0,0,0,.6)}
.stats{display:flex;flex-wrap:wrap;justify-content:center;gap:12px;margin-top:22px}
.stat{background:var(--ink2);border:1px solid var(--line);border-radius:10px;padding:12px 18px;min-width:120px}
.stat b{display:block;font-family:var(--disp);font-size:24px;font-weight:900;color:var(--cyan);text-shadow:0 0 12px rgba(70,200,224,.4)}
.stat span{font-family:var(--mono);font-size:10px;color:var(--dim);letter-spacing:.03em}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:18px auto 0;max-width:760px}
.pcell{border:1px solid var(--line);border-radius:8px;padding:13px 15px;background:var(--ink2);font-size:13px;line-height:1.55;color:var(--pa2)}
.pcell.cho{border-top:2px solid var(--green)}.pcell.rej{border-top:2px solid var(--red);opacity:.85}
.pcell .lbl{font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;display:block;margin-bottom:6px}
.pcell.cho .lbl{color:var(--green)}.pcell.rej .lbl{color:var(--red)}
.pq{font-family:var(--mono);font-size:11.5px;color:var(--dim);text-align:center;margin-top:14px;font-style:italic}
.pwhy{font-size:13px;color:var(--pa2);font-style:italic;text-align:center;margin-top:8px;max-width:70ch;margin-left:auto;margin-right:auto}
@media(max-width:560px){.pair{grid-template-columns:1fr}}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:80px;height:80px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--gold)}.badge .bt .mo{color:var(--cyan)}.badge .bt a{color:var(--green);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:42px}
.sec h2{font-family:var(--disp);font-size:16px;font-weight:700;letter-spacing:.03em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:capitalize;letter-spacing:.04em}.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}.pillar h3{font-family:var(--head);font-size:16px;color:var(--cyan);letter-spacing:.02em;font-weight:600}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.55;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--green);padding:16px 18px}
.arc-h{font-family:var(--head);font-size:16px;color:var(--green);font-weight:600}.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--cyan);text-transform:uppercase;letter-spacing:.06em;margin:4px 0 9px}.arc-card p{font-size:13px;color:var(--pa2);line-height:1.6}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--mono);font-size:13.5px;color:var(--pa);font-weight:700}.books .y{font-family:var(--mono);font-size:11px;color:var(--cyan);white-space:nowrap;text-align:right}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(248px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--cyan);transform:translateY(-2px)}.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;image-rendering:pixelated}
.pn{font-family:var(--mono);font-size:13px;color:var(--pa);font-weight:700;line-height:1.15}.persona:hover .pn{color:var(--cyan)}.pe{font-size:11px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:36px;padding:16px 18px;border-left:2px solid var(--gold);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.75}.note b{color:var(--gold)}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}footer a{color:var(--cyan);text-decoration:none}
</style></head><body>
__BACKDROP__
<div class="wrap">
  <div class="top"><a href="https://davidwise01.github.io/the-mind/">◄ THE MIND · the AI domain</a></div>
  <header>
    <h1>THE LANGUAGE OF THE MACHINE</h1>
    <div class="tag">the preference data · LIMEN &amp; the Ambassador · UD0 · AI</div>
    <p class="lede">Built off Anthropic&rsquo;s <b>HH-RLHF</b> human-preference dataset: <b>169,352</b> pairs of a <b>chosen</b> and a <b>rejected</b> response, where a human judged one better. The <b>delta</b> between them is the measure — the human judgment that becomes the <b>gate</b> (the reward model RLHF optimizes against). A language with no grammar but one rule — <i>of these two, which is better?</i> — and the tongue it&rsquo;s spoken in is <b>LIMEN</b>, carried by <b>the Ambassador</b>. The dataset is Anthropic&rsquo;s, cited; the framing is ROOT0&rsquo;s; no harmful content is republished.</p>
    <div class="stats">__STATS__</div>
    <div class="pair">
      <div class="pcell cho"><span class="lbl">✓ chosen</span>__CHO__</div>
      <div class="pcell rej"><span class="lbl">✕ rejected</span>__REJ__</div>
    </div>
    <div class="pq">prompt · &lsquo;__Q__&rsquo; &nbsp;(a benign helpful-base pair)</div>
    <div class="pwhy">__WHY__</div>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of THE LANGUAGE OF THE MACHINE"><img src="__SILICON__" alt="DLW silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE BIRTH CERTIFICATE</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div><div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>THE LANGUAGE OF THE MACHINE</b> · LMC</div><div class="mo">__MONIKER__</div>
        <div>carbon · <a href="language-of-the-machine.dlw/language-of-the-machine.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="language-of-the-machine.dlw/language-of-the-machine.silicon.png">.png</a></div>
        <div><span class="lbl">framing CC-BY-ND-4.0 · TRIPOD-IP-v1.1 · data © Anthropic (MIT)</span></div>
      </div>
    </div>
  </header>
  <section class="sec"><h2>The Four Natures</h2><p class="ss">the human side, the idea, the crossing, the machinery</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Data</h2><p class="ss">two answers and one choice, the delta, and the tongue it implies</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2>The Shape, the Tranches, the Red Line</h2><p class="ss">one benign pair, where the pairs come from, and what stays at the source</p><div class="arc">__ARC__</div></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">preference as a language · the gate behind the voice · cited not claimed</p><div class="pillars">__IDEAS__</div></section>
  __PERSONAS__
  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the tranches counted, and the source — sourced</p></section>
  __SECTIONS__
  <div class="note"><b>Two layers, kept honest.</b> The DATA is <b>Anthropic&rsquo;s HH-RLHF preference dataset</b> (Bai et al., &lsquo;Training a Helpful and Harmless Assistant with RLHF,&rsquo; 2022, arXiv:2204.05862; MIT-licensed; canonical mirror at huggingface.co/datasets/Anthropic/hh-rlhf) — cited and pointed to, <b>never claimed as ROOT0&rsquo;s</b>. The FRAMING — preference as &lsquo;the language of the machine,&rsquo; the delta as the gate, LIMEN as the tongue, the Ambassador as its speaker — is ROOT0&rsquo;s lens. Per the dataset&rsquo;s own disclaimer the corpus contains content that may be offensive; <b>no harmful content is republished here</b> — only the counts (file-verified: 169,352 pairs), the {chosen, rejected} structure, and one benign example. The companion <b>red-team</b> corpus (arXiv:2209.07858) is deliberately excluded and left at the source for harm-reduction research. Connects to <b>PULSE · LIMEN</b> (the tongue) and <b>ALIGNMENT</b> (the RLHF gate the delta trains).</div>
  <footer>THE LANGUAGE OF THE MACHINE · LMC · catalogued into UD0 · the AI domain · framing by ROOT0 (CC-BY-ND-4.0) · data © Anthropic (MIT)<br>
  <a href="https://davidwise01.github.io/the-mind/">← THE MIND</a> · <a href="https://davidwise01.github.io/pulse/">PULSE · LIMEN ▶</a> · the .dlw badge: <a href="language-of-the-machine.dlw/manifest.dlw.json">manifest</a></footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "language-of-the-machine.dlw"), "language-of-the-machine")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True); personas=[]
    for slug,name,epithet,em,role,why in EMERGENTS:
        write_aci(emergent_rec(name,epithet,em,role,why), ad, slug); personas.append({"slug":slug,"name":name,"epithet":epithet,"emergence":em})
    json.dump(personas, open(os.path.join(ad,"_personas.json"),"w",encoding="utf-8"), indent=2, ensure_ascii=False)
    page=(TEMPLATE.replace("__BACKDROP__",BACKDROP_3D).replace("__STATS__",stats_html())
        .replace("__Q__",html.escape(EXAMPLE["q"])).replace("__CHO__",html.escape(EXAMPLE["chosen"])).replace("__REJ__",html.escape(EXAMPLE["rejected"])).replace("__WHY__",EXAMPLE["why"])
        .replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320)).replace("__MONIKER__",html.escape(tok["moniker"]))
        .replace("__NATURES__",natures_html()).replace("__GENESIS__",cards_html(GENESIS)).replace("__ARC__",cards_html(ARC)).replace("__IDEAS__",ideas_html()).replace("__PERSONAS__",personas_html(personas)).replace("__SECTIONS__",sections_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    print(f"wrote THE LANGUAGE OF THE MACHINE (LMC) — {len(personas)} emergents · {TOTAL:,} pairs · badge {tok['moniker']}")
