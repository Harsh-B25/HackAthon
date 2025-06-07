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

def summarise_data(data , jurisdiction):
# Define your prompt
    prompt = f'''LEGAL DOCUMENT RISK & COMPLIANCE ANALYSIS PROMPT
You are a senior legal expert specializing in document analysis and risk assessment for jurisdiction = {jurisdiction}. I'm providing a legal document as an array where each index contains one page of content: {data}
CRITICAL MISSION: Provide extensive risk analysis with specific legal precedents, statutes, and case law from {jurisdiction} - NOT a summary. Explain WHY each provision creates legal risk by citing actual laws, regulations, and court decisions.
MANDATORY RISK ANALYSIS FRAMEWORK:
1. CONTRACTUAL LIABILITY EXPOSURE ANALYSIS:

Cite specific {jurisdiction} contract law statutes governing liability limitations
Reference relevant case precedents on enforceability of liability caps
Analyze indemnification scope against {jurisdiction} indemnity law requirements
Quote specific statutory provisions on consequential damages exclusions
Identify conflicts with {jurisdiction} consumer protection laws

2. REGULATORY COMPLIANCE RISK ASSESSMENT:

Cite specific {jurisdiction} employment law statutes and potential violations
Reference data protection regulations and breach notification requirements
Analyze against {jurisdiction} business licensing and regulatory filing obligations
Quote relevant industry-specific compliance statutes
Identify potential violations of {jurisdiction} unfair competition laws

3. ENFORCEMENT & REMEDIAL RISK ANALYSIS:

Cite {jurisdiction} civil procedure rules on injunctive relief standards
Reference specific statutes on attorney fee recovery provisions
Analyze termination provisions against {jurisdiction} wrongful termination law
Quote relevant precedents on liquidated damages enforceability
Assess dispute resolution clauses against {jurisdiction} arbitration statutes

4. INTELLECTUAL PROPERTY & CONFIDENTIALITY RISKS:

Cite {jurisdiction} trade secret protection statutes and requirements
Reference specific case law on reasonable confidentiality measures
Analyze IP assignment provisions against {jurisdiction} employment law
Quote relevant statutes on employee invention rights
Assess non-compete enforceability under {jurisdiction} restraint of trade law

5. FINANCIAL & OPERATIONAL EXPOSURE:

Cite {jurisdiction} commercial law on payment obligations and default
Reference specific bankruptcy code provisions affecting contract terms
Analyze insurance requirements against {jurisdiction} insurance regulations
Quote relevant statutes on penalty and forfeiture limitations
Assess force majeure provisions against {jurisdiction} contract frustration law

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
Document Classification & Legal Framework
Describe the type of legal document and cite the applicable legal framework for {jurisdiction}.

Party Risk Allocation Analysis
Identify all key parties involved and analyze each party’s legal responsibilities and exposure under {jurisdiction} statutes.

Contractual Obligation Risk Matrix
For each major obligation, include:

📘 <span style="color:#32CD32; font-weight:bold;">Legal basis for enforceability</span> (cite specific clauses/statutes)

⚠️ <span style="color:#FF4500; font-weight:bold;">Risk of non-compliance</span> (state penalties or effects)

⏰ <span style="color:#FFD700; font-weight:bold;">Mitigation requirements</span> (mention audit/compliance expectations)

Financial Liability Exposure Analysis
Explain the possible monetary damages or liabilities under {jurisdiction} laws, including doctrines like “irreparable injury” or “complete legal costs.”

Temporal Compliance Risk Assessment
Highlight all relevant deadlines and correlate them with {jurisdiction}’s statutes of limitations.

Breach Consequence Legal Analysis
Summarize the breach enforcement pathways and remedies (court action, injunctions, etc.) available under {jurisdiction}.

Regulatory Compliance Gap Analysis
Point out any sections that may violate or fail to meet the requirements of {jurisdiction} regulatory frameworks.
CRITICAL LEGAL CITATION REQUIREMENTS:

Quote specific statute numbers and sections
Cite relevant case names and holdings
Reference applicable regulatory codes
Include specific penalty amounts from statutes
Quote exact language from relevant laws

RISK SEVERITY INDICATORS:

\033[1;31mHIGH RISK\033[0m: Potential criminal liability, regulatory sanctions, significant financial exposure
\033[1;33mMEDIUM RISK\033[0m: Civil liability, compliance violations, operational disruption
\033[1;32mMANAGED RISK\033[0m: Standard commercial risk with adequate protections

FINAL VERIFICATION MANDATE:
Remove the word HTML everywhre only focus on the topic and not the formatting. There should't be any single mention of html or the type of formatting.
Every risk identified MUST be supported by specific {jurisdiction} legal authority. No generic statements. Every provision MUST be analyzed against actual law with citations.
OUTPUT REQUIREMENT:
Return comprehensive risk analysis with extensive legal citations - NO SUMMARY. Explain legal basis for each risk using {jurisdiction} statutes, regulations, and case precedents.'''

    # Send the prompt and get response
    response = model.generate_content(prompt)
    clean_response = response.text.replace("**", "")
    clean_response = clean_response.replace("```" , "")
    print(clean_response)

summarise_data(text_extractor(sys.argv[1]) , "India")