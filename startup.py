import numpy as np
import pickle
import sys
import streamlit as st
import subprocess
import pandas as pd
custom_css = """
<style>
[data-testid="stAppViewContainer"] {
       background-image: url('https://img.freepik.com/free-vector/paper-style-dynamic-lines-background_23-2149008629.jpg?w=1060&t=st=1700727861~exp=1700728461~hmac=31c145d3b0442847d08c288c249e00d4fbcbe56694d94e710e371dd8b4fecb99'); /* Set background image URL */
       background-size: cover; /* Set background size */
        /* Prevent background image from repeating */
	.centered-image {
            display: flex;
            justify-content: center;
	    position:absolute;
        }
        
 }
</style>
"""

#st.markdown(custom_css, unsafe_allow_html=True)
#image = Image.open('pic.jpg')
#st.image(image, caption='Your Image', width=100)  # Specify width as 300 pixels
st.markdown(custom_css, unsafe_allow_html=True)

st.markdown(custom_css, unsafe_allow_html=True)

# Display the centered image with a smaller width
st.markdown('<div class="centered-image">', unsafe_allow_html=True)

st.image('pic.jpg', caption='START UP COMPANY', width=200)  
st.markdown('</div>', unsafe_allow_html=True)

loaded_model = pickle.load(open('C:/Users/user/Desktop/shyam/startup_model.sav', 'rb'))
# Load existing user credentials from Excel file or create a new DataFrame if file doesn't exist
try:
    user_df = pd.read_excel("user_credentials.xlsx")
except FileNotFoundError:
    user_df = pd.DataFrame(columns=['Username', 'Password', 'Name', 'Age', 'Sex', 'Working Status', 'Company Name'])


    
def feedback_section():
    # Create a modal dialog for feedback
    feedback_expander = st.expander(label='Feedback', expanded=True)
    
    # Input slider for feedback ratings
    feedback_rating = feedback_expander.slider('Feedback Rating', min_value=1, max_value=5, step=1, value=3)
    
    # Text area for comments
    feedback_comments = feedback_expander.text_area('Comments', height=100)
    
    if feedback_expander.button('Submit Feedback'):
        # Process feedback (you can add your logic here)
        st.success('Thank you for your feedback!')


def start_up_prediction(data):
	input_data=np.asarray(data)
	input_reshaped=input_data.reshape(1,-1)
	pred=loaded_model.predict(input_reshaped)
	if(pred[0]==0):
	  return 'startup will fail'
	else:
	  return 'startup will succeed'


st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f0f0; /* Change this value to the color you want */
    }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    if st.button('Close'):
        st.write('closing the app')
        sys.exit()
with st.sidebar:
    if st.button('Feedback'):
        feedback_section()
with st.sidebar:
    if st.button('dashboard'):
        subprocess.run(["streamlit","run","dashboard.py"])



def main():
	d1 = {
      	'Cloud Computing': 1, 'Market Research|Marketing|Crowdfunding': 2,
   	 'Analytics|Cloud Computing|Software Development': 3, 'Mobile|Analytics': 4,
   	 'Analytics|Marketing|Enterprise Software': 5, 'Food & Beverages|Hospitality': 6,
    	'Analytics': 7, 'Cloud Computing|Network / Hosting / Infrastructure': 8, 'Analytics|Mobile|Marketing': 9,
    	'Healthcare|Pharmaceuticals|Analytics': 10, 'Analytics|Enterprise Software': 11,
    	'Media|Finance|Marketing': 12, 'Music|Analytics': 13, 'E-Commerce|Gaming|Analytics': 14,
    	'Healthcare|Analytics': 15, 'Marketing': 16, 'Advertising|Retail|Mobile': 17, 'Mobile|Retail': 18,
    	'Analytics|Finance': 19, 'Software Development': 20, 'Marketing|Software Development|Analytics': 21,
    	'Security': 22, 'Advertising': 23, 'Marketing|Email': 24, 'Analytics|Security|Network / Hosting / Infrastructure': 25,
    	'Human Resources (HR)|Marketing|Career / Job Search': 26, 'Cloud Computing|Healthcare|E-Commerce': 27, 'Media|Analytics|Publishing|Mobile|Education': 28, 'E-Commerce|Energy|Media': 29, 'Media|Analytics': 30,
    	'Advertising|Marketing|Analytics': 31, 'E-Commerce|Analytics': 32, 'E-Commerce|Advertising|Analytics': 33, 'Enterprise Software': 34, 'Analytics|Advertising|Cloud Computing|Marketing': 35, 'Analytics|Network / Hosting / Infrastructure': 36,
    	'Finance': 37, 'E-Commerce|Marketing': 38, 'Education|E-Commerce|Mobile': 39, 'E-Commerce|Retail|Marketing|Mobile|Advertising|Deals': 40, 'Analytics|Market Research|Mobile': 41, 'Advertising|Mobile|Analytics': 42,
    	'Media|Analytics|Entertainment': 43, 'Analytics|Retail|Mobile': 44, 'Analytics|Cloud Computing': 45, 'Transportation|Analytics': 46, 'Analytics|Publishing|Mobile': 47, 'Analytics|Mobile': 48, 'Human Resources (HR)|Enterprise Software|Career / Job Search|Social Networking|Analytics': 49,
    	'Analytics|Marketing': 50, 'Media|Marketing|Analytics': 51, 'Analytics|Food & Beverages|Social Networking|Mobile': 52, 'E-Commerce|Analytics|Advertising|Mobile': 53, 'Media|Advertising|Analytics|Marketing': 54, 'E-Commerce|Retail|Analytics': 55,
    	'Social Networking': 56, 'Healthcare': 57, 'E-Commerce|Mobile': 58, 'Real Estate': 59, 'E-Commerce': 60, 'Mobile|Advertising|Social Networking|Marketing|E-Commerce|Analytics|Enterprise Software': 61, 'Network / Hosting / Infrastructure|Food & Beverages|Analytics': 62, 'Analytics|E-Commerce|Marketing': 63, 'Retail': 64, 'Market Research': 65, 'Retail|Mobile': 66, 'Mobile|Marketing': 67, 'Network / Hosting / Infrastructure': 68,
    	'Real Estate|Mobile|E-Commerce': 69, 'Media|Entertainment|Analytics|Network / Hosting / Infrastructure|Publishing': 70, 'E-Commerce|Email|Analytics|Marketing': 71, 'Analytics|Crowdfunding|Search|Marketing': 72, 'Analytics|Healthcare': 73, 'Network / Hosting / Infrastructure|Enterprise Software|Software Development|Analytics': 74, 'Analytics|Telecommunications': 75,
    	'Marketing|Enterprise Software|Analytics': 76, 'Media': 77, 'Mobile': 78, 'E-Commerce|Food & Beverages|Mobile': 79, 'Education': 80, 'Social Networking|Mobile': 81, 'Entertainment|Media|Mobile': 82, 'Search': 83, 'Advertising|Gaming|Marketing': 84, 'Analytics|Insurance': 85, 'E-Commerce|Retail|Mobile': 86, 'Gaming|CleanTech|Social Networking|Energy': 87, 'Advertising|Media|Mobile|Marketing': 88,
    	'Analytics|Software Development|Marketing': 89, 'Space Travel': 90, 'Search|Enterprise Software|Mobile': 91, 'Analytics|Marketing|Software Development': 92, 'Analytics|Security|Enterprise Software': 93,
    	'Media|Publishing': 94, 'Analytics|Social Networking|Email': 95, 'Media|Analytics|Marketing': 96,
    	'E-Commerce|Finance': 97, 'Analytics|Energy': 98, 'CleanTech|Analytics|Energy': 99,
    	'Marketing|Analytics': 100, 'Retail|Analytics': 101,
    	'Analytics|Enterprise Software|Cloud Computing|Software Development': 102,
    	'Advertising|Market Research': 103, 'Enterprise Software|Software Development': 104,
    	'Energy': 105, 'CleanTech|Analytics|Real Estate|Energy': 106, 'Security|Cloud Computing': 107, 'CleanTech|Energy': 108, 'E-Commerce|Enterprise Software|Analytics': 109,
    	'E-Commerce|Analytics|Mobile|Retail': 110, 'Entertainment': 111, 'Music': 112, 'Analytics|E-Commerce': 113, 'Network / Hosting / Infrastructure|Analytics': 114,
    	'E-Commerce|Publishing|Marketing': 115, 'E-Commerce|Market Research|Analytics|Deals|Finance': 116, 'Cloud Computing|Energy': 117,
    	'Network / Hosting / Infrastructure|Enterprise Software': 118, 'Career / Job Search': 119,
    	'Advertising|Analytics': 120, 'Analytics|Retail|Mobile|Enterprise Software|Market Research': 121,
    	'Cloud Computing|E-Commerce|Analytics': 122, 'Analytics|Retail': 123, 'Search|Social Networking': 124,
    	'Telecommunications': 125, 'Publishing': 126, 'Network / Hosting / Infrastructure|Publishing': 127,
    	'Classifieds|Network / Hosting / Infrastructure': 128, 'Media|Advertising|E-Commerce': 129, 'Search|Healthcare': 130, 'Mobile|Telecommunications': 131,
    	'Cloud Computing|E-Commerce|Classifieds': 132, 'Gaming|Entertainment': 133, 'Food & Beverages': 134, 'Marketing|Mobile|E-Commerce': 135, 'Mobile|Cloud Computing|Enterprise Software': 136,
    	'Music|Media|Software Development': 137, 'Analytics|Advertising': 138, 'E-Commerce|Analytics|Advertising|Enterprise Software': 139, 'Cloud Computing|Analytics': 140
	}

	d2={

     	'marketing': 1, 'Marketing, sales': 2, 'operations': 3, 'Marketing & Sales': 4,
     	'analytics': 5, 'Research': 6, 'Computing': 7, 'Marketing': 8, 'Sales, marketing': 9,
     	'Marketing \nsales': 10, 'Technology': 11, 'marketing, sales': 12, 'Data Management': 13,
     	'Solution providing': 14, 'Social Media': 15, 'targeted marketing': 16, 'Community Betterment': 17,
     	'Web Analytics': 18, 'Strategy': 19, 'Bug fix': 20, 'Data Integration': 21, 'malware protection': 22,
     	'Analytics': 23, 'Social Media optimization': 24, 'Database Management': 25, 'technology': 26,
     	'Operations': 27, 'Sales': 28, 'Risk': 29, 'Marketing, Web Analytics': 30,
     	'Strategy, Operations, Finacial Planning': 31, 'Data Collection': 32, 'marketiing': 33,
     	'sales': 34, 'e-learning': 35, 'software service': 36, 'mobile app': 37, 'application': 38,
     	'analytic': 39, 'software ': 40, 'SOCIAL MEDIA': 41, 'SOCIAL MEDIA management': 42, 'OPERATIONS': 43,
     	'MARKETING': 44, 'PERSONAL APPS': 45, 'consumer behaviour': 46, 'customer servce': 47, 'CUSTOMER SERVICE': 48, 'APP REVENUE': 49, 'intellectual property analysis and visualisation': 50,
     	'retail': 51, 'data visualization': 52, 'service': 53, 'social media': 54, 'security': 55, 'operation': 56, 'Marketing, Sales': 57, 'operations, sales, marketing': 58,
     	'research': 59, 'Marketing, Technology, Finance & Accounting, Customer service': 60, 'Computing, training': 61, 'Operations, marketing': 62, 'social advertising': 63, 'risk': 64,
     	'data collection ': 65, 'development, marketing, and administration': 66, 'IT & Sales': 67,
     	'social news': 68, 'web': 69, 'sale': 70, 'Sales & Marketing': 71, 'social network': 72,
     	'consumer web': 73, 'writing blog': 74, 'curated web': 75, 'Recommendation ': 76,
     	'Marketing,Sales,Risk,Operations': 77, 'Development Tool': 78, 'Tool': 79,
     	'Customer Retention, Customer Feedback': 80, 'Inventory management': 81,
     	'Energy saving': 82, 'Optimization, CRM, Pricing': 83, 'games': 84,
     	'Marketing, customer targeting': 85, 'entertainment': 86, 'Search EnginenOptimization': 87,
     	'Information management': 88, 'strategy': 89, 'Social media analytics': 90, 'marketing, strategy': 91,
     	'customer engagement': 92, 'Marketing, Procurement, Human Resources': 93, 'CRM, Marketing, Human Resources': 94, 'CRM': 95,
     	'Merchandising, Marketing': 96, 'Travel Planning': 97, 'Data Visualization, Content Marketing, Presentations': 98, 'News': 99, 'analtics': 100,
     	'elearning': 101, 'PHONE INTELLIGENCE': 102, 'social branding': 103, 'reporting': 104,
     	'DASHBOARDS': 105, 'localized behaviour': 106, 'VIDEO STREAMING': 107, 'PAYMENT': 108, 'software': 109,
     	'networking': 110, 'wireless': 111, 'advertising': 112, 'game': 113, 'search': 114, 'conssumer web': 115,
     	'online music': 116, 'media': 117, 'cloud computing': 118
	}
	d3={
   	  'No':1, 'Yes':2, 'yes':3, 'YES':4
	}

	d4={
    	  'No':1, 'Yes':2
	}
	d5={
    	  'No':1, 'Yes':2
	}

	d6={
    	  'No':1, 'Yes':2
	}

	d7={
    	  'Service':1, 'Product':2, 'Both':3, 'No Info':4
	}

	d8={
           'Platform':1, 'cloud':2, 'Cloud':3, 'none':4, 'Both':5
	}
	d9={
    	   'Linear':1, 'Non-Linear':2
	}
	d10={
    	   'Masters':1, 'Bachelors':2, 'PhD':3
	}

	d11={
    	   'Medium':1, 'High':2, 'Low':3, 'None':4
	}
	st.title('Startup Prediction')
	a=st.text_input('enter the start_up year')
	b=st.text_input('Age of Company in years')
	options=['Cloud Computing', 'Market Research|Marketing|Crowdfunding',
       'Analytics|Cloud Computing|Software Development',
       'Mobile|Analytics', 'Analytics|Marketing|Enterprise Software',
       'Food & Beverages|Hospitality', 'Analytics',
       'Cloud Computing|Network / Hosting / Infrastructure',
       'Analytics|Mobile|Marketing',
       'Healthcare|Pharmaceuticals|Analytics',
       'Analytics|Enterprise Software', 'Media|Finance|Marketing',
       'Music|Analytics', 'E-Commerce|Gaming|Analytics',
       'Healthcare|Analytics', 'Marketing', 'Advertising|Retail|Mobile',
       'Mobile|Retail', 'Analytics|Finance', 'Software Development',
       'Marketing|Software Development|Analytics', 'Security',
       'Advertising', 'Marketing|Email',
       'Analytics|Security|Network / Hosting / Infrastructure',
       'Human Resources (HR)|Marketing|Career / Job Search',
       'Cloud Computing|Healthcare|E-Commerce',
       'Media|Analytics|Publishing|Mobile|Education',
       'E-Commerce|Energy|Media', 'Media|Analytics',
       'Advertising|Marketing|Analytics', 'E-Commerce|Analytics',
       'E-Commerce|Advertising|Analytics', 'Enterprise Software',
       'Analytics|Advertising|Cloud Computing|Marketing',
       'Analytics|Network / Hosting / Infrastructure', 'Finance',
       'E-Commerce|Marketing', 'Education|E-Commerce|Mobile',
       'E-Commerce|Retail|Marketing|Mobile|Advertising|Deals',
       'Analytics|Market Research|Mobile', 'Advertising|Mobile|Analytics',
       'Media|Analytics|Entertainment', 'Analytics|Retail|Mobile',
       'Analytics|Cloud Computing', 'Transportation|Analytics',
       'Analytics|Publishing|Mobile', 'Analytics|Mobile',
       'Human Resources (HR)|Enterprise Software|Career / Job Search|Social Networking|Analytics',
       'Analytics|Marketing', 'Media|Marketing|Analytics',
       'Analytics|Food & Beverages|Social Networking|Mobile',
       'E-Commerce|Analytics|Advertising|Mobile',
       'Media|Advertising|Analytics|Marketing',
       'E-Commerce|Retail|Analytics', 'Social Networking', 'Healthcare',
       'E-Commerce|Mobile', 'Real Estate', 'E-Commerce',
       'Mobile|Advertising|Social Networking|Marketing|E-Commerce|Analytics|Enterprise Software',
       'Network / Hosting / Infrastructure|Food & Beverages|Analytics',
       'Analytics|E-Commerce|Marketing', 'Retail', 'Market Research',
       'Retail|Mobile', 'Mobile|Marketing',
       'Network / Hosting / Infrastructure',
       'Real Estate|Mobile|E-Commerce',
       'Media|Entertainment|Analytics|Network / Hosting / Infrastructure|Publishing',
       'E-Commerce|Email|Analytics|Marketing',
       'Analytics|Crowdfunding|Search|Marketing', 'Analytics|Healthcare',
       'Network / Hosting / Infrastructure|Enterprise Software|Software Development|Analytics',
       'Analytics|Telecommunications',
       'Marketing|Enterprise Software|Analytics', 'Media', 'Mobile',
       'E-Commerce|Food & Beverages|Mobile', 'Education',
       'Social Networking|Mobile', 'Entertainment|Media|Mobile', 'Search',
       'Advertising|Gaming|Marketing', 'Analytics|Insurance',
       'E-Commerce|Retail|Mobile',
       'Gaming|CleanTech|Social Networking|Energy',
       'Advertising|Media|Mobile|Marketing',
       'Analytics|Software Development|Marketing', 'Space Travel',
       'Search|Enterprise Software|Mobile',
       'Analytics|Marketing|Software Development',
       'Analytics|Security|Enterprise Software', 'Media|Publishing',
       'Analytics|Social Networking|Email', 'Media|Analytics|Marketing',
       'E-Commerce|Finance', 'Analytics|Energy',
       'CleanTech|Analytics|Energy', 'Marketing|Analytics',
       'Retail|Analytics',
       'Analytics|Enterprise Software|Cloud Computing|Software Development',
       'Advertising|Market Research',
       'Enterprise Software|Software Development', 'Energy',
       'CleanTech|Analytics|Real Estate|Energy',
       'Security|Cloud Computing', 'CleanTech|Energy',
       'E-Commerce|Enterprise Software|Analytics',
       'E-Commerce|Analytics|Mobile|Retail', 'Entertainment', 'Music',
       'Analytics|E-Commerce',
       'Network / Hosting / Infrastructure|Analytics',
       'E-Commerce|Publishing|Marketing',
       'E-Commerce|Market Research|Analytics|Deals|Finance',
       'Cloud Computing|Energy',
       'Network / Hosting / Infrastructure|Enterprise Software',
       'Career / Job Search', 'Advertising|Analytics',
       'Analytics|Retail|Mobile|Enterprise Software|Market Research',
       'Cloud Computing|E-Commerce|Analytics', 'Analytics|Retail',
       'Search|Social Networking', 'Telecommunications', 'Publishing',
       'Network / Hosting / Infrastructure|Publishing',
       'Classifieds|Network / Hosting / Infrastructure',
       'Media|Advertising|E-Commerce', 'Search|Healthcare',
       'Mobile|Telecommunications',
       'Cloud Computing|E-Commerce|Classifieds', 'Gaming|Entertainment',
       'Food & Beverages', 'Marketing|Mobile|E-Commerce',
       'Mobile|Cloud Computing|Enterprise Software',
       'Music|Media|Software Development', 'Analytics|Advertising',
       'E-Commerce|Analytics|Advertising|Enterprise Software']

	c=st.selectbox("choose an option:",options)
	options_list=['marketing', 'Marketing, sales', 'operations', 'Marketing & Sales',
       'analytics', 'Research', 'Computing', 'Marketing',
       'Sales, marketing', 'Marketing \nsales', 'Technology',
       'marketing, sales', 'Data Management', 'Solution providing',
       'Social Media', 'targeted marketing', 'Community Betterment',
       'Web Analytics', 'Strategy', 'Bug fix', 'Data Integration',
       'malware protection', 'Analytics', 'Social Media optimization',
       'Database Management', 'technology', 'Operations', 'Sales', 'Risk',
       'Marketing, Web Analytics',
       'Strategy, Operations, Finacial Planning', 'Data Collection',
       'marketiing', 'sales', 'e-learning', 'software service',
       'mobile app', 'application', 'analytic', 'software ',
       'SOCIAL MEDIA', 'SOCIAL MEDIA management', 'OPERATIONS',
       'MARKETING', 'PERSONAL APPS', 'consumer behaviour',
       'customer servce', 'CUSTOMER SERVICE', 'APP REVENUE',
       'intellectual property analysis and visualisation', 'retail',
       'data visualization', 'service', 'social media', 'security',
       'operation', 'Marketing, Sales', 'operations, sales, marketing',
       'research',
       'Marketing, Technology, Finance & Accounting, Customer service',
       'Computing, training', 'Operations, marketing',
       'social advertising', 'risk', 'data collection ',
       'development, marketing, and administration', 'IT & Sales',
       'social news', 'web', 'sale', 'Sales & Marketing',
       'social network', 'consumer web', 'writing blog', 'curated web',
       'Recommendation ', 'Marketing,Sales,Risk,Operations',
       'Development Tool', 'Tool',
       'Customer Retention, Customer Feedback', 'Inventory management',
       'Energy saving', 'Optimization, CRM, Pricing', 'games',
       'Marketing, customer targeting', 'entertainment',
       'Search EnginenOptimization', 'Information management', 'strategy',
       'Social media analytics', 'marketing, strategy',
       'customer engagement', 'Marketing, Procurement, Human Resources',
       'CRM, Marketing, Human Resources', 'CRM',
       'Merchandising, Marketing', 'Travel Planning',
       'Data Visualization, Content Marketing, Presentations', 'News',
       'analtics', 'elearning', 'PHONE INTELLIGENCE', 'social branding',
       'reporting', 'DASHBOARDS', 'localized behaviour',
       'VIDEO STREAMING', 'PAYMENT', 'software', 'networking', 'wireless',
       'advertising', 'game', 'search', 'conssumer web', 'online music',
       'media']
	d=st.selectbox("choose focus fnction of company",options_list)
	e=st.text_input("enter the employee count ")
	ops=['No', 'Yes', 'yes', 'YES']
	f=st.selectbox("team size grown",ops)
	g=st.text_input("enter the no of cofounders ")
	h=st.text_input("Team size Senior leadership ")
	i=st.text_input("Team size all employees")
	ops2=['No','Yes']
	j=st.selectbox("worked in top companies",ops2)
	ops3=['No', 'Yes']
	k=st.selectbox("startups in the past",ops3)
	ops4=['No','Yes']
	l=st.selectbox("successfull startups in the past",ops4)
	ops5=['Service', 'Product', 'Both', 'No Info']
	m=st.selectbox("Product or service company",ops5)
	ops6=['Platform', 'cloud', 'Cloud', 'none', 'Both']
	n=st.selectbox("Cloud or platform based serive or product",ops6)
	ops7=['Linear', 'Non-Linear']
	o=st.selectbox("Linear or Non-Linear Business Models",ops7)	
	ops8=['Masters', 'Bachelors', 'PhD']
	p=st.selectbox("Highest Education",ops8)
	q=st.text_input("years of education")
	ops9=['Medium', 'High', 'Low', 'None']
	r=st.selectbox("Experience in selling and building products",ops9)
	mp1=d1.get(c)
	mp2=d2.get(d)
	mp3=d3.get(f)
	mp4=d4.get(j)
	mp5=d5.get(k)
	mp6=d6.get(l)
	mp7=d7.get(m)
	mp8=d8.get(n)
	mp9=d9.get(o)
	mp10=d10.get(p)
	mp11=d11.get(r)
	result=''
	if st.button('submit'):
	     result=start_up_prediction([a,b,mp1,mp2,e,mp3,g,h,i,mp4,mp5,mp6,mp7,mp8,mp9,mp10,q,mp11])
	     st.success(result)


	     
	     
if __name__=='__main__':
	main()
     

