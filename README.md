# Simple AI Agent

This project is a simple AI agent with a web interface that can perform three tasks: searching, calculating, and listing files.

## How to Run Locally

1.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Run the application:
    ```bash
    python app.py
    ```

3.  Open your browser and go to `http://127.0.0.1:5000`.

## How to Run on Google Colab

1.  Open the `run_in_colab.ipynb` file in Google Colab.

2.  Run the cells in the notebook sequentially.

3.  The output of the final cell will provide a public URL. Click on the URL to open the web interface.

## How to Deploy to Heroku

1.  Create a Heroku account and install the Heroku CLI.

2.  Log in to Heroku:
    ```bash
    heroku login
    ```

3.  Create a new Heroku app:
    ```bash
    heroku create
    ```

4.  Push the code to Heroku:
    ```bash
    git push heroku main
    ```

5.  Open the app in your browser:
    ```bash
    heroku open
    ```
