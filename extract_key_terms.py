import google.generativeai as genai
import fitz
import sys
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
    prompt = f'''You are a senior legal expert specializing in web‑based document analysis and interactive visualization. Your input will be a legal document provided as {data}.

🎯 TASK
Analyze the document and for an interactive flow‑chart plus a concise, styled HTML summary.

🔍 PROCESSING REQUIREMENTS
Extract all sections, clauses, and legal provisions.

Identify key terms, obligations, rights, risk factors.

Categorize by parties, obligations, rights, risks, compliance, timeline.

Create ≤ 20‑word summaries per section.

Assign risk levels (low / medium / high).

Map dependencies between sections.

MANDATORY STRUCTURE: Return the summary formatted as an HTML <ol> list with inline <span> styles to show color and bold text on a webpage.

Each heading must be:

Bold

Colored blue (#1E90FF)

Use inline spans for:

📘 Legal terms – bright green (#32CD32)

⚠️ Penalties or consequences – bright red (#FF4500)

⏰ Timeframes, dates, deadlines – golden yellow (#FFD700)

⚖️ Jurisdiction names – golden yellow (#FFD700)

🔹 Sections to be returned (as <li> items):

Contractual Obligation Risk Matrix
For each major obligation, include:

📘 <span style="color:#32CD32; font-weight:bold;">Legal basis for enforceability</span> (cite specific clauses/statutes)

⚠️ <span style="color:#FF4500; font-weight:bold;">Risk of non-compliance</span> (state penalties or effects)

⏰ <span style="color:#FFD700; font-weight:bold;">Mitigation requirements</span> (mention audit/compliance expectations)
RISK SEVERITY INDICATORS:

\033[1;31mHIGH RISK\033[0m: Potential criminal liability, regulatory sanctions, significant financial exposure
\033[1;33mMEDIUM RISK\033[0m: Civil liability, compliance violations, operational disruption
\033[1;32mMANAGED RISK\033[0m: Standard commercial risk with adequate protections
🧩 MANDATORY SUMMARY STRUCTURE
Document type/purpose – 10‑15 words

Key parties & roles – 15‑20 words

All obligations, rights, restrictions, disclosure rights – 80‑100 words

Financial terms & penalties – 20‑30 words, include “<span class="text-red-600 font-semibold">irreparable injury</span>” and “<span class="text-red-600 font-semibold">complete legal costs</span>”

Timelines & deadlines – 15‑25 words

Breach consequences & remedies – 15‑25 words

Key legal provisions – 15‑25 words

✅ FINAL VERIFICATION
Before returning, confirm you have captured every clause, exclusion, disclosure right, timeline, consequence, legal detail, and assignment or jurisdictional restriction. Nothing may be omitted—any missing element renders the summary incomplete.

Return only the refined prompt text shown above.
'''

    # Send the prompt and get response
    response = model.generate_content(prompt)
    clean_response = response.text.replace("**", "")
    clean_response = clean_response.replace("```" , "")
    clean_response = clean_response.replace("html" , "")
    # print(clean_response)
    print(clean_response)

key_words_extractor(text_extractor(sys.argv[1]))