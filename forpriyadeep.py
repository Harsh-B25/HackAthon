import os
import subprocess

# === Step 1: Collect user input ===
# title = input("Enter the document title: ")
# author = input("Enter your name: ")
# intro = input("Write a short introduction: ")
# main_content = input("Write the main content (e.g., topics or list items): ")
# conclusion = input("Write a short conclusion: ")

# === Step 2: Define LaTeX content with user input ===
# latex_content = rf"""
# \documentclass{{article}}
# \usepackage[utf8]{{inputenc}}

# \title{{{title}}}
# \author{{{author}}}
# \date{{\today}}

# \begin{{document}}

# \maketitle

# \section{{Introduction}}
# {intro}

# \section{{Main Content}}
# {main_content}

# \section{{Conclusion}}
# {conclusion}

# \end{{document}}
# """
latex_content = r"""\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[a4paper, margin=1in]{geometry}
\usepackage{setspace}
\usepackage{enumitem}

\setstretch{1.5}

\title{\textbf{Rent Agreement}}
\date{}
\begin{document}

\maketitle

This Rent Agreement is made on \textbf{\today}, between:

\textbf{Landlord:} Mr./Ms. \underline{\hspace{8cm}}\\
Address: \underline{\hspace{12cm}}

\textbf{AND}

\textbf{Tenant:} Mr./Ms. \underline{\hspace{8cm}}\\
Address: \underline{\hspace{12cm}}

\section*{1. Property}
The landlord agrees to rent out the property located at:\\
\underline{\hspace{16cm}}

\section*{2. Term}
The rental term shall begin on \underline{\hspace{5cm}} and end on \underline{\hspace{5cm}}, unless terminated earlier according to this agreement.

\section*{3. Rent}
The monthly rent shall be Rs. \underline{\hspace{3cm}} payable on or before the 5\textsuperscript{th} day of each month.

\section*{4. Security Deposit}
The tenant shall pay a refundable security deposit of Rs. \underline{\hspace{3cm}} at the time of signing this agreement.

\section*{5. Maintenance and Utilities}
\begin{itemize}[noitemsep]
    \item The tenant shall keep the premises clean and in good condition.
    \item Utilities (electricity, water, etc.) shall be paid by the tenant unless otherwise agreed.
\end{itemize}

\section*{6. Termination}
Either party may terminate this agreement by giving \underline{\hspace{3cm}} days’ written notice.

\section*{7. Governing Law}
This agreement shall be governed by the laws of the State of \underline{\hspace{5cm}}.

\vspace{2cm}

\noindent
\textbf{Landlord Signature:} \underline{\hspace{7cm}} \hfill Date: \underline{\hspace{2.5cm}}\\[1cm]
\textbf{Tenant Signature:} \underline{\hspace{7cm}} \hfill Date: \underline{\hspace{2.5cm}}

\end{document} 
"""

# === Step 3: Save to .tex file ===
filename = "custom_document.tex"
with open(filename, "w", encoding="utf-8") as f:
    f.write(latex_content)

# === Step 4: Compile LaTeX to PDF ===
subprocess.run(["pdflatex", filename])

# === Step 5: Clean up ===
aux_files = ["custom_document.aux", "custom_document.log"]
for aux in aux_files:
    if os.path.exists(aux):
        os.remove(aux)

print("✅ PDF generated: custom_document.pdf")
