# Vibezz 🎭✨

AI-powered poem generator that creates personalized verses using Google Gemini. Share your feelings through beautiful, custom poetry.

## Features

- 🎨 **Personalized Poetry**: Generate poems based on theme, mood, and recipient
- 🧠 **AI-Powered**: Uses Google Gemini AI for creative content generation
- 💾 **Database Storage**: Saves all generated poems with metadata
- 🎯 **Input Validation**: Secure input handling and sanitization
- 📱 **Responsive Design**: Clean, modern UI that works on all devices
- ⚡ **Real-time Generation**: Fast poem creation with loading states

## Tech Stack

- **Backend**: Django (Python)
- **AI**: Google Gemini API
- **Database**: SQLite (development)
- **Frontend**: HTML, CSS, Vanilla JavaScript
- **Styling**: Custom CSS with gradient themes

## Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd vibezz
   ```

2. **Install dependencies**
   ```bash
   pip install django python-decouple requests
   ```

3. **Environment setup**
   Create `.env` file:
   ```env
   SECRET_KEY=your-django-secret-key
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost
   GEMINI_API_KEY=your-gemini-api-key
   ```

4. **Database setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the application**
   ```bash
   python manage.py runserver
   ```

6. **Visit** `http://127.0.0.1:8000/`

## Usage

1. Enter a **theme** (e.g., love, nature, friendship)
2. Select a **mood** from the dropdown
3. Specify **recipient** (e.g., my partner, myself, friend)
4. Click "Generate Vibezz" and enjoy your personalized poem!

## API Endpoints

- `GET /` - Home page with poem generator interface
- `POST /get-vibe/` - Generate poem endpoint
  ```json
  {
    "theme": "love",
    "mood": "romantic", 
    "for": "my partner"
  }
  ```

## Security Features

- ✅ Input validation and sanitization
- ✅ SQL injection protection via Django ORM
- ✅ Environment variable configuration
- ✅ Error handling without information disclosure
- ✅ Request timeout protection
- ✅ Malicious pattern detection
- ✅ **Rate limiting** - 5 requests per minute per IP address

## TODO

### Immediate Security Improvements
- [x] **Add rate limiting** - ✅ Implemented (5 requests/minute per IP)
- [ ] **Add CSRF protection** - Secure form submissions

### Features in the Pipeline
- [ ] **Image Generation** - Create visual art based on the poem content
- [ ] **Social Media Sharing** - Generate beautiful poem + image snapshots
- [ ] **Download Functionality** - Export snapshots for sharing

### Future Enhancements
- [ ] User authentication and poem history
- [ ] Multiple poem styles and formats (haiku, sonnet, etc.)
- [ ] Favorite poems collection

**Made with ❤️ and AI magic** ✨

*Transform your emotions into beautiful poetry with Vibezz!*
