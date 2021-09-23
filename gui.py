import tkinter as tk
import event_manager

window = tk.Tk()
window.geometry('450x600')
window.resizable(False, False)
window.title('Python.org Scraper')

search_input_label = tk.Label(window, text='Enter what you want to search:', font=('default', 15))
search_input_label.place(x=25, y=70)

set_file_label = tk.Label(window, text='Set File Name:')
set_file_label.place(x=20, y=170)
set_file_label.config(font=('default', 15))
set_file_name = tk.Entry(window)
set_file_name.config(font=('default', 20))
set_file_name.place(x=20, y=200)

search_input = tk.Entry(window)
search_input.config(font=('default', 20))
search_input.place(x=25, y=103)

results_field = tk.Text(window)
results_field.place(x=25, y=300)
results_field.config(font=('default', 12), width=45, height=15)

submit_button = tk.Button(window, text="Submit", command=lambda: event_manager.on_submission(search_input, results_field))
submit_button.config(font=('default', 15))
submit_button.place(x=340, y=100)

save_file_btn = tk.Button(window, text="Save To File", command=lambda: event_manager.save_to_file(results_field, set_file_name.get()))
save_file_btn.place(x=25, y=540)
save_file_btn.config(font=('default', 15))

window.mainloop()
