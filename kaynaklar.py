"""Rules for Robots — sources outside the recording (kayıt dışı kaynaklar).
Only primary sources are used for constitutional text, court decisions, laws, executive orders and regulations. Each one was opened and
read on 2026-10-08; the 'dogrulama' line says what was checked. A law or an order can change after that date: in the lessons its status
is given 'as of 8 October 2026'.
  SOURCES  : id -> yazar (author), yil (year), baslik (title), yer (where), dogrulama (how it was verified)
  TEXT     : short passages quoted on the screen, copied from the National Archives transcription
  TABLES   : the data tables used in the course"""

SOURCES = dict(
    ced=dict(
        yazar="College Board", yil=2026,
        baslik="AP U.S. Government and Politics Course and Exam Description, Effective Fall 2026 (Course Framework V.1)",
        yer="https://apcentral.collegeboard.org/media/pdf/ap-us-government-and-politics-course-and-exam-description.pdf",
        dogrulama="PDF (202 pages) downloaded and read. Units and weights: Unit 1 Foundations of American Democracy 15–22%, Unit 2 "
                  "Interactions Among Branches of Government 25–36%, Unit 3 Civil Liberties and Civil Rights 13–18%, Unit 4 American "
                  "Political Ideologies and Beliefs 10–15%, Unit 5 Political Participation 20–27%. Topic titles 1.1–5.13 copied into "
                  "planlama/harita.py. Required foundational documents and the 14 required Supreme Court cases read from pages 25 and 29–30. "
                  "Free-response types: Concept Application, Quantitative Analysis, SCOTUS Comparison, Argument Essay. House 435 and "
                  "Senate 100 members: EK 2.1.A.2. Cell-phone searches and bulk metadata: EK 3.8.A. Margin of error: EK 4.5.A.2."),
    constitution=dict(
        yazar="National Archives and Records Administration", yil=None,
        baslik="The Constitution of the United States: A Transcription", yer="https://www.archives.gov/founding-docs/constitution-transcript",
        dogrulama="Page opened; Article I Sections 1 and 7, Article II Section 1, Article III Section 1 and Article VI read."),
    bill_of_rights=dict(
        yazar="National Archives and Records Administration", yil=None,
        baslik="The Bill of Rights: A Transcription", yer="https://www.archives.gov/founding-docs/bill-of-rights-transcript",
        dogrulama="Page opened; First, Fourth and Tenth Amendments read."),
    carpenter=dict(
        yazar="Supreme Court of the United States", yil=2018, baslik="Carpenter v. United States, No. 16-402, slip opinion",
        yer="https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf",
        dogrulama="PDF read. Argued November 29, 2017, decided June 22, 2018. Syllabus: 12,898 location points over 127 days, an average "
                  "of 101 per day. Held: the Government's acquisition of the cell-site records was a Fourth Amendment search."),
    riley=dict(
        yazar="Supreme Court of the United States", yil=2014, baslik="Riley v. California, No. 13-132 (docket) and Oyez case summary",
        yer="https://www.supremecourt.gov/docketfiles/13-132.htm · https://api.oyez.org/cases/2013/13-132",
        dogrulama="Docket read: decided Jun 25 2014, judgment reversed and remanded, opinion by Roberts, C. J. for eight justices, Alito, J. "
                  "concurring in part and in the judgment. Oyez conclusion: police generally need a warrant to search digital data on a "
                  "phone seized at arrest. The slip-opinion PDF link could not be opened (404); the holding is taken from Oyez."),
    take_it_down=dict(
        yazar="U.S. Government Publishing Office", yil=2025,
        baslik="Public Law 119-12, TAKE IT DOWN Act (S. 146), 139 Stat. 55", yer="https://www.govinfo.gov/content/pkg/PLAW-119publ12/html/PLAW-119publ12.htm",
        dogrulama="Text read. Approved May 19, 2025. Legislative history: passed Senate Feb. 13, 2025, passed House Apr. 28, 2025. "
                  "Covered platforms must remove a reported depiction within 48 hours; enforcement under the Federal Trade Commission Act. "
                  "Vote counts were not checked and are not used. congress.gov could not be opened (403)."),
    eo14110=dict(
        yazar="Federal Register", yil=2023, baslik="Executive Order 14110, Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence, 88 FR 75191",
        yer="https://www.federalregister.gov/documents/2023/11/01/2023-24283/safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence",
        dogrulama="Federal Register API: signing date 2023-10-30, citation 88 FR 75191."),
    eo14148=dict(
        yazar="Federal Register", yil=2025, baslik="Executive Order 14148, Initial Rescissions of Harmful Executive Orders and Actions, 90 FR 8237",
        yer="https://www.federalregister.gov/documents/2025/01/28/2025-01901/initial-rescissions-of-harmful-executive-orders-and-actions",
        dogrulama="Federal Register API: signing date 2025-01-20. That it revoked Executive Order 14110 is stated in Sec. 1 of "
                  "Executive Order 14365 ('I revoked my predecessor's attempt...') — the list inside 14148 itself was not read line by line."),
    eo14179=dict(
        yazar="Federal Register", yil=2025, baslik="Executive Order 14179, Removing Barriers to American Leadership in Artificial Intelligence, 90 FR 8741",
        yer="https://www.federalregister.gov/api/v1/documents.json?conditions[executive_order_numbers][]=14179",
        dogrulama="Federal Register API: signing date 2025-01-23, citation 90 FR 8741."),
    eo14365=dict(
        yazar="Federal Register", yil=2025, baslik="Executive Order 14365, Ensuring a National Policy Framework for Artificial Intelligence, 90 FR 58499",
        yer="https://www.federalregister.gov/documents/full_text/text/2025/12/16/2025-23092.txt",
        dogrulama="Full text read. Signed December 11, 2025. Sec. 3 AI Litigation Task Force within 30 days; Sec. 4 evaluation of state "
                  "AI laws within 90 days; Sec. 5 funding conditions; Sec. 6 FCC proceeding; Sec. 7 FTC policy statement; Sec. 8 legislative "
                  "recommendation for a federal framework that preempts conflicting state AI laws, with stated exceptions (child safety, "
                  "compute and data-center infrastructure, state procurement). Whether the deadlines were met was NOT checked."),
    apa553=dict(
        yazar="U.S. Government Publishing Office", yil=2023, baslik="5 U.S.C. 553, Rule making (United States Code, 2023 edition)",
        yer="https://www.govinfo.gov/content/pkg/USCODE-2023-title5/html/USCODE-2023-title5-partI-chap5-subchapII-sec553.htm",
        dogrulama="Text read: notice of proposed rule making in the Federal Register; interested persons may submit written data, views, "
                  "or arguments; a substantive rule is published not less than 30 days before its effective date, with exceptions."),
    eu_ai_act=dict(
        yazar="European Parliament and Council of the European Union", yil=2024,
        baslik="Regulation (EU) 2024/1689 (Artificial Intelligence Act), original text", yer="https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689",
        dogrulama="Original text read on EUR-Lex. Done at Brussels, 13 June 2024. Article 113: applies from 2 August 2026; Chapters I and II "
                  "from 2 February 2025; Article 6(1) from 2 August 2027. Article 5: prohibited AI practices. Recitals: risk-based approach. "
                  "Later amendments to these dates, if any, were NOT checked: the lesson says 'in the original text'."),
)

TEXT = dict(
    supremacy="This Constitution, and the Laws of the United States which shall be made in Pursuance thereof ... shall be the supreme Law of the Land",
    tenth="The powers not delegated to the United States by the Constitution, nor prohibited by it to the States, are reserved to the States respectively, or to the people.",
    fourth="The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated",
    first="Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press",
)

TABLES = dict(
    recording=dict(dosya="veri/cay_servisi_kaydi.csv",
                   aciklama="simulation recording: time, four joint angles of the right arm (rad), elbow velocity (rad/s), cup position x, y, z (m); "
                            "50 samples per second; not a measurement of a real robot. Used only as an example of the data a robot produces."),
)
