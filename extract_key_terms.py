import google.generativeai as genai
import fitz
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
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
    prompt = f'''# Enhanced Legal Document Analysis Prompt - Structured PDF Format

    ## Role Definition
    You are a senior legal expert specializing in comprehensive document analysis and professional legal documentation. Your expertise spans contract law, regulatory compliance, and legal terminology across multiple jurisdictions including U.S., India, and international frameworks.

    ## Input Requirements
    - Legal document provided as structured data: {data}
    - Each array index represents one complete page of the source document
    - Reference document structure: Internship Contract Agreement (4 pages, 13 sections)

    ## Primary Objective
    Create a professionally formatted PDF document that maintains the EXACT structural format of the provided reference document while providing 100% accurate legal analysis and enhanced educational content.

    ## Document Structure Requirements (MANDATORY - DO NOT DEVIATE)

    ### Page 1: Title Page and Document Introduction
    **Title**: "Comprehensive Legal Analysis: Essential Terms and Provisions"
    **Subtitle**: [Source Document Name] - Professional Legal Commentary
    **Document Metadata**:
    - Analysis Date: [Current Date]
    - Total Sections Analyzed: [Number]
    - Jurisdictional Scope: Multi-jurisdictional Analysis
    - Prepared by: Senior Legal Expert

    ### Page 2-3: Executive Summary and Key Findings
    **Executive Summary Section**:
    - Document classification and legal nature
    - Primary parties and their legal relationship
    - Critical legal obligations and rights summary
    - Risk assessment overview
    - Compliance requirements summary

    **Key Legal Themes Identified**:
    - List 5-7 major legal themes from the document
    - Each theme with brief explanation and section references

    ### Page 4 onwards: Detailed Legal Term Analysis
    **CRITICAL**: Follow the exact numbering and sectional structure of the source document

    For each section in the source document, provide:

    #### Section [X]. [Original Section Title]
    **Original Provision Summary**: [Exact content from source with article citations]

    **Legal Term Analysis**: [Key legal terms from this section]

    **Essential Legal Definitions**:
    - **[Term 1]**: 
    - Definition: [Precise legal definition]
    - Legal Significance: [Why this term matters legally]
    - Jurisdictional Context: [Relevant laws/cases from U.S., India, international]
    - Practical Application: [Real-world examples]
    - Compliance Requirements: [What parties must do]
    - Risk Assessment: [Consequences of non-compliance]

    - **[Term 2]**: [Same format]
    - **[Additional Terms]**: [Same format]

    **Section-Specific Legal Analysis**:
    - Rights created by this section
    - Obligations imposed by this section  
    - Exceptions or limitations
    - Temporal elements (if any)
    - Cross-references to other sections

    ## Enhanced Accuracy Requirements (100% Completeness)

    ### Provision Extraction Standards
    - **Article Mapping**: Extract EVERY section, subsection, bullet point, and clause
    - **Temporal Precision**: Capture exact dates, timeframes, notice periods
    - **Party Analysis**: Identify all entities, roles, and specific obligations
    - **Cross-Reference Validation**: Verify internal document references
    - **Legal Consequence Mapping**: Detail all breach scenarios and remedies

    ### Mandatory Completeness Verification Matrix
    For EACH section, verify capture of:
    □ **Primary Obligations** - All "must/shall/will/agrees to" provisions
    □ **Conditional Rights** - All "may/can/entitled to" with qualifying conditions  
    □ **Explicit Prohibitions** - All "cannot/shall not/prohibited from" clauses
    □ **Exception Clauses** - All "unless/except/provided that/if" conditions
    □ **Temporal Requirements** - All deadlines, durations, survival periods
    □ **Procedural Steps** - All notice, documentation, approval requirements
    □ **Defined Relationships** - All party roles and hierarchical structures
    □ **Breach Consequences** - All penalties, termination rights, damages
    □ **Modification Rules** - All amendment and waiver provisions
    □ **Enforceability Terms** - All governing law and dispute resolution clauses

    ### Legal Term Selection Criteria
    From the source document, identify and analyze:
    - **Foundational Terms**: Basic legal concepts essential to document understanding
    - **Risk Terms**: Provisions that create significant legal exposure
    - **Procedural Terms**: Requirements for proper document execution
    - **Relationship Terms**: Definitions of party roles and obligations
    - **Temporal Terms**: Time-sensitive provisions and deadlines
    - **Compliance Terms**: Regulatory and policy requirements
    - **Enforcement Terms**: Dispute resolution and remedial provisions

    ## Professional Formatting Standards (Maintain Original Structure)

    ### Typography Requirements
    - **Font**: Times New Roman, 12pt body text
    - **Section Headers**: Bold, 14pt, matching original document numbering
    - **Subsection Headers**: Bold, 12pt, underlined
    - **Legal Terms**: Bold on first use, italicized for emphasis
    - **Citations**: Bracketed, 10pt font
    - **Margins**: 1-inch all sides
    - **Line Spacing**: 1.15 for readability

    ### Visual Structure Requirements
    - **Page Breaks**: Match original document pagination flow
    - **Section Numbering**: EXACTLY mirror source document structure
    - **Bullet Points**: Maintain original formatting where present
    - **Paragraph Structure**: Preserve original paragraph breaks
    - **Footer**: Page numbers, document title, analysis date

    ### Content Organization Requirements
    - **Preserve Original Flow**: Analysis follows exact sequence of source document
    - **Section Integrity**: Each original section gets dedicated analysis space
    - **Cross-Reference Maintenance**: Preserve all internal document references
    - **Appendix Structure**: If source has appendices, maintain in analysis

    ## Quality Assurance Protocol

    ### Accuracy Validation Steps
    1. **Line-by-Line Verification**: Every sentence in source document accounted for
    2. **Citation Accuracy**: All section references verified against source
    3. **Legal Definition Verification**: All definitions checked against legal standards
    4. **Jurisdictional Appropriateness**: All legal contexts verified for accuracy
    5. **Completeness Audit**: Final check against completeness matrix

    ### Professional Review Standards
    - **Legal Accuracy**: All interpretations legally sound and current
    - **Accessibility**: Content understandable to both lawyers and non-lawyers
    - **Consistency**: Terminology and formatting uniform throughout
    - **Comprehensiveness**: No substantive provision omitted or misrepresented

    ## Output Specifications

    ### Final Deliverable Requirements
    - **PDF-Ready Content**: Formatted for direct PDF generation
    - **No Extraneous Content**: No flowcharts, debugging notes, or process comments
    - **Complete Analysis**: Every section of source document addressed
    - **Professional Presentation**: Legal document standards maintained
    - **Structural Fidelity**: Original document organization preserved exactly

    ### Content Exclusions
    - No ASCII art, diagrams, or visual flowcharts
    - No development comments or metadata
    - No prompt acknowledgments or processing notes
    - No reformatting of original document structure
    - No consolidation of original sections

    ## Success Criteria Validation

    The analysis achieves 100% accuracy when:
    1. **Structural Fidelity**: Document follows exact format of source document
    2. **Provision Coverage**: Every clause, sentence, and obligation captured
    3. **Legal Accuracy**: All interpretations jurisdictionally appropriate and current
    4. **Professional Standards**: Document meets legal industry formatting standards
    5. **Educational Value**: Content serves as comprehensive legal reference tool
    6. **Completeness Verification**: All checklist items confirmed complete

    **Final Instruction**: Generate ONLY the complete PDF content following the exact structural format of the source document. Maintain all original section numbers, titles, and organizational flow while providing comprehensive legal analysis within each section. No additional commentary, processing notes, or structural modifications permitted.
'''

    # Send the prompt and get response
    response = model.generate_content(prompt)
    clean_response = response.text.replace("**", "")
    # print(clean_response)
    return clean_response

def save_output_to_pdf(output_text, filename="output.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Write each line on a new line in the PDF
    y = height - 40  # Start from top of the page
    for line in output_text.split('\n'):
        c.drawString(40, y, line)
        y -= 15  # Move down by 15 points for each new line

    c.save()
    print(f"Output written to {filename}")

save_output_to_pdf(key_words_extractor(text_extractor("./legal_docs_1.pdf")))