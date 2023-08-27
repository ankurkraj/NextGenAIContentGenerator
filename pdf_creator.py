from fpdf import FPDF
from pathlib import Path
from PIL import Image
import numpy as np

def response_file_pdf(heading, dalle_heading, response):
    img = Image.open("DALLE2.jpg")
    print(img.size)
    new_img = img.resize((400, 400))
    new_img.save("DALLE2.jpg")

    HERE = Path(__file__).resolve().parent
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=800 / len(heading), style="B")
    pdf.set_text_color(100, 100, 1)
    pdf.set_fill_color(20, 20, 20)
    with pdf.local_context(text_mode=0, line_width=2):
        pdf.cell(txt=heading, center=True)

    top_left_x, top_left_y = 60, 200 / len(heading) + 20
    pdf.image("DALLE2.jpg", x=top_left_x, y=top_left_y, h=100, w=100)
    #with pdf.rect_clip(x=top_left_x + 12, y=top_left_y + 30, w=180, h=120):
    #    pdf.image(
    #        HERE / "DALLE2.jpg",
    #        x=top_left_x-30,
    #        y=top_left_y-30,
    #    )
    #top_left_x, top_left_y = 50, pdf.get_y() - 10
    #with pdf.round_clip(x=top_left_x + 12, y=top_left_y + 25, r=90):
    #    pdf.image(
    #        HERE / "DALLE2.jpg",
    #        x=top_left_x,
    #        y=top_left_y,
    #    )
    top_left_y = top_left_y+10
    pdf.set_line_width(0.1)
    pdf.set_draw_color(r=150, g=150, b=0)
    pdf.line(x1=50, y1=top_left_y + 110, x2=160, y2=top_left_y + 110)

    pdf.set_font("Helvetica", size=10, style="I")
    pdf.set_text_color(0, 200, 200)
    pdf.set_y(top_left_y + 93)
    flag=0
    if len(dalle_heading)>125:
        y_coordnt = pdf.get_y()
        pdf.cell(txt=dalle_heading[:125],
                 center=True)
        pdf.set_y(y_coordnt+5)
        pdf.cell(txt=dalle_heading[125:],
                 center=True)
        flag=1
    else:
        pdf.cell(txt=dalle_heading,
             center=True)
    pdf.set_font("Helvetica", size=10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_y(top_left_y + 100)
    if flag==1:
        pdf.set_y(pdf.get_y() + 4)
    pdf.write_html('Image Credits: <a href="https://www.openai.com/dalle2">DALLE2 Image Generator </a>', x=80)
    pdf.write(txt="\n\n\n\n")
    pdf.set_draw_color(10, 10, 10)
    pdf.set_line_width(1)
    pdf.line(x1=5, y1=5, x2=pdf.epw + 10, y2=5)
    # pdf.rect(5, 5, pdf.epw+10, pdf.eph+18, style="D")
    pdf.line(x1=5, y1=pdf.eph + 18, x2=pdf.epw + 10, y2=pdf.eph + 18)
    pdf.set_font("Times", size=15)
    txt_file = ""
    # pdf.set_y(135-(8-750/len(heading)))
    for a in range(len(response)):
        if response[a] == "\n":
            response = response[a + 1:]
            break
        txt_file = txt_file + response[a]

    pdf.write(txt=txt_file)

    pdf.set_font("Times", size=15)
    pdf.write(txt=response)
    pdf.set_draw_color(10, 10, 10)
    pdf.set_line_width(1)
    pdf.line(x1=5, y1=5, x2=pdf.epw + 10, y2=5)
    # pdf.rect(5, 5, pdf.epw+10, pdf.eph+18, style="D")
    pdf.line(x1=5, y1=pdf.eph + 18, x2=pdf.epw + 10, y2=pdf.eph + 18)

    #ycoordinte = pdf.get_y()
    #ycoordinte = ycoordinte + 10
    #if ycoordinte < 230:
    #    imgeLocation = ycoordinte
    #    height = min(pdf.eph / 2, 280 - ycoordinte - 10)
    #else:
    #    pdf.add_page()
    #    ycoordinte = 10
    #    imgeLocation = 10
    #    height = pdf.eph / 2

    #img_link1=img_link[0]
    #img_heading1=img_heading[0]
    #while 1:
    #    try:
    #        chosen_one = int(abs(10*(np.random.default_rng().random())))+1
    #        chosen_one=9
    #        img_link1=img_link[chosen_one-1]
    #        img_heading1=img_heading[chosen_one]
    #        img = Image.open("img"+str(chosen_one)+".jpg")
    #        size=img.size
    #        print(size)
    #        print(size[1]*(400/size[0]))
    #        new_img = img.resize((400,int(size[1]*(400/size[0]))))
    #        print(new_img.size)
    #        new_img.save("img"+str(chosen_one)+".jpg")
    #        pdf.image("img"+str(chosen_one)+".jpg", x=60, y=imgeLocation, h=height)
    #        pdf.set_y(ycoordinte + height + 4)
    #        pdf.set_font("Times", size=8)
    #        pdf.write_html('<a href="' + img_link[chosen_one] + '">Source :' + img_heading1 + ' </a>', x=pdf.epw / 2)
    #        break
    #    except Exception as E:
    #        continue

    #print(pdf.epw)

    #pdf.write_html('<a href="'+img_link1+'">Source :'+img_heading1+' </a>', x=pdf.epw/2)
    # pdf.text(txt="Headless CMS", x = 50, y=140)
    # pdf.set_page_background((252,212,255))
    pdf.output("varying_new_format.pdf")
    with open("varying_new_format.pdf", "rb") as f:
        return f.read()