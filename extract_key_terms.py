import google.generativeai as genai
import fitz

# Configure API key
genai.configure(api_key="AIzaSyA23skfhuiaYRBvTysoLXqp_TQx07Lg1lY")

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# Extracting text from pdf
def text_extractor(file_name):
    text = []
    doc = fitz.open(file_name)

    for page in doc:
        text.append(page.get_text())
    print("Function1 completed")
    return text

def key_words_extractor(data):
# Define your prompt
    prompt = f'''You are a senior legal expert specializing in document analysis and visual flowchart creation. I'm providing a legal document as an array where each index contains one page of content: {data}
Your task: Create a comprehensive, small , concise, reduced height, increased width/branching legal flowchart using ASCII art and ANSI colors for terminal display that achieves 100% accuracy by capturing EVERY provision.
CRITICAL ACCURACY REQUIREMENTS:

Extract EVERY article/section number and map to flowchart elements
Include ALL obligations, rights, exceptions, and consequences without omission
Verify each provision against source document by article reference
Cross-reference all temporal elements, parties, and legal concepts
Ensure no substantive provision is missing or misrepresented

MANDATORY COMPLETENESS CHECKLIST:
□ All contractual obligations (must/shall/will) with article citations
□ All rights & permissions (may/can) with specific conditions
□ All prohibitions (cannot/will not) with scope limitations
□ All exceptions (if/unless/except) with triggering conditions
□ All consequences (breach/violation results) with remedy types
□ All temporal elements (timeframes/duration/survival) with exact periods
□ All definitions with complete scope as defined in document
□ All party relationships and role-specific obligations
□ All notice/disclosure requirements with procedural details
□ All assignment/ownership provisions with intellectual property aspects
□ All termination conditions and post-termination obligations
□ All enforceability and modification provisions
ENHANCED LEGAL CATEGORIZATION:

Primary Obligations: Core duties with performance standards
Secondary Obligations: Supporting duties (notice, cooperation, etc.)
Conditional Rights: Permissions dependent on circumstances
Absolute Prohibitions: Never-allowed activities regardless of context
Conditional Prohibitions: Restricted activities with exceptions
Immediate Consequences: Instant effects of breach/compliance
Future Consequences: Long-term effects and ongoing obligations
Survival Provisions: Post-termination continuing obligations
Modification/Waiver Rules: How agreement can be changed
Dispute Resolution: Enforcement mechanisms and jurisdiction

PRECISION FLOWCHART MAPPING:

Each flowchart node must reference specific article/section number
Decision diamonds must show exact conditional language from document
Timeline branches must display precise duration periods
Exception paths must capture complete conditional logic
Consequence nodes must specify remedy type and enforcement method

VERIFICATION PROTOCOL:

Map each article number to flowchart location
Confirm no legal concept appears in document but not in flowchart
Verify all cross-references between provisions are visually connected
Ensure conditional logic mirrors document's exact language
Validate all timeframes match document specifications exactly

ASCII FLOWCHART FORMAT:
┌─────────────────┐    ◊─────────────────◊
│ \033[1;34m[Art.X] PROCESS\033[0m │ ──► ◊ \033[1;32m[Art.Y] CONDITION\033[0m ◊
└─────────────────┘    ◊─────────────────◊
       │                       │
       ▼                  ┌────┴────┐
┌─────────────┐           │ \033[1;33mYES│NO\033[0m │
│\033[1;31m[Art.Z]BREACH→\033[0m│           └─────────┘
│\033[1;31mCONSEQUENCE\033[0m   │
└─────────────┘

Allow as much branching as possible to decrease the height of the flowchart as it should not be overwhleming for the lay man user to see the flowchart as you need to keep in mind that common people will also be using this software
COLOR CODING WITH LEGAL PRECISION:

\033[1;34m[Art.#] Document Structure/Definitions\033[0m (bright blue)
\033[1;32m[Art.#] Obligations/Duties/Requirements\033[0m (bright green)
\033[1;31m[Art.#] Breaches/Penalties/Consequences\033[0m (bright red)
\033[1;33m[Art.#] Timeframes/Conditions/Triggers\033[0m (bright yellow)
\033[1;35m[Art.#] Exceptions/Rights/Permissions\033[0m (bright magenta)
\033[1;36m[Art.#] Key Definitions/Scope\033[0m (bright cyan)
\033[1;37m[Art.#] Procedural/Administrative\033[0m (bright white)

MANDATORY STRUCTURE SEQUENCE:

Document header with full title and nature
Party identification with role-specific obligations
Definitions section with complete scope mapping
Primary obligation clusters with article cross-references
Conditional obligation branches with exact trigger conditions
Prohibition networks with exception pathways
Temporal obligation flows with survival provisions
Breach consequence trees with remedy specifications
Administrative procedure flows (notices, modifications)
Termination cascade with post-termination obligations

FINAL VERIFICATION REQUIREMENT:
Before output, mentally audit: "Can I trace every single provision in the source document to a specific location in this flowchart?" If answer is not 100% yes, revise until complete.
OUTPUT: Return ONLY the complete ASCII flowchart with ANSI colors achieving 100% document coverage - no explanatory text, no omissions, no approximations.'''

    # Send the prompt and get response
    response = model.generate_content(prompt)
    clean_response = response.text.replace("**", "")
    print(clean_response)

key_words_extractor(text_extractor("./legal_docs_1.pdf"))