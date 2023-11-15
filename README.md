# Custom GPT with Third-Party API Integration

## Overview

This repository demonstrates the process of integrating a production-ready third-party API with a custom GPT (Generative Pre-trained Transformer). Unlike using a playground environment, this project focuses on deploying a serverless API using Firebase functions for scalability and efficiency. The primary use-case involves connecting Google Analytics Data API to a custom GPT for insightful analytics. This setup can be adapted for various APIs, making it a versatile solution for custom GPT applications.

## Setup and Installation

1. **Initial Setup:**
   - Create and clone a new GitHub repository.
   - Install Firebase CLI using npm: `npm -g install firebase-tools`.
   - Initialize Firebase functions in your project folder: `firebase init functions`.

2. **Service Account Setup:**
   - Generate a service account key from Google Cloud Console.
   - Securely store the key in the functions directory (do not commit to GitHub).

3. **Function Development:**
   - Modify the example function in [main.py](https://github.com/VRSEN/custom-gpt-api-tutorial/functinos/main.py) to suit your application.
   - Implement simple hardcoded token authentication for internal use.
   - Initialize the Google client (if needed) using the `from_service_account_file` function.

4. **Schema Definition:**
   - Define the OpenAI function schema using the instructor library.
   - Implement models such as `GA4QueryParams`, `DimensionSchema`, `MetricSchema`, and `DateRangeSchema`.

5. **API Endpoint Creation:**
   - Construct the API request body and define the logic for the endpoint.
   - Deploy the function using `firebase deploy —only functions`.

6. **OpenAPI Schema Generation:**
   - Run the schema definition file to generate the OpenAPI schema.
   - Update the schema with the deployed function's endpoint URL.

## Testing and Deployment

- Test the integration by creating a custom GPT in the GPT builder.
- Use the OpenAPI schema to define the GPT's functionality.
- Configure authentication using the API Key (Bearer auth type).

## Custom Function Integration

- Follow similar steps to integrate additional custom functions.
- Define new schemas and update the endpoint logic in main.py.
- Redeploy and update the OpenAPI schema as needed.

## Conclusion

Custom GPTs offer significant potential, especially when tailored for specific business needs. This repository provides a foundational approach for integrating third-party APIs with GPT, allowing for the creation of powerful and efficient AI-driven solutions.

## Feedback and Contribution

Your feedback is valuable. Please feel free to contribute to this project or share your thoughts in the comments section. For any queries or suggestions, open an issue in the repository.

---

Remember to subscribe to the [YouTube channel](https://youtube.com/@vrsen?si=MoNJ0OcxqjsUccQj) for more tutorials and insights into AI and GPT integrations.