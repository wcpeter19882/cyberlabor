Summaries for multiple meetings:

[Meeting: Tech Talk Session - RTC Signaling Services]
Meeting Date: 2026-01-30T00:03:21.206Z
Meeting Organizer: Ali Mehregani
Meeting Summary:
- [sec:intro] Welcome and introduction by Wei Feng  
  - Wei Feng from Suzhou rejoined the meeting after nine months and introduced himself and his team’s background in telemetry and standardization.
  - He explained that his team now owns two products: Package Modernizer (which he is responsible for) and OS Porter (owned by Sean Ten, with team members Yifan and Yanan presenting on his behalf).
  - Wei Feng introduced Xiao Chen from SS3 Platform Team, who will later share experiences using OS Porter for migrating services from Windows to Linux.
  - The meeting was outlined: the first half would cover Package Modernizer and the second half OS Porter.

- [sec:package_modernizer] Package Modernizer overview and migration capabilities  
  - Wei Feng described Package Modernizer’s two major functions: package upgrade and .NET migration (from .NET Framework to .NET Core).
  - The solution is delivered as a VS Code extension (also called a pack monetizer) that assists users in evaluating and executing migration tasks.
  - Key features include:
    - A standardized migration process backed by a migration knowledge base.
    - Tools for dependency analysis, API porting, and task management.
    - Reliance on GitHub Copilot and collaboration with the adaptive team for third-party migrations.
  - Internal usage was shared:
    - Package Modernizer has been used by the SS3 Data Platform Team for 8 projects and by the OSI Runtime Team for 20 projects.
    - It is also currently helping with the migration of PSTN Admin service and Control Plan from .NET Framework to .NET Core.
  - Wei Feng emphasized that the current focus is on code transformation to generate high-quality, buildable code, while acknowledging that service teams will still manually review and manage the migrated code.
  - He detailed the multi-agent approach for migration:
    - Building a project dependency graph and an API dependency graph to determine the migration order.
    - The designer agent generates migration designs per project, outlining API changes, impact analysis, and any potential functionality loss (e.g., a noted 4% functionality gap in one design proposal).
    - An iterative migration process is executed that distinguishes local fixes from dependency changes and eventually triggers code review agents to ensure API parity and quality.
    - To-do items and human review are generated for incomplete aspects (e.g., conditional compilation or missing policies for .NET 8).

- [sec:package_modernizer_qanda] Q&A discussion on migration agent granularity and process enhancements  
  - Kiran Madipally asked about the migration agent’s granularity.
    - Wei Feng clarified that the agent works at the repository level by analyzing dependency graphs and then migrating projects one by one.
  - Kiran recommended using a task list with modular (mini) steps and subsequent code reviews after each step to help reduce context bloat and improve agent performance.
    - Wei Feng acknowledged the suggestion and mentioned plans to split the large PRs into smaller, focused commits.
  - Sainath Yelamanchali queried if the agent also handles incompatibilities during migration.
    - Wei Feng confirmed it does, showing an example where the agent generates design proposals to handle conditional compilation and even output to-do items to prompt manual follow-up on functionality gaps.
  - Wei Feng illustrated an example output:
    - The design phase details what files need to change, reasons (such as differences in .NET Framework timeouts versus .NET 8) and suggested migration actions.
    - The agent can propose multiple design options (from conservative to aggressive) for human selection.

- [sec:package_modernizer_access] Package Modernizer for component upgrade and internal adoption  
  - Wei Feng briefly described the additional function of Package Modernizer for addressing component governance alert issues in SS3.
    - Currently piloted beyond C# code transformation, with over 100 merged PRs and more than 400 PRs created.
    - The tool leverages three pillars: common migration knowledge, an auto-generated knowledge base for library breaking changes, and inspection/decompilation for adjusting legacy code.
  - He encouraged teams to review previous emails and provided resources (linked in slide) for further details on how to set up and experiment with the tool.
  - Ali Mehregani asked for clarification about accessibility:
    - Wei Feng confirmed that while teams can download and use the VS Code extension directly, reaching out to the team for additional support is recommended.

- [sec:os_porter_intro] Transition to OS Porter and introduction by Xiao Chen  
  - Xiao Chen from SS3 Platform Team introduced himself and summarized his team’s experience:
    - His team has worked with Cosmic Linux migration on six services, using OS Porter extensively.
    - He highlighted that their efforts with OS Porter on the IC3 Enterprise Entity Runtime Store (Years) resulted in 7 PRs, reducing development and validation effort by about 28%.
    - An analysis showed OS Porter covers ~70% of the 50 identified migration tasks (spanning code changes, validation, deployment, and cleanup) though it is currently limited to fixing build errors.

- [sec:os_porter_demo_overview] OS Porter demonstration and functionality overview by Yifan Zhu  
  - Yifan Zhu (from AI Forward team) introduced OS Porter as a tool to accelerate Windows-to-Linux migration through AI-assisted code generation.
  - Key points of OS Porter include:
    - It is a Visual Studio Code extension officially recommended by the Cosmic Linux team.
    - The tool scans source code to:
      - Identify Windows-specific code and incompatible libraries.
      - Flag telemetry gaps and other configuration issues.
    - OS Porter organizes tasks into categories such as Windows-only dependencies, telemetry gaps, incompatible libraries (with sub-tasks for upgrades or migrations), and Cosmic Artifact migration.
  - Yifan detailed a demo scenario:
    - For a Windows system DLL replacement, the tool performs evaluation and then executes code refactoring, including introducing conditional logic (e.g., using libc for Linux alternatives).
    - Another example focused on CPU and memory performance counters, where OS Porter adjusts package references and provides human-action instructions to complete configuration updates.
    - The demo underscored that OS Porter integrates internal private knowledge to automatically fix code, yet still involves a human in the loop for validation.
  - He shared usage metrics:
    - Approximately 30 active users and over 50 services are currently being supported.
    - Several pilot services (including engagements with Defender, Substrate, and Sydney Services) are in progress.
  - Yifan outlined the migration process stages:
    - Stage 1: Assessment (discovery and analysis of source code)
    - Stage 2: Code Generation (automatic cross-platform code modifications)
    - Stage 3: Validation and Testing (inner loop, pending release)
    - Stages 4 & 5: Deployment and Windows-specific cleanup.
  - A demo video was shown (after a brief technical issue with audio sharing) to illustrate the end-to-end workflow in OS Porter.
  - Yifan concluded by discussing the upcoming “inner loop” feature:
    - The inner loop will automate local builds, unit tests, and sandbox validations with AI-powered iterations, significantly reducing manual turnaround time.

- [sec:os_porter_qanda] Q&A discussion on automation hooks and auto loop functionality  
  - Kiran Madipally inquired about automating rollback and rollout (the "auto loop") in addition to the inner loop.
    - He suggested providing a script hook for deployment or additional validations after the inner loop completes, thus offering teams an extensible way to integrate their own automation.
  - Yifan Zhu and Yanan Duan acknowledged the potential:
    - Yifan noted that while the current focus is on completing the inner loop feature, the team is open to exploring asynchronous script hook capabilities for rollout automation.
    - Kiran emphasized that a simple hook allowing teams to execute a custom script (e.g., via ADO API) could be a game changer without significant changes to OS Porter.
  - The discussion highlighted enthusiasm for enhanced automation and provided actionable ideas for extending OS Porter’s workflow.

- [sec:wrap_up] Meeting wrap-up  
  - Ali Mehregani thanked everyone for the comprehensive overview of both Package Modernizer and OS Porter.
  - The session concluded with thanks from Wei Feng, Yifan Zhu, and others, marking the end of the meeting.


[Meeting End]


[Meeting: FW: Weekly SOX RTC Bug Bash/Monthly Team Meeting]
Meeting Date: 2026-01-30T03:16:51.272Z
Meeting Organizer: Ming Yang (MEDIA)
Meeting Summary:
- [sec:slides-intro] Introduction and sharing of new AI-related slides  
  - Chao Wang announced a new slide deck on AI functionality and shared that it builds on previous prompt-sharing sessions.
  - He highlighted that the slides focus on the idea of combining his recent work in AI with traditional prompt techniques.

- [sec:graph-sampling-explanation] Explanation of the AI generator graph and sampling distribution  
  - Chao Wang introduced a graph from an AI generator showing a blue area representing the model’s output probability density when no prompt is provided.  
  - He contrasted the wide blue distribution (raw sampling output) with a more concentrated red curve (“ideal distribution”) that represents responses matching expected outcomes.  
  - He also mentioned a green “spiky” distribution that indicates overly narrow, robotic outputs.  
  - Gavin Wang raised a question about whether the red region indicates “fake” information outside the model’s natural capacity; Chao Wang elaborated further on the graph axes and sampling point concept.

- [sec:graph-axes-clarifications] Questions and clarifications regarding the graph's axes and their meanings  
  - Gavin Wang and Jun Ma asked for clarification on what the horizontal axis represents; Chao Wang explained it represents sampling points, acknowledging the high-dimensional nature of language model outputs.
  - The team discussed how the probability density (y-axis) might be interpreted and how one might understand the distribution’s central point as the “average” or ideal output.

- [sec:prompt-tricks-intuition] Discussion on intuitive versus counterintuitive prompt techniques  
  - Chao Wang explained that older “intuitive” prompt methods (structured, rule-based) are becoming less necessary compared to newer “counterintuitive” methods.  
  - He emphasized leveraging the language model’s innate “common sense” rather than prescribing detailed rules in prompts.
  - He illustrated using code review examples—suggesting that instead of writing extensive guidelines, one can ask the model to adopt a known code review standard (like from a Google team) and then use blacklists to fine-tune the output.

- [sec:QA-common-sense] Questions on model common sense and its utilization  
  - Zhiyuan Lv questioned how to determine and tap into the model’s inherent knowledge (common sense) such as accurate code review criteria.
  - Chao Wang suggested directly asking the model about its expertise (e.g., “Who is the smartest person?” or which standard it favors) to obtain specific guidelines, and then using that information in prompts.
  - Shuo Wang inquired about using subsets of common sense knowledge and ensuring that prompt instructions remain effective even with model upgrades; Chao Wang acknowledged the risk of drifting when models change and advised iterative adjustment.

- [sec:prompt-iteration-challenges] Discussion on prompt maintenance and the overfitting risk in iterative prompt refinement  
  - Ming Yang (MEDIA) shared his experience of using counterintuitive prompt methods to have AI generate prompts for himself, then refining them further.
  - Chao Wang warned that repeated iterations might lead to overfitting—where the prompt becomes too narrowly defined and rigid, resembling “a code snippet that is too specialized” rather than a general instruction.
  - He recommended initially using such methods for a quick start but later revising the prompt to avoid accumulating too much specific context.

- [sec:spec-driven-approach] Introduction of a spec-driven workflow for task management and prompt integration  
  - Chao Wang introduced the concept of “spec driven development” (using tools like spacket/SPEC kit) that integrates prompt templates, scripts, and a structured approach with a Constitution, Specifications, and Task Lists.  
  - He explained how this approach divides work into MVP (Minimum Viable Product) components and user stories, with tasks that can be automatically tracked and executed.
  - He shared practical insights, such as the necessity of not keeping legacy code in the contribution files and the importance of clearly defining the MVP to avoid a drift in requirements.

- [sec:integration-with-dev-tools] Discussion on integration with development tools and version management in AI-assisted workflows  
  - Ming Yang (MEDIA) asked how the introduced tool manages versioning and rollbacks, comparing it with tools like VS Code’s GitHub Copilot.  
  - Chao Wang answered that the system provides restore checkpoints (integrated with VS Code settings) allowing one to revert to previous user story checkpoints, though details depend on specific configurations and versions.
  - There was also a discussion on the frustration of being locked to a single language model in many current tools, with Ming Yang expressing interest in a command-line tool that decouples the prompt workflow from a fixed model.

- [sec:chain-of-thought-discussion] Discussion about 0-shot chain-of-thought (CoT) and its benefits  
  - Chao Wang mentioned that for smaller tasks, a 0-shot chain-of-thought prompt (a fixed sentence prompting the model to “think step by step”) can help trigger creation of a task list.  
  - This method can keep a long-running automated process in a single chat session, provided the context is well established.

- [sec:final-reflections-and-open-questions] Final reflections, feedback, and open questions for future sessions  
  - Ming Yang (MEDIA) recounted how he uses a double-check mechanism: he first receives a comprehensive list of issues (e.g., from a code review), then refines the list by asking for a re-check.
  - Wenlong Yang highlighted the usefulness of such double-check approaches, relating them to multiple samplings that raise the confidence in the final answer.
  - In the closing minutes, Wenlong Yang expressed interest in further exploring the “counterintuitive” prompt techniques in more detail in a follow-up session.
  - The meeting concluded with agreement to schedule another session (next Friday) to cover remaining topics and address additional questions.
[Meeting End]


[Meeting: Agent Engineering - Learning Series]
Meeting Date: 2026-01-30T19:03:52.169Z
Meeting Organizer: Kiran Madipally
Meeting Summary:
- [sec:challenges] Discussion of Challenges in AI-Centered Code Review  
  - Kiran Madipally opened by noting that while AI is generating code effectively, challenges remain in efficiently reviewing code across the full development lifecycle.  
  - He mentioned that existing coding problems are nearly solved, but non-coding aspects continue to require significant manual time.

- [sec:pr_tool_introduction] Introduction of the PR Review Tool (Stas Doc Application)  
  - Kiran explained he has bundled best practices from his own projects into a PR review tool called Stas Doc that facilitates AI-centric code review.  
  - The tool integrates with AZ shell to obtain tokens for DevOps and requires registering the local repository (e.g., “Team Scheduler”) for context.

- [sec:pr_tool_features_context] Features for Gathering PR Context  
  - The tool builds a git work tree for the branch to capture both PR-specific changes and related code (such as referenced methods not directly in the PR).  
  - It fetches context from Work IQ (meeting discussions, design notes) and work item details, gathering comments and additional context into a folder for the review process.

- [sec:pr_tool_features_review_modes] Demonstration of Review Modes and UI  
  - Kiran demonstrated that the tool allows selection of review presets (e.g., bug hunt, code style, performance, security audit) and even supports custom presets that can be saved and shared.  
  - The tool provides multiple ways to display review results: via in-ADO comments, a generated code walkthrough, and terminal output showing detailed differences with context.

- [sec:pr_tool_features_walkthrough] Code Walkthrough Generation  
  - The tool generates a walkthrough that outlines the flow of code changes (e.g., showing where ECS configuration, tenant validation, or cluster defaults are implemented) so reviewers can easily understand the context.  
  - Walkthroughs can be invoked by custom instructions on a portion of the PR, guiding reviewers in a logical order through the code changes.

- [sec:pr_tool_features_auto_fix] Automated Fixes and Interaction with AI Feedback  
  - Kiran showcased the tool’s ability to parse and act on review comments, proposing fixes (such as updating dates or clarifying comments) and automatically applying trivial fixes as separate commits.  
  - There is an option for “auto fix” where the tool uses either GitHub Copilot CLI or Cloud Terminal and even supports manual review of the AI-generated responses before committing changes.

- [sec:qa_context_and_accuracy] Q&A Regarding Context Gathering and Accuracy  
  - Sainath Yelamanchali asked how the tool ensures accurate context and comments; Kiran explained that it pulls data from multiple sources (Work IQ, PR descriptions, work items) and forks only the necessary files into a work tree, managing its context to avoid hitting LLM token limits.  
  - Rhett Thompson inquired whether the tool uses GitHub Copilot TLI or Cloud Code; Kiran clarified that the user can choose either, demonstrating both methods in the tool.

- [sec:pr_tool_ui_and_markdown] UI, Markdown Rendering, and Iterative Review Process  
  - Yang Sun raised a concern regarding markdown file output and how to manage errors in interpretation; Kiran described an iterative process where the LLM self-reviews its output to catch and correct errors.  
  - The tool also features rendering of moment diagrams (beyond standard markdown rendering in ADO) for improved visual representation of documentation and dependency flows.

- [sec:pr_tool_workflows] Demonstration of End-to-End PR Review Workflow  
  - Kiran transitioned to a second example PR review where the tool creates a work tree, reviews the commit (including diffs and test coverage gaps), and generates suggested improvements with commit SHAs provided as proof of automatic fixing.  
  - He emphasized that changes from the tool are made as separate commits for easier reversion and transparency.

- [sec:qa_vs_vs_integration] Q&A on Integration with Local Development Tools  
  - Inderpal Aulakh asked whether the tool might cause file locks when working across Visual Studio and VS Code; Kiran reassured that the tool runs separately in its own terminal which may be auto-closed after review, ensuring that no file locks interfere with the developer’s workflow.

- [sec:future_work_discussion] Discussion on Future Enhancements and Ecosystem Integration  
  - Kiran mentioned his future plans to extend the tool beyond PR review, including automating build and deploy pipelines, incident analysis (with integration of a “brain bot”), and creating a de-grip copilot for log analysis.  
  - Shahab Mokhtari suggested an agent-driven investigation for ICM incidents based on previous on-call investigations, while Kiran noted the need for converting grounding data (e.g., from OneNote) to markdown for proper context gathering.  
  - Tyler Stinson proposed having an extension model so users can append their own functionalities; Kiran confirmed that the tool’s backend (using Node.js and a web frontend) is designed with extensibility in mind, and that future updates may let agents generate plugins on demand.
  - Andrew Frantsuzov and Renato Barbosa Pereira discussed the potential impact on workflows and the need for mechanisms (like deep links and automated “ready for review” detection) to cope with accelerated PR and code change velocity.

- [sec:final_notes] Conclusion and Next Steps  
  - Kiran concluded by stating he will bundle and share a binary along with the source code on a repository for community contributions.  
  - Final thoughts centered on the tool’s role as an assistant to improve review speed for cross-cutting processes and ensuring that it assists rather than replaces manual review, with continued improvements planned based on team feedback.
[Meeting End]


Today is Wednesday, February 4, 2026

Podcast Opening Section Generation
Execute the Personalization CoT (Steps 1-4), then generate the full podcast script for hosts Andrew and Ava.
 
 Hosts should NEVER call each other's name.
 
 For meetings where the user was **Active** (presented, spoke), the script must:
 - NEVER summarize what the user said or presented
 - ONLY describe reactions, outcomes, next steps, or follow-up actions from others
 - Use minimal tokens
 
 Hosts should NEVER call each other's name.
 
 **Constraints**:
 - **NO Meta-Commentary**.
 - **NO Flattery**.
 - **NO Robot-Speak**.
 - **NO Recapping User's Speech**.

Personalization Tags
action-oriented;SOX;[Profile: Chao Wang, Core Identity: Role: Principal Applied Scientist. Organization: Microsoft. Primary Identifier: wangchao@microsoft.com. Organizational Placement: Operating at a senior research-to-production tier, the role involves high-level alignment with Strategic Leadership (Partner and Group-level Engineering Directors) and Technical Execution (Principal Software Engineering Managers and core Software Engineers). Key Collaborators: Ramesh R (Partner Director), Qiongfang Zhang (Principal Group Mgr), Bingqian Shen (Principal SWE Mgr), Bo Lu (Principal SWE Mgr), Yu Jin (Sr. SWE Mgr), Meng Zhou, and Wanqin Cao. Functional Focus: Applied Science: Specialized in translating scientific theory into scalable engineering frameworks. Cross-Functional Influence: Bridges the gap between research-heavy initiatives and product-driven engineering cycles.]"