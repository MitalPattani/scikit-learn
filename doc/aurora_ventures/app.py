"""Streamlit app for the Aurora Ventures marketing site."""

from datetime import datetime

import streamlit as st


FUND_THEMES = [
    "AI-enabled SaaS",
    "Digital health",
    "Climate tech",
    "Vertical enterprise software",
    "Fintech infrastructure",
    "Future of work",
    "Cybersecurity",
]

DOMICILES = ["New York, USA"]

GEOGRAPHIES = [
    "North America",
    "Europe",
]

INVESTMENT_STAGES = [
    "Seed",
    "Series A",
    "Series B",
    "Growth equity",
]

SECTOR_DESCRIPTIONS = {
    "Healthcare IT": "Scaling digital health solutions that improve patient outcomes and access.",
    "Financial Services": "Transforming the infrastructure powering global capital flows.",
    "Enterprise SaaS": "Backing systems of record and intelligence redefining work.",
    "Sustainability": "Fueling climate-positive platforms for a resilient planet.",
    "Cybersecurity": "Protecting data integrity across distributed ecosystems.",
    "Logistics": "Modernizing supply chains with automation and intelligence.",
    "Consumer marketplaces": "Curating trusted, high-engagement community experiences.",
}

DEGREES = [
    "MBA, Stanford GSB",
    "MBA, Harvard Business School",
    "MBA, Wharton School",
]

PAST_EMPLOYERS = [
    "Amazon",
    "Goldman Sachs",
    "McKinsey & Company",
]

SERVICE_PROVIDERS = {
    "legal": [
        "Cooley LLP",
        "Wilson Sonsini",
        "Fenwick & West",
        "Goodwin Procter",
    ],
    "audit": [
        "KPMG",
        "Deloitte",
        "PwC",
        "EY",
    ],
    "tax": [
        "BDO",
        "Grant Thornton",
        "RSM",
    ],
    "fund_administration": [
        "Apex Fund Services",
        "Standish Management",
        "Juniper Square",
    ],
}

FIRST_NAMES = [
    "Alex",
    "Jordan",
    "Taylor",
]

LAST_NAMES = [
    "Chen",
    "Gonzalez",
    "Patel",
]

COMPANY_DESCRIPTIONS = {
    "CarbonPath": "AI-driven carbon accounting SaaS for manufacturers",
    "MedAI": "Digital therapeutics for chronic disease",
    "NovaGrid": "Energy optimization for distributed solar networks",
}


st.set_page_config(
    page_title="Aurora Ventures | Investing in the Future",
    page_icon="✨",
    layout="wide",
)


HERO_BACKGROUND = (
    "linear-gradient(135deg, rgba(31, 60, 136, 0.95), rgba(15, 26, 43, 0.95)), "
    "url('https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1400&q=80')"
)


st.markdown(
    f"""
    <style>
        :root {{
            --primary: #1f3c88;
            --secondary: #f7b733;
            --dark: #0f1a2b;
            --light: #f5f7fa;
            --text: #2c2c2c;
        }}

        .main .block-container {{
            padding-top: 0;
            padding-bottom: 4rem;
        }}

        body {{
            background-color: var(--light);
        }}

        .aurora-hero {{
            background: {HERO_BACKGROUND} center/cover;
            color: #fff;
            padding: 4rem 3rem 5rem;
            text-align: center;
            position: relative;
            border-bottom-left-radius: 24px;
            border-bottom-right-radius: 24px;
            margin-bottom: 3rem;
        }}

        .aurora-hero::after {{
            content: "";
            position: absolute;
            inset: 0;
            background: rgba(15, 26, 43, 0.45);
        }}

        .aurora-hero > div {{
            position: relative;
            z-index: 1;
            max-width: 800px;
            margin: 0 auto;
        }}

        .aurora-hero h1 {{
            font-size: clamp(2.5rem, 4vw, 3.25rem);
            margin-bottom: 0.5rem;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }}

        .aurora-hero p {{
            font-size: 1.2rem;
        }}

        .tagline {{
            font-size: 1.05rem;
            color: rgba(255, 255, 255, 0.85);
            margin-bottom: 0.75rem;
        }}

        .aurora-section {{
            background-color: #fff;
            border-radius: 18px;
            padding: clamp(1.75rem, 3vw, 2.5rem);
            margin-bottom: 1.75rem;
            box-shadow: 0 25px 60px rgba(15, 26, 43, 0.08);
        }}

        .aurora-heading {{
            font-size: 1.55rem;
            color: var(--primary);
            letter-spacing: 0.04em;
            text-transform: uppercase;
            margin-bottom: 1.75rem;
        }}

        .aurora-card {{
            border-radius: 14px;
            border: 1px solid rgba(31, 60, 136, 0.1);
            background-color: #fdfdff;
            padding: 1.25rem;
            height: 100%;
        }}

        .aurora-team {{
            background: linear-gradient(135deg, rgba(31, 60, 136, 0.12), rgba(31, 60, 136, 0.02));
            border: 1px solid rgba(31, 60, 136, 0.12);
        }}

        .aurora-highlight {{
            color: var(--secondary);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            font-size: 0.85rem;
        }}

        .aurora-partners ul {{
            padding-left: 1.1rem;
        }}

        .aurora-footer {{
            text-align: center;
            padding: 2rem 0 1rem;
            color: rgba(44, 44, 44, 0.7);
        }}
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <section class="aurora-hero">
      <div>
        <p class="tagline">Aurora Ventures &mdash; Illuminating the next generation of category-defining founders</p>
        <h1>Backing Bold Founders Building the Future</h1>
        <p>
          We partner with visionary teams accelerating innovation across AI-enabled software, digital health, and climate resilience.
          From New York to the world, our network amplifies founders' ambitions.
        </p>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)


with st.container():
    st.markdown('<div class="aurora-section">', unsafe_allow_html=True)
    st.markdown('<div class="aurora-heading">Investment Blueprint</div>', unsafe_allow_html=True)
    left, right = st.columns((1, 1))
    with left:
        st.subheader("Fund Themes")
        st.markdown("\n".join(f"- {theme}" for theme in FUND_THEMES))
    with right:
        st.subheader("Investment Stages")
        st.markdown("\n".join(f"- {stage}" for stage in INVESTMENT_STAGES))

        st.subheader("Geographies")
        st.markdown("\n".join(f"- {geo}" for geo in GEOGRAPHIES))

        st.subheader("Domicile")
        st.markdown("\n".join(DOMICILES))
    st.markdown('</div>', unsafe_allow_html=True)


with st.container():
    st.markdown('<div class="aurora-section">', unsafe_allow_html=True)
    st.markdown('<div class="aurora-heading">Sector Expertise</div>', unsafe_allow_html=True)
    cols = st.columns(3)
    sector_items = list(SECTOR_DESCRIPTIONS.items())
    for idx, (sector, description) in enumerate(sector_items):
        with cols[idx % 3]:
            st.markdown(
                f"<div class='aurora-card'><strong>{sector}</strong><br>{description}</div>",
                unsafe_allow_html=True,
            )
    st.markdown('</div>', unsafe_allow_html=True)


with st.container():
    st.markdown('<div class="aurora-section">', unsafe_allow_html=True)
    st.markdown('<div class="aurora-heading">Portfolio Highlights</div>', unsafe_allow_html=True)
    cols = st.columns(3)
    for idx, (company, description) in enumerate(COMPANY_DESCRIPTIONS.items()):
        with cols[idx % 3]:
            st.markdown(
                f"<div class='aurora-card'><h3>{company}</h3><p>{description}.</p></div>",
                unsafe_allow_html=True,
            )
    st.markdown('</div>', unsafe_allow_html=True)


team_bios = [
    (
        FIRST_NAMES[0] + " " + LAST_NAMES[0],
        "Managing Partner",
        DEGREES[0],
        PAST_EMPLOYERS[0],
        "Alex leads AI-enabled SaaS and enterprise investments, bringing a builder's mindset to every partnership.",
    ),
    (
        FIRST_NAMES[1] + " " + LAST_NAMES[1],
        "Partner",
        DEGREES[1],
        PAST_EMPLOYERS[1],
        "Jordan heads fintech infrastructure and climate tech, blending capital markets rigor with sustainability insights.",
    ),
    (
        FIRST_NAMES[2] + " " + LAST_NAMES[2],
        "Partner",
        DEGREES[2],
        PAST_EMPLOYERS[2],
        "Taylor champions future of work and digital health, guiding founders on go-to-market and scaling strategies.",
    ),
]


with st.container():
    st.markdown('<div class="aurora-section">', unsafe_allow_html=True)
    st.markdown('<div class="aurora-heading">Investment Team</div>', unsafe_allow_html=True)
    cols = st.columns(3)
    for idx, (name, title, degree, employer, bio) in enumerate(team_bios):
        with cols[idx % 3]:
            st.markdown(
                """
                <div class="aurora-card aurora-team">
                    <h3>{name}</h3>
                    <p class="aurora-highlight">{title}</p>
                    <p>{degree}<br>Formerly at {employer}.</p>
                    <p>{bio}</p>
                </div>
                """.format(
                    name=name,
                    title=title,
                    degree=degree,
                    employer=employer,
                    bio=bio,
                ),
                unsafe_allow_html=True,
            )
    st.markdown('</div>', unsafe_allow_html=True)


SERVICE_HEADINGS = {
    "legal": "Legal",
    "audit": "Audit",
    "tax": "Tax",
    "fund_administration": "Fund Administration",
}


with st.container():
    st.markdown('<div class="aurora-section aurora-partners">', unsafe_allow_html=True)
    st.markdown('<div class="aurora-heading">Service Partner Network</div>', unsafe_allow_html=True)
    cols = st.columns(4)
    for idx, key in enumerate(["legal", "audit", "tax", "fund_administration"]):
        with cols[idx % 4]:
            st.subheader(SERVICE_HEADINGS[key])
            st.markdown("\n".join(f"- {provider}" for provider in SERVICE_PROVIDERS[key]))
    st.markdown('</div>', unsafe_allow_html=True)


with st.container():
    st.markdown('<div class="aurora-section">', unsafe_allow_html=True)
    st.markdown('<div class="aurora-heading">Partner with Aurora Ventures</div>', unsafe_allow_html=True)
    col_left, col_right = st.columns((1.2, 1))
    with col_left:
        st.write(
            "We invest in trailblazers who combine deep industry insight with relentless execution. "
            "Our partners gain access to capital, talent networks, and a community of operators dedicated to scaling impact."
        )
        st.write(
            "From first check through growth rounds, we bring hands-on support, strategic depth, and global reach."
        )
    with col_right:
        st.subheader("Reach out")
        st.markdown("[hello@auroravc.com](mailto:hello@auroravc.com)")
        st.subheader("Offices")
        st.write("45 Hudson Yards, Floor 38\nNew York, NY 10001")
    st.markdown('</div>', unsafe_allow_html=True)


st.markdown(
    """
    <div class="aurora-footer">
        &copy; {year} Aurora Ventures. All rights reserved.
    </div>
    """.format(year=datetime.now().year),
    unsafe_allow_html=True,
)

