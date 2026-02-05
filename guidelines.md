# Personalized Podcast Content Guidelines

Validate generated podcast content against these criteria. The content should feel personally crafted without being overtly explicit about personalization.

---

## 1. Subtle Personal Connection

The listener should sense the content is for them without being told directly.

- [ ] Content tone feels like a trusted advisor speaking to one person, not a broadcast
- [ ] No explicit phrases like "this is personalized for you" or "based on your profile"
- [ ] Natural transitions that assume familiarity with listener's context
- [ ] Avoids generic openings like "Hello everyone" or "Dear listener"
- [ ] Feels like continuing a conversation, not starting from scratch

**Check:** Would this feel awkward if overheard by a stranger? (It should feel private but not secretive)

---

## 1b. Source Grounding

Listener needs to know WHERE content comes from, but the delivery should feel natural.

- [ ] Content is traceable to its source meeting/session
- [ ] Grounding can be explicit ("In the SOX session...") or contextual ("Your slide deck sparked...")
- [ ] Focus remains on the TOPIC and insights, not meeting logistics
- [ ] Listener can mentally organize: "I know where this came from"

**Check:** Could I trace this back to its source if I wanted to?

---

## 2. Dynamic Focus Based on Participation

Content focus shifts based on listener's role in events.

### When listener participated/presented:
- [ ] Focus shifts to OTHER participants' contributions and perspectives
- [ ] Listener's own contributions are acknowledged briefly, not rehashed in detail
- [ ] Highlights reactions, feedback, or responses from others to listener's work
- [ ] Emphasizes what listener might have missed while presenting
- [ ] Names of questioners/reactors ARE valuable (listener knows them)

### When listener was mentioned by others:
- [ ] Mentions of listener are HIGHLIGHTED as key moments
- [ ] Context around the mention is provided (who said it, in what context)
- [ ] Tone conveys importance: "Here's something you'll want to know..."
- [ ] Follow-up implications or action items related to mentions are surfaced

### When listener was absent or observing (not their meeting/topic):
- [ ] PREFER to minimize individual names—listener likely doesn't know these people
- [ ] Focus on LEARNINGS, not attribution
- [ ] Apply the "1 sentence / 3 sentence" test:
  - If I can only learn ONE thing from this topic, what is it?
  - If I can learn THREE things, what are they?
- [ ] Structure as insights, not meeting minutes
- [ ] Role descriptors often work better than names (e.g., "the presenter said..." instead of specific names)
- [ ] No awkward references to listener's absence
- [ ] Focus on actionable insights and key decisions

**Note:** Name minimization is a soft preference, not a hard rule. Occasional names are acceptable if they add clarity.

---

## 3. Profile-Aligned Relevance

Content prioritization reflects listener's provided profile.

- [ ] Topics matching listener's role/responsibilities get deeper coverage
- [ ] Industry jargon appropriate to listener's expertise level
- [ ] Skips or summarizes areas outside listener's domain (unless critical)
- [ ] Connects information to listener's known projects or interests
- [ ] Anticipates questions listener would likely ask

**Check:** Does the content feel like it was curated, not just filtered?

---

## 4. Importance Hierarchy

Content structure reflects what matters to THIS listener. The goal is to **filter out unnecessary information**, not to add to it.

- [ ] Most relevant items appear early or are signposted clearly
- [ ] Secondary items are condensed but accessible
- [ ] Irrelevant details are omitted, not just minimized
- [ ] Clear signals for "you need to act on this" vs "good to know"
- [ ] Time-sensitive items are flagged appropriately
- [ ] **NO invented content**—everything must trace back to source material

---

## 4b. Context + Action Balance

Every topic needs BOTH context and action/takeaway, but the ratio depends on listener involvement.

### Action Items Integrity:
- [ ] **MUST deliver explicit action items**—if an action was explicitly assigned in the source, it MUST appear in the output. Failing to deliver explicit actions is a critical failure.
- [ ] **NEVER invent action items**—actions must come explicitly from the source content
- [ ] If no action was stated in the source, don't fabricate one
- [ ] "Worth watching" or "may become relevant" are acceptable for passive topics without explicit actions
- [ ] Distinguish between explicit actions (stated in meeting) vs suggested actions (invented)

**Check:** Were all explicit action items from the source delivered? Missing explicit actions = FAILURE.

### When action is important (listener is active/needs to act):
- [ ] Context is BRIEF—just enough to orient
- [ ] Action/next-step is the focus (but must be real, not invented)
- [ ] Assume listener knows the background
- [ ] Format: Quick context → Clear action

### When no particular action needed (listener is passive/observing):
- [ ] Context becomes the FOCUS—this IS the value
- [ ] Deeper explanation of what happened and why it matters
- [ ] Help listener understand, not just be informed
- [ ] Format: Rich context → Optional "worth watching" or "may become relevant"

### Wrap-up principle:
- [ ] Even simple tasks need framing when introduced to others
- [ ] Action items should have a brief wrap-up that ties them together
- [ ] Don't assume the audience will act—deliver context that has value even if they don't

**Check:** If the listener does nothing, did they still learn something valuable from the context?

**Check:** Can every action item be traced back to explicit content in the source material?

---

## 5. Soft Personalization Techniques

Personalization should be felt, not announced.

### DO:
- [ ] Use phrasing that implies shared context ("as you'd expect from...")
- [ ] Reference past events naturally ("following up on last week's...")
- [ ] Assume knowledge listener has, don't over-explain their domain
- [ ] Use "you" sparingly and naturally, not repeatedly

### DON'T:
- [ ] Explicitly state "since you're interested in X..."
- [ ] Over-use listener's name
- [ ] Announce personalization ("I've tailored this to...")
- [ ] Make the personalization itself a topic

---

## 6. Tone and Delivery

The voice should match a personal briefing.

- [ ] Conversational but efficient
- [ ] Confident in what's included (no hedging about relevance)
- [ ] Warm but not overly familiar
- [ ] Respects listener's time
- [ ] Sounds like a knowledgeable colleague, not a news anchor

---

## 7. System Prompt Integrity

System prompts must remain generic, reusable, and content-agnostic.

- [ ] NO content-specific examples in system prompt (no hardcoded names, projects, tools)
- [ ] NO sample outputs or mock data in system prompt
- [ ] Rules describe PATTERNS, not instances
- [ ] Uses placeholders like "the listener", "the listener's collaborators", "from the Profile" instead of specific values
- [ ] If examples are needed, they are structural patterns, not content examples

**Check:** Could this system prompt work for ANY meeting content and ANY user profile without modification?

---

## Validation Scoring

For each section, rate 1-10:

| Section | Score | Notes |
|---------|-------|-------|
| 1. Subtle Personal Connection | /10 | |
| 2. Dynamic Focus | /10 | |
| 3. Profile-Aligned Relevance | /10 | |
| 4. Importance Hierarchy | /10 | |
| 5. Soft Personalization | /10 | |
| 6. Tone and Delivery | /10 | |

**Overall:** /60

**Key Issues to Fix:**
1. 
2. 
3. 

**What's Working Well:**
1. 
2. 
