Final Project - Automated Student Feedback Generator
----------------------------------------------------

1. Create a Python program that automatically generates personalised feedback for students based on a digital scoring system that conforms to the example at end of doc.
2. The program must generate one text file per student, timestamped(YYYYMMDD_HHMMSS), and then also produce a timestamped ZIP archive.

Functional Requirements
-----------------------

Your program must:

- Maintain a student list
- Students can be hardcoded or manually inputed
- Collect scores (1–4) for each student across:
    - Overall performance
    - General understanding
    - Contribution level
    - Lab completion
    - Punctuality
    - Engagement
    - Further study level

3. Use mapping dictionaries to convert scores to feedback phrases
eg:
    performance_map = {
    1: "performed at a basic level.",
    2: "performed satisfactorily.",
    3: "performed well throughout.",
    4: "performed at an excellent standard!"
    }   

4. Apply mappings inside a feedback template under the headers "General comments", "punctuality", 
    and "Further Study".
eg:
    template = f"General Comments\n {student_name} did {x[{score}]} in this module.../n/n"
    template += f"Puctualiuty/n ...../n/n"

5. Get python to make a new directory and save one file per student inside it.

6. Automatically open each feedback file after saving for manual editing. (Notepad if windows)

7. Zip all feedback files into a timestamped archive in its own directory.

Code Quality
------------
Modularity - Use functions for mapping, template creation, writing files, zipping
Naming - Descriptive function + variable names
Comments & Docstrings - Explain why, not just what
Maintainability - Avoid duplication, keep template clean


Optional Stretch:
Use coloured CLI output + good formatting.

Marking guide
-------------
Functional features working	-- 40%
Mapping + Template design quality -- 20%
Feedback readability -- 20%
ZIP + Timestamps -- 10%
CLI formatting -- 10%


project/
│
├── feedback/
│   ├── Alice_20250317_103455_feedback.txt
│   ├── Bob_20250317_103456_feedback.txt
│   └── Mark_20250317_103457_feedback.txt
│
└── feedback_archive/
    └── feedback_20250317_103458.zip

MUST BE A SINGLE PYTHON SCRIPT WITH NO EXTERNAL DEPENDANCIES!!!

Deadline: 12.30 

example finished feedback: 

General comments
Mark did well in this module. He demonstrated a good understanding of concepts we 
covered and showed he has a broad knowledgebase. 
He contributed to discussions and asked relevant questions. 

Learner Punctuality and engagement 
Mark was punctual throughout the module and engaged well through Webex. 

Recommendations on further learning
Continue to practice the basics of containerisation, Kubernetes and pipelines.

- EMAIL when finished!! 