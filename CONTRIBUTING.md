# Contributing

Contributions are welcome and greatly appreciated! If you would like to contribute to this project, please follow these guidelines:

1. **Fork the Repository**

Click the "Fork" button at the top right of this page to create your own copy of the repository.

2. **Create a Branch**

Create a branch for your feature or bug fix:

```bash
git checkout -b feature/your-feature-name
```

3. **Add/Edit Applications**

To add a new Flask application:

- Create a new folder with the application name.
- Include the following files:

```bash
`Dockerfile`: Defines how the application will be containerized.

`app.py`: The main Flask application logic.

`test_app.py`: Unit tests to validate the correctness of the API.

`requirements.txt`: List of dependencies.

`README.md`: Documentation for the application.
```

4. Update the bash script and GitHub Actions workflow if needed.

5. Run Tests

Ensure your changes do not break existing functionality by running the tests:

6. Commit Changes

Write clear and concise commit messages:

```bash
git commit -m "Add: Description of your change"
```

7. Push Changes

Push your branch to your forked repository:

```bash
git push origin feature/your-feature-name
```

8. Open a Pull Request

Navigate to the original repository and open a pull request (PR). Provide a detailed description of your changes and why they should be merged.
