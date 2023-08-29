# Resume Generator Django Project

This Django project allows you to create a resume by entering your details and generates a PDF format of your resume.

## Installation and Setup

1. **Clone the Repository**

    ```bash
    git clone [repository_url]
    cd resume-generator-django
    ```

2. **Create Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Database Setup**

    ```bash
    python manage.py migrate
    ```

5. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

6. **Access the Application**

    Open your web browser and go to: `http://127.0.0.1:8000`

## Usage

1. Access the web application using the provided URL.

2. Fill in your details in the respective fields, including Name, Summary, Phone, School, University, Degree, Email, Experience, and Skills.

3. Click on the "Generate Resume" button.

4. Your resume details will be displayed on the page.

5. Click on the "Download PDF" button to download your resume in PDF format.

## Contributing

Contributions are welcome! If you have any improvements or new features to suggest, please create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
