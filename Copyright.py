# Re-run after code environment reset to regenerate the LaTeX file

# Re-create the data dictionary
import os
import subprocess

data = {
    "agreement_date": r"\underline{June 1, 2025}",
    "licensor_name": r"\underline{Creative Minds Inc.}",
    "licensor_type": r"\underline{company}",
    "licensor_jurisdiction": r"\underline{California, USA}",
    "licensor_address": r"\underline{123 Innovation Drive, San Francisco, CA}",

    "licensee_name": r"\underline{Bright Future Media}",
    "licensee_type": r"\underline{company}",
    "licensee_jurisdiction": r"\underline{New York, USA}",
    "licensee_address": r"\underline{789 Growth Avenue, New York, NY}",

    "licensed_works_description": r"\underline{digital illustrations, website templates, and marketing videos}",
    "effective_date": r"\underline{June 10, 2025}",
    "territory": r"\underline{worldwide}",
    "term_duration": r"\underline{perpetual}",
    "license_type": r"\underline{non-exclusive}",
    "license_transferability": r"\underline{non-transferable}",

    "license_purpose": r"\underline{commercial distribution}",
    "specific_permitted_uses": r"\underline{online marketing, printed brochures, and social media ads}",
    "use_limitations": r"\underline{Use in any defamatory or illegal content is prohibited}",

    "license_fee": r"\underline{5,000 USD}",
    "payment_terms": r"\underline{50percent upfront and 50percent within 30 days of delivery}",

    "termination_breach_days": r"\underline{15}",
    "termination_convenience_days": r"\underline{30}",

    "copyright_notice": r"\underline{ Creative Minds Inc., All Rights Reserved.}",

    "licensor_signatory_name": r"\underline{Alice Johnson}",
    "licensor_signatory_title": r"\underline{CEO}",
    "licensor_signature_date": r"\underline{June 1, 2025}",

    "licensee_signatory_name": r"\underline{Bob Stevens}",
    "licensee_signatory_title": r"\underline{Managing Director}",
    "licensee_signature_date": r"\underline{June 1, 2025}"
}


latex_text2 = rf"""\documentclass[12pt]{{article}}
\usepackage[utf8]{{inputenc}}
\usepackage[a4paper, margin=1in]{{geometry}}
\usepackage{{enumitem}}
\usepackage{{parskip}} % Adds vertical space between paragraphs
\setlength\parindent{{0pt}}

\begin{{document}}

\section*{{COPYRIGHT LICENSE AGREEMENT}}

\vspace{{1em}}

This Copyright License Agreement (hereinafter referred to as the “Agreement”) is made and entered into on this {data["agreement_date"]}, by and between:

\vspace{{1em}}

\textbf{{Licensor}}: {data["licensor_name"]}, a {data["licensor_type"]} organized and existing under the laws of {data["licensor_jurisdiction"]}, with its principal office at {data["licensor_address"]} (hereinafter referred to as the "Licensor"), 

\vspace{{0.5em}}

\textbf{{and}}

\vspace{{0.5em}}

\textbf{{Licensee}}: {data["licensee_name"]}, a {data["licensee_type"]} organized and existing under the laws of {data["licensee_jurisdiction"]}, with its principal office at {data["licensee_address"]} (hereinafter referred to as the "Licensee").

\vspace{{1em}}

The Licensor and Licensee may collectively be referred to as the “Parties” and individually as a “Party.”

\vspace{{1.5em}}

WHEREAS, the Licensor owns certain intellectual property rights in and to specific copyrighted works (the “Licensed Works”);

\vspace{{0.5em}}

WHEREAS, the Licensee wishes to obtain a license to use, reproduce, and distribute the Licensed Works under the terms and conditions set forth in this Agreement;

\vspace{{0.5em}}

NOW, THEREFORE, in consideration of the mutual covenants and agreements herein contained, the Parties agree as follows:

\vspace{{1.5em}}

\textbf{{1. DEFINITIONS}}

\vspace{{0.5em}}

1.1 \textbf{{Licensed Works}}: All copyrighted material owned by the Licensor, including but not limited to {data["licensed_works_description"]}.

1.2 \textbf{{Effective Date}}: The Effective Date of this Agreement shall be {data["effective_date"]}.

1.3 \textbf{{Territory}}: {data["territory"]}.

1.4 \textbf{{Term}}: {data["term_duration"]}.

1.5 \textbf{{Usage}}: The rights granted to the Licensee to use the Licensed Works as described in Section 2.

\vspace{{1em}}

\textbf{{2. GRANT OF LICENSE}}

\vspace{{0.5em}}

2.1 The Licensor hereby grants the Licensee a {data["license_type"]}, {data["license_transferability"]} license to use the Licensed Works for {data["license_purpose"]}.

2.2 The Licensee may:
\begin{{itemize}}[leftmargin=*]
    \item reproduce and copy the Licensed Works;
    \item publicly perform and display the Licensed Works;
    \item distribute copies digitally or physically;
    \item create derivative works, subject to Section 4.
\end{{itemize}}

2.3 All rights not expressly granted are reserved by the Licensor.

\vspace{{1em}}

\textbf{{3. CONSIDERATION AND PAYMENT TERMS}}

\vspace{{0.5em}}

3.1 License Fee: {data["license_fee"]}

3.2 Payment Schedule: {data["payment_terms"]}

3.3 Taxes: Licensee shall be responsible for applicable taxes.

\vspace{{1em}}

\textbf{{4. USE AND RESTRICTIONS}}

\vspace{{0.5em}}

4.1 Permitted Use: {data["specific_permitted_uses"]}

4.2 Prohibited Use: {data["use_limitations"]}

4.3 Derivative Works require written consent from the Licensor.

4.4 Moral Rights: The Licensor retains the right to be identified as the author.

\vspace{{1em}}

\textbf{{5. OWNERSHIP AND COPYRIGHT PROTECTION}}

\vspace{{0.5em}}

5.1 Ownership: The Licensor retains full ownership.

5.2 Copyright Notice: \textit{{"{data["copyright_notice"]}"}} must be included in all copies.

5.3 Infringement: The Licensee must notify the Licensor of any infringement.

\vspace{{1em}}

\textbf{{6. WARRANTIES AND REPRESENTATIONS}}

\vspace{{0.5em}}

6.1 The Licensor warrants full authority and originality.

6.2 The Licensee warrants compliance with laws.

6.3 No other warranties are implied.

\vspace{{1em}}

\textbf{{7. TERM AND TERMINATION}}

\vspace{{0.5em}}

7.1 Term: {data["term_duration"]}

7.2 Termination for Cause: Either party may terminate with {data["termination_breach_days"]} days notice of a material breach.

7.3 Termination for Convenience: Licensor may terminate with {data["termination_convenience_days"]} days notice.

7.4 Upon termination, Licensee shall cease use and return/destroy all Licensed Works.

\vspace{{1em}}

\textbf{{8. LIMITATION OF LIABILITY}}

\vspace{{0.5em}}

8.1 Neither party is liable for indirect damages.

8.2 Licensor's liability is limited to the License Fee.

\vspace{{1em}}

\textbf{{9. INDEMNIFICATION}}

\vspace{{0.5em}}

9.1 The Licensee indemnifies the Licensor for breaches and misuse.

9.2 The Licensor indemnifies the Licensee against infringement claims.

\vspace{{1em}}

\textbf{{10. CONFIDENTIALITY}}

\vspace{{0.5em}}

10.1 Each party shall protect the other's confidential information.

10.2 Confidentiality obligations include non-disclosure and care.

10.3 Exclusions apply to public domain or independently developed info.

\vspace{{1em}}

\textbf{{11. MISCELLANEOUS}}

\vspace{{0.5em}}

11.1 This Agreement is the full agreement between the parties.

11.2 Amendments must be in writing.

11.3 Waivers must be explicit.

11.4 Invalid clauses do not affect others.

11.5 No assignment without consent, except in corporate transfer.

11.6 Notices must be in writing.

11.7 Governing Law: {data["licensor_jurisdiction"]}

\vspace{{1.5em}}

\textbf{{12. SIGNATURES}}

\vspace{{1em}}

\textbf{{Licensor}}: {data["licensor_name"]} \\
By: \underline{{\hspace{{6cm}}}} \\
Name: {data["licensor_signatory_name"]} \\
Title: {data["licensor_signatory_title"]} \\
Date: {data["licensor_signature_date"]}

\vspace{{2em}}

\textbf{{Licensee}}: {data["licensee_name"]} \\
By: \underline{{\hspace{{6cm}}}} \\
Name: {data["licensee_signatory_name"]} \\
Title: {data["licensee_signatory_title"]} \\
Date: {data["licensee_signature_date"]}

\end{{document}}
"""





# === Step 3: Save to .tex file ===
filename = "COPYRIGHT.tex"
with open(filename, "w", encoding="utf-8") as f:
    f.write(latex_text2)

# === Step 4: Compile LaTeX to PDF ===
subprocess.run(["pdflatex", filename])

# === Step 5: Clean up ===
# aux_files = ["COPYRIGHT.aux", "COPYRIGHT.log"]
# for aux in aux_files:
#     if os.path.exists(aux):
#         os.remove(aux)

print("✅ PDF generated: COPYRIGHT`.pdf")