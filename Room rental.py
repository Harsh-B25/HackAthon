import os
import subprocess
from datetime import datetime

# === Step 1: User Data ===
data = {
    "landlord_name": r"\underline{Ravi Kumar}",
    "landlord_address": r"\underline{22 Park Street, Delhi, India}",
    "tenant_name": r"\underline{Anjali Mehra}",
    "tenant_address": r"\underline{Flat 402, Lakeview Apartments, Mumbai}",
    "property_address": r"\underline{Plot 9, Green Valley, Pune}",
    "start_date": r"\underline{July 1, 2025}",
    "end_date": r"\underline{June 30, 2026}",
    "monthly_rent": r"\underline{Rs. 20,000}",
    "security_deposit": r"\underline{Rs. 40,000}",
    "notice_period": r"\underline{30}",
    "state_law": r"\underline{Maharashtra}",
    "landlord_signature_date": r"\underline{June 6, 2025}",
    "tenant_signature_date": r"\underline{June 6, 2025}"
}

# === Step 2: LaTeX Template ===
latex_content = rf"""\documentclass[12pt]{{article}}
\usepackage[utf8]{{inputenc}}
\usepackage[a4paper, margin=1in]{{geometry}}
\usepackage{{setspace}}
\usepackage{{enumitem}}

\setstretch{{1.5}}

\title{{\textbf{{Rent Agreement}}}}
\date{{\today}}
\begin{{document}}

\maketitle

This Rent Agreement is made on \textbf{{\today}}, between:

\textbf{{Landlord:}} Mr./Ms. {data["landlord_name"]} \\
Address: {data["landlord_address"]}

\textbf{{AND}}

\textbf{{Tenant:}} Mr./Ms. {data["tenant_name"]} \\
Address: {data["tenant_address"]}

\section*{{1. Property}}
The landlord agrees to rent out the property located at:\\
{data["property_address"]}

\section*{{2. Term}}
The rental term shall begin on {data["start_date"]} and end on {data["end_date"]}, unless terminated earlier according to this agreement.

\section*{{3. Rent}}
The monthly rent shall be {data["monthly_rent"]} payable on or before the 5\textsuperscript{{th}} day of each month.

\section*{{4. Security Deposit}}
The tenant shall pay a refundable security deposit of {data["security_deposit"]} at the time of signing this agreement.

\section*{{5. Maintenance and Utilities}}
\begin{{itemize}}[noitemsep]
    \item The tenant shall keep the premises clean and in good condition.
    \item Utilities (electricity, water, etc.) shall be paid by the tenant unless otherwise agreed.
\end{{itemize}}

\section*{{6. Termination}}
Either party may terminate this agreement by giving {data["notice_period"]} days’ written notice.

\section*{{7. Governing Law}}
This agreement shall be governed by the laws of the State of {data["state_law"]}.

\vspace{{2cm}}

\noindent
\textbf{{Landlord Signature:}} \underline{{\hspace{{7cm}}}} \hfill Date: {data["landlord_signature_date"]} \\[1cm]
\textbf{{Tenant Signature:}} \underline{{\hspace{{7cm}}}} \hfill Date: {data["tenant_signature_date"]}

\end{{document}}
"""

# === Step 3: Save LaTeX File ===
filename = "RENT_AGREEMENT.tex"
with open(filename, "w", encoding="utf-8") as f:
    f.write(latex_content)

# === Step 4: Compile LaTeX to PDF ===
subprocess.run(["pdflatex", filename])

# === Step 5: Clean Up Temp Files ===
for ext in [".aux", ".log"]:
    path = filename.replace(".tex", ext)
    if os.path.exists(path):
        os.remove(path)

print("✅ PDF generated: RENT_AGREEMENT.pdf")
