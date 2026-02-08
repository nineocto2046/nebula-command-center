# Nebula Command Center

A real-time dashboard for managing your Nebula AI agents and Notion workspace.

## 🚀 Quick Deploy to GitHub Pages

### Option 1: Automatic (Recommended)
```bash
# Clone your repo
git clone https://github.com/nineocto2046/nebula-command-center.git
cd nebula-command-center

# Copy the dashboard files
cp /path/to/index.html .
cp -r /path/to/.github .

# Push to GitHub
git add .
git commit -m "Deploy Nebula Command Center dashboard"
git push origin main
```

The GitHub Actions workflow will automatically deploy to: **https://nineocto2046.github.io/nebula-command-center/**

### Option 2: Manual GitHub Pages Setup
1. Go to https://github.com/nineocto2046/nebula-command-center/settings/pages
2. Under "Build and deployment":
   - Source: Deploy from a branch
   - Branch: main
   - Folder: / (root)
3. Click Save
4. Wait 1-2 minutes for deployment

## ✨ Features

- **Dashboard**: Real-time overview of all 9 connected agents
- **Knowledge Graph**: Interactive visualization of agent connections
- **Task Manager**: Sync with Notion Tasks database
- **Scheduler**: Manage recurring automations
- **Notion Integration**: Pre-configured with 4 databases:
  - 🧠 Thoughts Database
  - ✅ Tasks Database
  - 💡 Ideas Database
  - 🤖 Agent Jobs Database

## 🔧 Notion Database IDs (Pre-configured)

The dashboard is already configured with your Notion databases:
- Thoughts: `7baef348-c02c-4485-baf1-0b964037d90b`
- Tasks: `21db2dd6-ed97-4887-b48f-7e29e173e261`
- Ideas: `599a14ce-c67b-4d51-b0dc-2a644bef0c6e`
- Agent Jobs: `423d9075-8180-4fcb-be7a-b6408c6d0197`

## 🛠️ Technology Stack

- **Frontend**: Pure HTML5 + Tailwind CSS
- **Charts**: Chart.js
- **Graph Visualization**: Vis.js
- **Deployment**: GitHub Pages (static hosting)
- **No build process required** ✨

## 📁 File Structure

```
nebula-command-center/
├── index.html              # Main dashboard (all-in-one file)
├── .github/
│   └── workflows/
│       └── static.yml      # Auto-deployment workflow
└── README.md               # This file
```

## 🔗 Live URL

Once deployed: https://nineocto2046.github.io/nebula-command-center/

---

Built with Nebula AI 🤖
