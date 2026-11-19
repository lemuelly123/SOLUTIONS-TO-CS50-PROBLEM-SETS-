from fpdf import FPDF
from pathlib import Path


#checks if the str input is valid returns str.strip().title() raises error if invalid
def valid_param(param, value):
    if not isinstance(param, str):
        raise ValueError(f"Expected string for {value} but got {type(param)} instead")
    if not param:
        raise ValueError(f"{param} cannot be empty")
    return param.strip()


def find_x_positions():
    ...


#image checker
def check_if_image_exist(img_name):
    img_name = img_name.strip().lower()
    script_dir = Path(__file__).resolve().parent
    img_file_path = script_dir/img_name
    if not img_file_path.is_file():
        raise FileNotFoundError(f"{img_file_path} not found")
    return img_file_path


class Shirtificate:
    def __init__(self, name):
        self.name = valid_param(name, "Name")
        self.pdf = FPDF(orientation='p',  unit="mm", format='A4')

    def create_pdf(self, displey_text):
        valid_display_text = valid_param(displey_text, "Display text")
        shirt_width = 200
        self.pdf.add_page()
        self.pdf.set_font("Helvetica", style="B", size=30, )
        self.pdf.set_x(80)
        self.pdf.cell(text=valid_display_text, align="C")
        x_position = (self.pdf.w - shirt_width) / 2
        y_position = 50
        image_filename = check_if_image_exist("shirtificate.png")
        self.pdf.image(image_filename, x_position, y=y_position, w=shirt_width)
        self.pdf.set_y(y_position + 90)
        self.pdf.set_x(0)
        self.pdf.set_text_color(255)
        self.pdf.cell(text=f"{self.name.title()} took CS50 course", w=self.pdf.w, align="C", h=10)
        self.pdf.output("shirtificate.pdf")

def main():
    user_name = input("Enter your name: ")
    name = valid_param(user_name, "name")
    shirt = Shirtificate(name)
    shirt.create_pdf("CS50 Shirtificate")

if __name__ == "__main__":
    main()






    


