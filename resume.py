import streamlit as st

st.set_page_config(layout="wide")

sidebar = st.sidebar.selectbox('Navigation', ('About Me', 'Projects', 'Resume', 'Contact'))

st.sidebar.write('Other resources:')
st.sidebar.write('[Resume](https://drive.google.com/file/d/1yDmbuPU1cBrUc-cSanBLV1QtgvlSzSsz/view?usp=sharing) (PDF)')
st.sidebar.write('[LinkedIn](https://www.linkedin.com/in/wadem117/)')
st.sidebar.write('[Github](https://github.com/wadem117)')
st.sidebar.write('[Vanderbilt Data Science Institute](https://www.vanderbilt.edu/datascience/person/michael-wade/)')

if sidebar == 'About Me':
    col1, col2 = st.beta_columns(2)

    with col1:
        st.markdown('## Michael Wade, MS')
        st.markdown('Welcome to my page!')
        st.write('I am currently a second-year student in the Master of Data Science'
                 ' Program at Vanderbilt University in Nashville, TN. In 2017, I received a '
                 ' BS in Biological Sciences from DePaul University in Chicago, IL.')
        st.write('I have a diverse background in working with data. My initial research involved '
                 'statistical modeling with an emphasis on population ecology. This led to several '
                 'projects with the College of Science and Health at DePaul University. My independent '
                 'research with the [LaMontagne Lab] (http://lamontagnelab.weebly.com/) served as the '
                 'subject for my Honors Program Thesis at DePaul in 2017.')
        st.write('In 2016, I completed a summer research fellowship with Lincoln Park Zoo in Chicago, IL. '
                 'My primary focus was managing the LPZ animal behavior database and aiding in the '
                 'development of the widely-used [ZooMonitor](https://zoomonitor.org/home) application. '
                 'I also performed an independent behavioral study involving African Wild Dogs, which I '
                 'presented at multiple conferences.')
        st.write('More recently, my research has shifted into machine learning, database development, '
                 'artificial intelligence, and working with big data. At Vanderbilt, I have collaborated '
                 'with the [Latin American Public Opinion Project](https://www.vanderbilt.edu/lapop/) to '
                 'develop an interactive data visualization dashboard, and I am currently working with a '
                 'team to develop a financial wellness application for professional athletes.')
        st.write('I believe strongly in the extraordinary possibilities achievable through rigorous '
                 'research and effective applications of data tools. Wherever possible, I seek to be '
                 'involved in the '
                 'scientific process. I served as the co-founder and president for DePaul Ecology, '
                 'Evolution, and Physiology, a student organization focused on collaboration and service '
                 'across a variety of STEM fields. I have also assisted the lab of [Dr. Philip Matich]'
                 '(https://www.tamug.edu/marb/faculty-bios/PhilipMatich.html) in performing estuarine shark '
                 'surveys, and have served as a guest lecturer in statistics and analytics with the '
                 '[School for Science and Math at Vanderbilt](https://www.vanderbilt.edu/cseo-ssmv/).')

    with col2:
        st.image('https://raw.githubusercontent.com/wadem117/profile/main/images/headshot.jpg',
                 caption='(2019) First day at the Vanderbilt Data Science Institute', use_column_width=True)
        st.write('')
        st.image('https://raw.githubusercontent.com/wadem117/profile/main/images/collab.jpg',
                 caption='(2016) Collecting animal behavior data at Lincoln Park Zoo', use_column_width=True)
        st.write('')
        st.image('https://raw.githubusercontent.com/wadem117/profile/main/images/shark.png',
                 caption='(2018) Performing a shark survey with Sam Houston State University',
                 use_column_width=True)


if sidebar == 'Projects':
    st.title('Projects')
    st.write('This page contains a list of some of my recent research and data science projects, along '
             ' with an overview of the significant conclusions of each and any corresponding materials. '
             ' Click to expand each topic.')
    st.write('')
    happiness = st.beta_expander("Analyzing National Ecological Footprint with Unsupervised Learning")
    with happiness:
        col1, col2 = st.beta_columns(2)
        with col1:
            st.markdown('## Analyzing National Ecological Footprint with Unsupervised Learning')
            st.write('Fall 2019')
            st.write('_Key elements: clustering, PCA, linear regression_')
            st.write('For this project, I worked with a team to analyze differences in national ecological'
                     ' footprints using several methods, including clustering analysis, model selection,'
                     ' and regression modeling. We correlated these results with other factors, such as GDP'
                     ' and national happiness survey findings.')
            st.write('Our primary findings were that national happiness tended to increase as ecological '
                     'footprint decreased within a country. This relationship was stronger for countries '
                     'with a higher GDP. ')
            st.write('We presented our findings to an interdisciplinary audience'
                     ' within the Vanderbilt community and beyond.')
            st.write('[Click here](https://drive.google.com/file/d/1rE9CUmiJrzawaDJ8degsIOqWXPIg7nWs/view?usp=sharing)'
                     ' to view our report.')

        with col2:
            st.image('https://raw.githubusercontent.com/wadem117/profile/main/images/cluster1.png', width=400)
            st.image('https://raw.githubusercontent.com/wadem117/profile/main/images/cluster2.png', width=400)

    spruce = st.beta_expander('Modeling Individual Growth of White Spruce in North America')
    with spruce:
        col1, col2 = st.beta_columns(2)
        with col1:
            st.markdown('## Modeling Individual Growth of White Spruce in North America')
            st.write('2015 - 2017')
            st.write('_Key elements: linear regression, correlation, model selection_')
            st.write("As an undergraduate biology student at DePaul University, I completed an"
                     " independent research project while working in Dr. Jalene LaMontagne's [population"
                     " ecology lab](http://lamontagnelab.weebly.com/).")
            st.write("This project involved modeling individual growth within white spruce"
                     " populations in Eastern North America.")
            st.write('The study involved analyzing growth differences between local populations over'
                     ' two distinct distance classes: between inland and lakeshore sites near Lake Superior, '
                     ' and between sites in Michigan, Ontario, and New Brunswick.')
            st.write('My main findings were that growing season temperature shares a significant relationship'
                     ' with annual residual growth. Specifically, warmer growing seasons are associated '
                     ' with less annual growth at the Michigan site and more annual growth at the New Brunswick'
                     ' site.')
            st.write('The conclusions of this project reveal potentially impactful information with regards'
                     ' to global climate change and the resilience of spruce populations. I presented this work'
                     ' at several research conferences, including the Midwest Ecology and Evolution Conference'
                     ' 2016 and the Chicago Area Undergraduate Research Symposium 2016.')
            st.write('[Click here](https://drive.google.com/file/d/13ciXwIcpflpa1JESwLtaKMk8yZPefST9/view?usp=sharing) '
                     ' to view the full report.')

        with col2:
            st.image('https://raw.githubusercontent.com/wadem117/profile/main/images/spruce3.png', width=400)
            st.image('https://raw.githubusercontent.com/wadem117/profile/main/images/spruce4.png', width=400)

    dogs = st.beta_expander('Modeling Stereotypic Behaviors in African Wild Dogs')
    with dogs:
        col1, col2 = st.beta_columns(2)
        with col1:
            st.markdown('## Modeling Stereotypic Behaviors in African Wild Dogs')
            st.write('Summer 2016')
            st.write('_Key elements: model selection, PCA, hypothesis testing_')
            st.write('While working as an animal research intern at Lincoln Park Zoo, I performed an independent'
                     ' study which sought to build understanding of stereotypic behaviors, or behaviors that are'
                     ' repetitive and have negative connotations, and their environmental triggers. For individuals '
                     ' in captivity, behavioral variation is an important consideration for welfare standards, '
                     ' and may be influenced by a number of factors, such as temperature, sound levels, crowd size, '
                     ' and weather.')
            st.write('Model selection and principal components analysis were used to determine which combinations '
                     ' of explanatory variables best explained the observed variation in behavioral richness. '
                     ' Ambient temperature alone was shown to have the greatest probability of explaining behavioral '
                     ' variation, but not at a substantially higher likelihood than the other models. Behavioral '
                     ' richness was shown to vary significantly at different times of the day, suggesting behavior '
                     ' is influenced by daily schedule.')
            st.write('I presented this research at multiple conferences, including the DePaul College of Science '
                     ' and Health Undergraduate Research Symposium in 2016.')
            st.write('[Click here](https://drive.google.com/file/d/1Hp7i4WLUzraG0AGuQ4ucWm6tBxfy-v_u/view?usp=sharing)'
                     ' to view the poster.')

        with col2:
            st.image('https://raw.githubusercontent.com/wadem117/profile/main/images/zoo.jpg', width=400)
            st.image('https://raw.githubusercontent.com/wadem117/profile/main/images/zoo2.png', width=400)

    other = st.beta_expander('Other reports and presentations')
    with other:
        st.write('* [Exploring life expectancy of zoo animals with clustering]'
                 '(https://drive.google.com/file/d/1vgy0ri0aSSIj5ueD5xp1P3hlE7aAWGrO/view?usp=sharing)')
        st.write('* [Estuarine microorganism population survey]'
                 '(https://drive.google.com/file/d/1rE9CUmiJrzawaDJ8degsIOqWXPIg7nWs/view?usp=sharing)')

if sidebar == 'Resume':
    st.title('Resume')
    st.markdown('## Michael Wade, MS')
    education = st.beta_expander('Education')
    with education:
        col1, col2, col3 = st.beta_columns(3)
        with col1:
            st.write('**MS, Data Science**')
        with col2:
            st.write('**Vanderbilt University, Nashville, TN**')
        with col3:
            st.write('**2021 (Expected)**')

        st.write('_Activities and Honors_:')
        st.write('* Teaching Assistantship, Exploratory Data Analysis (2020)')
        st.write('* Graduate student mentor (2020 - Present)')
        st.write('')

        col1, col2, col3 = st.beta_columns(3)
        with col1:
            st.write('**BS, Biological Sciences (Honors)**')
        with col2:
            st.write('**DePaul University, Chicago, IL**')
        with col3:
            st.write('**2017**')

        st.write('_Activities and Honors_:')
        st.write("* Fellow, Dean's Undergraduate Research Assistantship (2015 - 2017)")
        st.write("* Fellow, College of Science and Health Undergraduate Research Assistantship Program (2015 – 2017)")
        st.write("* University Honors Program (2013 - 2017)")

    experience = st.beta_expander('Professional Experience')
    with experience:
        col1, col2, col3 = st.beta_columns(3)
        with col1:
            st.write('**Database Developer (Contract)**')
        with col2:
            st.write('Raise the Roof Academy (Nashville, TN)')
        with col3:
            st.write('2020 - Present')
        st.write('I am developing a robust database based in MySQL and front-end interface based in Python for '
                 'Raise the Roof Academy, a non-profit community development organization based in central Uganda. '
                 'This application is hosted using Amazon Web Services.')
        st.write('')

        col1, col2, col3 = st.beta_columns(3)
        with col1:
            st.write('**Graduate Teaching Assistant**')
        with col2:
            st.write('Vanderbilt Data Science Institute (Nashville, TN)')
        with col3:
            st.write('2020')
        st.write('I served as a teaching assistant for Exploratory Data Analysis, a graduate-level course offered by '
                 'the Data Science Institute at Vanderbilt University. My responsibilities included co-managing the '
                 'course Github repository, grading assignments, and providing academic support for students.')
        st.write('')

        col1, col2, col3 = st.beta_columns(3)
        with col1:
            st.write('**Editorial Assistant**')
        with col2:
            st.write('Vanderbilt University Medical Center (Nashville, TN)')
        with col3:
            st.write('2018 - 2020')
        st.write("I served as the editorial assistant for VUMC's Department of Biostatistics and Center for "
                 " Quantitative Sciences. This role involved reviewing and editing research manuscripts prior "
                 " to publication, managing grant materials, and providing analytical summaries of events and "
                 " department offerings.")
        st.write('')

        col1, col2, col3 = st.beta_columns(3)
        with col1:
            st.write('**Undergraduate Research Assistant**')
        with col2:
            st.write('DePaul University (Chicago, IL)')
        with col3:
            st.write('2015 - 2017')
        st.write('I completed an independent research project which determined effects of local and distant '
                 'temperature changes on the growth of White Spruce in North America. This project involved data '
                 'collection and cleaning, data visualization, statistical modeling, and communicating results at '
                 'professional conferences.')
        st.write('')

        col1, col2, col3 = st.beta_columns(3)
        with col1:
            st.write('**Animal Research Intern**')
        with col2:
            st.write('Lincoln Park Zoo (Chicago, IL)')
        with col3:
            st.write('2016')
        st.write('I collected, analyzed, visualized, and presented animal behavior data as part of the Lincoln '
                 'Park Zoo Conservation & Science ZooMonitor Project. I also managed a team of volunteers who '
                 'contributed to a local animal behavior database.')

    service = st.beta_expander('Service')
    with service:
        col1, col2, col3 = st.beta_columns(3)
        with col1:
            st.write('**Guest Lecturer, Statistics & Analytics**')
        with col2:
            st.write('School for Science and Math at Vanderbilt (Nashville, TN)')
        with col3:
            st.write('2018')
        st.write('I provided a series of lectures and corresponding activities related to statistical '
                 'methods in STEM applications to a group of high-performing students from Metro Nashville'
                 'Public Schools')
        st.write('')

        col1, col2, col3 = st.beta_columns(3)
        with col1:
            st.write('**President & Co-Founder**')
        with col2:
            st.write('DePaul Ecology, Evolution, & Physiology (Chicago, IL)')
        with col3:
            st.write('2016-2017')
        st.write("I worked alongside several faculty to create a student organization based on allied "
                 "organismal biology fields, with a commitment to welcoming all who seek to better understand "
                 "the subjects in our focus, which are vital to preserving the health of our planet, as well "
                 "as furthering the collective appreciation for the natural world, and represent an urgent "
                 "need in the face of expanding human impact on our climate. I served as the organization's "
                 "founding president from 2016-2017.")

    skills = st.beta_expander('Technical skills')
    with skills:
        st.write('**Programming**')
        st.write('Python, R')
        st.write('')

        st.write('**Database Management**')
        st.write('MySQL, NoSQL')
        st.write('')

        st.write('**IDEs**')
        st.write('PyCharm, Jupyter Notebooks/Lab, Visual Studio Code, RStudio, MySQL Workbench')
        st.write('')

        st.write('**Machine Learning**')
        st.write('scikit-learn, TensorFlow, PyTorch')
        st.write('')

        st.write('**Cloud Services**')
        st.write('AWS, Microsoft Azure, Google Cloud')
        st.write('')

        st.write('**Other**')
        st.write('Github, Microsoft Office Suite, REDCap')

if sidebar == 'Contact':
    st.title('Contact')
    st.markdown('### Email:')
    st.write('[michael.wade@vanderbilt.edu](mailto:michael.wade@vanderbilt.edu)')
