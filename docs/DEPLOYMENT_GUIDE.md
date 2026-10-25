# Deployment Guide — AccessMap India

AccessMap India is designed as a cloud-native, zero-dependency static web application paired with a robust Python HTTP server for environments requiring native port binding.

---

## 1. Deploying on Render (Recommended)

Render provides free static web services and native web services.

### Option A: Via Blueprint (`render.yaml`)
1. Fork or push this repository to your GitHub account.
2. Sign in to your [Render Dashboard](https://dashboard.render.com).
3. Click **New +** $\rightarrow$ **Blueprint**.
4. Connect this GitHub repository. Render will automatically read `render.yaml`.
5. Click **Apply**. Render builds and deploys the application with a public `onrender.com` SSL URL.

### Option B: Manual Web Service
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt` (or empty if zero external dependencies)
- **Start Command**: `python server.py`
- **Port**: Automatic (reads `$PORT` variable)

---

## 2. Deploying on Vercel

```bash
npm install -g vercel
cd accessmap-site
vercel deploy --prod
```

---

## 3. Local Development

```bash
# Windows
Start-AccessMap.bat

# Linux / macOS
chmod +x start
./start
```
Navigate to `http://localhost:8000` in any modern web browser.
