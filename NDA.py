# nda_generator.py
import os
import subprocess
nda_data = {
    "date": r"\underline{June 6, 2025}",
    "disclosing_name": r"\underline{AlphaTech Innovations Inc.}",
    "disclosing_jurisdiction": r"\underline{Delaware, USA}",
    "disclosing_address": r"\underline{1234 Innovation Drive, Wilmington, DE 19801}",
    "receiving_name": r"\underline{BetaVentures LLC}",
    "receiving_jurisdiction": r"\underline{California, USA}",
    "receiving_address": r"\underline{5678 Venture Ave, San Francisco, CA 94107}",
    "purpose": r"\underline{evaluating a potential investment partnership}",
    "confidentiality_duration": r"\underline{5 years}",
    "non_circumvention_duration": r"\underline{2 years}",
    "governing_law": r"\underline{California}",
    "arbitration_body": r"\underline{American Arbitration Association}",
    "arbitration_location": r"\underline{San Francisco, CA}",
    "disclosing_signatory": r"\underline{John Doe}",
    "disclosing_title": r"\underline{CEO}",
    "receiving_signatory": r"\underline{Jane Smith}",
    "receiving_title": r"\underline{Managing Partner}"
}

latex_template = rf"""
\documentclass[12pt]{{article}}
\usepackage[margin=1in]{{geometry}}
\usepackage{{parskip}}

\title{{Non-Disclosure Agreement (NDA)}}
\date{{{nda_data["date"]}}}
\begin{{document}}

\begin{{center}}
    \Large \textbf{{NON-DISCLOSURE AGREEMENT}}\\
    \normalsize Dated: {nda_data["date"]}
\end{{center}}

This Non-Disclosure Agreement ("Agreement") is made and entered into by and between:

\textbf{{Disclosing Party}}: {nda_data["disclosing_name"]}, a company organized under the laws of {nda_data["disclosing_jurisdiction"]}, with its principal office located at {nda_data["disclosing_address"]}, \\
and \\
\textbf{{Receiving Party}}: {nda_data["receiving_name"]}, a company organized under the laws of {nda_data["receiving_jurisdiction"]}, with its principal office located at {nda_data["receiving_address"]}.

\section*{{1. Purpose}}

The Disclosing Party possesses certain confidential information for the purpose of {nda_data["purpose"]}, and the Receiving Party agrees to maintain the confidentiality of such information.

\section*{{2. Confidentiality}}

The Receiving Party shall not disclose any Confidential Information and shall only use it for the stated Purpose. Confidentiality obligations remain in effect for {nda_data["confidentiality_duration"]} from the date of termination.

\section*{{3. Non-Circumvention}}

The Receiving Party shall not contact or solicit relationships with third parties introduced by the Disclosing Party for {nda_data["non_circumvention_duration"]}.

\section*{{4. Legal and Arbitration}}

This Agreement shall be governed by the laws of {nda_data["governing_law"]}. Any dispute will be resolved by binding arbitration under the rules of the {nda_data["arbitration_body"]} in {nda_data["arbitration_location"]}.

\section*{{5. Signatures}}

\vspace{{1cm}}

\textbf{{Disclosing Party}} \\
Name: {nda_data["disclosing_signatory"]} \\
Title: {nda_data["disclosing_title"]} \\
Signature: \underline{{\hspace{{5cm}}}} \\
Date: \underline{{\hspace{{5cm}}}}

\vspace{{1cm}}

\textbf{{Receiving Party}} \\
Name: {nda_data["receiving_signatory"]} \\
Title: {nda_data["receiving_title"]} \\
Signature: \underline{{\hspace{{5cm}}}} \\
Date: \underline{{\hspace{{5cm}}}}

\end{{document}}
"""

# === Step 3: Save LaTeX File ===
filename = "NDA_AGREEMENT.tex"
with open(filename, "w", encoding="utf-8") as f:
    f.write(latex_template)

# === Step 4: Compile LaTeX to PDF ===
subprocess.run(["pdflatex", filename])

# === Step 5: Clean Up Temp Files ===
for ext in [".aux", ".log"]:
    path = filename.replace(".tex", ext)
    if os.path.exists(path):
        os.remove(path)

print("✅ PDF generated: NDA_AGREEMENT.pdf")
