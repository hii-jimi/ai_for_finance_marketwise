# ai_for_finance_marketwise
# MarketWise - Your AI-Powered Finance and Economics Assistant

## Overview

MarketWise is a web application that provides users with an AI-powered chatbot specializing in finance and economics. The chatbot is built using the Gemini API and can answer questions and provide insights on a wide range of topics, including macroeconomics, microeconomics, banking, investments, trade, crypto, corporate finance, public policy, real estate, and behavioral economics.

The application also includes user registration and login functionality with OTP (One-Time Password) verification for enhanced security.

## Features

* **AI-Powered Chatbot:** Ask any question related to finance and economics and receive intelligent responses powered by the Gemini API.
* **Specialized Domain:** The AI assistant is specifically trained in finance and economics, ensuring relevant and accurate information.
* **User Registration:** Securely create an account to access the application.
* **OTP Login:** Log in using a one-time password sent to your registered email for added security.
* **Email Verification:** Verify your email address during registration using an OTP.
* **Potential for Future Database Integration:** The backend is being developed with the potential to integrate databases for storing financial data, economic indicators, and a knowledge base to enhance the chatbot's capabilities.

## Technologies Used

* **Backend:** Django (Python)
* **AI Model:** Google Gemini API
* **Database:** (Currently under development - potential for PostgreSQL, MySQL, etc.)
* **Frontend:** (Likely JavaScript, HTML, CSS - details in the frontend repository if separate)
* **Email:** Django's built-in email functionality

## Setup Instructions

### Backend Setup (Django)

1.  **Clone the repository:**
    ```bash
    git clone <your_repository_url>
    cd backend
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You might need to create a `requirements.txt` file if you haven't already. Include `django`, `google-generativeai`, and any other backend dependencies.)*

4.  **Set up environment variables:**
    * Create a `.env` file in the `backend` directory.
    * Add your Google Gemini API key:
        ```env
        GOOGLE_API_KEY=YOUR_ACTUAL_GEMINI_API_KEY
        ```
    * You might also need to configure email settings in your `backend/settings.py` and add corresponding environment variables (e.g., `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USE_TLS`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`).

5.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser (optional, for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The backend server should now be running at `http://127.0.0.1:8000/`.

### Frontend Setup (If Separate)

* *(Instructions for setting up the frontend will depend on the specific framework or technologies used. If you have a separate frontend repository, include those instructions here. Ensure the frontend is configured to communicate with the backend API at `http://localhost:8000/api/chat/` for the chatbot functionality.)*

## How to Use

1.  **Access the application:** Open your web browser and navigate to the frontend URL (usually `http://localhost:3000` or similar if you have a separate frontend).
2.  **Register:** If you don't have an account, click on the "Register" or "Sign Up" link and fill in the required details. You will receive an OTP via email to verify your account.
3.  **Log In:** Once registered and verified, log in using your email and the OTP sent to you during the login process.
4.  **Chat with the AI:** Once logged in, you should see a chat interface. Type your finance or economics-related questions in the input field and send them. The AI-powered chatbot will respond with relevant information.

## API Endpoints (Backend)

* `/api/chat/` (POST): Endpoint for sending messages to the AI chatbot. Expects a JSON request with a `message` field. Returns a JSON response with the chatbot's `response` and potentially `comparison` data.
* `/api/register/` (POST): Endpoint for user registration. Expects JSON data with `name`, `email`, and `password`.
* `/api/verify_otp/` (POST): Endpoint for verifying the OTP received during registration. Expects JSON data with `email` and `otp`.
* `/api/login_otp/` (POST): Endpoint to request a login OTP. Expects JSON data with `name` and `email`.
* `/api/verify_login_otp/` (POST): Endpoint for verifying the login OTP. Expects JSON data with `email` and `otp`.

## Contributing

*(If you plan to allow contributions to your project, add guidelines here. This might include information on how to fork the repository, create branches, submit pull requests, and coding standards.)*

## License

*(Add your project's license information here. If you're not sure which license to use, you can find helpful resources online, such as choosealicense.com.)*

## Contact

*(Add your contact information or links to your social media profiles if you want to be contacted about the project.)*
