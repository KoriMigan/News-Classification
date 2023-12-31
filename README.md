# East Africa News Classification
> The main objective of this project was to develop a machine learning model that can accurately classify East African news articles into relevant categories or topics. Through this project, we have met this objective, and also obtained the following results: accuracy of predicting the swahili news category is at around 81%. This meets and surpasses our success metric of 75% accuracy.
> News articles were obtained from kaggle containing over 20,000 rows and additional data was scraped from TAIFA LEO website.
> The column <b>label</b> is the target. It contains 6 distinct categories.
> The rationale for predicting this target is to aid news companies classify their articles without necessarily knowing the theme of the article.
> The final model i.e. <b>Random Forest</b> perfomed well as described above.

---
![alt text](image.jpeg)

![numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)  ![pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)   ![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)    ![scikitlearn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)    ![nlp](https://img.shields.io/badge/nlp-209117?style=for-the-badge&logo=nlp&logoColor=white)
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
> 
## Specific Objectives
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
> To Reproduce the project, follow these steps:
1. Clone the repository
2. Install the requirements.txt file ( `pip install -r requirements.txt` )
3. Run the application (`python api.py')
4. The terminal should give you a local URL in the form ( `http://localhost:5000` )
5. [Link to download original dataset](https://www.kaggle.com/datasets/thedevastator/east-african-news-classification) 
---
### [Usage](#usage)
> To test the news API, follow these steps:
1. Donwload and install postman
2. Paste the URL (`http://localhost:5000`) in the GET bar the add the predict extension such that the URL on postman look this way (`http://localhost:5000/predict`)
3. In the KEY section write 'text' and check the checkbox then paste the article in the 'value' section.
4. Hit the blue button SEND
5. You should see the output at the bottom of the screen.
---
### [Contributors](#contributors)
>
> The following people have contributed to this project:
- [Fiona Njuguna](https://github.com/KoriMigan)
- [Fiona Kungu](https://github.com/Fiona-Kungu)
- [Daniel Nyamweya](https://github.com/Daniel1999Akama)
- [Edwin Muhiu](https://github.com/rurungamuhia)
- [Steve Githinji](https://github.com/stevegithinji)
- [Winfred Muthoni](https://github.com/WinnieKabuya)
---
### [License](#license)
> This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details
---
### [Acknowledgements](#acknowledgements)
#### Institution
- [Moringa School](https://moringaschool.com/)
#### Technologies Used
- [Flask](https://flask.palletsprojects.com/) for deploying model as API.
- [Scikit-learn](https://scikit-learn.org/) for creating the models.
- [NLTK](https://www.nltk.org/) for text preprocessing.
- [Pandas](https://pandas.pydata.org/) for data manipulation.
- [Matplotlib](https://matplotlib.org/) for visulizations.
- [Postman](https://www.postman.com/downloads/) for testing the API.
---
> Thank you for reading this README.md file. If you have any questions, please contact the contributors of this project.
