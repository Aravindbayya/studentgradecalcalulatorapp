import streamlit as st

st.title("Students Grade Calculator")
name=st.text_input("Please enter your name::")
sub1= st.number_input('Enter sub 1 marks :: ',0,100)
sub2= st.number_input('Enter sub 2 marks :: ',0,100)
sub3= st.number_input('Enter sub 3 marks :: ',0,100)
sub4= st.number_input('Enter sub 4 marks :: ',0,100)
sub5= st.number_input('Enter sub 5 marks :: ',0,100)
sub6= st.number_input('Enter sub 6 marks :: ',0,100)

if st.button('Calculate'):
    total=sub1+sub2+sub3+sub4+sub5+sub6
    percentage = total/6


    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    st.write(f'**Student Name**: {name}')
    st.write(f"**Total Marks:** {total}/600")
    st.write(f"**Percentage:** {percentage:.2f}%")
    st.write(f"**Grade:** {grade}")


