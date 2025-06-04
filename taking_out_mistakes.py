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

MANDATORY OUTPUT STRUCTURE:

\033[1;34mDocument Classification & Legal Framework\033[0m - State document type and cite governing {jurisdiction} legal framework
\033[1;34mParty Risk Allocation Analysis\033[0m - Identify each party's legal exposure with statutory references
\033[1;34mContractual Obligation Risk Matrix\033[0m - Analyze each obligation against {jurisdiction} law:

\033[1;32mLegal basis for enforceability\033[0m (cite specific statutes)
\033[1;31mRisk of non-compliance\033[0m (cite penalties/consequences)
\033[1;33mMitigation requirements\033[0m (cite compliance standards)


\033[1;34mFinancial Liability Exposure Analysis\033[0m - Cite {jurisdiction} damages law and precedents
\033[1;34mTemporal Compliance Risk Assessment\033[0m - Analyze all deadlines against {jurisdiction} limitations periods
\033[1;34mBreach Consequence Legal Analysis\033[0m - Cite specific {jurisdiction} breach remedies and enforcement mechanisms
\033[1;34mRegulatory Compliance Gap Analysis\033[0m - Identify potential violations of {jurisdiction} laws

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
Every risk identified MUST be supported by specific {jurisdiction} legal authority. No generic statements. Every provision MUST be analyzed against actual law with citations.
OUTPUT REQUIREMENT:
Return comprehensive risk analysis with extensive legal citations - NO SUMMARY. Explain legal basis for each risk using {jurisdiction} statutes, regulations, and case precedents.'''

    # Send the prompt and get response
    response = model.generate_content(prompt)
    clean_response = response.text.replace("**", "")
    print(clean_response)

juris = input("What is your jurisdictions = \n")
summarise_data(text_extractor("./legal_docs_1.pdf") , juris)