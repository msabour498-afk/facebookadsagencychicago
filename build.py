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
    "street": "229 W Madison St, Suite A",
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
    {
        "slug": "landing-pages",
        "name": "Landing Pages",
        "nav": "Landing pages",
        "card": "Fast, single-purpose pages that turn ad clicks into leads.",
        "title": "Landing Pages for Facebook Ads in Chicago | Landing Page Design",
        "desc": "Landing pages for Facebook and Instagram ads, built in Chicago: fast, mobile-first pages that match your ad and turn clicks into qualified leads. Free audit.",
        "h1": "Landing pages for ads",
        "lede": "Sending ad traffic to your home page makes people hunt for what they clicked on. A landing page repeats the ad's promise, answers the main questions and asks for one thing: the lead.",
        "includes": [
            "One page per offer, written to match the ad that sends traffic to it",
            "Mobile-first layout, since most Facebook and Instagram clicks come from phones",
            "Fast load times, with no heavy sliders or auto-playing video",
            "Short forms that connect to your CRM",
            "Pixel and Conversions API events for form submits and calls",
            "A/B tests on headline, offer and form length",
        ],
        "faqs": [
            ("Can't I just send ads to my website?",
             "You can, but a general site has many paths and distractions. A page built for one offer usually gives you a cleaner read on what the ad is doing and makes it easier for visitors to act."),
            ("Where do the pages live?",
             "On your own domain, either inside your current site or on a simple standalone page. We'll recommend whichever is faster to launch and easier for you to keep."),
            ("Landing page or lead form?",
             "Both have a place. Lead forms usually cost less per lead; landing pages give people more information before they reach out. When budget allows, we test both."),
        ],
    },
    {
        "slug": "video-ads",
        "name": "Video Ads",
        "nav": "Video ads",
        "card": "Short vertical video for Reels, Stories and Feed.",
        "title": "Facebook Video Ads in Chicago | Reels and Video Ad Agency",
        "desc": "Facebook and Instagram video ads for Chicago businesses: short vertical video for Reels, Stories and Feed, with hooks and captions built to bring leads. Free audit.",
        "h1": "Facebook and Instagram video ads",
        "lede": "Short video is where much of the attention on Facebook and Instagram goes now. We plan, script and edit vertical videos that stop the scroll and lead to a clear next step.",
        "includes": [
            "Concepts and short scripts built around one message per video",
            "Hooks in the first few seconds, where most viewers decide",
            "Captions on every video, since many people watch with the sound off",
            "Editing of your own phone footage into Reels, Stories and Feed versions",
            "Simple filming guides for you or your team",
            "Retargeting audiences built from people who watched",
        ],
        "faqs": [
            ("Do we need a production crew?",
             "Usually not. Clear phone video of a real person explaining something useful often fits the platform better than a polished commercial."),
            ("How long should a video ad be?",
             "Most of our tests start at 15 to 30 seconds. The opening matters more than the length, so we test several openings on the same video."),
            ("Who appears in the videos?",
             "Ideally you or someone on your team. People respond to the actual faces behind the business, and it builds trust before the first call."),
        ],
    },
    {
        "slug": "messenger-ads",
        "name": "Click-to-Message Ads",
        "nav": "Click-to-message ads",
        "card": "Ads that start a Messenger, WhatsApp or Instagram chat.",
        "title": "Click-to-Message Ads in Chicago | Messenger and WhatsApp Ads",
        "desc": "Click-to-message ads for Chicago businesses: Facebook and Instagram ads that open a Messenger, WhatsApp or Instagram Direct chat with qualifying questions. Free audit.",
        "h1": "Click-to-message ads",
        "lede": "Some people would rather ask a quick question than fill out a form. Click-to-message ads open a conversation in Messenger, WhatsApp or Instagram Direct, so they can reach you in the app they already use.",
        "includes": [
            "Campaigns that send people to Messenger, WhatsApp or Instagram Direct",
            "A greeting and a few quick-reply questions to qualify each chat",
            "Routing so chats reach the right person on your team",
            "Saved replies for common questions about price, timing and service area",
            "Tracking of conversations that turn into booked calls or quotes",
            "Spanish-language versions where your audience prefers it",
        ],
        "faqs": [
            ("Who answers the messages?",
             "Your team. We set up the greeting and qualifying questions so you see who someone is and what they want before you reply."),
            ("What kinds of businesses does this suit?",
             "Service businesses where people want to ask something first: price ranges, availability, whether you cover their area. It's also useful for audiences who prefer WhatsApp."),
            ("How fast do we need to reply?",
             "Quickly. People expect a chat to feel like a chat, so slow replies lose leads. If your team can't answer fast, a lead form may be a better fit."),
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

# Industry pages. "parent" is b2b or b2c; "match" is the industry name on the parent page it links from.
NICHES = [
    {
        "slug": "hvac", "parent": "b2c", "match": "Home services",
        "name": "HVAC", "nav": "HVAC companies",
        "card": "Tune-ups, maintenance plans and replacement estimates.",
        "title": "Facebook Ads for HVAC Companies in Chicago | HVAC Leads",
        "desc": "Facebook ads for Chicago HVAC companies: seasonal tune-up, maintenance plan and replacement campaigns targeted to your service area. Free ad account audit.",
        "h1": "Facebook ads for HVAC companies",
        "lede": "Chicago's seasons drive HVAC demand: AC in early summer, furnaces when the first cold snap hits. Facebook ads let you get in front of homeowners in your service area before they need an emergency call.",
        "works": [
            "Seasonal campaigns: AC tune-ups in spring, furnace checks in fall",
            "Separate campaigns for maintenance plans and system replacements",
            "Service-area targeting by the ZIP codes and suburbs you cover",
            "Short videos of your techs explaining common problems",
            "Lead forms that ask for ZIP code, service type and urgency",
        ],
        "offers": ["Seasonal tune-up price", "Maintenance plan sign-up", "Free replacement estimate", "Second opinion on a replacement quote"],
        "watch": "If you advertise financing, Meta treats it as a financial product ad, which runs under Special Ad Category rules with limited targeting. We keep financing in separate campaigns so it doesn't restrict the rest.",
        "faqs": [
            ("Can Facebook bring in emergency repair calls?",
             "Some, but people with no heat usually search on Google. Facebook works best for planned work: tune-ups, maintenance plans and replacements people are thinking about before they're urgent."),
            ("Should we advertise all year?",
             "Usually, yes, with the message and budget shifting by season. Keeping campaigns running also keeps Meta's data warm for the busy months."),
        ],
    },
    {
        "slug": "roofing", "parent": "b2c", "match": "Home services",
        "name": "Roofing", "nav": "Roofing companies",
        "card": "Inspections and replacement estimates in the areas you serve.",
        "title": "Facebook Ads for Roofing Companies in Chicago | Roofing Leads",
        "desc": "Facebook ads for Chicago roofing contractors: inspection and replacement campaigns, neighborhood targeting and lead forms that qualify homeowners. Free audit.",
        "h1": "Facebook ads for roofers",
        "lede": "Most homeowners don't think about their roof until something goes wrong or a neighbor gets one replaced. Facebook ads put your company in front of them at that moment, in the neighborhoods you actually work.",
        "works": [
            "Inspection offers that start the conversation without a hard sell",
            "Neighborhood targeting around recent jobs and after major storms",
            "Photos and short videos of your own crews and finished roofs",
            "Lead forms asking for address, roof age and the reason for the request",
            "Retargeting for homeowners who are comparing quotes",
        ],
        "offers": ["Free roof inspection", "Replacement estimate", "Storm damage check", "Gutter and roof package"],
        "watch": "Homeowners have learned to be wary of storm chasers. Ads that show your real crew, your address and your years in the area build more trust than urgent \"act now\" messages.",
        "faqs": [
            ("Do roofing ads only work after storms?",
             "Storms bring spikes, but replacement and inspection campaigns can run steadily through the season. Older neighborhoods with aging roofs are good year-round targets."),
            ("How do we keep out low-quality leads?",
             "Ask a few qualifying questions in the form, such as homeowner status and roof age, and follow up fast. That screens out most of the people who were just curious."),
        ],
    },
    {
        "slug": "remodeling", "parent": "b2c", "match": "Home services",
        "name": "Remodeling", "nav": "Remodeling contractors",
        "card": "Kitchen, bath and whole-home projects with long planning cycles.",
        "title": "Facebook Ads for Remodeling Contractors in Chicago",
        "desc": "Facebook ads for Chicago remodelers: kitchen, bath and basement campaigns with portfolio creative, budget qualifying and long-window retargeting. Free audit.",
        "h1": "Facebook ads for remodelers",
        "lede": "Remodeling projects are big decisions that people plan for months. Facebook and Instagram are where homeowners collect ideas, which makes them a good place to show your work and stay in front of them until they're ready.",
        "works": [
            "Carousel and video ads showing your own finished projects",
            "Separate campaigns for kitchens, baths and basements",
            "Lead forms that ask about project type, budget range and timeline",
            "Retargeting windows of several months to match planning time",
            "Design consultation offers rather than discounts",
        ],
        "offers": ["Design consultation", "In-home estimate", "Project cost guide", "Showroom visit"],
        "watch": "Low-budget inquiries can swamp your calendar. Asking for a budget range up front, and stating a starting price in the ad, keeps the leads closer to the projects you want.",
        "faqs": [
            ("How long before ads turn into projects?",
             "Expect a longer gap than most home services because people plan these projects for months. Track consultations booked, not just leads, so you can judge the campaign fairly."),
            ("We don't have professional photos. Is that a problem?",
             "Not necessarily. Clear phone photos and short walkthrough videos of real projects often outperform polished images that look like stock."),
        ],
    },
    {
        "slug": "dental", "parent": "b2c", "match": "Health and wellness",
        "name": "Dental", "nav": "Dental practices",
        "card": "New patients, implants and aligners for local practices.",
        "title": "Facebook Ads for Dentists in Chicago | Dental Practice Marketing",
        "desc": "Facebook ads for Chicago dental practices: new patient, implant and clear aligner campaigns that follow Meta's health ad policies. Free ad account audit.",
        "h1": "Facebook ads for dentists",
        "lede": "Dental practices grow by filling the schedule with new patients and higher-value treatments like implants and clear aligners. Facebook ads can do both, with creative and tracking that respect health privacy rules.",
        "works": [
            "New-patient campaigns focused on the few miles around your office",
            "Separate campaigns for implants, aligners and cosmetic work",
            "Videos of your dentists and team that show what a visit feels like",
            "Online booking or lead forms that ask about insurance and treatment interest",
            "Retargeting for people who read your treatment pages",
        ],
        "offers": ["New patient exam and cleaning", "Implant consultation", "Clear aligner consultation", "Whitening offer"],
        "watch": "Meta doesn't allow ads that imply someone has a health condition (\"Embarrassed by your teeth?\"), and detailed targeting by health topics is limited. Tracking also needs care so no protected health information is sent to Meta.",
        "faqs": [
            ("Can we target people who need implants?",
             "Not directly. Meta limits targeting by health topics. Instead, we target the right area and age range and let the creative attract people interested in implants."),
            ("Is the Meta Pixel safe for a dental website?",
             "It can be if it's set up carefully. We avoid sending page-level health details and keep tracking to general events like a form submission or booking."),
        ],
    },
    {
        "slug": "med-spas", "parent": "b2c", "match": "Health and wellness",
        "name": "Med Spas", "nav": "Med spas",
        "card": "Consultations and bookings for injectables, laser and skin.",
        "title": "Facebook Ads for Med Spas in Chicago | Med Spa Marketing",
        "desc": "Facebook and Instagram ads for Chicago med spas: consultation and booking campaigns for injectables, laser and skin treatments within Meta's ad rules. Free audit.",
        "h1": "Facebook ads for med spas",
        "lede": "Med spa clients find treatments on Instagram and Facebook long before they book. Ads that show your providers, explain treatments plainly and make booking easy turn that interest into appointments.",
        "works": [
            "Instagram-first creative: Reels and Stories featuring your providers",
            "Separate campaigns for injectables, laser and skin treatments",
            "Consultation offers that let people ask questions before committing",
            "Click-to-message ads for people who want to ask about price first",
            "Retargeting for visitors who looked at a treatment page",
        ],
        "offers": ["Free consultation", "New client offer", "Membership program", "Treatment package"],
        "watch": "Meta limits cosmetic procedure ads to people 18 and older and restricts before-and-after imagery and claims about results. We plan creative within those rules so ads don't get rejected or limited.",
        "faqs": [
            ("Can we show before-and-after photos?",
             "Meta restricts them for cosmetic procedures. We usually rely on provider videos, treatment explanations and client experience instead."),
            ("Should we advertise prices?",
             "A starting price can filter out people who aren't a fit. Many med spas pair it with a consultation offer so the focus stays on the right treatment."),
        ],
    },
    {
        "slug": "real-estate", "parent": "b2c", "match": "Real estate and mortgage",
        "name": "Real Estate", "nav": "Real estate",
        "card": "Buyer and seller leads within Meta's housing ad rules.",
        "title": "Facebook Ads for Real Estate Agents in Chicago | Real Estate Leads",
        "desc": "Facebook ads for Chicago real estate agents and teams: home valuation, buyer and listing campaigns run within Meta's housing Special Ad Category. Free audit.",
        "h1": "Facebook ads for real estate",
        "lede": "Facebook is one of the main places agents find buyer and seller leads. Housing ads come with extra rules, so the campaigns and creative have to be built for them from the start.",
        "works": [
            "Home valuation offers for seller leads",
            "New listing and open house ads with video walkthroughs",
            "Buyer guides and alerts for first-time buyers",
            "Lead forms paired with an instant text or email reply",
            "Long follow-up sequences, since many leads buy months later",
        ],
        "offers": ["Free home valuation", "New listings alert", "First-time buyer guide", "Open house invite"],
        "watch": "Real estate ads run under Meta's housing Special Ad Category. You can't target by age, gender or ZIP code, and location targeting has to stay broad. Lookalike audiences are replaced by a limited version.",
        "faqs": [
            ("Can we target specific Chicago neighborhoods?",
             "Not tightly. Housing ads need broad location targeting. We use creative that names the neighborhood so the right people raise their hand."),
            ("Are Facebook real estate leads any good?",
             "They're usually early in the process. Agents who follow up fast and keep in touch for months get the most from them."),
        ],
    },
    {
        "slug": "fitness", "parent": "b2c", "match": "Fitness studios and gyms",
        "name": "Fitness", "nav": "Gyms and fitness studios",
        "card": "Trial classes and memberships from people nearby.",
        "title": "Facebook Ads for Gyms and Fitness Studios in Chicago",
        "desc": "Facebook and Instagram ads for Chicago gyms and fitness studios: trial class, challenge and membership campaigns aimed at people near your location. Free audit.",
        "h1": "Facebook ads for gyms",
        "lede": "People choose a gym or studio close to home or work, and they decide based on what it feels like inside. Short videos of your classes, coaches and members, shown to people nearby, do a lot of the selling.",
        "works": [
            "Tight targeting around each location, since people rarely travel far",
            "Trial class or intro offers with a clear next step",
            "Reels of real classes, coaches and members",
            "Click-to-message ads for people who want to ask a question first",
            "Bigger pushes in January and early spring, when interest peaks",
        ],
        "offers": ["Free trial class", "Intro week pass", "Six-week challenge", "First month discount"],
        "watch": "Meta's rules on health and fitness ads limit claims about weight loss and before-and-after body images. We keep the focus on the experience, schedule and community instead.",
        "faqs": [
            ("How far should we target from our location?",
             "In the city, often just a few miles or a handful of neighborhoods. In the suburbs it can be wider. We set it by where your current members live."),
            ("Trial offer or discount?",
             "A free or low-cost trial usually brings more people through the door, and your team closes them in person. We test both when there's budget."),
        ],
    },
    {
        "slug": "saas", "parent": "b2b", "match": "SaaS and software",
        "name": "SaaS", "nav": "SaaS and software",
        "card": "Demos and trials from the right company size and role.",
        "title": "Facebook Ads for SaaS Companies in Chicago | B2B SaaS Leads",
        "desc": "Facebook and Instagram ads for SaaS and software companies: demo, trial and content campaigns with CRM sync and qualified-lead tracking. Free ad account audit.",
        "h1": "Facebook ads for SaaS",
        "lede": "Meta can be a cost-effective channel for software companies, especially for products business owners and team leads buy themselves. The work is in reaching the right roles and teaching Meta which leads become customers.",
        "works": [
            "Lookalike audiences built from your best customers",
            "Short demo videos that show the product solving one problem",
            "Lead forms asking about company size, role and current tool",
            "CRM sync so qualified leads and closed deals go back to Meta",
            "Retargeting for trial users and demo no-shows",
        ],
        "offers": ["Product demo", "Free trial", "Template or checklist download", "Live webinar"],
        "watch": "Job-title targeting on Meta is less precise than on LinkedIn. We rely more on lookalikes, creative that calls out the role and qualifying questions that filter leads.",
        "faqs": [
            ("Is Facebook better than LinkedIn for SaaS?",
             "They do different jobs. LinkedIn targets by role precisely but costs more per click. Meta often reaches the same people for less. Many companies run both and compare cost per qualified lead."),
            ("Demo or free trial?",
             "Whichever your sales process handles best. Trials suit simpler products; demos suit higher-priced ones. Track each to revenue before deciding."),
        ],
    },
    {
        "slug": "law-firms", "parent": "b2b", "match": "Professional services",
        "name": "Law Firms", "nav": "Law firms",
        "card": "Case inquiries by practice area, within advertising rules.",
        "title": "Facebook Ads for Law Firms in Chicago | Lawyer Lead Generation",
        "desc": "Facebook ads for Chicago law firms: practice-area campaigns for personal injury, family, estate planning and business law, with factual creative. Free audit.",
        "h1": "Facebook ads for law firms",
        "lede": "People rarely look for a lawyer on Facebook until they need one, but they do remember the firm they've seen explain things clearly. Practice-area campaigns and fast intake turn that into consultations.",
        "works": [
            "Separate campaigns for each practice area",
            "Short videos of your attorneys answering common questions",
            "Lead forms that ask for case type and a brief description",
            "Fast intake follow-up, by phone or text",
            "Retargeting for people who read your practice area pages",
        ],
        "offers": ["Free case review", "Consultation", "Estate planning guide", "Business legal checkup"],
        "watch": "Attorney advertising rules apply to social ads. We keep claims factual, avoid promises about outcomes and have you review every ad before it runs.",
        "faqs": [
            ("Which practice areas work on Facebook?",
             "Areas with broad consumer demand, such as personal injury, family law, estate planning and workers' compensation, tend to fit best. Niche business practices often do better with retargeting and referrals."),
            ("How do we handle intake?",
             "Leads go straight to your CRM or intake team with an instant reply, so someone can call while the person is still thinking about it."),
        ],
    },
    {
        "slug": "it-services", "parent": "b2b", "match": "IT and managed services",
        "name": "IT Services", "nav": "IT and managed services",
        "card": "Assessments and consultations from local business owners.",
        "title": "Facebook Ads for IT and Managed Service Providers in Chicago",
        "desc": "Facebook ads for Chicago IT and managed service providers: security assessment and consultation campaigns aimed at local business owners. Free audit.",
        "h1": "Facebook ads for IT services",
        "lede": "Small and mid-sized business owners scroll Facebook like everyone else, and many handle IT decisions themselves. Ads that speak to their real worries, such as downtime, security and slow support, open the door to an assessment.",
        "works": [
            "Targeting business owners in the areas you can service on site",
            "Assessment offers with a clear, limited scope",
            "Short videos explaining one common risk at a time",
            "Lead forms asking about company size and current IT setup",
            "Long retargeting windows, since contracts take time to switch",
        ],
        "offers": ["Free security assessment", "Network health check", "Backup and recovery review", "IT cost review"],
        "watch": "Fear-heavy security ads can feel like spam. Plain explanations and a specific, useful assessment build more trust with owners who are already skeptical of IT vendors.",
        "faqs": [
            ("Can Facebook reach business decision-makers?",
             "Yes, especially owners of small and mid-sized companies. We combine location targeting with business-owner interests and use qualifying questions to filter."),
            ("How long until a lead becomes a contract?",
             "Often months, because businesses wait for a contract to end or a problem to happen. Retargeting and email follow-up keep you in mind until then."),
        ],
    },
]

AREAS = [
    {
        "slug": "chicago", "name": "Chicago",
        "title": "Facebook Ads Agency in Chicago, IL | Chicago Facebook Ads",
        "desc": "Chicago Facebook ads agency in the Loop: Facebook and Instagram campaigns targeted by neighborhood, from River North to Hyde Park. Free account audit.",
        "lede": "Chicago is our home base, with an office at 229 W Madison St in the Loop, and the city is a market of very different neighborhoods rather than one audience.",
        "about": "A dense downtown full of offices and professional services sits next to residential neighborhoods with their own character and spending habits. That makes Chicago a strong market for law firms, real estate, med spas, fitness studios, restaurants and B2B companies, as long as targeting follows the neighborhoods you actually serve.",
        "target": [
            "Neighborhood-level targeting by ZIP code or radius, such as the Loop, River North, West Loop, Lincoln Park, Lakeview, Logan Square and Hyde Park",
            "Separate ads for downtown workers and for residents",
            "Small radius targeting for studios, clinics and restaurants, since city customers rarely travel far",
            "City-wide campaigns for services that come to the customer, such as HVAC and remodeling",
        ],
        "niches": ["law-firms", "real-estate", "med-spas", "fitness"],
        "near": ["evanston", "oak-park"],
        "faq": ("Do you work with businesses outside downtown?",
                "Yes. We're based in the Loop, but we run campaigns for businesses in every part of the city and the suburbs, targeted to the neighborhoods each one serves."),
    },
    {
        "slug": "naperville", "name": "Naperville",
        "title": "Facebook Ads Agency in Naperville, IL | Naperville Facebook Ads",
        "desc": "Facebook and Instagram ads for Naperville businesses: local targeting across Naperville, Aurora, Lisle and Plainfield, built to bring in leads. Free audit.",
        "lede": "Naperville is one of the largest Chicago suburbs, spread across DuPage and Will counties, with a busy downtown along the Riverwalk and a large family population.",
        "about": "Families and homeowners make up much of the audience here, which suits home services, dental and health practices, tutoring and fitness studios. Downtown restaurants and shops draw people from neighboring towns too.",
        "target": [
            "Naperville ZIP codes 60540, 60563, 60564 and 60565",
            "Nearby towns: Aurora, Lisle, Wheaton, Bolingbrook and Plainfield",
            "Separate ads for the north and south sides when your service area differs",
            "Family-focused offers and messaging",
        ],
        "niches": ["hvac", "remodeling", "dental", "fitness"],
        "near": ["aurora", "oak-brook"],
        "faq": ("Do you only work with Naperville businesses on site?",
                "We work remotely with businesses across the Chicago area, from our office in the Loop. Campaigns are planned around your specific service area."),
    },
    {
        "slug": "schaumburg", "name": "Schaumburg",
        "title": "Facebook Ads Agency in Schaumburg, IL | Schaumburg Facebook Ads",
        "desc": "Facebook and Instagram ads for Schaumburg businesses: B2B and local campaigns targeting Schaumburg, Hoffman Estates, Palatine and Elk Grove Village. Free audit.",
        "lede": "Schaumburg is one of the northwest suburbs' main business centers, home to Woodfield Mall and many corporate offices along the I-90 corridor.",
        "about": "That mix means two audiences: thousands of people who work here during the day, and the families who live in the surrounding neighborhoods. It suits B2B services as well as retail, dining and home services.",
        "target": [
            "Schaumburg ZIP codes 60173, 60193, 60194 and 60195",
            "Nearby towns: Hoffman Estates, Elk Grove Village, Palatine and Rolling Meadows",
            "Workday targeting around office areas for B2B and lunch offers",
            "Residential targeting for home services and health practices",
        ],
        "niches": ["it-services", "saas", "hvac", "dental"],
        "near": ["arlington-heights", "oak-brook"],
        "faq": ("Can you target people who work in Schaumburg but live elsewhere?",
                "Partly. Meta's location targeting can include people recently in an area, not just residents, which helps reach the daytime office population."),
    },
    {
        "slug": "evanston", "name": "Evanston",
        "title": "Facebook Ads Agency in Evanston, IL | Evanston Facebook Ads",
        "desc": "Facebook and Instagram ads for Evanston businesses: local campaigns reaching Evanston, Skokie, Wilmette and Rogers Park residents. Free account audit.",
        "lede": "Evanston sits on the lakefront just north of Chicago, home to Northwestern University and a walkable downtown full of independent businesses.",
        "about": "The audience mixes students, university staff, young professionals and long-time homeowners in older houses. That suits remodeling and home services, health practices, fitness studios, tutoring and restaurants.",
        "target": [
            "Evanston ZIP codes 60201, 60202 and 60203",
            "Nearby areas: Skokie, Wilmette and Chicago's Rogers Park",
            "Separate messaging for students and for homeowners",
            "Walkable radius targeting for studios and restaurants",
        ],
        "niches": ["remodeling", "fitness", "dental", "law-firms"],
        "near": ["oak-park", "arlington-heights"],
        "faq": ("Should we target Northwestern students?",
                "Only if they're truly your customers. Student audiences can drive cheap clicks that don't convert, so we usually exclude them for home services and include them for food, fitness and tutoring."),
    },
    {
        "slug": "oak-brook", "name": "Oak Brook",
        "title": "Facebook Ads Agency in Oak Brook, IL | Oak Brook Facebook Ads",
        "desc": "Facebook and Instagram ads for Oak Brook businesses: B2B and premium local campaigns reaching Oak Brook, Hinsdale, Elmhurst and Downers Grove. Free audit.",
        "lede": "Oak Brook is a DuPage County business hub, with corporate offices, Oakbrook Center and a small but affluent residential population surrounded by larger suburbs.",
        "about": "Many businesses here sell to other companies or to higher-income households in Hinsdale, Elmhurst and nearby towns. It suits professional services, B2B companies, med spas, cosmetic dentistry and premium home services.",
        "target": [
            "Oak Brook ZIP code 60523 and the surrounding DuPage towns",
            "Nearby towns: Hinsdale, Elmhurst, Downers Grove, Westmont and Lombard",
            "Business-owner and professional targeting for B2B offers",
            "Premium offers and creative for higher-ticket services",
        ],
        "niches": ["law-firms", "med-spas", "saas", "remodeling"],
        "near": ["naperville", "oak-park"],
        "faq": ("Is Oak Brook too small to target on its own?",
                "Usually, yes. We treat it as the center of a wider area that includes the surrounding DuPage suburbs, which gives Meta enough people to work with."),
    },
    {
        "slug": "oak-park", "name": "Oak Park",
        "title": "Facebook Ads Agency in Oak Park, IL | Oak Park Facebook Ads",
        "desc": "Facebook and Instagram ads for Oak Park businesses: local campaigns reaching Oak Park, Forest Park, River Forest and Berwyn homeowners. Free audit.",
        "lede": "Oak Park borders Chicago's West Side, known for its Frank Lloyd Wright homes, tree-lined streets and walkable business districts.",
        "about": "Older homes mean steady demand for remodeling, roofing, HVAC and other home services. A walkable, community-minded population also supports local studios, health practices and restaurants.",
        "target": [
            "Oak Park ZIP codes 60301, 60302 and 60304",
            "Nearby towns: Forest Park, River Forest and Berwyn",
            "Homeowner targeting for older-home services",
            "Local, community-focused creative",
        ],
        "niches": ["remodeling", "roofing", "hvac", "fitness"],
        "near": ["evanston", "oak-brook"],
        "faq": ("Do historic homes need different ads?",
                "Often, yes. Owners of older homes care about craftsmanship and preservation, so creative that shows careful, period-appropriate work tends to resonate more than discount offers."),
    },
    {
        "slug": "aurora", "name": "Aurora",
        "title": "Facebook Ads Agency in Aurora, IL | Aurora Facebook Ads",
        "desc": "Facebook and Instagram ads for Aurora businesses, in English and Spanish: local campaigns across Aurora, Naperville, Oswego and North Aurora. Free audit.",
        "lede": "Aurora is Illinois's second-largest city, spanning Kane, DuPage, Will and Kendall counties, with a large Spanish-speaking community.",
        "about": "Its size and diversity make it a strong market for home services, health and dental practices, auto services and local retail. For many businesses, Spanish-language ads reach customers competitors overlook.",
        "target": [
            "Aurora ZIP codes 60502, 60503, 60504, 60505 and 60506",
            "Nearby towns: Naperville, North Aurora, Montgomery and Oswego",
            "Spanish-language ads and lead forms where your audience prefers them",
            "Click-to-message ads through WhatsApp",
        ],
        "niches": ["hvac", "roofing", "dental", "fitness"],
        "near": ["naperville", "oak-brook"],
        "faq": ("Should we run ads in Spanish?",
                "If your team can serve Spanish-speaking customers, yes. Running Spanish versions of your ads and forms, with replies in Spanish, often reaches people your competitors miss."),
    },
    {
        "slug": "arlington-heights", "name": "Arlington Heights",
        "title": "Facebook Ads Agency in Arlington Heights, IL | Facebook Ads",
        "desc": "Facebook and Instagram ads for Arlington Heights businesses: local campaigns reaching Arlington Heights, Palatine, Mount Prospect and Buffalo Grove. Free audit.",
        "lede": "Arlington Heights is a large northwest Cook County suburb with a lively downtown along the Metra line and established residential neighborhoods.",
        "about": "Homeowners here keep home service, remodeling and health businesses busy, and downtown restaurants and shops draw from neighboring towns. Local businesses also benefit from strong community attachment.",
        "target": [
            "Arlington Heights ZIP codes 60004 and 60005",
            "Nearby towns: Palatine, Mount Prospect, Buffalo Grove and Rolling Meadows",
            "Homeowner targeting for home services and remodeling",
            "Downtown-focused ads for dining and retail",
        ],
        "niches": ["hvac", "remodeling", "dental", "real-estate"],
        "near": ["schaumburg", "evanston"],
        "faq": ("Should we target Arlington Heights alone or the whole northwest suburbs?",
                "It depends on how far you'll travel or how far customers will come to you. Most service businesses do better with the surrounding towns included, so Meta has more people to work with."),
    },
    {
        "slug": "orland-park", "name": "Orland Park",
        "title": "Facebook Ads Agency in Orland Park, IL | Orland Park Facebook Ads",
        "desc": "Facebook and Instagram ads for Orland Park businesses: local campaigns reaching Orland Park, Tinley Park, Palos Heights and Mokena. Free account audit.",
        "lede": "Orland Park is a southwest suburban hub, with Orland Square Mall and the LaGrange Road shopping corridor drawing people from across the area.",
        "about": "A large family population supports home services, dental and health practices, fitness studios and auto services, while retail and dining pull customers from the surrounding southwest suburbs.",
        "target": [
            "Orland Park ZIP codes 60462 and 60467",
            "Nearby towns: Tinley Park, Palos Heights, Mokena and Orland Hills",
            "Family-focused offers for home and health services",
            "Retail and dining ads around the LaGrange Road corridor",
        ],
        "niches": ["hvac", "roofing", "dental", "fitness"],
        "near": ["oak-park", "naperville"],
        "faq": ("Can you cover the whole southwest suburbs?",
                "Yes. We can target Orland Park as the center and include the towns you serve, adjusting the area based on where your leads and customers actually come from."),
    },
]

for _a in AREAS:
    _a["nav"] = _a["name"]
    _a["card"] = _a["lede"].split(",")[0].rstrip(".") + "."
    _a["h1"] = f"Facebook ads in {_a['name']}"

NICHE_BY_SLUG = {n["slug"]: n for n in NICHES}
AREA_BY_SLUG = {a["slug"]: a for a in AREAS}

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
        "logo": SITE["domain"] + "/logo.png",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": SITE["street"],
            "addressLocality": SITE["city"],
            "addressRegion": SITE["region"],
            "postalCode": SITE["zip"],
            "addressCountry": SITE["country"],
        },
        "areaServed": [{"@type": "City", "name": "Chicago"}] + [{"@type": "City", "name": f"{a['name']}, IL"} for a in AREAS],
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
def dropdown(key, label, overview_slug, overview_label, items, wide=False):
    links = "".join(f'<li><a href="{url(i["slug"])}">{e(i["nav"])}</a></li>' for i in items)
    cls = "dd dd-wide" if wide else "dd"
    return f"""<li class="has-dd">
          <button type="button" class="dd-btn" aria-expanded="false" aria-controls="dd-{key}">{label}<svg aria-hidden="true" width="10" height="10" viewBox="0 0 10 10"><path d="M1.5 3.5 5 7l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></button>
          <ul class="{cls}" id="dd-{key}">
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
    <a class="brand" href="/">
      <img src="/logo.svg" width="206" height="36" alt="{e(SITE["name"])} home">
    </a>
    <nav class="primary" aria-label="Main">
      <ul class="nav-list">
        {dropdown("services", "Services", "services", "All services", SERVICES)}
        {dropdown("industries", "Industries", "industries", "All industries", INDUSTRIES + NICHES, wide=True)}
        {dropdown("areas", "Areas", "areas", "All areas", AREAS)}
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
      {mobile_group("Industries", "industries", "All industries", INDUSTRIES + NICHES)}
      {mobile_group("Areas", "areas", "All areas", AREAS)}
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
    ind = "".join(f'<li><a href="{url(i["slug"])}">{e(i["nav"])}</a></li>' for i in INDUSTRIES + NICHES)
    ar = "".join(f'<li><a href="{url(a["slug"])}">{e(a["name"])}</a></li>' for a in AREAS)
    tl = "".join(f'<li><a href="{url(t["slug"])}">{e(t["nav"])}</a></li>' for t in TOOLS)
    tools_col = f'<div><h2 class="f-h">Free tools</h2><ul>{tl}</ul></div>' if TOOLS else ""
    return f"""<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="f-about">
      <img class="f-logo" src="/logo.svg" width="183" height="32" alt="{e(SITE["name"])}">
      <p>{e(SITE["tagline"])}</p>
      <address>
        {e(address_line())}<br>
        Text <a href="sms:{SITE["phone_e164"]}">{SITE["phone_display"]}</a><br>
        <a href="mailto:{SITE["email"]}">{SITE["email"]}</a>
      </address>
    </div>
    <div><h2 class="f-h">Services</h2><ul>{svc}</ul></div>
    <div><h2 class="f-h">Industries</h2><ul>{ind}</ul></div>
    <div><h2 class="f-h">Areas</h2><ul>{ar}</ul></div>
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
  <a href="mailto:{SITE["email"]}" data-contact="email">Email us</a>
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
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
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
      <a class="btn btn-ghost" href="sms:{SITE["phone_e164"]}">Text {SITE["phone_display"]}</a>
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
    <ul class="pill-list">{"".join(f'<li><a href="{url(n["slug"])}">{e(n["nav"])}</a></li>' for n in NICHES)}</ul>
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

<section class="section">
  <div class="wrap">
    <div class="section-top">
      <h2 class="section-h">Areas we serve</h2>
      <a class="text-link" href="/areas">All areas <span aria-hidden="true">&rarr;</span></a>
    </div>
    <p class="muted">We're based in the Chicago Loop and run campaigns for businesses across the city and suburbs.</p>
    <ul class="pill-list">{"".join(f'<li><a href="{url(a["slug"])}">{e(a["name"])}</a></li>' for a in AREAS)}</ul>
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
<section class="section">
  <div class="wrap">
    <h2 class="section-h">By industry</h2>
    {card_grid(NICHES, "Read more")}
  </div>
</section>
{cta_band()}"""
    page(
        "industries",
        "Industries We Serve | Facebook Ads Agency Chicago",
        "Facebook and Instagram ads for Chicago B2B and B2C businesses: SaaS, professional services, home services, health and wellness, real estate and more.",
        body,
        crumbs=[("Industries", "industries")],
    )


def niche_links(parent, match):
    ns = [n for n in NICHES if n["parent"] == parent and n["match"] == match]
    if not ns:
        return ""
    return '<p class="ind-links">' + " &middot; ".join(f'<a href="{url(n["slug"])}">{e(n["name"])}</a>' for n in ns) + "</p>"


def build_industry(i):
    inds = "".join(f"<li><h3>{e(n)}</h3><p>{e(d)}</p>{niche_links(i['slug'], n)}</li>" for n, d in i["industries"])
    guides = [n for n in NICHES if n["parent"] == i["slug"]]
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
    <h2 class="section-h">Industry pages</h2>
    {card_grid(guides, "Read more")}
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


def build_niche(n):
    parent = next(i for i in INDUSTRIES if i["slug"] == n["parent"])
    siblings = [x for x in NICHES if x["parent"] == n["parent"] and x["slug"] != n["slug"]][:3]
    offers = "".join(f"<li>{e(o)}</li>" for o in n["offers"])
    areas = [a for a in AREAS if n["slug"] in a["niches"]] or AREAS[:4]
    body = f"""{page_hero(n["h1"], n["lede"], eyebrow="Chicago Facebook ads agency")}
<section class="section tight">
  <div class="wrap split">
    <div>
      <h2 class="section-h">What works</h2>
      {check_list(n["works"])}
      <h2 class="small-h">Offers to test</h2>
      <ul class="pill-list static">{offers}</ul>
      <div class="note"><h2>Watch out for</h2><p>{e(n["watch"])}</p></div>
    </div>
    <aside class="side-box">
      <h2>Get a free audit</h2>
      <p>We'll review your current ads, or your plan if you haven't started, and send you a written list of what to fix first.</p>
      <a class="btn btn-block" href="{SITE["offer_url"]}">Get a free audit</a>
      <p class="side-meta">{e(SITE["credential"])}</p>
    </aside>
  </div>
</section>
{faq_section(n["faqs"])}
<section class="section">
  <div class="wrap">
    <h2 class="section-h">Related industries</h2>
    {card_grid(siblings, "Read more")}
    <p class="muted area-line">Serving {e(n["nav"].lower() if n["slug"] not in ("saas",) else "SaaS companies")} in Chicago and nearby: {", ".join(f'<a href="{url(a["slug"])}">{e(a["name"])}</a>' for a in areas)}.</p>
  </div>
</section>
{cta_band()}"""
    page(
        n["slug"], n["title"], n["desc"], body,
        schemas=[service_schema(f"Facebook ads for {n['nav'].lower() if n['slug'] != 'saas' else 'SaaS companies'}", n["desc"], n["slug"], "Facebook advertising"), faq_schema(n["faqs"])],
        crumbs=[("Industries", "industries"), (parent["name"], parent["slug"]), (n["name"], n["slug"])],
    )


def build_areas_overview():
    rows = "".join(
        f"""<li>
      <div><h2><a href="{url(a["slug"])}">{e(a["name"])}</a></h2><p>{e(a["lede"])}</p></div>
      <a class="text-link" href="{url(a["slug"])}" aria-label="Facebook ads in {e(a["name"])}">Details <span aria-hidden="true">&rarr;</span></a>
    </li>"""
        for a in AREAS
    )
    body = f"""{page_hero("Areas we serve", "We're based at 229 W Madison St in the Chicago Loop and run Facebook and Instagram ads for businesses across the city and suburbs. Each campaign is targeted to the area you actually serve.")}
<section class="section tight">
  <div class="wrap"><ul class="rows">{rows}</ul></div>
</section>
{cta_band()}"""
    page(
        "areas",
        "Areas We Serve | Facebook Ads Agency Chicago and Suburbs",
        "Facebook ads agency serving Chicago and suburbs including Naperville, Schaumburg, Evanston, Oak Brook, Oak Park, Aurora, Arlington Heights and Orland Park.",
        body,
        crumbs=[("Areas", "areas")],
    )


def build_area(a):
    niches = [NICHE_BY_SLUG[s] for s in a["niches"]]
    near = [AREA_BY_SLUG[s] for s in a["near"]]
    body = f"""{page_hero(a["h1"], a["lede"], eyebrow=f"{a['name']}, Illinois")}
<section class="section tight">
  <div class="wrap split">
    <div>
      <h2 class="section-h">Businesses here</h2>
      <p>{e(a["about"])}</p>
      <h2 class="section-h area-h">How we target {e(a["name"])}</h2>
      {check_list(a["target"])}
    </div>
    <aside class="side-box">
      <h2>Free audit for {e(a["name"])} businesses</h2>
      <p>We'll review your ads, or your plan if you're starting out, and send a written list of what to fix first.</p>
      <a class="btn btn-block" href="{SITE["offer_url"]}">Get a free audit</a>
      <p class="side-meta">{e(SITE["credential"])}</p>
    </aside>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2 class="section-h">Industries we help</h2>
    {card_grid(niches, "Read more")}
  </div>
</section>
{faq_section([a["faq"]])}
<section class="section">
  <div class="wrap">
    <h2 class="section-h">Nearby areas</h2>
    {card_grid(near, "See area")}
  </div>
</section>
{cta_band()}"""
    page(
        a["slug"], a["title"], a["desc"], body,
        schemas=[{
            "@context": "https://schema.org", "@type": "Service",
            "name": f"Facebook advertising in {a['name']}, IL", "serviceType": "Facebook advertising",
            "description": a["desc"], "url": abs_url(a["slug"]), "provider": {"@id": BUSINESS_ID},
            "areaServed": {"@type": "City", "name": f"{a['name']}, IL"},
        }, faq_schema([a["faq"]])],
        crumbs=[("Areas", "areas"), (a["name"], a["slug"])],
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
      <p class="lede">Questions about Facebook or Instagram ads? Text us, email us or send a message and we'll get back to you.</p>
      <ul class="contact-list">
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
        "Contact a Facebook Ads Agency in Chicago | Text or Email",
        f"Contact Facebook Ads Agency Chicago at {address_line()}. Text {SITE['phone_display']} or email us about Facebook and Instagram ads.",
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
    for n in NICHES:
        build_niche(n)
    build_areas_overview()
    for a in AREAS:
        build_area(a)
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
