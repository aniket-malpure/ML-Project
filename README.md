# END TO END MACHINE LEARNING PROJECT

This project aims to build an end-to-end Machine Learning (ML) project while adhering to industry standards and best practices. The primary goals are:
- Code Structure: Organize the codebase in a way that enhances readability and accessibility. This involves creating a clear and logical folder structure, using meaningful file names, and following consistent coding conventions.
-  Industry Standards: Implement industry-standard practices for ML project development, including version control, documentation, and modular design.
- Regression Algorithms: Explore and implement various supervised regression algorithms. This will involve:
    - Selecting appropriate regression algorithms based on the nature of the data and problem at hand.
    - Implementing and comparing different regression techniques such as Linear Regression and potentially more advanced methods like Random Forest or Gradient Boosting Regressors.
    - Evaluating the performance of each algorithm using relevant metrics.
- End-to-End Pipeline: Develop a complete ML pipeline that covers all stages from data preprocessing to model deployment. This includes:
    - Data collection and cleaning
    - Feature engineering and selection
    - Model training and hyperparameter tuning
    - Model evaluation and validation
    - Model deployment
- Reproducibility: Ensure that the project is reproducible by using environment management tools and providing clear instructions for setup and execution.
- Documentation: Create comprehensive documentation that explains the project structure, methodology, and how to use and extend the codebase.
By focusing on these aspects, the project aims to demonstrate not only the technical implementation of regression algorithms but also the professional practices that are crucial in real-world ML projects. Additionally, this project uses a virtual environment to manage dependencies.

## Dataset Overview
The dataset contains the following features:
- gender: Student's gender (female/male)
- race_ethnicity: Student's race/ethnicity (grouped A through E)
- parental_level_of_education: Highest education level of the student's parent(s)
- lunch: Type of lunch the student receives (standard or free/reduced)
- test_preparation_course: Whether the student completed a test preparation course (none/completed)
- reading_score: Student's score in reading
- writing_score: Student's score in writing
- math_score: Student's score in math (output)

## Project Structure

- `setup.py`: Key purposes of setup.py:
    - Package metadata: Provides information about the package, including its name, version, author, and license.
    - Dependency management: Specifies the dependencies required by the package, such as other Python packages or libraries.
    - Build and installation: Defines the steps needed to build and install the package, including compiling C extensions, copying files, and running tests.
    - Distribution: Generates distribution files (e.g., source archives, wheel packages) for easy distribution and installation.
- `requirements.txt`: Required Python libraries
- `src`: Package folder
    - `__init__.py`: Defines the src folder as a package
    - `exception.py`: Custom exception handling code for easier debugging
    - `logger.py`: Logs information to identify which processes have run
    - `utils.py`: Contains common functionality for the entire application
    - `components/`
      - `__init__.py`: Bind it into a package
      - `data_ingestion.py`: Contains code to read and split the data
      - `data_transformation.py`: Transforms input data (e.g., one-hot encoding)
      - `model_trainer.py`: Trains models, performs hyperparameter tuning, and evaluates models
    - `pipeline/`
      - `__init__.py`: Binds the folder into a package
      - `predict_pipeline.py`: Predicts new data using generated pickle files
- `artifacts/`: Contains generated CSV data files and pickle files
- `logs/`: Contains all logs
- `notebook/`
    - `data/`: Contains the input dataset file
    - `EDA STUDENT PERFORMANCE.ipynb`: Shows mathematical and graphical analysis of the dataset
- `application.py`: Entry point for the Flask application
- `templates`
    - `index.html`: Home Page
    - `home.html`: Webpage for inputting data to get math score predictions

## Machine Learning Algorithms:
- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor
- Linear Regression
- K Neighbors Regressor
- XGB Regressor
- CatBoost Regressor
- AdaBoost Regressor

## AWS Elastic Beanstalk Deployment:
- Creates a server instance (Linux machine) with an environment to deploy the code
- Requires a python.config file to connect with the application
- Uses CodePipeline to deploy code from this GitHub repository to the AWS Beanstalk instance

## EC2 Instance with ECR Deployment:
- Creates a Dockerfile to package the codebase and set up a base Python image
- Uses a main.yaml file for integration, building and pushing ECR images, and continuous deployment
- AWS ECR manages and deploys private Docker images to EC2 instances
- Sets up a GitHub workflow (GitHub to ECR to EC2 instance)
- Creates an ECR Repository
- Creates an Amazon Linux EC2 instance
- Builds a runner in GitHub to push changes
- Add action secret keys:
    - AWS_ACCESS_KEY_ID
    - AWS_ACCESS_LOGIN_URI
    - AWS_REGION
    - AWS_SECRET_ACCESS_KEY
    - ECR_REPOSITORY_NAME
 
## Azure Web App with Container Registry Deployment:
- Similar to ECR deployment in AWS, Azure offers the same service using Container Registry

# Project Lifecycle

## 1. Project Setup and Environment Configuration
- Create virtual environment
- Install required dependencies
- Set up project structure
- Configure version control (Git)
- Create requirements.txt

## 2. Data Collection and Validation
- Load student performance dataset
- Validate data integrity
- Check for missing values
- Verify data types

## 3. Exploratory Data Analysis (EDA)
- Analyze feature distributions
- Study correlations between features
- Identify patterns in:
  - Gender-based performance
  - Race/ethnicity influence
  - Parental education impact
  - Lunch program effects
  - Test preparation influence
- Create visualizations

## 4. Data Preprocessing
- Handle categorical variables
- Feature scaling/normalization
- Feature engineering
- Split data into training and testing sets
- Create data transformation pipeline

## 5. Model Development
- Implement baseline models
- Train multiple regression algorithms:
  - Linear Regression
  - Random Forest
  - Gradient Boosting
  - Other relevant algorithms
- Hyperparameter tuning

## 6. Model Evaluation
- Calculate performance metrics:
  - R-squared score
- Compare model performances
- Feature importance analysis
- Model interpretation

## 7. Production Pipeline
- Create modular code structure
- Implement logging
- Add exception handling
- Create prediction pipeline
- Save trained models

## 8. Documentation and Reporting
- Document code
- Create README file
- Generate performance reports
- Document deployment instructions
- Create user guide

## 9. Deployment and Maintenance
- Package the application
- Create deployment scripts
- Set up monitoring
- Plan for model updates
