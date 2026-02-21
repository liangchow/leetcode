# Node.js Notes

## Table of Contents
1. [Setup Quickguide](#setup-quickguide)
2. [Optimize Email Signup Functionality](#optimize-email-signup-functionality)
    - [Utility Functions](#utility-functions)
    - [Front End](#front-end)
    - [Script Obfuscation (Front End)](#script-obfuscation-front-end)
    - [Server Endpoint (Node.js)](#server-endpoint-nodejs)
3. [Additional References](#additional-references)


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

### Utility Functions
- **Sanitize inputs**: Trim whitespace and remove `<>` to prevent malicious script tags uploaded.
```
function sanitizeInput(input) {
    if (typeof input !== 'string') return ''
    return input.trim().replace(/[<>]/g, '')
}
```
- **Validate email**: Validate email formatting
```
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return emailRegex.test(email) && email.length <= 254 //RFC 5321
}
```
- **Limit rate**: Basic in-memory implementation
```
const rateLimitMap = new Map()
const RATE_LIMIT_WINDOW = 60000    //1 minute
const MAX_REQUEST = 5

function checkRateLimit(id){
    const now = Date.now()
    const userRequests = rateLimitMap.get(id) || []

    // Remove old requests outside the timeframe
    const recentRequests = userRequests.filter(time => now - time < RATE_LIMIT_WINDOW>)

    if (recentRequests.length >= MAX_REQUESTS){
        return false  //Rate limit exceeded
    }

    recentRequests.push(now)
    rateLimitMap.set(id, recentRequests)
    return true
}
```

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
### Script Obfuscation (Front End)
- Compile with **babel.js**: Babel is used to compile modern JavaScript (ES6+) into a version that is compatible with older browsers and maintains cross-browser compatibility.
- Obfuscate


### Server Endpoint (Node.js)

- **Response handling**: Returns proper JSON response with `res.json()`.
- **Email validation**: Server side validation for security. 
- **Timestamp**: Uses `subscribeAt` to track when users join.
- **Error logging**: Console log for debugging.

```
app.post('/signup', async (req, res) => {
    try {

        const rawEmail = req.body?.email || ''
        const newEmail = sanitizeInput(rawEmail).toLowerCase()
        
        if (!newEmail) {
            return res.status(400).json({ message: 'Email required' })
        }
        
        // Basic email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
        if (!emailRegex.test(newEmail)) {
            return res.status(400).json({ message: 'Invalid email format' })
        }
        
        // Check email already exists and is active. Enable re-subscription.
        if (userDoc.exists && userDoc.data().active === true){
            return res.status(400).json({message: "You're already subscribed"})
        }

        await db.collection('users').doc(newEmail).set({ 
            email: newEmail,
            subscribedAt: FieldValue.serverTimestamp(),
            active: true, 
         }, { merge: true })
        
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
## Additional References
[How to Add JavaScript to HTML for Beginners](https://www.digitalocean.com/community/tutorials/how-to-add-javascript-to-html)
