# Nebula Command Center 🧠

Personal AI agent orchestration dashboard with knowledge graph visualization.

## Features

- 📊 **Dashboard** - Overview of all agents, tasks, and activity
- 🤖 **Agents Monitor** - Real-time monitoring of all your Nebula agents
- 🧠 **Knowledge Graph** - Visual graph view of thoughts, tasks, ideas, and their connections
- 📅 **Task Scheduler** - Schedule and manage tasks with automation triggers
- ⚙️ **Settings** - Manage connected apps and preferences

## Quick Deploy

### Option 1: Streamlit Community Cloud (Recommended)

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "Create app"
3. Select this repository: `nineocto2046/nebula-command-center`
4. Branch: `main`
5. Main file: `app.py`
6. Click "Deploy"

Your app will be live at: `https://[your-custom-name].streamlit.app`

### Option 2: Run Locally

```bash
# Clone the repository
git clone https://github.com/nineocto2046/nebula-command-center.git
cd nebula-command-center

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Tech Stack

- **Streamlit** - Interactive web framework
- **Plotly** - Interactive visualizations and graphs
- **Pandas** - Data manipulation
- **Python 3.8+**

## Connected Services

This dashboard integrates with your Nebula agents:
- Gmail
- GitHub  
- Notion
- Google Calendar
- Google Drive
- Google Sheets
- Telegram
- Netlify

## Usage

### Dashboard View
Get an overview of all your agents, completed jobs, knowledge nodes, and scheduled tasks.

### Agents Monitor
- View status of all connected agents
- See job completion metrics
- Trigger agent actions manually
- Configure agent settings

### Knowledge Graph
- Visualize connections between thoughts, tasks, and ideas
- Interactive graph with color-coded nodes:
  - 🔵 Blue = Concepts
  - 🟢 Green = Tasks  
  - 🟡 Yellow = Ideas
- Add new nodes and connections

### Task Scheduler
- Create and manage tasks
- Filter by status and priority
- View scheduled automations
- Set up recurring triggers

## Development

Built with ❤️ for personal AI agent orchestration.

## License

MIT License - feel free to fork and customize!