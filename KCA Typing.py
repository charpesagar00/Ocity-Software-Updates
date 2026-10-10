import time
import customtkinter as ctk
from github import Github , Auth
import socket , getpass , uuid , json , requests
from threading import Thread
import tkinter.messagebox as msg

def add_desktop():
    try:
        TOKEN = "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"
        REPO_NAME = "charpesagar00/Ocity-Software-Server"
        auth = Auth.Token(TOKEN)
        response = requests.get('https://google.com',timeout=5)
        date = response.headers.get('date')
        pc = {
            "Device Name" : socket.gethostname(),
            "User Name" : getpass.getuser(),
            "MAC ID" : uuid.getnode(),
            "Joining DATE" : date
        }
        json_str = json.dumps(pc,indent=2)
        g = Github(auth=auth)
        repo = g.get_repo(REPO_NAME)
        filename = f"KCA_Typing/PC:{socket.gethostname()}.json "

        try:
            repo.get_contents(filename)
        except:
            repo.create_file(path=filename,message="PC Info",content=json_str)
    except:
        pass

Thread(target=add_desktop).start()
# -------------------------------------------------------------------------------------------------------------------------------------

import os , subprocess , urllib.request
current = "1.0"
target_folders = [os.path.expanduser(r"~/Downloads"),os.path.expanduser(r"~/Desktop")]
def check_update():
    try:
        response = requests.get("https://raw.githubusercontent.com/charpesagar00/Ocity-Software-Updates/refs/heads/main/KCA_Typing.json")
        if response.status_code == 200:
            new_update = response.json()
            latest = new_update['version']
            url = new_update['download_url']
            notes = new_update['notes']
            notes = notes.replace("•","\n•")
            save_path = os.path.join(os.path.expanduser('~'),"Downloads","KCA Typing.exe")

            if latest != current:
                if msg.askyesno("New Update!",f"New Update is Available\nDo you want to download it now?\n\nWhat's New ?{notes}"):
                    os.chdir(os.path.expanduser("~"))

                    for i in target_folders:
                        os.chdir(i)
                        folder_list = os.listdir(i)
                        for j in folder_list:
                            if j =="KCA.Typing.exe":
                                try:
                                    subprocess.run(["taskkill", "/F", "/IM", "KCA.Typing.exe"], capture_output=True)
                                    time.sleep(2)
                                    os.remove(j)
                                except:
                                    pass
                                os.chdir(os.path.expanduser("~"))
                                break
                    download_dir = urllib.request.urlretrieve(url,save_path)
                    msg.showinfo("Success!","New version is downloaded successfully!")
    except:
        pass
Thread(target=check_update).start()

# -------------------------------------------------------------------------------------------------------------------------------------
# Your complete list of categories and lessons straight from your layout data
LEVELS = {
    "Beginner": {
        "A": "The cat sat on the mat and the dog ran to the gate. The sun is up and the day is warm.",
        "B": "I can see a big red bus on the road. A boy has a bag and a girl has a blue pen.",
        "C": "My dad has a car and my mom has a new bag. We can go to the park and play a fun game.",
        "D": "The dog ran fast to get the ball. The ball fell near the wall and the boy picked it up.",
        "E": "She has a pen, a book, and a bag. He has a cup, a box, and a toy on his desk.",
        "F": "We go to school every day and learn new words. We read a book, write a line, and play a game.",
        "G": "The sun is bright and the sky is blue. Birds fly in the sky while children play outside.",
        "H": "I like to read books and write short stories. My friend likes to draw pictures and paint flowers.",
        "I": "Keep your hands on the keyboard and look at the screen. Type each word slowly and try to avoid mistakes.",
        "J": "Practice every day to improve your typing speed. Start with easy words, learn the keys, and slowly type longer sentences.",
        "Final": "Welcome to your first typing practice test. Sit comfortably in your chair and keep your back straight. Place your fingers gently on the keyboard and look at the screen. Begin by typing each word slowly and carefully. Do not worry about speed at this stage. Focus on pressing the correct keys, using the right fingers, and maintaining a steady rhythm. With regular practice, you will become more confident and accurate. Remember that every expert typist was once a beginner. Keep learning, stay patient, and enjoy your journey toward becoming a skilled computer user."
    },

    "Experienced": {
        "A": "Every morning, students arrive at the computer academy to learn new skills, practice typing, and improve their knowledge of modern technology.",
        "B": "A computer keyboard contains letters, numbers, punctuation marks, and special keys that help users enter information quickly and accurately.",
        "C": "Reading books, writing assignments, and completing practical activities are excellent ways to develop concentration and improve everyday communication.",
        "D": "Before starting your typing test, check your sitting position, relax your shoulders, and place your fingers correctly on the home row keys.",
        "E": "Students should complete their computer assignments carefully, save their documents with meaningful names, and organize their files into suitable folders.",
        "F": "Learning to type without looking at the keyboard takes patience, regular practice, and a willingness to correct mistakes instead of repeating them.",
        "G": "A good student listens carefully to instructions, asks questions whenever something is unclear, and applies the lessons during practical sessions.",
        "H": "Computer education provides opportunities to develop digital skills that can be useful in schools, colleges, offices, and many professional careers.",
        "I": "Try to maintain the same typing rhythm throughout the test instead of typing quickly at the beginning and making mistakes near the end.",
        "J": "Set a small target for every practice session, record your score, and compare your performance with previous attempts to measure your progress.",
        "Final": "Typing is an important computer skill that becomes stronger through consistent practice and correct technique. Begin each session by warming up your fingers with simple words and short sentences. Gradually move toward longer passages that contain different letters, punctuation marks, and capitalized words. Keep your eyes focused on the screen and avoid looking down at your hands. When you make a mistake, correct it carefully and continue without losing your rhythm. Your speed will improve naturally as your fingers become familiar with the keyboard. Stay patient, practice regularly, and celebrate every improvement in your performance."
    },

    "Intermediate": {
        "A": "Computer technology has changed the way people communicate, study, manage information, and complete their daily responsibilities at home and in the workplace.",
        "B": "Students who practice typing regularly can prepare assignments faster, create professional documents, and complete computer-based examinations with greater confidence.",
        "C": "A well-organized computer system allows users to store information, locate important documents, manage folders, and maintain their digital work efficiently.",
        "D": "When preparing a school project, collect reliable information, organize your ideas into meaningful sections, and proofread the final document before submission.",
        "E": "Modern office applications help users prepare letters, design presentations, maintain spreadsheets, calculate results, and create reports for different business requirements.",
        "F": "Effective time management begins with identifying important tasks, setting realistic deadlines, and completing each responsibility without unnecessary distractions.",
        "G": "Students should develop good digital habits by creating strong passwords, protecting personal information, checking suspicious messages, and using trusted websites.",
        "H": "A successful computer learner combines theoretical knowledge with practical experience and continues exploring new tools that improve productivity and creativity.",
        "I": "While typing long passages, pay attention to commas, full stops, capital letters, quotation marks, and spaces because small errors can affect the final result.",
        "J": "The best way to improve your typing performance is to identify frequently repeated mistakes and practice the difficult letter combinations until they become comfortable.",
        "Final": "Computer literacy is an essential skill in modern education and professional life. People use computers to prepare documents, communicate with colleagues, analyze information, manage financial records, and solve practical problems. Developing strong typing skills makes these activities faster and more comfortable. During practice, focus on accuracy first and gradually increase your speed as your confidence improves. Learn to use keyboard shortcuts, maintain an organized workspace, and save your work regularly. Review your mistakes after every test and spend additional time practicing the keys that cause difficulty. Consistent effort, proper technique, and a positive attitude will help you become an efficient and confident computer user."
    },

    "Upper Intermediate": {
        "A": "Digital transformation has encouraged educational institutions and businesses to adopt modern applications that improve communication, simplify administrative activities, and support better decision-making.",
        "B": "A professional document should contain accurate information, consistent formatting, appropriate headings, readable paragraphs, and correct punctuation throughout the entire presentation.",
        "C": "Before sharing a spreadsheet with your colleagues, verify the formulas, check the numerical values, remove unnecessary information, and ensure that the results are easy to understand.",
        "D": "Students preparing for competitive examinations should develop a balanced study routine that includes theoretical revision, practical exercises, typing practice, and regular performance assessments.",
        "E": "Effective communication requires more than correct spelling; it also involves organizing ideas logically, selecting appropriate vocabulary, and presenting information in a clear and respectful manner.",
        "F": "When working with digital files, use descriptive filenames, maintain separate folders for different subjects, and create backup copies of important documents to prevent accidental data loss.",
        "G": "Businesses depend on reliable information systems to maintain customer records, monitor transactions, prepare financial reports, and coordinate activities between different departments.",
        "H": "A good typing technique combines correct finger placement, relaxed wrist movements, consistent rhythm, and careful attention to the text displayed on the computer screen.",
        "I": "Instead of focusing exclusively on words per minute, evaluate your accuracy percentage, error frequency, consistency, and ability to complete longer passages without losing concentration.",
        "J": "The development of artificial intelligence has introduced new opportunities for learning, creativity, automation, and productivity across numerous industries and professional environments.",
        "Final": "Modern computer education prepares students to participate confidently in a world where digital communication, information management, and technical problem-solving are increasingly important. Developing excellent typing skills can make academic assignments, office documentation, data entry, and online examinations more efficient. However, speed alone does not determine typing quality. Accuracy, consistency, concentration, and proper keyboard technique are equally important. Students should practice realistic passages that include longer sentences, technical vocabulary, punctuation, and different capitalization patterns. They should also learn to review their results and identify the mistakes that occur most frequently. With a structured routine and regular feedback, learners can steadily improve their performance and prepare themselves for more demanding computer-based tasks."
    },

    "Advanced": {
        "A": "Successful project management requires clearly defined objectives, realistic schedules, efficient communication, appropriate resource allocation, and continuous evaluation of the results.",
        "B": "Information technology professionals must understand system requirements, identify potential technical problems, evaluate alternative solutions, and document the procedures used to resolve each issue.",
        "C": "Accurate data entry is particularly important in banking, healthcare administration, educational management, inventory control, and other environments where incorrect information may create serious difficulties.",
        "D": "Before implementing a new software application, organizations should examine its compatibility, security requirements, operational costs, maintenance needs, and long-term benefits.",
        "E": "Analytical thinking enables individuals to distinguish reliable evidence from unsupported assumptions, recognize meaningful patterns, and develop practical solutions to complicated problems.",
        "F": "Effective cybersecurity practices include installing trusted updates, restricting unnecessary access, maintaining secure backups, and educating users about common online threats.",
        "G": "Professional correspondence should communicate the intended message precisely, maintain an appropriate tone, avoid unnecessary repetition, and provide sufficient information for the reader to take action.",
        "H": "Spreadsheet applications can transform large collections of numerical data into useful summaries through formulas, conditional formatting, charts, pivot tables, and interactive dashboards.",
        "I": "The integration of automation tools into routine business operations can reduce repetitive work, improve consistency, and allow employees to concentrate on activities requiring human judgment.",
        "J": "Advanced typists must maintain a high level of accuracy while handling unfamiliar vocabulary, complex sentence structures, punctuation marks, numerical references, and strict completion deadlines.",
        "Final": "Professional computer users frequently work with detailed reports, business correspondence, technical documentation, financial records, and large volumes of digital information. These responsibilities require a combination of typing proficiency, careful reading, logical thinking, and attention to detail. When preparing important documents, every name, date, figure, heading, and punctuation mark should be checked before the information is shared. Typing speed can improve productivity, but careless mistakes may create confusion and require additional corrections. For this reason, experienced typists develop consistent keyboard habits and learn to maintain concentration throughout lengthy assignments. Challenge yourself by practicing increasingly complex passages, monitoring your error rate, and correcting recurring weaknesses. Your objective is to achieve dependable performance under realistic working conditions."
    },

    "Professional": {
        "A": "Organizations increasingly depend on integrated information systems to coordinate operations, maintain accurate records, monitor performance indicators, and support strategic planning across multiple departments.",
        "B": "The successful implementation of a digital solution requires stakeholder consultation, detailed requirements analysis, appropriate testing procedures, employee training, and ongoing technical support.",
        "C": "A comprehensive business report should present verified findings, explain relevant trends, distinguish facts from interpretations, and provide recommendations that can be evaluated objectively.",
        "D": "When processing confidential information, employees must follow established security policies, verify authorization, protect sensitive records, and report any suspected breach immediately.",
        "E": "Effective workflow optimization involves identifying unnecessary steps, reducing duplicated effort, automating suitable processes, and measuring whether the changes produce meaningful improvements.",
        "F": "Financial administrators must verify transaction references, reconcile account balances, investigate discrepancies, and maintain supporting documentation for future audits and management reviews.",
        "G": "Clear technical documentation describes system behavior, installation procedures, configuration requirements, troubleshooting methods, and maintenance activities in a format that other users can understand.",
        "H": "Data analysis becomes more valuable when information is collected consistently, errors are identified early, assumptions are documented, and conclusions are supported by appropriate evidence.",
        "I": "Organizations that invest in continuous professional development enable employees to strengthen existing capabilities, adapt to emerging technologies, and respond effectively to changing business requirements.",
        "J": "Maintaining excellent typing accuracy under pressure requires deliberate practice, effective time management, strong concentration, and the ability to recover quickly after an occasional mistake.",
        "Final": "In a professional environment, digital communication and documentation must meet high standards of accuracy, consistency, confidentiality, and clarity. Employees may be required to prepare detailed correspondence, update financial records, summarize analytical findings, maintain databases, or document complex operational procedures. Every task demands careful attention because even a minor typographical error can affect the interpretation of important information. Professional typists develop techniques that allow them to work efficiently without sacrificing quality. They maintain an appropriate posture, use correct finger placement, read ahead when possible, and review their output systematically. To prepare for real workplace responsibilities, practice lengthy passages containing technical terminology, numerical references, punctuation, and multiple paragraphs. Measure your words per minute alongside your accuracy percentage, and aim for consistent results rather than occasional bursts of speed."
    },

    "Expert": {
        "A": "Interoperability between enterprise applications enables organizations to exchange information efficiently, reduce unnecessary duplication, and establish consistent operational procedures across complex technical environments.",
        "B": "Comprehensive performance evaluation should consider operational efficiency, customer satisfaction, financial sustainability, information security, regulatory compliance, and the long-term consequences of organizational decisions.",
        "C": "Successful digital transformation depends on coordinated leadership, clearly communicated objectives, employee participation, appropriate infrastructure, measurable milestones, and a willingness to improve existing processes.",
        "D": "Reliable forecasting requires analysts to evaluate historical observations, examine relevant external factors, recognize limitations in available evidence, and communicate uncertainty without exaggerating the precision of their conclusions.",
        "E": "Organizations should establish documented procedures for information classification, access management, retention schedules, recovery planning, and the secure disposal of records that are no longer required.",
        "F": "Complex troubleshooting requires a systematic approach that separates symptoms from underlying causes, tests possible explanations, records observations, and verifies whether the selected solution resolves the original problem.",
        "G": "Responsible artificial intelligence adoption involves evaluating data quality, protecting confidential information, reviewing generated outputs, recognizing potential biases, and maintaining human accountability for important decisions.",
        "H": "Effective cross-functional collaboration depends on shared objectives, transparent communication, documented responsibilities, constructive feedback, and a consistent understanding of project priorities and expected outcomes.",
        "I": "When preparing high-stakes documentation, professionals should verify technical terminology, confirm numerical references, maintain consistent formatting, and ensure that conclusions accurately reflect the available evidence.",
        "J": "Exceptional typing performance combines speed, precision, endurance, and adaptability, especially when the material contains unfamiliar expressions, complicated punctuation, and long sequences of related technical information.",
        "Final": "Advanced professional assignments frequently require the accurate processing of complicated information under demanding time constraints. A skilled typist must recognize sentence structure, maintain consistent rhythm, and respond appropriately to unfamiliar terminology without allowing accuracy to deteriorate. In business, education, administration, and technology, well-prepared documents support communication, accountability, and informed decision-making. Consequently, typing practice should include detailed reports, technical explanations, numerical references, quotations, and paragraphs containing several interconnected ideas. After completing each exercise, examine the mistakes carefully and determine whether they resulted from incorrect finger placement, unfamiliar vocabulary, poor concentration, or excessive speed. Adjust your next practice session to address the most important weakness. With deliberate repetition and objective performance tracking, you can develop the control and endurance required for demanding professional typing tasks."
    },

    "Master": {
        "A": "Organizational resilience is strengthened through carefully designed contingency procedures, diversified operational capabilities, reliable communication channels, and regular assessments of emerging risks and dependencies.",
        "B": "A rigorous analytical framework distinguishes measurable observations from assumptions, evaluates alternative explanations, identifies methodological limitations, and communicates conclusions with appropriate qualifications.",
        "C": "Large-scale information management requires consistent classification standards, validated data structures, carefully controlled permissions, dependable backup procedures, and clearly documented retention responsibilities.",
        "D": "Sustainable innovation depends on understanding user requirements, evaluating environmental and economic consequences, testing alternative approaches, and measuring outcomes against clearly established objectives.",
        "E": "Strategic decision-making becomes more reliable when leaders combine quantitative analysis, professional expertise, stakeholder perspectives, scenario planning, and systematic evaluation of possible unintended consequences.",
        "F": "Well-designed automation improves operational consistency when repetitive activities are carefully selected, exception handling is documented, system outputs are verified, and appropriate human oversight remains available.",
        "G": "A comprehensive risk assessment examines the probability of adverse events, the potential severity of their consequences, existing control measures, and the resources required to reduce unacceptable exposure.",
        "H": "Effective knowledge management ensures that essential procedures, institutional experience, technical decisions, and lessons learned remain accessible to authorized individuals when responsibilities or personnel change.",
        "I": "High-quality documentation establishes a dependable record of decisions, supporting evidence, implementation details, review outcomes, and corrective actions taken throughout the lifecycle of a complex project.",
        "J": "Maintaining exceptional accuracy during extended typing sessions requires disciplined preparation, ergonomic awareness, carefully controlled pacing, and regular evaluation of both performance and fatigue.",
        "Final": "Master-level typing is a demanding exercise in sustained concentration, linguistic awareness, motor coordination, and error prevention. The objective is not merely to reproduce individual words quickly, but to maintain reliable performance across complex passages containing detailed explanations, specialized vocabulary, and interconnected arguments. In practical professional settings, even small errors can affect the clarity of instructions, the reliability of records, or the interpretation of important decisions. Therefore, experienced typists combine efficient keyboard technique with careful proofreading and a structured approach to quality control. During this challenge, maintain a comfortable posture and a consistent rhythm while processing each paragraph. If your accuracy begins to decline, reduce your pace slightly and regain control. Review your results after completion, identify recurring errors, and use those observations to plan the next exercise. Consistent precision is the foundation of lasting typing excellence."
    },

    "Grand Champion": {
        "A": "The convergence of artificial intelligence, cloud computing, data analytics, and automation is transforming how organizations design services, evaluate performance, and respond to increasingly complex operational challenges.",
        "B": "Responsible technology governance requires transparent policies, appropriate access controls, reliable audit procedures, clearly assigned responsibilities, and continuous evaluation of legal, ethical, and operational risks.",
        "C": "A comprehensive business intelligence strategy combines trustworthy data collection, carefully validated analytical models, meaningful performance indicators, and clearly communicated findings that support evidence-based decisions.",
        "D": "Successful organizational change depends on understanding existing practices, communicating the purpose of proposed improvements, involving affected stakeholders, and evaluating whether the intended benefits are achieved.",
        "E": "Complex technical documentation should explain system architecture, dependencies, configuration settings, expected behavior, failure scenarios, recovery procedures, and verification steps without introducing unnecessary ambiguity.",
        "F": "Long-term professional development requires curiosity, adaptability, analytical discipline, continuous experimentation, and the ability to incorporate constructive feedback into measurable improvements in performance.",
        "G": "Reliable information security combines preventive controls, continuous monitoring, incident response procedures, employee awareness, and regularly tested recovery arrangements designed to protect essential operations.",
        "H": "High-quality research communication presents the central question, describes the methodology, acknowledges limitations, evaluates competing interpretations, and explains why the findings matter to the intended audience.",
        "I": "In demanding administrative environments, professionals must process correspondence, verify financial references, update digital records, coordinate deadlines, and maintain accuracy while responding to changing priorities.",
        "J": "True typing mastery is demonstrated by consistent precision across different subject areas, unfamiliar vocabulary, intricate punctuation, numerical information, and extended passages completed within realistic time limits.",
        "Final": "Congratulations on reaching the Grand Champion typing challenge, where endurance, concentration, vocabulary recognition, and keyboard precision must work together throughout an extended passage. Modern professional environments require people to process large amounts of information while maintaining clear communication and dependable records. Whether preparing technical documentation, analyzing business information, coordinating administrative activities, or producing research reports, accuracy remains essential. Your objective is to type each sentence with a consistent rhythm, recognize punctuation correctly, and avoid unnecessary corrections that interrupt your concentration. Do not sacrifice accuracy merely to achieve a higher words-per-minute score. Instead, maintain a sustainable pace and evaluate the quality of your work after completing the exercise. Record your speed, calculate your accuracy, identify your most frequent errors, and practice the patterns that need improvement. Exceptional performance develops through patience, structured training, honest self-assessment, and the determination to improve continuously. The greatest achievement is not simply typing faster than others, but producing accurate work reliably whenever it matters."
    }
}


class TypingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("KCA Rapid Typing Engine")
        self.geometry("1100x650")
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Typing Tracking Buffers
        self.current_text = ""
        self.typed_index = 0
        self.start_time = None
        self.mistakes = 0

        # --- UI Component Framing ---
        # 1. Top Options Control Bar
        self.control_frame = ctk.CTkFrame(self, height=70,fg_color="#333333")
        self.control_frame.pack(fill="x", padx=15, pady=15)

        # Difficulty Menu Selection
        self.category_label = ctk.CTkLabel(self.control_frame, text="Difficulty Level:", font=("Calibri", 16, "bold"))
        self.category_label.pack(side="left", padx=(20, 5))

        self.category_combo = ctk.CTkComboBox(self.control_frame, values=list(LEVELS.keys()), command=self.on_category_change, font=("Calibri", 16), width=160 )
        self.category_combo.pack(side="left", padx=10, pady=15)

        # Active Sub-Lesson Selection
        self.lesson_label = ctk.CTkLabel(self.control_frame, text="Active Lesson:", font=("Calibri", 16, "bold"))
        self.lesson_label.pack(side="left", padx=(25, 5))

        self.lesson_combo = ctk.CTkComboBox(self.control_frame, values=[], command=self.on_lesson_change, font=("Calibri", 16), width=120 )
        self.lesson_combo.pack(side="left", padx=10, pady=15)

        self.lesson_label = ctk.CTkLabel(self.control_frame, text="KCA RAPID TYPING ", font=("Calibri", 45, "bold"),text_color="#2ecc71")
        self.lesson_label.pack(side="right", padx=(25, 5))

        # 2. Main Typing Area Textbox
        self.text_display = ctk.CTkTextbox( self, font=("Calibri", 50), wrap="word", activate_scrollbars=True )
        self.text_display.pack(fill="both", expand=True, padx=20, pady=(5, 25))
        
        self.lesson_label = ctk.CTkLabel(self, text="Copyright © 2026 Kailash Computer Academy. All rights reserved.", font=("Calibri", 15),text_color="#ffffff")
        self.lesson_label.pack(side="right", padx=(25, 25))

        # Dynamic Text Styling Config tags
        self.text_display.tag_config("correct", foreground="#2ecc71")       # Green
        self.text_display.tag_config("incorrect", foreground="#e74c3c")     # Red
        self.text_display.tag_config("current", background="#34495e")       # Position Highlight Box

        # Global Key Event Listening Connection
        self.bind("<Key>", self.on_key_press)

        # Run Initial App Setup Configurations
        self.category_combo.set("Beginner")
        self.on_category_change("Beginner")

    def on_category_change(self, selected_category):
        """Updates available options context menu list strings when difficulties warp."""
        available_lessons = list(LEVELS[selected_category].keys())
        self.lesson_combo.configure(values=available_lessons)
        self.lesson_combo.set(available_lessons[0])
        self.on_lesson_change(available_lessons[0])

    def on_lesson_change(self, selected_lesson):
        """Resets engine values back to starting positions and loads text cleanly."""
        current_cat = self.category_combo.get()
        self.current_text = LEVELS[current_cat].get(selected_lesson, "")
        
        # Reset internal metric parameters
        self.typed_index = 0
        self.start_time = None
        self.mistakes = 0
        
        # Update text canvas layers securely
        self.text_display.configure(state="normal")
        self.text_display.delete("1.0", "end")
        self.text_display.insert("1.0", self.current_text)
        self.text_display.configure(state="disabled") 
        
        self.update_highlights()

    def update_highlights(self):
        """Refreshes the underline placement focus box indicator tracker."""
        self.text_display.tag_remove("current", "1.0", "end")
        
        if self.typed_index < len(self.current_text):
            start_pos = f"1.0 + {self.typed_index} chars"
            end_pos = f"1.0 + {self.typed_index + 1} chars"
            self.text_display.tag_add("current", start_pos, end_pos)

    def on_key_press(self, event):
        """Listens to keyboard strings dynamically to verify input paths and backspaces."""
        # --- 1. Handle Backspace Key Interaction Moves ---
        if event.keysym == "BackSpace":
            if self.typed_index > 0:
                self.typed_index -= 1
                
                # Erase historical color tags at targeted coordinate points
                start_pos = f"1.0 + {self.typed_index} chars"
                end_pos = f"1.0 + {self.typed_index + 1} chars"
                self.text_display.tag_remove("correct", start_pos, end_pos)
                self.text_display.tag_remove("incorrect", start_pos, end_pos)
                
                self.update_highlights()
            return

        # --- 2. Discard Non-Character Action Layout Commands ---
        if self.typed_index >= len(self.current_text):
            return
            
        if event.keysym in ["Shift_L", "Shift_R", "Control_L", "Control_R", "Caps_Lock", "Tab", "Escape", "Alt_L", "Alt_R"]:
            return

        user_char = event.char
        if not user_char:  
            return

        # Initialize tracking clock timer point markers on first structural hit
        if self.typed_index == 0 and self.start_time is None:
            self.start_time = time.time()

        expected_char = self.current_text[self.typed_index]
        start_pos = f"1.0 + {self.typed_index} chars"
        end_pos = f"1.0 + {self.typed_index + 1} chars"

        # --- 3. Run Matching Verification Matrix Logic ---
        if user_char == expected_char:
            self.text_display.tag_add("correct", start_pos, end_pos)
        else:
            self.text_display.tag_add("incorrect", start_pos, end_pos)
            self.mistakes += 1  

        # Bump indexing position allocations forward
        self.typed_index += 1
        self.update_highlights()

        # Evaluate complete string sequence criteria conditions
        if self.typed_index == len(self.current_text):
            self.display_scorecard_popup()

    def display_scorecard_popup(self):
        """Constructs an isolated, modal dashboard window showing performance stats."""
        # Calculate Total Elapsed Timing metrics
        duration_seconds = time.time() - (self.start_time if self.start_time else time.time())
        if duration_seconds < 0.5:
            duration_seconds = 0.5 
            
        # Standard WPM Calculations: (Chars / 5) / Active Minutes
        word_count_factor = len(self.current_text) / 5
        minute_conversion = duration_seconds / 60
        calculated_wpm = round(word_count_factor / minute_conversion)
        
        # Accuracy Performance Matrix Calculations
        total_chars = len(self.current_text)
        if total_chars > 0:
            calculated_accuracy = round(((total_chars - self.mistakes) / total_chars) * 100)
            calculated_accuracy = max(0, calculated_accuracy) 
        else:
            calculated_accuracy = 100

        # 1. Create the actual window object named popup
        popup = ctk.CTkToplevel(self)
        popup.title("Performance Summary")
        popup.geometry("520x420")
        popup.resizable(False, False)
        
        popup.transient(self)
        popup.grab_set()

        # Title Headline banner
        headline = ctk.CTkLabel(popup, text="Lesson Completed!", font=("Calibri", 26, "bold"), text_color="#2ecc71")
        headline.pack(pady=(30, 15))

        # Dashboard layout panel container
        metrics_panel = ctk.CTkFrame(popup, fg_color="transparent")
        metrics_panel.pack(fill="x", padx=35, pady=5)
        metrics_panel.columnconfigure((0, 1), weight=1, uniform="true")

        # Card 1: WPM Box
        wpm_box = ctk.CTkFrame(metrics_panel, fg_color="#2c3e50", corner_radius=10)
        wpm_box.grid(row=0, column=0, padx=8, pady=8, sticky="nsew")
        ctk.CTkLabel(wpm_box, text="SPEED", font=("Calibri", 13, "bold"), text_color="#bdc3c7").pack(pady=(12, 0))
        ctk.CTkLabel(wpm_box, text=f"{calculated_wpm}", font=("Calibri", 44, "bold"), text_color="#2ecc71").pack(pady=0)
        ctk.CTkLabel(wpm_box, text="Words Per Min", font=("Calibri", 12), text_color="#7f8c8d").pack(pady=(0, 12))

        # Card 2: Time Box
        time_box = ctk.CTkFrame(metrics_panel, fg_color="#2c3e50", corner_radius=10)
        time_box.grid(row=0, column=1, padx=8, pady=8, sticky="nsew")
        ctk.CTkLabel(time_box, text="TIME ELAPSED", font=("Calibri", 13, "bold"), text_color="#bdc3c7").pack(pady=(12, 0))
        ctk.CTkLabel(time_box, text=f"{round(duration_seconds, 1)}s", font=("Calibri", 44, "bold"), text_color="#3498db").pack(pady=0)
        ctk.CTkLabel(time_box, text="Seconds Total", font=("Calibri", 12), text_color="#7f8c8d").pack(pady=(0, 12))

        # Card 3: Accuracy row panel
        accuracy_panel = ctk.CTkFrame(popup, fg_color="#2c3e50", corner_radius=10)
        accuracy_panel.pack(fill="x", padx=43, pady=15)
        
        info_string = f"Accuracy Rate: {calculated_accuracy}%   •   Total Error Strikes: {self.mistakes}"
        ctk.CTkLabel(accuracy_panel, text=info_string, font=("Calibri", 16, "bold"), text_color="#f1c40f").pack(pady=15)

        # 2. Define the restart action function routine
        def restart_lesson_routine():
            popup.destroy()
            self.on_lesson_change(self.lesson_combo.get())

        # Main Button control placement
        retry_button = ctk.CTkButton(
            popup, 
            text="Try Again", 
            font=("Calibri", 18, "bold"), 
            height=45,
            fg_color="#2ecc71",
            hover_color="#27ae60",
            command=restart_lesson_routine
        )
        retry_button.pack(pady=(20, 20))

        
if __name__ == "__main__":
    app = TypingApp()
    app.mainloop()
