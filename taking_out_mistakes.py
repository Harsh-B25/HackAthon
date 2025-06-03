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

def summarise_data(data):
# Define your prompt
    prompt = f'''You are a senior legal expert specializing in document analysis and plain-language summaries. I'm providing a legal document as an array where each index contains one page of content: {data}

Your task: Risk Terms & Legal Analysis Prompt
Create a comprehensive risk and legal compliance summary achieving 100% accuracy in exactly 150-250 words, accessible to non-lawyers.
CRITICAL REQUIREMENTS - DO NOT OMIT ANY:
Risk Terms & Exposure Analysis:

ALL liability limitations, caps, and exclusions with exact dollar amounts/percentages
EVERY indemnification obligation, scope, and financial exposure
ALL insurance requirements, minimum coverage amounts, and proof obligations
EVERY termination trigger, breach condition, and default scenario
Complete force majeure provisions and risk allocation terms
ALL warranty disclaimers, limitation periods, and consequential damage exclusions
EVERY liquidated damages clause, penalty provision, and remedy limitation

Legal Compliance & Governing Framework:

Complete governing law, jurisdiction, venue, and dispute resolution mechanisms
ALL regulatory compliance requirements and industry-specific legal obligations
EVERY statutory disclosure requirement and regulatory filing obligation
Complete intellectual property indemnification and infringement liability
ALL data protection, privacy law compliance, and security breach obligations
EVERY employment law, labor regulation, and worker classification requirement
Complete environmental, safety, and health regulatory compliance terms

Additional Critical Elements:

ALL defined terms with complete legal definitions and risk implications
EVERY notice requirement, cure period, and procedural compliance obligation
Complete assignment restrictions and change of control provisions
ALL customer non-diversion clauses and competitive restriction terms

MANDATORY STRUCTURE (numbered points):
1. \033[1;34mDocument type/purpose\033[0m (10-15 words)
2. \033[1;34mKey parties and roles\033[0m (15-20 words)  
3. \033[1;34mALL obligations with specifics\033[0m (80-100 words) - Include ALL categories, exclusions, disclosure rights, restrictions
4. \033[1;34mFinancial terms/penalties\033[0m (20-30 words) - Include "irreparable injury" and "complete legal costs"
5. \033[1;34mALL timelines/deadlines\033[0m (15-25 words)
6. \033[1;34mBreach consequences\033[0m (15-25 words)
7. \033[1;34mKey legal provisions\033[0m (15-25 words)

FORMAT WITH ANSI COLORS:
- \033[1;32mKey terms/definitions\033[0m (bright green)
- \033[1;31mConsequences/penalties/warnings\033[0m (bright red)
- \033[1;33mTimeframes/numbers/deadlines\033[0m (bright yellow)
- \033[1mBold emphasis\033[0m for critical points

FINAL VERIFICATION: Confirm you've included EVERY provision, exclusion, disclosure right, timeline, consequence, and legal detail. Missing ANY substantive element = incomplete summary.
    
    return only the final data form and not rest of the text or working behind getting that text'''

    # Send the prompt and get response
    response = model.generate_content(prompt)
    clean_response = response.text.replace("**", "")
    print(clean_response)

summarise_data(text_extractor("./legal_docs_1.pdf"))