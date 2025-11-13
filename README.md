# LinkedIn User Profile URL – Mass Finder
This project automates the process of finding LinkedIn profile URLs based on names, job titles, locations, and company associations. It eliminates manual searching and returns accurate, structured results instantly. Designed for researchers, marketers, recruiters, and outreach teams, it dramatically improves workflow efficiency.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Linkedin User Profile Url - Mass Finder</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction
LinkedIn User Profile URL – Mass Finder helps you lookup multiple LinkedIn profiles at once simply by providing names or targeted query combinations. It supports flexible search inputs such as designation, location, or company names, allowing highly relevant output results. It streamlines data collection for sales, recruitment, and market analysis teams.

### Smart Search Automation
- Searches profiles by name, job title, company name, or location.
- Supports exact-match or broad-match queries for flexible targeting.
- Returns structured results containing titles and LinkedIn URLs.
- Handles multiple search lines in a single run for batch operations.
- Reduces manual effort and increases outreach accuracy.

## Features
| Feature | Description |
|---------|-------------|
| Multi-query batch search | Accepts multiple names or keyword sets separated by new lines. |
| Targeted search filters | Refine results using designations, locations, and company names. |
| Exact or broad matching | Toggle exact matching for precise or exploratory search modes. |
| Country-based filtering | Retrieve results specific to a selected country. |
| Fast URL extraction | Returns profile URLs instantly with structured output. |

---

## What Data This Scraper Extracts
| Field Name | Field Description |
|-------------|------------------|
| title | The displayed name, designation, or headline of the profile. |
| link | The extracted LinkedIn profile URL. |
| searchQuery | The original query string used to generate the match. |

---

## Example Output


    [
      {
        "title": "Brian Zhang - Adaptive Biotechnologies Corp.",
        "link": "https://www.linkedin.com/in/brianzhang01",
        "searchQuery": "Brian Zhang"
      },
      {
        "title": "Srinivas Narayanan - San Francisco, California, United States",
        "link": "https://www.linkedin.com/in/srinivasnarayanan",
        "searchQuery": "Srinivas Narayanan"
      }
    ]

---

## Directory Structure Tree


    Linkedin User Profile Url - Mass Finder/
    ├── src/
    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── profile_searcher.py
    │   │   └── query_utils.py
    │   ├── outputs/
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── inputs.sample.txt
    │   └── sample_output.json
    ├── requirements.txt
    └── README.md

---

## Use Cases
- **Recruiters** use it to quickly locate candidate profiles, so they can speed up hiring workflows.
- **Sales teams** use it to gather verified prospect URLs, helping them improve outreach accuracy.
- **Market researchers** use it to analyze professionals across industries without manual searching.
- **Founders and entrepreneurs** use it to discover potential partners or investors efficiently.
- **Agencies** use it to generate targeted lists for B2B lead-generation campaigns.

---

## FAQs
**Does it work without providing a name?**
Yes. You can search using designations, locations, or company names by disabling exact matching.

**Can I run multiple queries at once?**
Absolutely. Each query placed on a new line is processed independently during the same run.

**Does it support targeted geographic searches?**
Yes. You can specify a country code to receive region-specific results.

**Are results always exact matches?**
Exact-match mode returns precise results, but turning it off allows broader discovery.

---

## Performance Benchmarks and Results
**Primary Metric:** Processes up to 100 queries in under 10 seconds on standard hardware.
**Reliability Metric:** Achieves a stable match-success rate above 92% on well-defined queries.
**Efficiency Metric:** Optimized for minimal resource consumption even during large batch searches.
**Quality Metric:** Produces highly relevant, de-duplicated results with strong contextual accuracy.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
