# Rewriting the full LaTeX version of the contract using the full content from the updated PDF.
# We'll inject user-supplied values into the LaTeX document without summarizing any sections.

# Sample user data for placeholder substitution
import os
import subprocess
data = {
    "intern_full_name": r"\underline{Harsh Bansal}",
    "intern_address": r"\underline{123 Intern Street, Cityville, State, 12345}",
    "company_name": r"\underline{InnovateX Technologies Pvt. Ltd.}",
    "company_address": r"\underline{456 Corporate Blvd, Metro City, State, 67890}",
    "internship_field": r"\underline{Software Development}",
    "intern_tasks": r"\underline{bug fixing, feature development, and code reviews}",
    "industry_skills": r"\underline{version control systems, Agile development, software testing}",
    "start_date": r"\underline{June 15, 2025}",
    "end_date": r"\underline{August 30, 2025}",
    "hours_per_week": r"\underline{20}",
    "is_paid": r"\underline{paid}",
    "stipend_or_wage": r"\underline{INR 15,000 per month}",
    "payment_frequency": r"\underline{monthly}",
    "termination_notice_period": r"\underline{7}",
    "representative_name": r"\underline{Jane Smith}",
    "representative_title": r"\underline{HR Manager}",
    "signature_date_company": r"\underline{June 10, 2025}",
    "signature_date_intern": r"\underline{June 10, 2025}"
}

# Full LaTeX content preserving the contract structure
latex_content = rf"""\documentclass[12pt]{{article}}
\usepackage[utf8]{{inputenc}}
\usepackage[a4paper, margin=1in]{{geometry}}
\usepackage{{enumitem}}
\setlength\parindent{{0pt}}

\title{{\textbf{{Internship Contract Agreement}}}}
\date{{}}
\begin{{document}}
\maketitle

This Internship Agreement (“Agreement”) is made and entered into as of the date of signing by and between: \\\\

Intern’s Name: {data["intern_full_name"]}  \\\\
Intern’s Address: {data["intern_address"]} \\\\
(Hereinafter referred to as “Intern”) \\\\

and \\\\

Company’s Name: {data["company_name"]} \\\\
Company’s Address: {data["company_address"]} \\\\
(Hereinafter referred to as “Company”) \\\\

This Agreement sets forth the terms and conditions under which the Intern will participate in an internship program at the Company.

\section*{{1. Purpose and Scope of Internship}}
The Company agrees to offer the Intern an internship position, which is intended to provide a valuable learning experience. The purpose of the internship is for the Intern to gain hands-on experience in the field of {data["internship_field"]}, including but not limited to the following tasks and responsibilities:

\begin{{itemize}}[noitemsep]
    \item Assisting with {data["intern_tasks"]}.
    \item Participating in team meetings and collaborating with team members.
    \item Learning about {data["industry_skills"]}.
    \item Performing administrative or clerical duties as necessary.
\end{{itemize}}

\section*{{2. Internship Duration and Schedule}}
The internship will commence on {data["start_date"]} and will conclude on {data["end_date"]}, unless terminated earlier in accordance with the terms of this Agreement. The Intern agrees to work a minimum of {data["hours_per_week"]} hours per week during the internship period.

\section*{{3. Compensation}}
This internship is a {data["is_paid"]} position. In the case of a paid internship, the Intern will receive a stipend or hourly wage of {data["stipend_or_wage"]} paid on a {data["payment_frequency"]} basis.

\begin{{itemize}}[noitemsep]
    \item Academic credit (if applicable).
    \item Access to resources and networking opportunities.
    \item The opportunity to gain practical experience in the field.
    \item A letter of recommendation upon successful completion of the internship.
\end{{itemize}}

The Intern acknowledges that the internship is not an employment relationship, and no other benefits, such as health insurance, paid leave, or retirement benefits, will be provided.

\section*{{4. Confidentiality and Non-Disclosure}}
The Intern acknowledges that during the internship, they may have access to confidential or proprietary information belonging to the Company. The Intern agrees to:
\begin{{itemize}}[noitemsep]
    \item Maintain the confidentiality of all confidential and proprietary information received during the course of the internship.
    \item Not disclose such information to any third party without the prior written consent of the Company.
    \item Use the confidential information solely for the purpose of performing their duties during the internship.
\end{{itemize}}

This confidentiality obligation extends beyond the termination or conclusion of the internship and will remain in effect for as long as the information remains confidential and proprietary.

\section*{{5. Intellectual Property}}
Any work product, inventions, designs, discoveries, ideas, or other creations developed or contributed by the Intern during the internship (hereinafter referred to as “Work Product”) shall be the exclusive property of the Company. The Intern agrees to assign any and all rights, titles, and interests in such Work Product to the Company, including the right to use, modify, and distribute the Work Product without compensation to the Intern.

\section*{{6. Supervision and Mentorship}}
The Company agrees to provide the Intern with appropriate supervision and mentorship. The Company will designate a supervisor or mentor who will be responsible for guiding the Intern throughout the internship. The supervisor will provide feedback on the Intern’s performance, assist with learning opportunities, and ensure that the Intern is gaining the skills and knowledge necessary for their professional development.

\section*{{7. Expectations and Responsibilities}}
The Intern agrees to:
\begin{{itemize}}[noitemsep]
    \item Perform their duties to the best of their ability and in a professional manner.
    \item Maintain punctuality and adhere to the agreed-upon internship schedule.
    \item Follow the policies and procedures of the Company, including workplace rules, dress code, and any applicable safety protocols.
    \item Communicate effectively with their supervisor and team members.
    \item Complete any required documentation, reports, or projects assigned during the internship.
    \item Participate in meetings, training, and other activities as required.
\end{{itemize}}

The Company agrees to:
\begin{{itemize}}[noitemsep]
    \item Provide the Intern with meaningful work experience.
    \item Offer a supportive learning environment.
    \item Provide clear instructions and expectations regarding the Intern’s tasks.
    \item Ensure that the Intern receives constructive feedback on their performance.
    \item Offer opportunities for the Intern to engage with employees and gain exposure to various aspects of the company.
\end{{itemize}}

\section*{{8. Professional Conduct and Ethics}}
The Intern agrees to uphold professional standards of conduct during the internship. This includes treating all Company employees, clients, and partners with respect and professionalism, refraining from discriminatory, harassing, or unethical behavior, and acting in accordance with the Company’s code of conduct and workplace policies.

The Intern acknowledges that any breach of these standards, including violations of Company policy, could result in the immediate termination of the internship.

\section*{{9. Termination of Internship}}
Either party may terminate the internship at any time, with or without cause, by providing written notice to the other party.

If the Intern decides to terminate the internship, the Intern will provide the Company with a notice of at least {data["termination_notice_period"]} days before the termination date.

\section*{{10. Health and Safety}}
The Company will ensure that the workplace complies with applicable health and safety laws and regulations. The Intern agrees to:
\begin{{itemize}}[noitemsep]
    \item Follow all safety guidelines and procedures established by the Company.
    \item Immediately report any health or safety concerns to their supervisor or the designated health and safety officer.
    \item Be mindful of their own health and safety while performing internship duties.
\end{{itemize}}

The Intern acknowledges that the Company is not responsible for any injuries or illnesses that occur during the internship unless such injuries or illnesses are caused by the Company’s negligence.

\section*{{11. No Employment Relationship}}
The Intern acknowledges and agrees that this internship does not constitute an employment relationship, and that the Intern is not entitled to any of the rights or benefits afforded to employees of the Company, including but not limited to health insurance, paid time off, or other benefits typically associated with employment. This internship is intended solely for educational purposes.

\section*{{12. Miscellaneous Provisions}}
\begin{{itemize}}[noitemsep]
    \item \textbf{{Entire Agreement}}: This Agreement constitutes the entire understanding between the parties with respect to the internship and supersedes any prior discussions, understandings, or agreements between the parties, whether oral or written.
    \item \textbf{{Amendments}}: This Agreement may be amended only by written agreement signed by both the Company and the Intern.
    \item \textbf{{Severability}}: If any provision of this Agreement is found to be invalid or unenforceable, the remaining provisions shall continue in full force and effect.
    \item \textbf{{Assignment}}: The Company may assign or transfer its rights and obligations under this Agreement to any affiliate or successor entity, but the Intern may not assign this Agreement without the prior written consent of the Company.
    \item \textbf{{Waiver}}: No waiver of any provision of this Agreement shall be deemed to be a further or continuing waiver of such provision or any other provision.
\end{{itemize}}

\section*{{13. Acknowledgment and Acceptance}}

\textbf{{Company Representative:}} \\
Name: {data["representative_name"]} \\
Title: {data["representative_title"]} \\
Signature: \underline{{\hspace{{6cm}}}} \hfill Date: {data["signature_date_company"]} \\\\

\textbf{{Intern:}} \\
Name: {data["intern_full_name"]} \\
Signature: \underline{{\hspace{{6cm}}}} \hfill Date: {data["signature_date_intern"]}

\end{{document}}
"""

# # Save LaTeX to .tex file
# tex_path = "/mnt/data/internship_full_contract.tex"
# with open(tex_path, "w", encoding="utf-8") as f:
#     f.write(latex_full)

# tex_path


# === Step 3: Save to .tex file ===
filename = "INTERNSHIP.tex"
with open(filename, "w", encoding="utf-8") as f:
    f.write(latex_content)

# === Step 4: Compile LaTeX to PDF ===
subprocess.run(["pdflatex", filename])

# === Step 5: Clean up ===
aux_files = ["INTERNSHIP.aux", "INTERNSHIP.log"]
for aux in aux_files:
    if os.path.exists(aux):
        os.remove(aux)

print("✅ PDF generated: INTERNSHIP.pdf")