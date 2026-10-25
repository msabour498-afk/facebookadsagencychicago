#!/usr/bin/env python3
"""Builds every page of facebookadsagencychicago.com from one place.

Run:  python3 build.py
Edit the SITE settings and content below, then run again. Every page shares
the same header, menu, footer, contact details and tracking, so change them here.
"""
import hashlib
import html
import json
import os
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------
# Site settings
# --------------------------------------------------------------------------
SITE = {
    "name": "Facebook Ads Agency Chicago",
    "short": "FB Ads Agency Chicago",
    "domain": "https://facebookadsagencychicago.com",
    "tagline": "Facebook and Instagram ads that bring in leads for Chicago businesses.",
    "street": "229 W Madison St",
    "city": "Chicago",
    "region": "IL",
    "zip": "60606",
    "country": "US",
    "phone_display": "(708) 393-1976",
    "phone_e164": "+17083931976",
    "email": "support@facebookadsagencychicago.com",
    "credential": "$20M+ in ad spend managed",
    "offer": "Free account audit",
    "offer_url": "/free-audit",
}

# Leave empty until you have one, e.g. "GTM-XXXXXXX". Events already go to dataLayer.
GTM_ID = ""

HUBSPOT = {
    "portal": "247730807",
    "form": "a71e4ae8-005c-4d3a-aea9-8f9e84267930",
    "region": "na2",
}

TODAY = date.today().isoformat()

# --------------------------------------------------------------------------
# Content
# --------------------------------------------------------------------------
PROCESS = [
    ("Audit", "We review your ad account, tracking, offer and lead flow, and send you a written list of what to fix first."),
    ("Plan", "We agree on the goal, budget, audiences and offer, and decide what counts as a good lead for your sales team."),
    ("Launch", "We build the campaigns, ads and forms, test the tracking, and go live."),
    ("Improve", "Every week we review lead volume, cost and quality, cut what isn't working and test the next idea."),
]

SERVICES = [
    {
        "slug": "facebook-ads",
        "name": "Facebook Ads",
        "nav": "Facebook ads",
        "card": "Strategy, setup and weekly management of your Facebook campaigns.",
        "title": "Facebook Ads Management in Chicago | Facebook Ads Agency",
        "desc": "Chicago Facebook ads management for B2B and B2C businesses: strategy, setup, creative testing and weekly optimization focused on qualified leads. Free audit.",
        "h1": "Facebook ads management",
        "lede": "We run your Facebook campaigns end to end: strategy, setup, creative testing and weekly optimization. The goal is simple: more qualified leads for the money you spend.",
        "includes": [
            "Campaign structure built around your lead goal",
            "Audience strategy: broad, interest, lookalike and customer-list audiences",
            "Meta Pixel and Conversions API setup, so Meta optimizes for real leads",
            "Ad creative and copy, tested in a planned order",
            "Budget pacing and bid strategy",
            "Lead quality checks with your sales team",
            "Plain-English reports on leads, cost per lead and what we're changing next",
        ],
        "faqs": [
            ("How much should I spend on Facebook ads?",
             "It depends on your cost per lead and how many leads you need. Meta's system learns fastest when an ad set gets around 50 conversions a week, so very small budgets take longer to settle. Our budget calculator gives you a starting point, and the free audit gives you a specific number."),
            ("How long before I see leads?",
             "Leads can start soon after launch, but plan on the first few weeks being a learning period while Meta gathers data and we test audiences and creative."),
            ("Do I need my own ad account?",
             "It's best to run ads in an ad account your business owns, so the data and history stay with you. If you don't have one yet, we'll help you set it up."),
        ],
    },
    {
        "slug": "instagram-ads",
        "name": "Instagram Ads",
        "nav": "Instagram ads",
        "card": "Ads for Feed, Stories and Reels, built to look native on each.",
        "title": "Instagram Ads Agency in Chicago | Instagram Ads Management",
        "desc": "Instagram ads management in Chicago: Feed, Stories and Reels campaigns with vertical creative and lead forms, managed alongside your Facebook ads. Free audit.",
        "h1": "Instagram ads management",
        "lede": "Instagram ads run through the same Meta system as Facebook. We plan creative for Feed, Stories and Reels so your ads look native on each placement and send people to a lead form or landing page.",
        "includes": [
            "Placement strategy across Feed, Stories, Reels and Explore",
            "Vertical 9:16 creative and copy for each placement",
            "Shared tracking and audiences with your Facebook campaigns",
            "Lead forms that open inside Instagram",
            "Testing the first seconds of video, where most viewers decide",
            "Reporting split by placement, so you see where leads come from",
        ],
        "faqs": [
            ("Should I run Instagram ads or Facebook ads?",
             "Usually both. They're managed in the same Ads Manager, and Meta can shift budget toward whichever placement brings leads at a lower cost. We split them out only when your results show a clear difference."),
            ("Do I need a lot of followers?",
             "No. Ads reach people who don't follow you. A business Instagram account connected to your Meta business portfolio is enough."),
            ("Can Instagram ads work for B2B?",
             "Often, yes. Decision-makers use Instagram too. Short video that explains a problem you solve, paired with a qualifying lead form, is a good place to start."),
        ],
    },
    {
        "slug": "retargeting-ads",
        "name": "Retargeting Ads",
        "nav": "Retargeting ads",
        "card": "Follow-up ads for people who already showed interest.",
        "title": "Facebook Retargeting Ads in Chicago | Retargeting Agency",
        "desc": "Facebook and Instagram retargeting for Chicago businesses: follow-up ads for site visitors, video viewers and lead form openers, with sensible frequency. Free audit.",
        "h1": "Facebook retargeting ads",
        "lede": "Most people don't fill out a form on their first visit. Retargeting shows follow-up ads to people who already visited your site, watched your videos or opened your lead form, so the interest you paid for doesn't go to waste.",
        "includes": [
            "Audiences from website visitors, video viewers, page and profile engagers, and lead form openers",
            "Customer list uploads to reach or exclude past customers",
            "Sequenced messages: proof, answers to common objections, then the offer",
            "Frequency limits so people aren't overwhelmed",
            "Exclusions so current leads and customers don't see prospecting ads",
            "Retargeting windows matched to how long your sales cycle runs",
        ],
        "faqs": [
            ("Does retargeting still work after the privacy changes?",
             "Yes, but audiences are smaller than they used to be because of browser and iOS privacy changes. A Conversions API setup helps Meta match more of your website visitors."),
            ("How much traffic do I need?",
             "Retargeting works best once you have steady traffic or video views to build from. Very small audiences still run, but they deliver slowly and get repetitive, so we keep them broad enough to be useful."),
            ("Won't people get annoyed?",
             "They can if ads repeat too often. We rotate creative, limit frequency and stop showing ads once someone becomes a lead."),
        ],
    },
    {
        "slug": "lead-form-ads",
        "name": "Lead Form Ads",
        "nav": "Lead form ads",
        "card": "Instant forms that bring in leads your team wants to call.",
        "title": "Facebook Lead Ads Agency in Chicago | Lead Form Ads",
        "desc": "Facebook and Instagram lead form ads for Chicago businesses: qualifying questions, higher-intent forms and instant CRM sync for faster follow-up. Free audit.",
        "h1": "Facebook lead form ads",
        "lede": "Lead ads let people request a quote or a callback without leaving Facebook or Instagram. They're fast to fill out, which is both the upside and the risk. We set them up to bring in leads your team actually wants to call.",
        "includes": [
            "Form design with the right number of fields for your offer",
            "Qualifying questions such as budget, timeline and service area",
            "Meta's higher-intent form type when lead quality matters most",
            "CRM sync (HubSpot and others) so leads don't sit inside Meta",
            "Instant follow-up email or text set up with your team",
            "Feedback from sales used to tighten targeting and questions",
        ],
        "faqs": [
            ("Are lead form leads lower quality?",
             "They can be, because the forms are easy to submit. Qualifying questions, the higher-intent form type and fast follow-up all help a lot."),
            ("Should I use a lead form or a landing page?",
             "Lead forms usually cost less per lead. Landing pages often bring more considered leads. When the budget allows, we test both and keep whichever brings more customers, not just more form fills."),
            ("How fast should we follow up?",
             "As fast as you can. Leads go cold quickly, so we connect the form to your CRM and set up an instant reply."),
        ],
    },
    {
        "slug": "ad-creative",
        "name": "Ad Creative and Testing",
        "nav": "Ad creative and testing",
        "card": "Ad concepts, copy and video, tested one idea at a time.",
        "title": "Facebook Ad Creative and Testing in Chicago | Ad Creative",
        "desc": "Facebook and Instagram ad creative for Chicago businesses: concepts, copy, static, carousel and short video ads, tested in a planned order. Free audit.",
        "h1": "Ad creative and testing",
        "lede": "Targeting on Meta is increasingly automated, so the ad itself does much of the work of finding the right people. We write, design and test ads in a planned order so you learn what works and why.",
        "includes": [
            "Ad concepts built on your offer and the questions customers ask",
            "Static, carousel and short video formats",
            "Headline and copy variations",
            "Structured tests that change one thing at a time",
            "Your own photos and footage, never stock images",
            "Fresh ads before performance fades",
        ],
        "faqs": [
            ("How many ads should we run?",
             "Enough to test a few clearly different ideas. Usually that's a handful per campaign, not dozens."),
            ("Do we need professional video?",
             "No. Simple phone video of your team, your work or your product often fits Facebook and Instagram better than polished ads, because it looks like the content around it."),
            ("What if we don't have photos or video?",
             "We can start with text, graphics and screen recordings, and send you a short list of shots to capture so later ads use real footage."),
        ],
    },
    {
        "slug": "pixel-conversions-api",
        "name": "Pixel and Conversions API",
        "nav": "Pixel and Conversions API",
        "card": "Tracking that tells Meta which ads bring real leads.",
        "title": "Meta Pixel and Conversions API Setup in Chicago",
        "desc": "Meta Pixel and Conversions API setup for Chicago businesses, so Facebook and Instagram ads optimize for real leads and qualified customers. Free audit.",
        "h1": "Pixel and Conversions API",
        "lede": "Meta can only optimize for the leads it can see. We set up the Meta Pixel and Conversions API so form submissions, calls and qualified leads are reported back accurately, which gives Meta better data to find more people like them.",
        "includes": [
            "Meta Pixel install and event setup",
            "Conversions API (server-side) for events browsers block",
            "Deduplication so the same lead isn't counted twice",
            "Qualified-lead and closed-deal events sent from your CRM",
            "Domain verification in your Meta business settings",
            "Testing in Events Manager before any campaign launches",
        ],
        "faqs": [
            ("Why do I need the Conversions API if I have the Pixel?",
             "Browsers and ad blockers stop some Pixel events. The Conversions API sends events from your server or CRM, so Meta sees more of your results."),
            ("Can you send CRM data back to Meta?",
             "Yes. Sending qualified-lead or closed-deal events lets Meta optimize toward leads that turn into customers, not just form fills."),
            ("Does this work with HubSpot?",
             "Yes. HubSpot can share lead stage changes with Meta as conversion events, and we can also send events server-side."),
        ],
    },
]

INDUSTRIES = [
    {
        "slug": "b2b",
        "name": "B2B",
        "nav": "B2B companies",
        "card": "Qualified leads for companies that sell to other businesses.",
        "title": "Facebook Ads for B2B Companies in Chicago | B2B Lead Generation",
        "desc": "Facebook and Instagram ads for Chicago B2B companies: SaaS, professional services, IT, contractors and manufacturers. Qualified leads, CRM sync. Free audit.",
        "h1": "Facebook ads for B2B",
        "lede": "Facebook and Instagram reach business owners and decision-makers when they're off the clock. For B2B, the work is in qualifying leads and following up across a longer sales cycle.",
        "industries": [
            ("SaaS and software", "Demo and trial requests from the right company size and role."),
            ("Professional services", "Law, accounting and consulting firms looking for new clients."),
            ("IT and managed services", "Consultations and assessments for local businesses."),
            ("Commercial contractors and facility services", "Bid and quote requests from property and facility managers."),
            ("Manufacturing and industrial suppliers", "Quote and catalog requests from buyers and engineers."),
            ("Staffing and recruiting", "Employer leads, plus job ads run under Meta's employment rules."),
        ],
        "approach": [
            "Offers worth a business email, such as an assessment, consultation or guide",
            "Lead forms with questions about company size, role and timeline",
            "Lookalike audiences built from your customer list",
            "Longer retargeting windows to match longer sales cycles",
            "CRM sync and qualified-lead events, so Meta learns which leads close",
        ],
    },
    {
        "slug": "b2c",
        "name": "B2C",
        "nav": "B2C businesses",
        "card": "Calls, bookings and quote requests from local customers.",
        "title": "Facebook Ads for B2C Businesses in Chicago | Local Lead Generation",
        "desc": "Facebook and Instagram ads for Chicago B2C businesses: home services, health and wellness, fitness, real estate, education and retail. Free audit.",
        "h1": "Facebook ads for B2C",
        "lede": "For consumer businesses, Facebook and Instagram can bring in calls, bookings and quote requests from people in your service area, as long as the offer is clear and follow-up is fast.",
        "industries": [
            ("Home services", "HVAC, roofing, remodeling, plumbing and other quote-driven trades."),
            ("Health and wellness", "Dental practices, med spas, chiropractors and clinics."),
            ("Fitness studios and gyms", "Trial classes, intro offers and memberships."),
            ("Real estate and mortgage", "Buyer, seller and refinance leads, run under Meta's housing and financial rules."),
            ("Education, tutoring and coaching", "Consultations, enrollments and info sessions."),
            ("Restaurants and local retail", "Events, catering inquiries and in-store offers."),
            ("Auto sales and service", "Test drives, service bookings and trade-in requests."),
            ("E-commerce", "First purchases and repeat orders, tracked to revenue."),
        ],
        "approach": [
            "Clear, specific offers people can act on today",
            "Targeting focused on the ZIP codes and neighborhoods you serve",
            "Short video and photos of your real team and work",
            "Instant follow-up by text or email",
            "Retargeting for people who compared options and didn't book yet",
        ],
        "note": "Ads about housing, employment, credit and other financial products, and social or political issues must run under Meta's Special Ad Categories. These limit targeting by age, gender and ZIP code. We plan these campaigns within those rules from the start.",
    },
]

TOOLS = [
    {
        "slug": "ad-budget-calculator",
        "name": "Ad Budget and Lead Calculator",
        "nav": "Budget and lead calculator",
        "card": "See how many leads and customers a monthly budget could bring.",
        "title": "Facebook Ads Budget Calculator | Leads and ROI Estimator",
        "desc": "Free Facebook ads budget calculator from a Chicago Facebook ads agency. Estimate leads, customers, cost per customer and return from your monthly budget.",
        "h1": "Budget and lead calculator",
        "lede": "Enter a monthly budget and your own numbers to estimate leads, customers and return. Everything runs in your browser. Nothing is sent anywhere.",
    },
    {
        "slug": "break-even-calculator",
        "name": "Break-even ROAS Calculator",
        "nav": "Break-even ROAS calculator",
        "card": "Find the most you can pay per lead and still make money.",
        "title": "Break-even ROAS and CPA Calculator for Facebook Ads",
        "desc": "Free break-even ROAS calculator from a Chicago Facebook ads agency. Find your maximum cost per customer and cost per lead before Facebook ads lose money.",
        "h1": "Break-even ROAS calculator",
        "lede": "Find the most you can spend to win a customer, and per lead, before your ads stop paying for themselves. Everything runs in your browser. Nothing is sent anywhere.",
    },
]

AUDIT_CHECKS = [
    ("Account structure", "Campaigns, ad sets and budgets: whether they help Meta learn or split your data too thin."),
    ("Tracking", "Pixel, Conversions API and lead events: whether Meta is optimizing for real leads."),
    ("Audiences", "Who you're reaching, who you're paying for twice and who you're missing."),
    ("Creative and offer", "Whether your ads and offer give people a reason to act now."),
    ("Lead flow", "Forms, follow-up speed and how leads get to your sales team."),
]


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------
def e(s):
    return html.escape(s, quote=True)


def url(slug):
    return "/" if slug == "index" else "/" + slug


def abs_url(slug):
    return SITE["domain"] + url(slug)


def asset_version(name):
    with open(os.path.join(ROOT, name), "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()[:8]


def address_line():
    return f'{SITE["street"]}, {SITE["city"]}, {SITE["region"]} {SITE["zip"]}'


BUSINESS_ID = SITE["domain"] + "/#business"


def business_schema():
    return {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "@id": BUSINESS_ID,
        "name": SITE["name"],
        "url": SITE["domain"] + "/",
        "description": SITE["tagline"],
        "telephone": SITE["phone_e164"],
        "email": SITE["email"],
        "image": SITE["domain"] + "/og.png",
        "logo": SITE["domain"] + "/favicon.svg",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": SITE["street"],
            "addressLocality": SITE["city"],
            "addressRegion": SITE["region"],
            "postalCode": SITE["zip"],
            "addressCountry": SITE["country"],
        },
        "areaServed": {"@type": "City", "name": "Chicago"},
        "knowsAbout": ["Facebook advertising", "Instagram advertising", "Lead generation", "Meta Conversions API"],
    }


def breadcrumb_schema(trail):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": abs_url(slug)}
            for i, (name, slug) in enumerate(trail)
        ],
    }


def faq_schema(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }


def service_schema(name, desc, slug, service_type):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "serviceType": service_type,
        "description": desc,
        "url": abs_url(slug),
        "provider": {"@id": BUSINESS_ID},
        "areaServed": {"@type": "City", "name": "Chicago"},
    }


# --------------------------------------------------------------------------
# Shared layout
# --------------------------------------------------------------------------
def dropdown(key, label, overview_slug, overview_label, items):
    links = "".join(f'<li><a href="{url(i["slug"])}">{e(i["nav"])}</a></li>' for i in items)
    return f"""<li class="has-dd">
          <button type="button" class="dd-btn" aria-expanded="false" aria-controls="dd-{key}">{label}<svg aria-hidden="true" width="10" height="10" viewBox="0 0 10 10"><path d="M1.5 3.5 5 7l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></button>
          <ul class="dd" id="dd-{key}">
            <li><a href="{url(overview_slug)}">{overview_label}</a></li>
            {links}
          </ul>
        </li>"""


def mobile_group(label, overview_slug, overview_label, items):
    links = "".join(f'<li><a href="{url(i["slug"])}">{e(i["nav"])}</a></li>' for i in items)
    return f"""<div class="m-group">
          <p class="m-label">{label}</p>
          <ul>
            <li><a href="{url(overview_slug)}">{overview_label}</a></li>
            {links}
          </ul>
        </div>"""


def header():
    tools_dd = dropdown("tools", "Tools", "tools", "All free tools", TOOLS) if TOOLS else ""
    tools_m = mobile_group("Free tools", "tools", "All free tools", TOOLS) if TOOLS else ""
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-row">
    <a class="brand" href="/" aria-label="{e(SITE["name"])} home">
      <span class="brand-mark" aria-hidden="true">FA</span>
      <span class="brand-text">Facebook Ads Agency<span>Chicago</span></span>
    </a>
    <nav class="primary" aria-label="Main">
      <ul class="nav-list">
        {dropdown("services", "Services", "services", "All services", SERVICES)}
        {dropdown("industries", "Industries", "industries", "All industries", INDUSTRIES)}
        {tools_dd}
        <li><a class="nav-link" href="{SITE["offer_url"]}">Free audit</a></li>
      </ul>
    </nav>
    <a class="btn btn-small header-contact" href="/contact">Contact</a>
    <button type="button" class="menu-toggle" aria-expanded="false" aria-controls="mobile-menu">Menu</button>
  </div>
  <nav class="mobile-menu" id="mobile-menu" aria-label="Mobile" hidden>
    <div class="wrap">
      {mobile_group("Services", "services", "All services", SERVICES)}
      {mobile_group("Industries", "industries", "All industries", INDUSTRIES)}
      {tools_m}
      <div class="m-actions">
        <a class="btn" href="{SITE["offer_url"]}">Get a free audit</a>
        <a class="btn btn-ghost" href="/contact">Contact us</a>
      </div>
    </div>
  </nav>
</header>"""


def footer():
    svc = "".join(f'<li><a href="{url(s["slug"])}">{e(s["nav"])}</a></li>' for s in SERVICES)
    ind = "".join(f'<li><a href="{url(i["slug"])}">{e(i["nav"])}</a></li>' for i in INDUSTRIES)
    tl = "".join(f'<li><a href="{url(t["slug"])}">{e(t["nav"])}</a></li>' for t in TOOLS)
    tools_col = f'<div><h2 class="f-h">Free tools</h2><ul>{tl}</ul></div>' if TOOLS else ""
    return f"""<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="f-about">
      <p class="f-name">{e(SITE["name"])}</p>
      <p>{e(SITE["tagline"])}</p>
      <address>
        {e(address_line())}<br>
        <a href="tel:{SITE["phone_e164"]}">{SITE["phone_display"]}</a><br>
        <a href="mailto:{SITE["email"]}">{SITE["email"]}</a>
      </address>
    </div>
    <div><h2 class="f-h">Services</h2><ul>{svc}</ul></div>
    <div><h2 class="f-h">Industries</h2><ul>{ind}</ul></div>
    {tools_col}
    <div><h2 class="f-h">Company</h2><ul>
      <li><a href="{SITE["offer_url"]}">Free account audit</a></li>
      <li><a href="/contact">Contact</a></li>
      <li><a href="/privacy">Privacy policy</a></li>
    </ul></div>
  </div>
  <div class="wrap f-legal">
    <p>&copy; {date.today().year} {e(SITE["name"])}. Not affiliated with or endorsed by Meta Platforms, Inc.</p>
  </div>
</footer>
<div class="float-contact" role="group" aria-label="Contact us">
  <a href="sms:{SITE["phone_e164"]}" data-contact="sms">Text us</a>
  <a href="tel:{SITE["phone_e164"]}" data-contact="phone">Call us</a>
</div>"""


def gtm_head():
    base = "<script>window.dataLayer=window.dataLayer||[];</script>"
    if not GTM_ID:
        return base
    return base + f"""
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM_ID}');</script>"""


def gtm_body():
    if not GTM_ID:
        return ""
    return f'<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>'


PAGES = []  # (slug, include_in_sitemap)


def page(slug, title, desc, body, schemas=None, crumbs=None, sitemap=True, noindex=False):
    schemas = [business_schema()] + (schemas or [])
    if crumbs:
        schemas.append(breadcrumb_schema([("Home", "index")] + crumbs))
    ld = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas
    )
    crumb_html = ""
    if crumbs:
        parts = ['<a href="/">Home</a>']
        for i, (name, s) in enumerate(crumbs):
            if i == len(crumbs) - 1:
                parts.append(f'<span aria-current="page">{e(name)}</span>')
            else:
                parts.append(f'<a href="{url(s)}">{e(name)}</a>')
        crumb_html = f'<nav class="crumbs wrap" aria-label="Breadcrumb">{" <span aria-hidden=\"true\">/</span> ".join(parts)}</nav>'
    canonical = abs_url(slug)
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{robots}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(SITE["name"])}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE["domain"]}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#fbfbf9">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/style.css?v={asset_version("style.css")}">
{gtm_head()}
<script>window.SITE_CONFIG={json.dumps({"portal": HUBSPOT["portal"], "form": HUBSPOT["form"], "region": HUBSPOT["region"]})};</script>
<script src="/site.js?v={asset_version("site.js")}" defer></script>
{ld}
</head>
<body>
{gtm_body()}
{header()}
<main id="main">
{crumb_html}
{body}
</main>
{footer()}
</body>
</html>
"""
    with open(os.path.join(ROOT, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    PAGES.append((slug, sitemap))


# --------------------------------------------------------------------------
# Reusable sections
# --------------------------------------------------------------------------
def cta_band(heading="Start with a free audit", text=None):
    text = text or "We'll review your ad account, tracking and lead flow, and send you a written list of what to fix first. No obligation."
    return f"""<section class="cta-band">
  <div class="wrap cta-inner">
    <div>
      <h2>{heading}</h2>
      <p>{text}</p>
    </div>
    <div class="cta-actions">
      <a class="btn" href="{SITE["offer_url"]}">Get my free audit</a>
      <a class="btn btn-ghost" href="tel:{SITE["phone_e164"]}">Call {SITE["phone_display"]}</a>
    </div>
  </div>
</section>"""


def card_grid(items, cta="Learn more"):
    cards = "".join(
        f"""<a class="card" href="{url(i["slug"])}">
        <h3>{e(i["nav"][0].upper() + i["nav"][1:])}</h3>
        <p>{e(i["card"])}</p>
        <span class="card-more">{cta} <span aria-hidden="true">&rarr;</span></span>
      </a>"""
        for i in items
    )
    return f'<div class="cards">{cards}</div>'


def process_section(heading="How it works"):
    steps = "".join(
        f'<li><span class="step-n">{n:02d}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>'
        for n, (t, d) in enumerate(PROCESS, 1)
    )
    return f"""<section class="section">
  <div class="wrap">
    <h2 class="section-h">{heading}</h2>
    <ol class="steps">{steps}</ol>
  </div>
</section>"""


def faq_section(faqs):
    items = "".join(
        f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in faqs
    )
    return f"""<section class="section">
  <div class="wrap narrow">
    <h2 class="section-h">Common questions</h2>
    <div class="faq">{items}</div>
  </div>
</section>"""


def check_list(items):
    return '<ul class="checks">' + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"


def page_hero(h1, lede, actions=True, eyebrow=None):
    eb = f'<p class="eyebrow">{e(eyebrow)}</p>' if eyebrow else ""
    act = ""
    if actions:
        act = f"""<div class="hero-actions">
      <a class="btn" href="{SITE["offer_url"]}">Get a free audit</a>
      <a class="btn btn-ghost" href="/contact">Talk to us</a>
    </div>"""
    return f"""<section class="page-hero">
  <div class="wrap narrow-left">
    {eb}
    <h1>{e(h1)}</h1>
    <p class="lede">{e(lede)}</p>
    {act}
  </div>
</section>"""


# --------------------------------------------------------------------------
# Forms
# --------------------------------------------------------------------------
def honeypot():
    return '<div class="hp" aria-hidden="true"><label>Leave this empty<input type="text" name="hp_field" tabindex="-1" autocomplete="off"></label></div>'


def audit_form():
    return f"""<form class="lead-form" data-form="free_audit" novalidate>
  <div class="field">
    <label for="a-name">Full name <span class="req">required</span></label>
    <input id="a-name" name="name" type="text" autocomplete="name" required>
  </div>
  <div class="field">
    <label for="a-email">Work email <span class="req">required</span></label>
    <input id="a-email" name="email" type="email" autocomplete="email" required>
  </div>
  <div class="field-row">
    <div class="field">
      <label for="a-phone">Phone</label>
      <input id="a-phone" name="phone" type="tel" autocomplete="tel">
    </div>
    <div class="field">
      <label for="a-company">Company</label>
      <input id="a-company" name="company" type="text" autocomplete="organization">
    </div>
  </div>
  <div class="field">
    <label for="a-website">Website</label>
    <input id="a-website" name="website" type="text" inputmode="url" autocomplete="url" placeholder="example.com">
  </div>
  <div class="field-row">
    <div class="field">
      <label for="a-budget">Monthly ad budget</label>
      <select id="a-budget" name="budget" data-label="Monthly ad budget">
        <option value="">Choose one</option>
        <option>Not running ads yet</option>
        <option>Under $1,000</option>
        <option>$1,000 to $5,000</option>
        <option>$5,000 to $20,000</option>
        <option>Over $20,000</option>
      </select>
    </div>
    <div class="field">
      <label for="a-type">You sell to</label>
      <select id="a-type" name="business_type" data-label="Sells to">
        <option value="">Choose one</option>
        <option>Businesses (B2B)</option>
        <option>Consumers (B2C)</option>
        <option>Both</option>
      </select>
    </div>
  </div>
  <div class="field">
    <label for="a-goals">What do you want from your ads?</label>
    <textarea id="a-goals" name="goals" rows="4" data-label="Goals"></textarea>
  </div>
  <div class="tool-results" hidden>
    <p class="tool-results-h">Your calculator results will be sent with this request</p>
    <pre class="tool-results-body"></pre>
    <button type="button" class="link-btn tool-results-remove">Don't include these</button>
  </div>
  {honeypot()}
  <p class="fine">By sending this form you agree we can contact you about your request. See our <a href="/privacy">privacy policy</a>.</p>
  <button class="btn btn-block" type="submit">Request my free audit</button>
  <p class="form-status" role="status" aria-live="polite"></p>
  <noscript><p class="form-status">This form needs JavaScript. Email us at <a href="mailto:{SITE["email"]}">{SITE["email"]}</a> instead.</p></noscript>
</form>"""


def contact_form():
    return f"""<form class="lead-form" data-form="contact" novalidate>
  <div class="field">
    <label for="c-name">Full name <span class="req">required</span></label>
    <input id="c-name" name="name" type="text" autocomplete="name" required>
  </div>
  <div class="field-row">
    <div class="field">
      <label for="c-email">Email <span class="req">required</span></label>
      <input id="c-email" name="email" type="email" autocomplete="email" required>
    </div>
    <div class="field">
      <label for="c-phone">Phone</label>
      <input id="c-phone" name="phone" type="tel" autocomplete="tel">
    </div>
  </div>
  <div class="field">
    <label for="c-message">How can we help? <span class="req">required</span></label>
    <textarea id="c-message" name="goals" rows="5" required data-label="Message"></textarea>
  </div>
  {honeypot()}
  <p class="fine">By sending this form you agree we can contact you about your request. See our <a href="/privacy">privacy policy</a>.</p>
  <button class="btn btn-block" type="submit">Send message</button>
  <p class="form-status" role="status" aria-live="polite"></p>
  <noscript><p class="form-status">This form needs JavaScript. Email us at <a href="mailto:{SITE["email"]}">{SITE["email"]}</a> instead.</p></noscript>
</form>"""


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------
def build_home():
    body = f"""<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Facebook and Instagram ads in Chicago</p>
    <h1>Facebook ads that bring leads</h1>
    <p class="lede">We plan, launch and manage Facebook and Instagram campaigns for B2B and B2C businesses. Everything is built around leads your team can follow up on, not likes.</p>
    <div class="hero-actions">
      <a class="btn" href="{SITE["offer_url"]}">Get a free audit</a>
      <a class="btn btn-ghost" href="/services">See services</a>
    </div>
    <ul class="proof">
      <li><strong>{e(SITE["credential"])}</strong></li>
      <li>B2B and B2C campaigns</li>
      <li>Based in the Chicago Loop</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-top">
      <h2 class="section-h">What we do</h2>
      <a class="text-link" href="/services">All services <span aria-hidden="true">&rarr;</span></a>
    </div>
    {card_grid(SERVICES)}
  </div>
</section>

{process_section()}

<section class="section">
  <div class="wrap">
    <div class="section-top">
      <h2 class="section-h">Who we work with</h2>
      <a class="text-link" href="/industries">All industries <span aria-hidden="true">&rarr;</span></a>
    </div>
    {card_grid(INDUSTRIES, "See industries")}
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <h2 class="section-h">The free audit</h2>
      <p>Send us a few details and we'll look at your current setup, or your plan if you haven't started yet. You get a written summary of what's working, what isn't and what to fix first.</p>
      <a class="btn" href="{SITE["offer_url"]}">Request my audit</a>
    </div>
    <ul class="audit-list">
      {"".join(f'<li><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d in AUDIT_CHECKS)}
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-top">
      <h2 class="section-h">Free tools</h2>
      <a class="text-link" href="/tools">All tools <span aria-hidden="true">&rarr;</span></a>
    </div>
    {card_grid(TOOLS, "Open the tool")}
  </div>
</section>

{cta_band()}"""
    page(
        "index",
        "Facebook Ads Agency in Chicago | Free Ad Account Audit",
        "Chicago Facebook ads agency running Facebook and Instagram campaigns that bring in leads for B2B and B2C businesses. $20M+ in ad spend managed. Free audit.",
        body,
    )


def build_services_overview():
    rows = "".join(
        f"""<li>
      <div><h2><a href="{url(s["slug"])}">{e(s["name"])}</a></h2><p>{e(s["card"])}</p></div>
      <a class="text-link" href="{url(s["slug"])}" aria-label="More about {e(s["name"])}">Details <span aria-hidden="true">&rarr;</span></a>
    </li>"""
        for s in SERVICES
    )
    body = f"""{page_hero("Our services", "Everything you need to turn Facebook and Instagram into a steady source of leads, from tracking and creative to day-to-day campaign management.")}
<section class="section tight">
  <div class="wrap"><ul class="rows">{rows}</ul></div>
</section>
{process_section()}
{cta_band()}"""
    page(
        "services",
        "Facebook Ads Services in Chicago | Facebook Ads Agency Chicago",
        "Facebook ads services in Chicago: Facebook and Instagram ads management, retargeting, lead form ads, ad creative and Conversions API setup. Free audit.",
        body,
        crumbs=[("Services", "services")],
    )


def build_service(s):
    others = [o for o in SERVICES if o["slug"] != s["slug"]][:3]
    body = f"""{page_hero(s["h1"], s["lede"], eyebrow="Chicago Facebook ads agency")}
<section class="section tight">
  <div class="wrap split">
    <div>
      <h2 class="section-h">What's included</h2>
      {check_list(s["includes"])}
    </div>
    <aside class="side-box">
      <h2>Not sure where to start?</h2>
      <p>The free audit shows what to fix first in your current setup, or how to launch if you haven't started.</p>
      <a class="btn btn-block" href="{SITE["offer_url"]}">Get a free audit</a>
      <p class="side-meta">{e(SITE["credential"])}</p>
    </aside>
  </div>
</section>
{process_section()}
{faq_section(s["faqs"])}
<section class="section">
  <div class="wrap">
    <h2 class="section-h">Related services</h2>
    {card_grid(others)}
  </div>
</section>
{cta_band()}"""
    page(
        s["slug"],
        s["title"],
        s["desc"],
        body,
        schemas=[service_schema(s["name"], s["desc"], s["slug"], s["name"]), faq_schema(s["faqs"])],
        crumbs=[("Services", "services"), (s["name"], s["slug"])],
    )


def build_industries_overview():
    blocks = ""
    for i in INDUSTRIES:
        names = ", ".join(n for n, _ in i["industries"])
        blocks += f"""<li>
      <div><h2><a href="{url(i["slug"])}">{e(i["nav"][0].upper() + i["nav"][1:])}</a></h2><p>{e(i["card"])}</p><p class="muted">{e(names)}.</p></div>
      <a class="text-link" href="{url(i["slug"])}" aria-label="More about {e(i["nav"])}">Details <span aria-hidden="true">&rarr;</span></a>
    </li>"""
    body = f"""{page_hero("Who we work with", "We run Facebook and Instagram ads for companies that sell to other businesses and for businesses that sell to consumers. The approach is different for each.")}
<section class="section tight">
  <div class="wrap"><ul class="rows">{blocks}</ul></div>
</section>
{cta_band()}"""
    page(
        "industries",
        "Industries We Serve | Facebook Ads Agency Chicago",
        "Facebook and Instagram ads for Chicago B2B and B2C businesses: SaaS, professional services, home services, health and wellness, real estate and more.",
        body,
        crumbs=[("Industries", "industries")],
    )


def build_industry(i):
    inds = "".join(f"<li><h3>{e(n)}</h3><p>{e(d)}</p></li>" for n, d in i["industries"])
    note = ""
    if i.get("note"):
        note = f'<div class="note"><h2>Special Ad Categories</h2><p>{e(i["note"])}</p></div>'
    body = f"""{page_hero(i["h1"], i["lede"], eyebrow="Chicago Facebook ads agency")}
<section class="section tight">
  <div class="wrap">
    <h2 class="section-h">Industries we work with</h2>
    <ul class="ind-grid">{inds}</ul>
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <div>
      <h2 class="section-h">How we approach it</h2>
      {check_list(i["approach"])}
      {note}
    </div>
    <aside class="side-box">
      <h2>See what to fix first</h2>
      <p>Tell us about your business and we'll send a written audit of your ads, or a launch plan if you're starting out.</p>
      <a class="btn btn-block" href="{SITE["offer_url"]}">Get a free audit</a>
    </aside>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2 class="section-h">Services</h2>
    {card_grid(SERVICES[:3])}
  </div>
</section>
{cta_band()}"""
    page(
        i["slug"],
        i["title"],
        i["desc"],
        body,
        schemas=[service_schema(f"Facebook ads for {i['name']} businesses", i["desc"], i["slug"], "Facebook advertising")],
        crumbs=[("Industries", "industries"), (i["name"], i["slug"])],
    )


def build_tools_overview():
    body = f"""{page_hero("Free ad calculators", "Quick calculators for planning Facebook and Instagram ad budgets. They run in your browser, and nothing you type is sent anywhere.", actions=False)}
<section class="section tight">
  <div class="wrap">{card_grid(TOOLS, "Open the tool")}</div>
</section>
{cta_band()}"""
    page(
        "tools",
        "Free Facebook Ads Calculators | Facebook Ads Agency Chicago",
        "Free Facebook ads calculators from a Chicago Facebook ads agency: estimate leads from your budget and find your break-even ROAS and cost per lead.",
        body,
        crumbs=[("Free tools", "tools")],
    )


def num_field(fid, label, value, prefix="", suffix="", step="any", hint=""):
    pre = f'<span class="affix">{prefix}</span>' if prefix else ""
    suf = f'<span class="affix">{suffix}</span>' if suffix else ""
    h = f'<span class="hint">{e(hint)}</span>' if hint else ""
    return f"""<div class="field">
      <label for="{fid}">{e(label)}</label>
      <div class="input-affix">{pre}<input id="{fid}" name="{fid}" type="number" inputmode="decimal" min="0" step="{step}" value="{value}">{suf}</div>
      {h}
    </div>"""


def build_tool_budget(t):
    calc = f"""<div class="tool" data-tool="{t["slug"]}" data-tool-name="{e(t["name"])}">
  <div class="tool-inputs">
    <p class="hint">Example numbers. Change them to yours.</p>
    {num_field("budget", "Monthly ad budget", "3000", prefix="$", step="50")}
    {num_field("cpl", "Expected cost per lead", "40", prefix="$", step="1", hint="Use your past results if you have them.")}
    {num_field("close", "Leads that become customers", "10", suffix="%", step="0.5")}
    {num_field("value", "Average value of a customer", "2500", prefix="$", step="50")}
    {num_field("goal", "Leads you want per month (optional)", "", step="1")}
  </div>
  <div class="tool-output" aria-live="polite">
    <dl class="results">
      <div><dt>Leads per month</dt><dd data-out="leads">-</dd></div>
      <div><dt>New customers per month</dt><dd data-out="customers">-</dd></div>
      <div><dt>Cost per customer</dt><dd data-out="cpa">-</dd></div>
      <div><dt>Revenue from those customers</dt><dd data-out="revenue">-</dd></div>
      <div><dt>Return per $1 of ad spend</dt><dd data-out="roas">-</dd></div>
      <div data-goal-row hidden><dt>Budget for your lead goal</dt><dd data-out="goalBudget">-</dd></div>
    </dl>
    <a class="btn btn-block tool-to-offer" href="{SITE["offer_url"]}?tool={t["slug"]}">Send these results with a free audit</a>
  </div>
</div>"""
    body = f"""{page_hero(t["h1"], t["lede"], actions=False)}
<section class="section tight">
  <div class="wrap">{calc}</div>
</section>
<section class="section">
  <div class="wrap narrow">
    <h2 class="section-h">How to read this</h2>
    <p>This is simple math on the numbers you enter: budget divided by cost per lead gives leads, and your close rate turns leads into customers. Real results move around month to month, and cost per lead changes with your offer, audience and creative.</p>
    <p>If you don't know your cost per lead yet, try a few values to see a range. The free audit can give you a more grounded estimate for your market.</p>
  </div>
</section>
{cta_band("Want a real estimate?", "We'll look at your offer, market and current results and tell you what a realistic budget and cost per lead look like.")}"""
    page(t["slug"], t["title"], t["desc"], body, crumbs=[("Free tools", "tools"), (t["name"], t["slug"])])


def build_tool_breakeven(t):
    calc = f"""<div class="tool" data-tool="{t["slug"]}" data-tool-name="{e(t["name"])}">
  <div class="tool-inputs">
    <p class="hint">Example numbers. Change them to yours.</p>
    {num_field("value", "Average sale value", "2500", prefix="$", step="50", hint="First sale, or lifetime value if customers return.")}
    {num_field("margin", "Gross margin", "40", suffix="%", step="1", hint="What's left after the direct cost of delivering the sale.")}
    {num_field("close", "Leads that become customers", "10", suffix="%", step="0.5")}
  </div>
  <div class="tool-output" aria-live="polite">
    <dl class="results">
      <div><dt>Break-even ROAS</dt><dd data-out="roas">-</dd></div>
      <div><dt>Most you can pay per customer</dt><dd data-out="cpa">-</dd></div>
      <div><dt>Most you can pay per lead</dt><dd data-out="cpl">-</dd></div>
    </dl>
    <p class="hint">Spend less than these and each sale covers its ad cost. Spend more and you lose money on the first sale.</p>
    <a class="btn btn-block tool-to-offer" href="{SITE["offer_url"]}?tool={t["slug"]}">Send these results with a free audit</a>
  </div>
</div>"""
    body = f"""{page_hero(t["h1"], t["lede"], actions=False)}
<section class="section tight">
  <div class="wrap">{calc}</div>
</section>
<section class="section">
  <div class="wrap narrow">
    <h2 class="section-h">How to read this</h2>
    <p><strong>Break-even ROAS</strong> is the revenue you need for every $1 of ad spend just to cover the cost of the ads. It's 1 divided by your gross margin.</p>
    <p><strong>Most you can pay per customer</strong> is your sale value times your margin. <strong>Most you can pay per lead</strong> takes your close rate into account. Use it to judge whether a campaign's cost per lead is healthy.</p>
    <p>If customers buy again, use lifetime value instead of a single sale. Your break-even numbers will rise.</p>
  </div>
</section>
{cta_band("Are your ads above break-even?", "Send us your numbers and we'll show you where your account stands and what to change.")}"""
    page(t["slug"], t["title"], t["desc"], body, crumbs=[("Free tools", "tools"), (t["name"], t["slug"])])


def build_audit():
    checks = "".join(f"<li><h3>{e(t)}</h3><p>{e(d)}</p></li>" for t, d in AUDIT_CHECKS)
    body = f"""<section class="page-hero">
  <div class="wrap offer-grid">
    <div>
      <p class="eyebrow">Free, no obligation</p>
      <h1>Get a free account audit</h1>
      <p class="lede">Tell us about your business and your ads. We'll review your setup and send you a written summary of what's working, what isn't and what to fix first.</p>
      <h2 class="small-h">What we check</h2>
      <ul class="audit-list compact">{checks}</ul>
      <p class="muted">Not running ads yet? We'll review your plan and offer instead. {e(SITE["credential"])}.</p>
    </div>
    <div class="form-card" id="form">
      <h2>Request your audit</h2>
      {audit_form()}
    </div>
  </div>
</section>"""
    page(
        "free-audit",
        "Free Facebook Ads Account Audit | Facebook Ads Agency Chicago",
        "Get a free Facebook and Instagram ads account audit from a Chicago Facebook ads agency. A written review of your tracking, targeting, creative and lead flow.",
        body,
        schemas=[service_schema("Free Facebook ads account audit", "A written review of a Facebook and Instagram ad account: structure, tracking, audiences, creative and lead flow.", "free-audit", "Advertising audit")],
        crumbs=[("Free audit", "free-audit")],
    )


def build_contact():
    maps = "https://www.google.com/maps/search/?api=1&query=" + address_line().replace(" ", "+").replace(",", "%2C")
    body = f"""<section class="page-hero">
  <div class="wrap offer-grid">
    <div>
      <h1>Contact us</h1>
      <p class="lede">Questions about Facebook or Instagram ads? Call, text or send a message and we'll get back to you.</p>
      <ul class="contact-list">
        <li><span class="c-label">Call</span><a href="tel:{SITE["phone_e164"]}">{SITE["phone_display"]}</a></li>
        <li><span class="c-label">Text</span><a href="sms:{SITE["phone_e164"]}">{SITE["phone_display"]}</a></li>
        <li><span class="c-label">Email</span><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></li>
        <li><span class="c-label">Office</span><a href="{maps}" rel="noopener">{e(address_line())}</a></li>
      </ul>
      <div class="side-box slim">
        <h2>Want a review of your ads?</h2>
        <p>The free audit form asks a few more questions so we can prepare.</p>
        <a class="text-link" href="{SITE["offer_url"]}">Go to the free audit <span aria-hidden="true">&rarr;</span></a>
      </div>
    </div>
    <div class="form-card">
      <h2>Send a message</h2>
      {contact_form()}
    </div>
  </div>
</section>"""
    page(
        "contact",
        "Contact a Facebook Ads Agency in Chicago | Call or Text",
        f"Contact Facebook Ads Agency Chicago at {address_line()}. Call or text {SITE['phone_display']} or email us about Facebook and Instagram ads.",
        body,
        crumbs=[("Contact", "contact")],
    )


def build_privacy():
    body = f"""{page_hero("Privacy policy", "How we handle the information you share with us on this website.", actions=False)}
<section class="section tight">
  <div class="wrap narrow prose">
    <p class="muted">Last updated {date.today().strftime("%B %-d, %Y")}</p>
    <h2>What we collect</h2>
    <p>When you fill out a form, we collect what you enter, such as your name, email, phone number, company, website and message. We use it to respond to your request and to talk with you about our services.</p>
    <h2>Where it goes</h2>
    <p>Form submissions are stored in HubSpot, the customer relationship management tool we use. We don't sell your information.</p>
    <h2>Calculators</h2>
    <p>Our free calculators run entirely in your browser. Nothing you type into them is sent to us unless you choose to include the results with a form.</p>
    <h2>Analytics and cookies</h2>
    <p>We may use analytics tools to understand how people use this site. These tools may set cookies. You can block cookies in your browser settings.</p>
    <h2>Your choices</h2>
    <p>To ask what information we hold about you, or to have it corrected or deleted, email <a href="mailto:{SITE["email"]}">{SITE["email"]}</a>.</p>
    <h2>Contact</h2>
    <p>{e(SITE["name"])}, {e(address_line())}. Phone {SITE["phone_display"]}.</p>
  </div>
</section>"""
    page(
        "privacy",
        "Privacy Policy | Facebook Ads Agency Chicago",
        "Privacy policy for Facebook Ads Agency Chicago: what we collect through forms, how we use it, and how to reach us about your information.",
        body,
        crumbs=[("Privacy policy", "privacy")],
    )


def build_404():
    body = f"""<section class="page-hero">
  <div class="wrap narrow-left">
    <p class="eyebrow">Error 404</p>
    <h1>Page not found</h1>
    <p class="lede">The page you're looking for has moved or doesn't exist. Try one of these instead.</p>
    <div class="hero-actions">
      <a class="btn" href="/">Go to the home page</a>
      <a class="btn btn-ghost" href="/services">See services</a>
      <a class="btn btn-ghost" href="{SITE["offer_url"]}">Get a free audit</a>
    </div>
  </div>
</section>"""
    page("404", "Page Not Found | Facebook Ads Agency Chicago", "This page could not be found.", body, sitemap=False, noindex=True)


def build_sitemap():
    entries = []
    for slug, include in PAGES:
        if not include:
            continue
        pr = "1.0" if slug == "index" else ("0.9" if slug in ("free-audit", "services") else "0.7")
        entries.append(
            f"  <url><loc>{abs_url(slug)}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>"
        )
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(entries) + "\n</urlset>\n"
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /build.py\n\nSitemap: {SITE['domain']}/sitemap.xml\n")


def main():
    build_home()
    build_services_overview()
    for s in SERVICES:
        build_service(s)
    build_industries_overview()
    for i in INDUSTRIES:
        build_industry(i)
    if TOOLS:
        build_tools_overview()
        build_tool_budget(TOOLS[0])
        build_tool_breakeven(TOOLS[1])
    build_audit()
    build_contact()
    build_privacy()
    build_404()
    build_sitemap()
    print(f"Built {len(PAGES)} pages + sitemap.xml + robots.txt")


if __name__ == "__main__":
    main()
