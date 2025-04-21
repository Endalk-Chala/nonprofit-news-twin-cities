# nonprofit-news-twin-cities

Comparative content analysis of MinnPost and Sahan Journal coverage on public safety, education inequities, and environmental justice in the Twin Cities using web scraping, full-text parsing, and qualitative methods.

![SahanvsMinnPost](https://github.com/Endalk-Chala/nonprofit-news-twin-cities/blob/a6ac618d6e4afdb1270b8300129acfdf522f7fa5/Sahan%20vs%20MinnPost.png)

# Twin Cities News Comparison

**A Digital Content Analysis of Nonprofit News Coverage in the Twin Cities**

This repository contains the tools, data, and documentation for a comparative content analysis project examining the editorial practices and narrative strategies of two influential nonprofit newsrooms in the Twin Cities region: *MinnPost* and *Sahan Journal*. The project investigates how these newsrooms frame and report on three structurally embedded civic issues—public safety and policing, educational inequities, and environmental justice—with an eye toward understanding how nonprofit journalism engages local publics, represents communities, and navigates institutional and civic obligations.

## 🧠 Project Rationale

In the contemporary media environment, nonprofit news organizations have emerged as vital institutions for local communities. Yet little empirical work has examined how these outlets construct the "local public" through coverage, whose voices are elevated or excluded, and what ideological or narrative frameworks guide their reporting.

This project aims to bridge that gap by combining **digital methods**, **qualitative coding**, and **comparative analysis** to examine:
- **Media framing of structural issues**
- **Audience positioning and community engagement**
- **Source diversity and representation**
- **Editorial decisions within nonprofit constraints**

## 📰 Newsrooms Under Study

- **MinnPost**: A nonprofit newsroom founded in 2007, known for in-depth reporting on Minnesota politics, policy, and civic life.
- **Sahan Journal**: Established in 2019, this newsroom focuses on immigrant and communities of color, centering racial equity and lived experience in local reporting.

## 📚 Research Questions

1. How do MinnPost and Sahan Journal frame public safety, education, and environmental justice issues in their reporting?
2. What types of sources are most frequently quoted or cited across these topics?
3. How do these newsrooms differ in their editorial orientation and imagined audiences?
4. In what ways do nonprofit missions shape narrative strategies and the construction of civic identity?
5. How do term co-occurrences reflect thematic emphasis and framing patterns across the two newsrooms?

## 🧰 Methodology

### 1. Web Scraping and Data Collection
- Collected over 100 articles from both outlets between **March 2024 and December 2024**.
- Used Python with `requests`, `BeautifulSoup`, and `newspaper3k` for full-text scraping.
- Filtered articles by topic section (Metro / Democracy & Politics) and publication date.

### 2. Full-Text Analysis and Co-occurrence Mapping
- Preprocessed text to extract keywords and build term co-occurrence networks.
- Used `NetworkX` to visualize how issues and themes cluster together in discourse.

### 3. Semi-Structured Interviews
- Interviews with 4–6 newsroom personnel at each outlet (editors, reporters, audience leads).
- Focused on editorial priorities, community outreach, and institutional challenges.
- Transcribed and thematically coded in NVivo or Dedoose.

### 4. Comparative Content Analysis
- A purposive sample of 20–30 articles per outlet (~60 total).
- Topics include:
  - Public safety and policing
  - Education inequities 
  - Environmental justice / urban redevelopment 
- Both news reporting and opinion pieces are included.
- Coded for:
  - Framing (structural, institutional, individual)
  - Source types (government, community, experts, activists)
  - Language and tone (emotive, neutral, advocacy-oriented)
  - Audience positioning and civic engagement cues
  - Visual representation (photos, captions, imagery)

## 🛠️ Tools & Technologies
- **Python** for article scraping and text processing
  - `newspaper3k`, `BeautifulSoup`, `requests`, `pandas`, `nltk`
- **NetworkX** and `matplotlib` for co-occurrence network visualization
- **NVivo / Dedoose** for qualitative thematic coding
- **Jupyter Notebooks** for exploratory data analysis and interactive workflows
- **Gephi** for advanced network graph modeling

---

This repository is part of an ongoing research project on nonprofit journalism, media framing, and civic discourse in the Twin Cities. Feedback and collaboration are welcome.



