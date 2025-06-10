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
    # print("Function1 completed")
    return text

def summarise_data(data):
# Define your prompt
    prompt = f'''Create a comprehensive summary of 150–250 words that is:

100% accurate

Fully inclusive of every legal detail

Easily understandable by non-lawyers

Styled for beautiful web display

✅ CRITICAL REQUIREMENTS – Include Every Single One:
All specific numbers: exact time periods, percentages, dollar amounts, deadlines

Every defined term with its full definition and category

All obligations, rights, restrictions, exclusions, and disclosure rights

Return requirements, notice obligations, and moral rights waivers

Customer non-diversion clauses and business opportunity restrictions

All penalties, remedies, consequences, including irreparable injury and complete legal cost recovery

Governing law, jurisdiction, and assignment restrictions

🧩 Summary Structure (Use Numbered Points):
Document type/purpose (10–15 words)

Key parties and roles (15–20 words)

All obligations, rights, restrictions, and disclosure rights (80–100 words)

Financial terms and penalties (20–30 words)

All timelines and deadlines (15–25 words)

Breach consequences and remedies (15–25 words)

Key legal provisions (15–25 words)

🎨 Styling Rules for Web Display:
Use bright green for key terms and definitions

Use bright red for penalties, consequences, and waivers

Use bright yellow for timeframes, deadlines, and numbers

Use bold for all critical concepts and points

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


✅ Final Verification:
Before submitting, confirm you have:

Included every substantive clause

Fully explained all definitions, exclusions, waivers, and consequences

Only give the summary related text and not anything else. Missing even one element invalidates the summary.'''

    # Send the prompt and get response
    response = model.generate_content(prompt)
    clean_response = response.text.replace("**", "")
    clean_response = clean_response.replace("```" , "")
    clean_response = clean_response.replace("html" , "")
    print(clean_response)

summarise_data(text_extractor(sys.argv[1]))