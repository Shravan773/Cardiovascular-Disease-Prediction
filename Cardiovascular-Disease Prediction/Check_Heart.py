import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from joblib import load
from fpdf import FPDF
import os

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = int((screen_width - width) / 2)
    y_coordinate = int((screen_height - height) / 2)

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

def generate_pdf_report(report_text, username, age, sex, chest_pain, trestbps, chol, fbs, rest_ecg, thalach, ex_ang, old_peak, slope, ca, thal,text_color):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.rect(5.0,5.0, 200.0, 278.0)  # Adjust the dimensions as needed

    # Set position for content inside the rectangle
    # pdf.set_xy(margin + 5, margin + 5)
    # Define column widths and heights for better organization
    col_width = 60
    col_height = 8

    pdf.set_font("Arial", style='B', size=18)  # Bold and increased font size for the title
    pdf.cell(0, 10, txt=f"Patient Report for {username}", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.set_draw_color(0, 0, 0)  # Set color to black
    pdf.line(10, pdf.get_y(), 200 - 10, pdf.get_y())  # Reset font to normal for rest of the content
    pdf.cell(0, 10, txt="", ln=True) 

    # Write patient information

    
    pdf.cell(col_width, col_height, txt="Age:", ln=False)
    pdf.cell(col_width, col_height, txt=age, ln=True)
    pdf.cell(col_width, col_height, txt="Sex:", ln=False)
    pdf.cell(col_width, col_height, txt='Female' if sex == '0' else 'Male', ln=True)
    pdf.cell(col_width, col_height, txt="Chest Pain:", ln=False)
    pdf.cell(col_width, col_height, txt='Typical' if chest_pain == '1' else 'Asymptomatic' if chest_pain == '2' else 'Non-typical', ln=True)
    pdf.cell(col_width, col_height, txt="Trestbps:", ln=False)
    pdf.cell(col_width, col_height, txt=f"{trestbps} mm Hg", ln=True)
    pdf.cell(col_width, col_height, txt="Chol:", ln=False)
    pdf.cell(col_width, col_height, txt=f"{chol} mg/dl", ln=True)
    pdf.cell(col_width, col_height, txt="FBS:", ln=False)
    pdf.cell(col_width, col_height, txt='True' if fbs == '1' else 'False', ln=True)
    pdf.cell(col_width, col_height, txt="RestECG:", ln=False)
    pdf.cell(col_width, col_height, txt='Normal' if rest_ecg == '0' else 'Having ST-T wave abnormality' if rest_ecg == '1' else 'Showing probable or definite left ventricular hypertrophy', ln=True)
    pdf.cell(col_width, col_height, txt="Thalach:", ln=False)
    pdf.cell(col_width, col_height, txt=str(thalach), ln=True)
    pdf.cell(col_width, col_height, txt="ExANG:", ln=False)
    pdf.cell(col_width, col_height, txt='Yes' if ex_ang == '1' else 'No', ln=True)
    pdf.cell(col_width, col_height, txt="Old Peak:", ln=False)
    pdf.cell(col_width, col_height, txt=str(old_peak), ln=True)
    pdf.cell(col_width, col_height, txt="Slope:", ln=False)
    pdf.cell(col_width, col_height, txt='Fixed' if slope == '1' else 'Normal' if slope == '2' else 'Reversible', ln=True)
    pdf.cell(col_width, col_height, txt="Ca:", ln=False)
    pdf.cell(col_width, col_height, txt=str(ca), ln=True)
    pdf.cell(col_width, col_height, txt="Thal:", ln=False)
    pdf.cell(col_width, col_height, txt='Fixed' if thal == '1' else 'Normal' if thal == '2' else 'Reversible' if thal == '3' else 'Asymptomatic', ln=True)

    # Add conclusions
    pdf.cell(0, 10, txt="", ln=True) 
    pdf.set_font("Arial", size=14,style='B')
    pdf.cell(col_width * 3, col_height, txt="\nConclusions:", ln=True)
    pdf.set_font("Arial", size=12)

    conclusions = []
    if int(age) > 50:
        conclusions.append("Your age is above 50, which may increase the risk of heart disease. Ensure regular check-ups and maintain a healthy lifestyle to mitigate risks.")
    if float(chol) > 200:
        conclusions.append("Your cholesterol level is higher than the normal range (200 mg/dl). To reduce cholesterol, consider a low-cholesterol diet, regular exercise, and medication if prescribed by your doctor.")
    if fbs == '1':
        conclusions.append("Your fasting blood sugar level is higher than normal. Control sugar intake, exercise regularly, and consult your doctor for further evaluation.")

    # Add each conclusion line by line
    for conclusion in conclusions:
        pdf.multi_cell(col_width * 3, col_height, txt=conclusion)
    
    # pdf.set_font("Arial", size=14,style='B')
    # pdf.cell(col_width * 3, col_height, txt="Report:", ln=True)
    # pdf.set_font("Arial", size=14)


    if text_color == 'red':
        pdf.set_text_color(255, 0, 0)  # Red color
    elif text_color == 'green':
        pdf.set_text_color(0, 128, 0)  # Green color

    # Add report text
    pdf.multi_cell(col_width * 3, col_height, txt=report_text,align='C')

    # Save PDF file
    folder_path = "patient-report"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    pdf_filename = os.path.join(folder_path, f"{username}_Report.pdf")
    pdf.output(pdf_filename)
    return pdf_filename



def open_pdf_file(pdf_filename):
    os.startfile(pdf_filename)

def Train():
    def Detect():
        # Check if all fields are filled except for Sex
        empty_fields = [index for index, entry_var in enumerate(entry_vars) if index != 2 and entry_var.get() == ""]
        if empty_fields:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        numeric_fields = [1, 2, 4, 5, 8, 10, 11]
        for index in numeric_fields:
            value = entry_vars[index].get()
            try:
                float(value)
            except ValueError:
                messagebox.showerror("Error", f"Invalid input in field '{labels[index]}'. Please enter a numeric value.")
                return

        valid_values = {
            2: ["0", "1"],
            6: ["0", "1"],
            7: ["0", "1", "2"],
            9: ["0", "1"],
            12: ["0", "1", "2", "3"]
        }
        for index, value in valid_values.items():
            if entry_vars[index].get() not in value:
                messagebox.showerror("Error", f"Invalid input in field '{labels[index]}'. Please enter a valid value.")
                return

        model = load('HEART_DISEASE_MODEL.joblib')

        inputs = [entry_var.get() for entry_var in entry_vars[1:]]  # Exclude username

        prediction = model.predict([inputs])[0]

        username = entry_vars[0].get()
        username = entry_vars[0].get()
        if prediction == 1:
            result_text = "Abnormality Detected! Report is Generated"
            result_color = "red"
            report_text = "\n As per input data Heart Abnormality Detected."
            text_color = 'red'
        else:
            result_text = "No Abnormality Detected. Report is Generated"
            result_color = "green"
            report_text = "\n As per input data No Heart Disease Detected\n\nRelax and Follow below mentioned Lifestyle Changes:\n\n1. Eat a healthy diet\n2. Regular exercise\n3. Maintain a healthy weight\n4. Quit smoking\n5. Limit alcohol consumption\n6. Manage stress\n7. Get enough sleep\n8. Regular health check-ups"
            text_color = 'green'

        result_label = ttk.Label(frame_alpr, text=result_text, background=result_color, foreground="white",
                                 font=('Helvetica', 12, 'bold'), width=40)
        result_label.grid(row=len(labels), columnspan=3, pady=10)

        pdf_filename = generate_pdf_report(report_text, username, *inputs, text_color=text_color)

        root.after(1000, lambda: open_pdf_file(pdf_filename))

    root = tk.Tk()
    root.title("Check Heart Disease")

    window_width = 570
    window_height = 670
    root.geometry(f"{window_width}x{window_height}")

    center_window(root, window_width, window_height)

    root.configure(bg="#F0F0F0")

    root.resizable(False, False)

    style = ttk.Style()
    style.theme_use('clam')

    frame_alpr = ttk.Frame(root, padding=(20, 20, 20, 10), relief=tk.RAISED)
    frame_alpr.pack(fill=tk.BOTH, expand=True)

    labels = ["Username:", "Age:", "Sex:", "Chest Pain:", "Trestbps:", "Chol:", "FBS:", "RestECG:", "Thalach:", "ExANG:", "Old Peak:", "Slope:", "Ca:", "Thal:"]
    entry_vars = []
    placeholders = ["username", "age", "0-female, 1-male", "Chest pain type", "in mm Hg",
                    "mg/dl", "1 = true; 0 = false", "0/1/2",
                    "enter value", "0-no, 1-yes",
                    "enter value", "enter value",
                    "0/1/2/3"]

    info_lines = ["*The reading of the resting blood pressure", "*Level of serum cholesterol",
                  "*Fasting blood sugar > 120 mg/dl", "*Resting electrocardiographic result",
                  "*The maximum heart rate", "*Exercise induced angina (1 for pain, 0 for no pain)",
                  "*ST depression induced by exercise relative to rest.", "*The slope of the peak exercise ST segment.",
                  "*Number of major vessels colored by fluoroscopy."]

    def clear_placeholder(event):
        entry = event.widget
        if entry.get() == placeholders[entry.grid_info()["row"]]:
            entry.delete(0, tk.END)
            entry.config(foreground="black")

    def restore_placeholder(event):
        entry = event.widget
        if entry.get() == "":
            entry.insert(0, placeholders[entry.grid_info()["row"]])
            entry.config(foreground="gray")

    for i, label_text in enumerate(labels):
        label = ttk.Label(frame_alpr, text=label_text, font=('Helvetica', 12, 'bold'))
        label.grid(row=i, column=0, sticky='w', pady=5)

        if i >= 4 and i - 4 < len(info_lines):
            info_label = ttk.Label(frame_alpr, text=info_lines[i - 4], font=('Helvetica', 10), wraplength=250, justify='left')
            info_label.grid(row=i, column=2, columnspan=2, sticky='w', pady=5, padx=(10, 20))
        
        if label_text == "Username:":
            entry_var = tk.StringVar(root)
            entry = ttk.Entry(frame_alpr, textvariable=entry_var, font=('Helvetica', 12), width=15)
            entry.grid(row=i, column=1, sticky='w', pady=7)
            entry.insert(0, placeholders[i])
            entry.config(foreground="gray")
            entry.bind("<FocusIn>", clear_placeholder)
            entry.bind("<FocusOut>", restore_placeholder)
            entry_vars.append(entry_var)
        elif label_text in ["Chest Pain:", "Thal:"]:
            values = ["Typical", "Asymptomatic", "Non-typical"] if label_text == "Chest Pain:" else ["Fixed", "Normal", "Reversable"]
            entry_var = tk.StringVar(root, "1")
            for j, value in enumerate(values):
                radio = ttk.Radiobutton(frame_alpr, text=value, value=str(j+1), variable=entry_var)
                radio.grid(row=i, column=j+1, sticky='w', padx=(7, 10))
            entry_vars.append(entry_var)
        else:
            entry_var = tk.StringVar(root)
            entry = ttk.Entry(frame_alpr, textvariable=entry_var, font=('Helvetica', 12), width=15)
            entry.grid(row=i, column=1, sticky='w', pady=7, padx=(0, 20))
            entry.insert(0, placeholders[i])
            entry.config(foreground="gray")
            entry.bind("<FocusIn>", clear_placeholder)
            entry.bind("<FocusOut>", restore_placeholder)
            entry_vars.append(entry_var)

    button_submit = ttk.Button(frame_alpr, text="Submit", command=Detect)
    button_submit.grid(row=len(labels)+1, columnspan=3, pady=10)

    root.mainloop()

Train()