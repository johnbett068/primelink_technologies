from pathlib import Path
import subprocess
import re
from html.parser import HTMLParser

root=Path(__file__).resolve().parent
out=root/'qa-output'; out.mkdir(exist_ok=True)
class Check(HTMLParser):
    def __init__(self): super().__init__(); self.ids=[]; self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        self.links += [a[k] for k in ('href','src') if k in a]
c=Check();c.feed((root/'index.html').read_text(encoding='utf-8'))
assert len(c.ids)==len(set(c.ids))
for link in c.links:
    if link.startswith('#'):assert link[1:] in c.ids,link
    elif ':' not in link:assert (root/link).exists(),link
print('Local links and assets: PASS')
harness='''<!doctype html><html><body><pre id="results">RUNNING</pre><iframe style="border:0;height:1000px" src="../index.html"></iframe><script>
const frame=document.querySelector('iframe'), results=[];
const check=(ok,msg)=>{if(!ok)throw Error(msg);results.push('PASS: '+msg)};
frame.onload=async()=>{try{
const w=frame.contentWindow,d=w.document;
w.addEventListener('error',e=>results.push('ERROR: '+e.message));
[...d.images].forEach(i=>{i.loading='eager';});
await new Promise(r=>setTimeout(r,1500));
for(const width of [320,375,425,768,1024,1440,1920]){
frame.style.width=width+'px'; await new Promise(r=>setTimeout(r,100));
check(d.documentElement.scrollWidth<=width,'No overflow at '+width+'px');
check([...d.images].every(i=>i.complete&&i.naturalWidth>0),'Images at '+width+'px');
if(width<=768){const menu=d.querySelector('.menu-toggle');menu.click();check(menu.getAttribute('aria-expanded')==='true','Mobile menu opens');d.querySelector('#main-nav a[href="#services"]').click();check(menu.getAttribute('aria-expanded')==='false','Mobile menu closes');}
}
for (const tab of d.querySelectorAll('.environment-tab')) {
tab.click();
check(tab.getAttribute('aria-selected')==='true','Environment selected: '+tab.dataset.environment);
check(d.querySelectorAll('.environment-panel:not([hidden])').length===1,'One environment panel visible');
check(!d.querySelector('#'+tab.getAttribute('aria-controls')).hidden,'Correct environment panel');
}
const firstTab=d.querySelector('.environment-tab'); firstTab.click();
firstTab.dispatchEvent(new w.KeyboardEvent('keydown',{key:'ArrowDown',bubbles:true}));
check(d.activeElement.id==='tab-schools','Environment keyboard navigation');
firstTab.click();
d.querySelector('[data-service="Cybersecurity"]').click();
check(d.querySelector('#service').value==='Cybersecurity','Service enquiry selection');
d.querySelector('[data-enquiry="Schools"]').click();
check(d.querySelector('#message').value.includes('schools'),'Environment enquiry context');
d.querySelector('#contact').scrollIntoView({behavior:'instant'});
w.dispatchEvent(new w.Event('scroll'));
check(d.querySelector('#main-nav a[aria-current="location"]').getAttribute('href')==='#contact','Active navigation follows scroll');
check(d.querySelector('#message').validationMessage==='','Autofilled message validity refreshed');
w.scrollTo({top:0,behavior:'instant'});
w.open=url=>{w.testURL=url;return null};
const f=d.querySelector('form');
for(const [name,value] of Object.entries({name:'Test User',phone:'123',email:'test@example.com',service:'Software Development',message:'Please quote for our new business website.'})){f.elements.namedItem(name).value=value;}
f.dispatchEvent(new w.Event('input',{bubbles:true}));f.requestSubmit();check(!w.testURL,'Invalid phone blocked');
f.elements.phone.value='+254 720 394 517';f.dispatchEvent(new w.Event('input',{bubbles:true}));f.requestSubmit();
check(w.testURL.startsWith('https://wa.me/254720394517?text='),'WhatsApp recipient');
const decoded=decodeURIComponent(w.testURL);check(['Test User','test@example.com','Software Development','Please quote'].every(t=>decoded.includes(t)),'Enquiry details encoded');
check(d.querySelector('#form-status a').href===w.testURL,'Popup fallback link');
check(!results.some(t=>t.startsWith('ERROR:')),'No runtime errors');
document.querySelector('#results').textContent=results.join('\\n')+'\\nALL PASSED';
}catch(e){document.querySelector('#results').textContent=results.join('\\n')+'\\nFAIL: '+e.stack;}};
</script></body></html>'''
(out/'checks.html').write_text(harness,encoding='utf-8')
chrome=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
base=[chrome,'--headless','--disable-gpu','--no-first-run','--allow-file-access-from-files','--hide-scrollbars']
result=subprocess.run(base+['--dump-dom','--virtual-time-budget=15000',(out/'checks.html').as_uri()],capture_output=True,text=True,timeout=60)
(out/'result.html').write_text(result.stdout,encoding='utf-8')
match=re.search(r'<pre id="results">(.*?)</pre>',result.stdout,re.S)
print(match.group(1) if match else result.stderr[-2000:])
for width in [375,1440]:
    # Chrome's desktop headless window has a minimum width. Use an iframe
    # for a true mobile CSS viewport inside that window.
    (out/'preview.html').write_text(f'<html><body style="margin:0;background:#ddd"><iframe src="../index.html" style="border:0;width:{width}px;height:20000px"></iframe></body></html>',encoding='utf-8')
    subprocess.run(base+[f'--window-size={max(width,600)},5000',f'--screenshot={out/f"website-{width}.png"}','--virtual-time-budget=2000',(out/'preview.html').as_uri()],capture_output=True,timeout=60)
print('Desktop and mobile previews saved in qa-output.')
assert match and 'ALL PASSED' in match.group(1)
