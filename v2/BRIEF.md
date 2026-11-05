# Syntea case study v2: content brief

Draft for review. This is the storyline and content plan behind `Syntea_Case_Study_v2.html`. Layout, type and spacing follow the Polygon case study. Teams and Fluent details appear inside the exhibits, because the product lived in Microsoft Teams.

## The one-line story

New hires stay quiet so they don't bother busy colleagues. I designed a Teams agent that answers for them, asks the expert when it doesn't know, and gets better with every message. It ended up on stage at a Microsoft keynote.

## What changes from v1

| v1 | v2 |
|---|---|
| 11 long sections, mostly text and tables | 12 short chapters. Each has a heading, two lines of copy, one interactive exhibit, and the detail in chips or accordions |
| Research shown as tables (platform audit, intent map, decision log, sources) | Research shown as things to try: a day in the life, a pain map, persona tabs |
| The keynote is mentioned only in the outcome | The keynote video is the hero exhibit and returns in the outcome as stills |
| No team, no testimonials | Team ecosystem below the title (with an Easter egg), and a testimonials chapter near the end |
| Data is not part of the story | A closing chapter makes data the product's success metric |
| Two separate prototypes plus static mockups | One evolution prototype (4 stages, live dummy bot) and one "three moments" click dummy |

**Cut or folded into accordions:** platform audit table, competitive teardown, assumption matrix, decision log, sources table, rollout swimlane, architecture strip, research principles grid. Their substance survives in the "Why" chips and in one or two lines of copy.

## Chapter plan

| # | Rail label | Heading | Exhibit (interactive) | Substance it must carry |
|---|---|---|---|---|
| 0 | Overview | **Syntea** · Teams agent · Copilot · Onboarding | Keynote video in a Teams-meeting style frame. Muted loop, sound on tap | It shipped and Microsoft's CEO showed it on stage |
| – | (title panel) | Role strip + team ecosystem | 5 team avatars + 2 client avatars, connected. An "Easter egg" sticky reveals the Miro + Slack huddle screenshot | Who did what. I was the only designer |
| 1 | The problem | New hires don't ask. They wait. | Dot-number stats from our own research (3 days, 9 fields, 6 themes) | The cost of onboarding is social |
| 2 | Process | Twelve weeks, four moves. | Phase tiles W1 to W12 with "What I did / Methods / What I took from it" | DPS framework, shortened |
| 3 | A day one | Mira's first day, hour by hour. | Illustrated timeline 9:00 to 17:00 with a mood line. Toggle "Without / With Syntea" | The use case, told as a story |
| 4 | Pain map | Six pains, one bull's eye. | Interactive bull's eye. Tap a pain to see the quote and which Syntea behaviour answers it | Pain–solution fit |
| 5 | People | Two people, one chat. | Persona tabs: Isabelle (manager), Mira (new hire) | Who we designed for |
| 6 | Define | One question, one canvas. | HMW card + Lean DPS Canvas on the real template | Why onboarding, not upskilling |
| 7 | Decisions | Three calls that shaped the agent. | "I could have… / My pick" cards per decision | Meet people in Teams · ask first · say when it doesn't know |
| 8 | It learns | How the bot learned to talk. | Dark Teams thread, 4 stages on a loop, live dummy bot | From file dispenser to onboarding buddy |
| 9 | Try it | Three moments it was built for. | Light Teams click dummy with 3 scenarios | The flows we tested |
| 10 | Data loop | Every message makes it smarter. | Flywheel + a "messages" slider showing how answers grow. Labelled as an illustrative model | Data is the success metric |
| 11 | On stage | Onboardly stalled. Syntea didn't. | 3 keynote stills + outcome numbers | The honest outcome |
| 12 | Words | What it was like to work with me. | Testimonial cards (placeholders for now) | Credibility |
| 13 | Learnings | What I'd keep, and do sooner. | 4 accordions | Reflection |

## Microsoft and Teams elements to use

- Teams chat chrome (rail, chat list, header tabs, compose box) only inside exhibits, never as page chrome.
- Fluent-style details: 4px/8px radii and Fluent shadows on Teams parts, Segoe UI inside Teams mockups, Teams purple `#5B5FC7` as the page's single accent (replaces Polygon's magenta).
- Adaptive Card patterns for plans and people cards. A proactive Teams toast in the day-one story.
- No Microsoft or Copilot logos. The keynote video carries the brand on its own.

## Data chapter: the argument

1. A question comes in → Syntea answers from company docs, with the source.
2. No confident answer → it asks the owner and follows up.
3. The owner replies → the answer is stored.
4. The next new hire gets it instantly.

So every conversation adds to what the agent knows. The metrics that prove it are: share of questions answered without a person, time to an answer, answers stored per week, and down votes per answer. The chart is an illustrative model, not production data. The production numbers belong to the client.

## What I still need from you

1. **Team names and photos**: 2 AI engineers, 1 software engineer, 1 PM, and the 2 client contacts (product director, AI engineer). Each avatar currently shows its role only.
2. **Testimonials**: the quotes, who said them, and their role. The chapter shows clearly marked placeholders until then.
3. **Easter egg screenshot**: it shows teammates' faces and, in small print, client slides marked "Confidential". Please confirm everyone is fine with it being on a portfolio page, or I can blur the slides.
4. **Keynote facts**: the event name, city and date, so the caption can say more than "Microsoft keynote".
5. **Numbers**: any real figures you're allowed to share (testers, sessions, questions asked). Without them the page uses only figures from the research.
