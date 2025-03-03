function generateUserId(prefix) {
    return '${prefix}-${Math.random().toString(36).substr(2, 9)}';
}

function generatePassword() {
    return Math.random().toString(36).substr(2, 8);
}

function registerUser(type) {
    const email = document.getElementById('email').value;
    const document = document.getElementById('document').files[0];

    const userId = generateUserId(type === 'voter' ? 'VOTER' : 'CANDIDATE');
    const password = generatePassword();

    const formData = new FormData();
    formData.append('email', email);
    formData.append('document', document);
    formData.append('user_id', userId);
    formData.append('password', password);
    formData.append('user_type', type);

    fetch('/register', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        if (data.success) {
            resultDiv.innerHTML = `
                <p>Registration successful!</p>
                <p>User ID: ${userId}</p>
                <p>Password: ${password}</p>
            `;
        } else {
            resultDiv.innerHTML = `
                <p>Registration failed: ${data.message}</p>
            `;
        }
    })
    .catch(error => {
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `
            <p>Registration failed: ${error.message}</p>
        `;
    });
}

function loginUser() {
    const userId = document.getElementById('user_id').value;
    const password = document.getElementById('password').value;

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user_id: userId,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        if (data.success) {
            window.location.href = '/success';
        } else {
            resultDiv.innerHTML = `
                <p>Login failed: ${data.message}</p>
            `;
        }
    })
    .catch(error => {
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `
            <p>Login failed: ${error.message}</p>
        `;
    });
}