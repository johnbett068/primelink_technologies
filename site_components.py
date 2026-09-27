"""Reusable static HTML components for the PrimeLink site. No runtime dependency."""
from html import escape

SERVICE_MEDIA = [
    ('software', 'Laptop and monitor with programming and software architecture interfaces', 'Discuss your needs', 'Websites · Business systems · APIs'),
    ('support', 'Professional helpdesk headset and computer diagnostics workstation', 'Get IT Support', 'Troubleshooting · Setup · Consultancy'),
    ('security', 'Security shield above a connected motherboard', 'Secure Your Business', 'System protection · Backups · Data security'),
    ('cctv', 'Professional bullet and dome CCTV cameras with monitoring screens', 'Plan Your Security', 'IP cameras · Installation · Monitoring'),
    ('network', 'Enterprise switch, blue ethernet cables and Wi-Fi access point', 'Plan Your Network', 'LAN & Wi-Fi · Cabling · Infrastructure'),
    ('repair', 'Laptop internals, RAM, SSD and precision repair tools', 'Repair Your Device', 'Diagnostics · Repairs · Upgrades'),
    ('equipment', 'Business laptop, desktop monitor, printer and computer accessories', 'Request Equipment', 'Computers · Printers · Accessories'),
    ('supplies', 'Organized office stationery, printing paper, binders and toner', 'Request Supplies', 'Stationery · Toners · Office essentials'),
]

def brand(footer=False):
    lazy = ' loading="lazy"' if footer else ''
    return f'<a class="brand" href="#home" aria-label="PrimeLink Technologies home"><img src="assets/logo/primelink-roundel.webp" width="212" height="200" alt="Original PrimeLink logo"{lazy}><span class="brand-type">Prime<span>Link</span><small>TECHNOLOGIES</small></span></a>'

def service_cards(services, icon):
    cards=[]
    for n, ((i,t,d),(asset,alt,cta,tags)) in enumerate(zip(services,SERVICE_MEDIA),1):
        cards.append(f'''<article class="service-card" id="service-{asset}">
  <div class="service-visual"><img src="assets/images/{asset}.webp" width="768" height="512" loading="lazy" decoding="async" alt="{alt}"><span class="service-number">0{n}</span><span class="service-icon">{icon(i)}</span></div>
  <div class="service-content"><h3>{escape(t)}</h3><p>{escape(d)}</p><span class="service-tags">{escape(tags)}</span><a href="#contact" data-service="{escape(t)}">{cta} {icon('arrow')}</a></div>
</article>''')
    return '\n'.join(cards)

def approach(icon):
    return f'''<section class="approach" aria-labelledby="approach-title"><div class="container approach-inner"><div class="approach-label"><span class="approach-arrow">{icon('network')}</span><p id="approach-title">The PrimeLink<br><strong>Approach</strong></p></div><p class="approach-words"><span>TECHNOLOGY.</span><i></i><span>SUPPORT.</span><i></i><span>SECURITY.</span><i></i><span>SOLUTIONS.</span></p><a href="#services">Discover what we do <span>↓</span></a></div></section>'''

ENVIRONMENTS = [
    ('business','Businesses','building','equipment','A stronger foundation for everyday business.','Bring your business systems, devices and network together with practical technology and dependable technical support.',['Business software','Cybersecurity','Office networking','IT support']),
    ('schools','Schools','file','software','Connected classrooms. Supported learning.','Equip classrooms and administration with computers, campus Wi-Fi, networking and CCTV designed around your institution.',['Computer labs','Campus Wi-Fi','CCTV systems','Technical support']),
    ('homes','Homes','home','network','A connected, more secure home.','Plan your home internet, Wi-Fi coverage and CCTV setup with help choosing and configuring the right equipment.',['Internet setup','Home Wi-Fi','CCTV cameras','Device support']),
    ('offices','Offices','monitor','equipment','A workplace that works with you.','Keep your team equipped with computers, printers, reliable connectivity and the supplies that support daily work.',['Workstations','Printers & supplies','Structured cabling','IT maintenance']),
    ('retail','Retail Shops','shop','cctv','Technology for your day-to-day trade.','Connect your shop, look after your devices and plan CCTV coverage for the spaces that matter to your business.',['Business systems','CCTV coverage','Network setup','Computer support']),
    ('hospitality','Hospitality','hospitality','network','Better connections for guests and teams.','Plan guest Wi-Fi, staff networks, CCTV and technical support around the needs of your hotel or hospitality business.',['Guest Wi-Fi','CCTV systems','Network infrastructure','IT support']),
    ('institutions','Institutions','building','security','Technology that supports your mission.','Bring systems, infrastructure and equipment together for institutions, NGOs and organizations with varied operational needs.',['Secure systems','ICT equipment','Network planning','Ongoing support']),
    ('remote','Remote / Rural Sites','pin','network','Practical connections, wherever you work.','Discuss connectivity options, site requirements and equipment suitable for your remote or rural location in Kenya.',['Connectivity planning','Wi-Fi distribution','Equipment setup','Maintenance']),
]

def environments(icon):
    tabs=[];panels=[]
    for key,title,i,asset,heading,description,tags in ENVIRONMENTS:
        tabs.append(f'<button class="environment-tab" id="tab-{key}" type="button" data-environment="{key}">{icon(i)}<span>{title}</span>{icon("arrow")}</button>')
        panels.append(f'''<article class="environment-panel" id="environment-{key}" aria-labelledby="tab-{key}"><div class="environment-image"><img src="assets/images/{asset}.webp" width="768" height="512" loading="lazy" decoding="async" alt="Technology equipment for {escape(title.lower())}"><span class="environment-badge">{icon(i)} {escape(title)}</span></div><div class="environment-copy"><p class="eyebrow">BUILT AROUND YOUR ENVIRONMENT</p><h3>{heading}</h3><p>{description}</p><ul>{''.join(f'<li>{icon("check")}{escape(tag)}</li>' for tag in tags)}</ul><a class="text-link" href="#contact" data-enquiry="{title}">Let’s plan your solution {icon('arrow')}</a></div></article>''')
    return '<div class="environment-layout"><div class="environment-tabs" aria-label="Choose your environment">'+''.join(tabs)+'</div><div class="environment-panels">'+''.join(panels)+'</div></div>'

def ecosystem(icon):
    nodes=[('code','Software','software'),('network','Network','network'),('shield','Security','security'),('camera','CCTV','cctv'),('monitor','Computers','equipment'),('support','Support','support'),('file','Supplies','supplies')]
    positions=[(170,60),(500,35),(830,60),(890,230),(725,390),(280,390),(105,230)]
    paths=''.join(f'<path d="M500 225 Q{x} 225 {x} {y}"/>' for x,y in positions)
    links=''.join(f'<a href="#service-{asset}" class="ecosystem-node node-{n}">{icon(i)}<span>{title}</span></a>' for n,(i,title,asset) in enumerate(nodes))
    return f'''<section class="section ecosystem" aria-labelledby="ecosystem-title"><div class="container"><div class="center-heading"><p class="eyebrow">THE POWER OF CONNECTED TECHNOLOGY</p><h2 id="ecosystem-title">One partner.<br><span>Every connection.</span></h2><p>Software, systems, security and supplies.<br>Designed to work together. Supported by PrimeLink.</p></div><div class="ecosystem-map"><svg class="ecosystem-lines" viewBox="0 0 1000 450" preserveAspectRatio="none" aria-hidden="true"><g fill="none" stroke="#2183b2" stroke-width="1">{paths}</g><g class="data-lines" fill="none" stroke="#6bd9f5" stroke-width="2" stroke-dasharray="3 160">{paths}</g><ellipse cx="500" cy="225" rx="220" ry="150" fill="none" stroke="#164461" stroke-dasharray="2 8"/></svg><div class="ecosystem-core"><img src="assets/logo/primelink-roundel.webp" width="212" height="200" loading="lazy" alt="PrimeLink Technologies — one connected technology partner"></div>{links}</div></div></section>'''
