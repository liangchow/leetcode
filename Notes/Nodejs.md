# Node.js Notes

## Setup Quickguide
1. Install node.js by using `npm -init -y`. 
2. Add dependencies, for example, `npm -i express firebase-admin cors stripe dotenv`.
3. Create a new file called `server.js` in root folder. 
4. Under "scripts", add `"dev": "nodemon server.js"` in `package.json`:
    ```
    "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "dev": "nodemon server.js"
    },
    ```
4. Install `nodemon` using `npm i --save-dev nodemon`.
5. Now, you should be able to run server by typing `npm run dev` in the terminal.


## Optimize Email Signup Functionality

### Front End

- **Email validation**: Use regex to validate input.
- **Error handling**: Check response status and catch errors. 
- **UI feedback**: Disable button during request to prevent double submissions
- **Enter key support**: Press Enter to submit.
- **Message management**: Properly show/hide messages
- **Auto rest**: Clears success message after 3 seconds

```
const input = document.getElementById('userEmail')
const signup_btn = document.getElementById('signup_btn')
const errMsg = document.querySelector('.errMsg')
const subMsg = document.querySelector('.subMsg')

// Hide messages initially
errMsg.style.display = 'none'
subMsg.style.display = 'none'

// Email validation regex
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/

async function signupNewUser() {
    const user_email = input.value.trim()
    
    // Hide all messages
    errMsg.style.display = 'none'
    subMsg.style.display = 'none'
    
    // Validate email
    if (!user_email || !emailRegex.test(user_email)) {
        errMsg.style.display = 'inline'
        return
    }
    
    // Disable button during request
    signup_btn.style.pointerEvents = 'none'
    signup_btn.style.opacity = '0.6'
    
    try {
        const res = await fetch('/signup', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: user_email })
        })
        
        if (!res.ok) {
            throw new Error('Signup failed')
        }
        
        // Success
        subMsg.style.display = 'inline'
        input.value = ''
        input.disabled = true
        
        // Optional: Re-enable after 3s delay
        setTimeout(() => {
            input.disabled = false
            subMsg.style.display = 'none'
        }, 3000)
        
    } catch (err) {
        console.error('Signup error:', err)
        errMsg.style.display = 'inline'
    } finally {
        // Re-enable button
        signup_btn.style.pointerEvents = 'auto'
        signup_btn.style.opacity = '1.0'
    }
}

// Event listeners
signup_btn.addEventListener('click', signupNewUser)

// Allow Enter key to submit
input.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        signupNewUser()
    }
})
```

### Server Endpoint (Node.js)

- **Response handling**: Returns proper JSON response with `res.json()`.
- **Email validation**: Server side validation for security. 
- **Timestamp**: Uses `subscribeAt` to track when users join.
- **Error logging**: Console log for debugging.

```
app.post('/signup', async (req, res) => {
    const newEmail = (req.body && req.body.email || '').trim()
    
    if (!newEmail) {
        return res.status(400).json({ message: 'Email required' })
    }
    
    // Basic email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!emailRegex.test(newEmail)) {
        return res.status(400).json({ message: 'Invalid email format' })
    }
    
    try {
        await db.collection('users').doc(newEmail).set(
            { 
                email: newEmail,
                subscribedAt: new Date().toISOString()
            }, 
            { merge: true }
        )
        
        // Send success response
        res.status(200).json({ 
            message: 'Successfully subscribed!',
            email: newEmail 
        })
        
    } catch (err) {
        console.error('Firebase error:', err)
        res.status(500).json({ message: 'Failed to register' })
    }
})

```
