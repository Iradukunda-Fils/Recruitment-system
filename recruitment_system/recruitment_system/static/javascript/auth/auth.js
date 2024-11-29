// Registration Form Validation
const registrationForm = document.getElementById('registration-form');

registrationForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const nameInput = document.getElementById('name');
  const emailInput = document.getElementById('email');
  const passwordInput = document.getElementById('password');
  const confirmPasswordInput = document.getElementById('confirm-password');

  // Perform form validation
  if (nameInput.value.trim() === '') {
    alert('Please enter your name.');
    return;
  }

  if (emailInput.value.trim() === '') {
    alert('Please enter your email address.');
    return;
  }

  if (passwordInput.value.trim() === '') {
    alert('Please enter a password.');
    return;
  }

  if (confirmPasswordInput.value.trim() === '') {
    alert('Please confirm your password.');
    return;
  }

  if (passwordInput.value !== confirmPasswordInput.value) {
    alert('Passwords do not match.');
    return;
  }

  // If all validation passes, submit the form
  registrationForm.submit();
});

// Login Form Validation
const loginForm = document.getElementById('login-form');

loginForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const emailInput = document.getElementById('email');
  const passwordInput = document.getElementById('password');

  // Perform form validation
  if (emailInput.value.trim() === '') {
    alert('Please enter your email address.');
    return;
  }

  if (passwordInput.value.trim() === '') {
    alert('Please enter your password.');
    return;
  }

  // If all validation passes, submit the form
  loginForm.submit();
});

// auth.js

// Add event listener to the form
document.addEventListener('DOMContentLoaded', function() {
  var form = document.querySelector('form.form-container');
  if (form) {
    form.addEventListener('submit', function(event) {
      event.preventDefault();
      // Add any custom form validation or processing logic here
      form.submit();
    });
  }
});