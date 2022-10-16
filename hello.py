
import streamlit as st
import pandas as pd
import random


ronQuotes=[
'There is only one bad word: taxes.',
'Theres more than one crib tree in a forest. Thats not a lesson, by the way, just a comment on lumber availability.',
'When people get too chummy with me, I like to call them by the wrong name to let them know I dont really care about them.',
'Capitalism: Gods way of determining who is smart and who is poor.',
'Crying: Acceptable at funerals and the Grand Canyon.',
'Fishing relaxes me. Its like yoga, except I still get to kill something.',
'History began on July 4, 1776. Everything that happened before that was a mistake.',
'Birthdays were invented by Hallmark to sell cards.',
'Any dog under fifty pounds is a cat and cats are useless.',
'I would rather bleed out than sit here and talk about my feelings for 10 minutes.',
'Give 100%. 110% is impossible. Only idiots recommend that.',
'There are only three ways to motivate people: money, fear, and hunger.',
'There are three acceptable haircuts: high and tight, crew cut, buzz cut.',
'Id wish you the best of luck, but I believe luck is a concept created by the weak to explain their failures.',
'Give a man a fish and feed him for a day. Dont teach a man to fish…and feed yourself. Hes a grown man. And fishings not that hard.',
'Theres only one thing I hate more than lying: skim milk. Which is water thats lying about being milk.',
'Strippers do nothing for me… but I will take a free breakfast buffet anytime, anyplace.',
'Clear alcohols are for rich women on diets.',
'Im not interested in caring about people. I once worked with a guy for three years and never learned his name. Best friend I ever had. We still never talk sometimes.',
'On my deathbed, my final wish is to have my ex-wives rush to my side so I can use my dying breath to tell them both to go to hell one last time.'

]

print(random.choice(ronQuotes))

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.write('')

with col2:
    st.image("https://upload.wikimedia.org/wikipedia/en/a/ae/RonSwanson.jpg")
    st.write(random.choice(ronQuotes))

with col3:
    st.write('')
