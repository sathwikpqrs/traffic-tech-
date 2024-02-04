<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
      font-family: Arial, sans-serif;
    }

    form {
      max-width: 300px;
      margin: 20px auto;
    }

    input {
      width: 100%;
      padding: 10px;
      margin-bottom: 10px;
      box-sizing: border-box;
    }

    button {
      background-color: #4CAF50;
      color: white;
      padding: 10px;
      border: none;
      width: 100%;
      cursor: pointer;
    }
  </style>
  <script>
    document.addEventListener('DOMContentLoaded', function () {
      const registerForm = document.getElementById('registerForm');
      const loginForm = document.getElementById('loginForm');

      registerForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const username = document.getElementById('regUsername').value;
        const password = document.getElementById('regPassword').value;

        // Save credentials to local storage
        localStorage.setItem('username', username);
        localStorage.setItem('password', password);

        alert('Registration successful!');
        registerForm.reset();
      });

      loginForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const username = document.getElementById('loginUsername').value;
        const password = document.getElementById('loginPassword').value;

        // Retrieve credentials from local storage
        const storedUsername = localStorage.getItem('username');
        const storedPassword = localStorage.getItem('password');

        if (username === storedUsername && password === storedPassword) {
          alert('Login successful!');
        } else {
          alert('Invalid credentials. Please try again.');
        }

        loginForm.reset();
      });
    });
  </script>
</head>
<body>

  <form id="registerForm">
    <h2>Register</h2>
    <input type="text" id="regUsername" placeholder="Username" required>
    <input type="password" id="regPassword" placeholder="Password" required>
    <button type="submit">Register</button>
  </form>

  <form id="loginForm">
    <h2>Login</h2>
    <input type="text" id="loginUsername" placeholder="Username" required>
    <input type="password" id="loginPassword" placeholder="Password" required>
    <button type="submit">Login</button>
  </form>

</body>
</html>
