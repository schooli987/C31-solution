from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.core.window import Window
class StudentApp(App):
    def build(self):
         
        self.root_panel = TabbedPanel(do_default_tab=False)
         # Set each tab's width to 50% of the window width
        self.root_panel.tab_width = Window.width / 2

        # --- Form Tab ---
        registration_tab = TabbedPanelItem(text='Student Registration')
        self.form_layout = self.build_form_screen()
        registration_tab.add_widget(self.form_layout)
        self.root_panel.add_widget( registration_tab)

        # --- View Tab ---
        view_tab = TabbedPanelItem(text='View Students')
        self.view_layout = self.build_view_screen()
        view_tab.add_widget(self.view_layout)
        self.root_panel.add_widget(view_tab)

        return self.root_panel

    def build_form_screen(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # --- Form Inputs ---
        form = GridLayout(cols=2, spacing=10, row_force_default=True, row_default_height=40)

        self.name_input = TextInput()
        self.age_input = TextInput(input_filter='int')
        self.gender_spinner = Spinner(text='Select', values=['Male', 'Female'])
        self.class_input = TextInput()
        self.address_input = TextInput()

        form.add_widget(Label(text="Name:"))
        form.add_widget(self.name_input)
        form.add_widget(Label(text="Age:"))
        form.add_widget(self.age_input)
        form.add_widget(Label(text="Gender:"))
        form.add_widget(self.gender_spinner)
        form.add_widget(Label(text="Class/Grade:"))
        form.add_widget(self.class_input)
        form.add_widget(Label(text="Address:"))
        form.add_widget(self.address_input)
        layout.add_widget(form)

        layout.add_widget(Label(text="Select Subjects:", size_hint_y=None, height=30))
       
       
  
        grid_layout = GridLayout(cols=2,padding=[400,0,400,0])
        self.cb_math = CheckBox()
        lb_math = Label(text="Math")
        grid_layout.add_widget(self.cb_math)
        grid_layout.add_widget(lb_math)

        self.cb_english = CheckBox()
        lb_english = Label(text="English")
        grid_layout.add_widget(self.cb_english)
        grid_layout.add_widget(lb_english)

        self.cb_science = CheckBox()
        lb_science = Label(text="Science")  
        grid_layout.add_widget(self.cb_science)
        grid_layout.add_widget(lb_science)

        self.cb_computer = CheckBox()
        lb_computer = Label(text="Computer")
        grid_layout.add_widget(self.cb_computer)
        grid_layout.add_widget(lb_computer)


        layout.add_widget(grid_layout)
       
        
        # --- Buttons & Status ---
        self.status_label = Label(text="", font_size=16, size_hint_y=None, height=40, markup=True)
        submit_btn = Button(text="Submit", size_hint_y=None, height=50,on_press=self.submit_data)
       
       
        layout.add_widget(submit_btn)
        layout.add_widget(self.status_label)

        
        return layout
    def build_view_screen(self):
                print("View Screen")

                
    def submit_data(self, instance):
       
        name = self.name_input.text.strip()
        age = self.age_input.text.strip()
        gender = self.gender_spinner.text
        class_grade = self.class_input.text.strip()
        address = self.address_input.text.strip()
        selected_subjects=[]
        if self.cb_math.active:
            selected_subjects.append("Math")
        if self.cb_english.active:
            selected_subjects.append("English")
        if self.cb_science.active:
            selected_subjects.append("Science")
        if self.cb_computer.active:
            selected_subjects.append("Computer")


        if not name or not age or gender == 'Select' or not class_grade or not address or not selected_subjects:
            self.status_label.text = "Please fill in all fields"

        else:
            try:
                with open("students.txt", "a") as f:
                    line = f"{name},{age},{gender},{class_grade},{address},{','.join(selected_subjects)}\n"
                    f.write(line)
                self.status_label.text = f"Thank you, {name}! Your data was saved."
                self.clear_form()
            except:
                self.status_label.text = f"Error"
    def clear_form(self):
        self.name_input.text = ""
        self.age_input.text = ""
        self.gender_spinner.text = "Select"
        self.class_input.text = ""
        self.address_input.text = ""
        self.cb_math.active = False
        self.cb_english.active = False
        self.cb_science.active = False
        self.cb_computer.active = False 
    
    def load_students(self, instance=None):
        self.cards_container.clear_widgets()
        try:
            with open("students.txt", "r") as f:
                for line in f:
                    card = self.create_student_card(line)
                    self.cards_container.add_widget(card)
        except:
            self.cards_container.add_widget(Label(text="No data found."))
    
    def create_student_card(self, line):
        name, age, gender, grade, address, subjects = line.strip().split(",", 5)
        card = BoxLayout(orientation='vertical', padding=10, size_hint_y=None, height=140)
        card.add_widget(Label(text=f"Name: {name}"))
        card.add_widget(Label(text=f"Age:{age}, Gender: {gender}"))
        card.add_widget(Label(text=f"Grade: {grade}"))
        card.add_widget(Label(text=f"Address: {address}"))
        card.add_widget(Label(text=f"Subjects: {subjects}"))
        return card

        

if __name__ == '__main__':
    StudentApp().run()
