from fpdf import Template
import streamlit as st
import datetime

from PIL import Image
image = Image.open('https://raw.githubusercontent.com/crazycse/kanmaniearthmovers/master/src/logo.png')

import os
import base64





def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href


#t=st.text_input("Enter link to download", '')
st.title('Kanmani Earth movers')

st.image(image, caption="KEM",use_column_width=True)
#this will define the ELEMENTS that will compose the template. 
elements = [
    { 'name': 'company_logo', 'type': 'I', 'x1': 20.0, 'y1': 17.0, 'x2': 48.0, 'y2': 30.0, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'logo', 'priority': 2, },
    { 'name': 'company_name', 'type': 'T', 'x1': 17.0, 'y1': 32.5, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 13.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
    { 'name': 'address1', 'type': 'T', 'x1': 17.0, 'y1': 37.5, 'x2': 115.0, 'y2': 42.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
    { 'name': 'phone', 'type': 'T', 'x1': 17.0, 'y1': 42.5, 'x2': 115.0, 'y2': 47.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
    { 'name': 'box', 'type': 'B', 'x1': 15.0, 'y1': 15.0, 'x2': 185.0, 'y2': 260.0, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 0, },
    #{ 'name': 'box_x', 'type': 'B', 'x1': 95.0, 'y1': 15.0, 'x2': 105.0, 'y2': 25.0, 'font': 'Arial', 'size': 0.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 2, },
    { 'name': 'line1', 'type': 'L', 'x1': 100.0, 'y1': 15.0, 'x2': 100.0, 'y2': 57.0, 'font': 'Arial', 'size': 0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 3, },
    { 'name': 'line2', 'type': 'L', 'x1': 15, 'y1': 57.0, 'x2': 185.0, 'y2': 57.0, 'font': 'Arial', 'size': 0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 3, },
    { 'name': 'c_name', 'type': 'T', 'x1': 17.0, 'y1': 62.5, 'x2': 115.0, 'y2': 67.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
    { 'name': 'date', 'type': 'T', 'x1': 137.0, 'y1': 62.5, 'x2': 115.0, 'y2': 67.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
    { 'name': 'main_box', 'type': 'B', 'x1': 20.0, 'y1': 80.0, 'x2': 180.0, 'y2': 160.0, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 0, },
    { 'name': 'mline1', 'type': 'L', 'x1': 20.0, 'y1': 90.0, 'x2': 180.0, 'y2': 90.0, 'font': 'Arial', 'size': 0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 3, },
    { 'name': 'mline2', 'type': 'L', 'x1': 50.0, 'y1': 80.0, 'x2': 50.0, 'y2': 160.0, 'font': 'Arial', 'size': 0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 3, },
    { 'name': 'mline3', 'type': 'L', 'x1': 110.0, 'y1': 80.0, 'x2': 110.0, 'y2': 160.0, 'font': 'Arial', 'size': 0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 3, },
    { 'name': 'mline4', 'type': 'L', 'x1': 130.0, 'y1': 80.0, 'x2': 130.0, 'y2': 160.0, 'font': 'Arial', 'size': 0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 3, },
    { 'name': 'mline5', 'type': 'L', 'x1': 150.0, 'y1': 80.0, 'x2': 150.0, 'y2': 160.0, 'font': 'Arial', 'size': 0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 3, },
    { 'name': 'mtitle', 'type': 'T', 'x1': 25.0, 'y1': 125.5, 'x2': 115.0, 'y2': 47.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
    { 'name': 'barcode', 'type': 'BC', 'x1': 20.0, 'y1': 246.5, 'x2': 140.0, 'y2': 254.0, 'font': 'Interleaved 2of5 NT', 'size': 0.75, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '9443567491', 'priority': 3, },
    { 'name': 'total', 'type': 'T', 'x1': 25.0, 'y1': 300.5, 'x2': 115.0, 'y2': 47.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
]
c_n=st.text_input("Name",'')
c_no=st.text_input("Contact",'')
v=list(st.text_input("Vechicle", '').split())
t=list(map(str,st.text_input("time", '').split()))
r=list(map(int,st.text_input("rate", '').split()))
bata=st.text_input("Bata",'')
s=[]
if v!='' and t!='' and r!='':
    x=155.0
    for i in range(len(v)):
        elements.append({ 'name': v[i], 'type': 'T', 'x1': 25.0, 'y1': x, 'x2': 115.0, 'y2': 47.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },)
        x=x+20.0
        if 'h' in t[i]:
            t[i]=str(int(t[i][:-1])*60)
        if v[i]=='jcb':
            s.append([v[i],t[i],r[i],(int(t[i])/100)*int(r[i])])
            continue    
        s.append([v[i],t[i],r[i],(int(t[i])/60)*int(r[i])])    
    elements.append({ 'name': "bata", 'type': 'T', 'x1': 25.0, 'y1': x, 'x2': 115.0, 'y2': 47.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },)
    #here we instantiate the template and define the HEADER
    f = Template(format="A4", elements=elements,
                title="Sample Invoice")
    f.add_page()
    su=int(bata)
    for i in s:
        su=su+i[3]
        f[i[0]]="29042000"+" "*25+str(i[0])+" "*(35-len(str(i[0]))-3)+str(i[1])+"           "+str(i[2])+" "*(17-len(str(i[2]))-3)+str(round(i[3],2))

    #we FILL some of the fields of the template with the information we want
    #note we access the elements treating the template instance as a "dict"
    f["company_name"] = "Kanmani Earth Movers"
    f["c_name"]="Mr."+c_n+"("+c_no+")"
    f["date"]=str(datetime.datetime.now())[:-7]
    f["address1"]="NH Main Road , Perumanallur"
    f["company_logo"] = "logo.png"
    f["bata"]=" "*41+"Bata"+" "*63+bata
    f["Phone"]="Contact:9443567491,9443567490"
    f["mtitle"]="Date                                Particulars                  Time         Rate          Amount"
    #and now we render the page
    f["total"]="                                                                                             TOTAL       "+str(su)
    f.render("./template.pdf")
    st.markdown(get_binary_file_downloader_html('template.pdf', 'pdf'), unsafe_allow_html=True)



