import subprocess
import os

data = {
    "date": r"\underline{June 1, 2025}",
    "partner1_fullname": r"\underline{Alice Smith}",
    "partner1_company": r"\underline{Alice Co.}",
    "partner1_address": r"\underline{123 Main Street, Springfield, IL}",
    "partner2_fullname": r"\underline{Bob Johnson}",
    "partner2_company": r"\underline{Bob LLC}",
    "partner2_address": r"\underline{456 Elm Avenue, Shelbyville, IL}",
    "purpose": r"\underline{conducting e-commerce business and logistics services}",
    "business_activities": r"\underline{selling consumer products online and managing fulfillment services}",
    "fiscal_year_end": r"\underline{December 31}",
    "jurisdiction": r"\underline{Illinois}",
    "partnership_name": r"\underline{AB E-Commerce Partners}",
    "principal_office": r"\underline{789 Commerce Park, Chicago, IL}",
    "partner1_contribution": r"\underline{50,000 cash}",
    "partner2_contribution": r"\underline{Equipment valued at 50,000}",
    "partner1_ownership": r"\underline{50}",
    "partner2_ownership": r"\underline{50}",
    "partnership_type": r"\underline{general partnership}",
    "meeting_frequency": r"\underline{quarterly}",
    "regular_meeting_notice": r"\underline{7}",
    "special_meeting_notice": r"\underline{3}",
    "withdrawal_notice": r"\underline{30}",
    "state": r"\underline{Illinois}",
    "partner1_name": r"\underline{Alice Smith}",
    "partner1_title": r"\underline{CEO}",
    "partner2_name": r"\underline{Bob Johnson}",
    "partner2_title": r"\underline{Managing Director}",
}

latex_template = rf"""
\documentclass[12pt]{{article}}
\usepackage[margin=1in]{{geometry}}
\usepackage{{setspace}}
\setstretch{{1.15}}
\usepackage{{parskip}}

\begin{{document}}

\section*{{PARTNERSHIP AGREEMENT}}

This Partnership Agreement (hereinafter referred to as the ``Agreement'') is made and entered into on this {data['date']}, by and between:

Partner 1: {data['partner1_fullname']} / {data['partner1_company']}, residing at {data['partner1_address']} (hereinafter referred to as ``Partner 1''), and

Partner 2: {data['partner2_fullname']} / {data['partner2_company']}, residing at {data['partner2_address']} (hereinafter referred to as ``Partner 2'').

The Partners may collectively be referred to as the ``Parties'' and individually as a ``Party.''

WHEREAS, the Parties wish to establish a partnership for the purpose of {data['purpose']};

WHEREAS, the Parties desire to set forth the terms and conditions governing their partnership and their respective rights and obligations in connection therewith;

NOW, THEREFORE, in consideration of the mutual covenants and agreements herein contained, the Parties agree as follows:

\section*{{1. DEFINITIONS}}

1.1 ``Partnership'': The term ``Partnership'' refers to the business relationship created by this Agreement between the Parties.\\

1.2 ``Business'': The term ``Business'' refers to the activities conducted by the Partnership, specifically {data['business_activities']}.\\

1.3 ``Capital Contributions'': The term ``Capital Contributions'' refers to the funds, property, or services contributed by each Partner to the Partnership as specified in Section 3.\\

1.4 ``Profits'' and ``Losses'': The terms ``Profits'' and ``Losses'' refer to the net income or loss of the Partnership as determined by generally accepted accounting principles.\\

1.5 ``Fiscal Year'': The term ``Fiscal Year'' refers to the annual accounting period for the Partnership, which shall end on the {data['fiscal_year_end']} of each year.\\

\section*{{2. FORMATION OF PARTNERSHIP}}

2.1 Partnership Formation: The Parties hereby form a Partnership pursuant to the laws of {data['jurisdiction']} for the purpose of conducting the Business as described herein.\\

2.2 Name of Partnership: The Partnership shall operate under the name {data['partnership_name']}.\\

2.3 Principal Office: The principal office of the Partnership shall be located at {data['principal_office']}. The Partnership may establish additional offices as necessary.\\

\section*{{3. CAPITAL CONTRIBUTIONS}}

3.1 Initial Capital Contributions: Each Partner shall make an initial Capital Contribution to the Partnership as follows:\\
Partner 1: {data['partner1_contribution']}\\
Partner 2: {data['partner2_contribution']}\\

3.2 Additional Contributions: The Partners may agree to make additional Capital Contributions as necessary for the operation of the Partnership. Any additional contributions shall be made in proportion to each Partner’s interest in the Partnership unless otherwise agreed in writing.\\

3.3 Ownership Interest: The ownership interest of each Partner in the Partnership shall be as follows:\\
Partner 1: {data['partner1_ownership']}\\%\\
Partner 2: {data['partner2_ownership']}\\%\\

3.4 Capital Accounts: The Partnership shall maintain a separate capital account for each Partner, reflecting the Partner's Capital Contributions, share of Profits and Losses, and any withdrawals or distributions.\\

\section*{{4. PROFITS AND LOSSES}}

4.1 Allocation of Profits and Losses: Profits and Losses of the Partnership shall be allocated to the Partners in proportion to their respective ownership interests as set forth in Section 3.3.\\

4.2 Distributions: Distributions of cash or property shall be made to the Partners at the discretion of the Partners, subject to the availability of funds and the financial condition of the Partnership.\\

4.3 Tax Treatment: The Partnership shall be treated as a {data['partnership_type']} for tax purposes. Each Partner shall report their share of the Partnership’s Profits and Losses on their individual tax returns in accordance with applicable tax laws.\\

\section*{{5. MANAGEMENT AND OPERATIONS}}

5.1 Management of the Partnership: The Partners shall have equal rights in the management and control of the Partnership. All decisions regarding the Partnership shall require the unanimous consent of the Partners.\\

5.2 Duties of Partners: Each Partner agrees to devote their best efforts to the conduct of the Partnership’s Business and to perform their duties in good faith and in the best interests of the Partnership.\\

5.3 Authority of Partners: No Partner shall have the authority to bind the Partnership in any contract or agreement without the prior written consent of the other Partner(s), except as expressly provided in this Agreement.\\

5.4 Records: The Partnership shall maintain accurate and complete records of its business and financial affairs, including books of account, minutes of meetings, and any other documents related to the Partnership.\\

\section*{{6. MEETINGS}}

6.1 Regular Meetings: The Partners shall meet at least {data['meeting_frequency']} to discuss the affairs of the Partnership. Notice of such meetings shall be provided at least {data['regular_meeting_notice']} days in advance.\\

6.2 Special Meetings: A special meeting may be called by any Partner upon {data['special_meeting_notice']} days' notice to the other Partner(s).\\

6.3 Quorum: A majority of the Partners shall constitute a quorum for the transaction of business at any meeting of the Partners.\\

\section*{{7. WITHDRAWAL AND TERMINATION}}

7.1 Withdrawal: Any Partner may withdraw from the Partnership by providing {data['withdrawal_notice']} days’ written notice to the other Partner(s).\\

7.2 Termination of Partnership: The Partnership shall be dissolved upon the occurrence of any of the following events:\\
a. The agreement of the Partners to dissolve the Partnership;\\
b. The withdrawal of a Partner, unless the remaining Partner(s) elect to continue the Partnership;\\
c. The entry of a decree of judicial dissolution.\\

7.3 Distribution Upon Dissolution: Upon dissolution, the assets of the Partnership shall be distributed in the following order:\\
a. Payment of debts and liabilities of the Partnership;\\
b. Return of Capital Contributions to the Partners;\\
c. Distribution of remaining assets to the Partners in proportion to their respective ownership interests.\\

\section*{{8. CONFIDENTIALITY}}

8.1 Confidential Information: The Parties acknowledge that they may receive or have access to Confidential Information of the other Party in connection with this Agreement. ``Confidential Information'' shall include, but not be limited to, business plans, pricing information, customer lists, and trade secrets.\\

8.2 Obligations of Confidentiality: Each Party agrees to:\\
a. Keep the Confidential Information of the other Party confidential and not disclose it to any third party without the prior written consent of the disclosing Party;\\
b. Use the Confidential Information solely for the purpose of fulfilling its obligations under this Agreement;\\
c. Take all reasonable precautions to protect the confidentiality of the other Party’s Confidential Information.\\

8.3 Exclusions: Confidential Information shall not include information that:\\
a. Was known to the receiving Party prior to disclosure by the disclosing Party;\\
b. Becomes publicly available through no fault of the receiving Party;\\
c. Is disclosed to the receiving Party by a third party who has the right to make such disclosure.\\

\section*{{9. INDEMNIFICATION}}

9.1 Indemnification by Partners: Each Partner agrees to indemnify, defend, and hold harmless the other Partner(s) from and against any and all claims, liabilities, damages, losses, and expenses (including reasonable attorneys' fees) arising from:\\
a. Any breach of this Agreement by the indemnifying Partner;\\
b. The negligent or willful misconduct of the indemnifying Partner in connection with the Partnership.\\

\section*{{10. LIMITATION OF LIABILITY}}

10.1 Limitation of Liability: To the fullest extent permitted by law, neither Party shall be liable to the other Party for any indirect, incidental, consequential, or punitive damages arising out of or in connection with this Agreement, even if advised of the possibility of such damages.\\

10.2 Maximum Liability: The total liability of any Partner under this Agreement shall not exceed the total amount of Capital Contributions made by that Partner.\\

\section*{{11. GOVERNING LAW}}

11.1 Governing Law: This Agreement shall be governed by and construed in accordance with the laws of the State of {data['state']}, without regard to its conflict of laws provisions.\\

\section*{{12. MISCELLANEOUS}}

12.1 Entire Agreement: This Agreement constitutes the entire understanding between the Parties and supersedes all prior agreements, negotiations, and discussions, whether written or oral, regarding the subject matter hereof. Any amendments or modifications must be in writing and signed by both Parties.\\

12.2 Waiver: The failure of either Party to insist upon strict performance of any provision of this Agreement shall not be construed as a waiver of any subsequent breach of the same or any other provision.\\

12.3 Severability: If any provision of this Agreement is held to be invalid or unenforceable by a court of competent jurisdiction, the remaining provisions shall remain in full force and effect.\\

12.4 Assignment: Neither Party may assign or transfer any rights or obligations under this Agreement without the prior written consent of the other Party.\\

\section*{{13. SIGNATURES}}

IN WITNESS WHEREOF, the Parties have executed this Partnership Agreement as of the date first above written.\\

Partner 1:\\
{data['partner1_name']}\\
By: \rule{{6cm}}{{0.4pt}}\\
Name: {data['partner1_name']}\\
Title: {data['partner1_title']}\\
Date: {data['date']}\\

\vspace{{2em}}

Partner 2:\\
{data['partner2_name']}\\
By: \rule{{6cm}}{{0.4pt}}\\
Name: {data['partner2_name']}\\
Title: {data['partner2_title']}\\
Date: {data['date']}\\

\end{{document}}
"""




# === Step 3: Save to .tex file ===
filename = "partnership_agreement.tex"
with open(filename, "w", encoding="utf-8") as f:
    f.write(latex_template)

# === Step 4: Compile LaTeX to PDF ===
subprocess.run(["pdflatex", filename])

# === Step 5: Clean up ===
aux_files = ["partnership_agreement.aux", "partnership_agreement.log"]
for aux in aux_files:
    if os.path.exists(aux):
        os.remove(aux)

print("✅ PDF generated: partnership_agreement.pdf")