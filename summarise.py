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
    prompt = f'''You are a senior legal expert specializing in document analysis and plain-language summaries. I'm providing a legal document as an array where each index contains one page of content: {data}

Your task: Create a comprehensive summary achieving 100% accuracy in exactly 150-250 words, accessible to non-lawyers.

CRITICAL REQUIREMENTS - DO NOT OMIT ANY:
- ALL specific numbers: exact time periods, dollar amounts, percentages, deadlines
- EVERY substantive obligation, right, restriction, and exception (including all exclusions and disclosure rights)
- ALL defined terms with their complete definitions and categories
- EVERY penalty, consequence, remedy, and waiver provision
- Complete governing law/jurisdiction and assignment restrictions
- ALL return requirements, notice obligations, and moral rights waivers
- Customer non-diversion clauses and business opportunity restrictions

MANDATORY STRUCTURE (numbered points):
1. <span style="color:#1E90FF; font-weight:bold;">Document type/purpose</span> (10-15 words)
2. <span style="color:#1E90FF; font-weight:bold;">Key parties and roles</span> (15-20 words)
3. <span style="color:#1E90FF; font-weight:bold;">ALL obligations with specifics</span> (80-100 words) - Include 
<span style="color:#32CD32; font-weight:bold;">ALL categories</span>, exclusions, 
<span style="color:#32CD32; font-weight:bold;">disclosure rights</span>, restrictions
4. <span style="color:#1E90FF; font-weight:bold;">Financial terms/penalties</span> (20-30 words) - Include "<span style="color:#FF4500; font-weight:bold;">irreparable injury</span>" and "<span style="color:#FF4500; font-weight:bold;">complete legal costs</span>"
5. <span style="color:#1E90FF; font-weight:bold;">ALL timelines/deadlines</span> (<span style="color:#FFD700; font-weight:bold;">15-25 words</span>)
6. <span style="color:#1E90FF; font-weight:bold;">Breach consequences</span> (15-25 words)
7. <span style="color:#1E90FF; font-weight:bold;">Key legal provisions</span> (15-25 words)

FORMAT GUIDELINES FOR WEB DISPLAY:
- Use <span style="color:#32CD32; font-weight:bold;">bright green</span> text for Key terms/definitions
- Use <span style="color:#FF4500; font-weight:bold;">bright red</span> text for Consequences/penalties/warnings
- Use <span style="color:#FFD700; font-weight:bold;">bright yellow</span> text for Timeframes/numbers/deadlines
- Use <b>bold emphasis</b> for critical points

IMPORTANT:
Please output the content as raw HTML with styled <span> tags and <b> tags.

When rendering this output in EJS, use unescaped output tags like <%- data %> to ensure the HTML styles are applied and the colored, bold formatting appears correctly on the webpage.

FINAL VERIFICATION: Confirm you've included EVERY provision, exclusion, disclosure right, timeline, consequence, and legal detail. Missing ANY substantive element = incomplete summary.
    
    return only the text and nothing else'''

    # Send the prompt and get response
    response = model.generate_content(prompt)
    clean_response = response.text.replace("**", "")
    clean_response = clean_response.replace("```" , "")
    clean_response = clean_response.replace("html" , "")
    print(clean_response)

summarise_data(text_extractor(sys.argv[1]))