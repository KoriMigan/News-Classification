# East Africa News Classification
![numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)  ![pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)   ![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)    ![scikitlearn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)    ![nlp](https://img.shields.io/badge/nlp-209117?style=for-the-badge&logo=nlp&logoColor=white)
> The main objective of this project was to develop a machine learning model that can accurately classify East African news articles into relevant categories or topics. Through this project, we have met this objective, and also obtained the following results: accuracy of predicting the swahili news category is at around 81%. This meets and surpasses our success metric of 75% accuracy.
---
## Table Of Contents
- [East Africa News Classification](#East-Africa-News-classification)
  - [Table Of Contents](#table-of-contents)
    - [Business Objectives](#business-objectives)
    - [Project Overview](#project-overview)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Contributors](#contributors)
    - [License](#license)
    - [Acknowledgements](#acknowledgements)
      - [Institution](#institution)
      - [Technologies Used](#technologies-used)
---
### Business Objectives
---
> #### General Objectives
> * Ensure consistency and accuracy in news categorization.
> * Streamline the news outlet's operations by implementing a robust text classification model.
> ####Specific Objectives
> * To develop a machine learning model that can accurately classify East African news articles into relevant categories or topics.
> * To provide an API that integrates with existing news platforms or search engines, enabling easy adoption and integration for news organizations and content providers.
---
### Project Overview
---
> This project followed the CRISP-DM process. The CRISP-DM process is a data mining process model that describes commonly used approaches that data mining experts use to tackle problems. The CRISP-DM process is divided into six phases; Business Understanding, Data Understanding, Data Preparation, Modelling, Evaluation, and Deployment. The following is a brief description of each phase:
---
- **Business Understanding**: Exploring the business reasons for our data mining effort and what the company hopes to gain from the project. This is done by attempting to come up with an model that classifies articles using an API.
- **Data Understanding**: The datasets we utilized comprised of 2 datasets; News classification from kaggle and scraped data from Taifa leo.
- **Data Preparation**: It mainly involved; selecting the data to discover the columns to be used, cleaning the data to correct and remove erroneous values, and integrating the datasets to create a merged dataset for effective analysis.
- **Preprocessing**: The goal of this procedure is to prepare the data for modelling.
- **Modelling**: To further support and provide insight we built various models from a baseline to more complex models.
- **Evaluation**: Accuracy was used to measure the correcteness of classification in general.
- **Recommendation and Conclusion**: it involved offering opinions based on the whole process, proposing a solution to the gap discovered in the research that needs to be filled, and the next steps to be undertaken in future analysis.
---
### [Installation](#installation)
> To install the project, follow these steps:
1. Clone the repository
2. Install the requirements.txt file ( `pip install -r requirements.txt` )
3. Run the application (`python api.py')
4. Open the application in your browser ( `http://localhost:5000` )
---
### [Usage](#usage)
> To test the news API, follow these steps:
1. Donwload and install postman
2. Paste the URL (`http://localhost:5000`) in the GET bar.
3. In the KEY section write 'text' then paste the article in the 'value' section.
4. You should see the output at the bottom.
---
### [Contributors](#contributors)
>
> The following people have contributed to this project:
- [Fiona Njuguna](https://github.com/KoriMigan)
- [Fiona Kungu]
- [Daniel Nyamweya](https://github.com/Daniel1999Akama)
- [Edwin Muhiu](https://github.com/rurungamuhia)
- [Steve Githinji]
- [Winfred Muthoni](https://github.com/WinnieKabuya)
---
### [License](#license)
> This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details
---
### [Acknowledgements](#acknowledgements)
#### Institution
- [Moringa School](https://moringaschool.com/)
#### Technologies Used
- [Flask](https://flask.palletsprojects.com/)
- [Scikit-learn](https://scikit-learn.org/)
- [NLTK](https://www.nltk.org/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Postman](https://www.postman.com/downloads/)
---
> Thank you for reading this README.md file. If you have any questions, please contact the contributors of this project.
