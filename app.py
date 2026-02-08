import streamlit as st
import requests
import json
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# Page config
st.set_page_config(
    page_title="Nebula Command Center",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #6366f1;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f8fafc;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #6366f1;
    }
    .status-active {
        color: #10b981;
        font-weight: bold;
    }
    .status-inactive {
        color: #ef4444;
        font-weight: bold;
    }
    .status-pending {
        color: #f59e0b;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/150x50/6366f1/ffffff?text=Nebula", use_column_width=True)
    st.markdown("## 🧠 Command Center")
    
    page = st.radio("", [
        "📊 Dashboard",
        "🤖 Agents Monitor",
        "🧠 Knowledge Graph",
        "📅 Task Scheduler",
        "⚙️ Settings"
    ])
    
    st.markdown("---")
    st.markdown(f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# Mock data for demonstration
def get_mock_agents():
    return [
        {"name": "Gmail Agent", "slug": "gmail-agent", "status": "active", "jobs_completed": 127, "last_run": "2 minutes ago"},
        {"name": "GitHub Agent", "slug": "github-agent", "status": "active", "jobs_completed": 89, "last_run": "5 minutes ago"},
        {"name": "Notion Agent", "slug": "notion-agent", "status": "active", "jobs_completed": 213, "last_run": "1 minute ago"},
        {"name": "Telegram Agent", "slug": "telegram-agent", "status": "active", "jobs_completed": 45, "last_run": "10 minutes ago"},
        {"name": "Google Calendar", "slug": "google-calendar-agent", "status": "active", "jobs_completed": 56, "last_run": "3 minutes ago"},
        {"name": "Google Drive", "slug": "google-drive-agent", "status": "active", "jobs_completed": 34, "last_run": "7 minutes ago"},
        {"name": "Google Sheets", "slug": "google-sheets-agent", "status": "active", "jobs_completed": 78, "last_run": "4 minutes ago"},
        {"name": "Google Slides", "slug": "google-slides-agent", "status": "active", "jobs_completed": 23, "last_run": "15 minutes ago"},
        {"name": "Netlify Agent", "slug": "netlify-agent", "status": "active", "jobs_completed": 12, "last_run": "20 minutes ago"},
    ]

def get_mock_knowledge_graph():
    return {
        "nodes": [
            {"id": 1, "label": "Agent System", "group": "concept", "size": 30},
            {"id": 2, "label": "Dashboard Design", "group": "task", "size": 25},
            {"id": 3, "label": "Notion Integration", "group": "idea", "size": 20},
            {"id": 4, "label": "Knowledge Graph", "group": "concept", "size": 28},
            {"id": 5, "label": "Task Automation", "group": "task", "size": 22},
            {"id": 6, "label": "Web Scraping", "group": "idea", "size": 18},
            {"id": 7, "label": "Data Visualization", "group": "concept", "size": 24},
            {"id": 8, "label": "Deploy to Netlify", "group": "task", "size": 20},
        ],
        "links": [
            {"source": 1, "target": 2, "value": 2},
            {"source": 1, "target": 3, "value": 3},
            {"source": 1, "target": 4, "value": 4},
            {"source": 2, "target": 7, "value": 2},
            {"source": 3, "target": 4, "value": 3},
            {"source": 4, "target": 5, "value": 2},
            {"source": 5, "target": 8, "value": 1},
            {"source": 6, "target": 4, "value": 2},
            {"source": 7, "target": 2, "value": 3},
        ]
    }

def get_mock_tasks():
    return [
        {"title": "Build Dashboard UI", "status": "In Progress", "priority": "High", "due_date": "2026-02-09"},
        {"title": "Connect Notion API", "status": "Done", "priority": "High", "due_date": "2026-02-08"},
        {"title": "Deploy to Netlify", "status": "Todo", "priority": "Medium", "due_date": "2026-02-10"},
        {"title": "Add Graph Visualization", "status": "In Progress", "priority": "High", "due_date": "2026-02-09"},
        {"title": "Setup Automation Triggers", "status": "Todo", "priority": "Medium", "due_date": "2026-02-11"},
    ]

# Main content
if page == "📊 Dashboard":
    st.markdown('<div class="main-header">🧠 Nebula Command Center</div>', unsafe_allow_html=True)
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    agents = get_mock_agents()
    active_agents = len([a for a in agents if a["status"] == "active"])
    total_jobs = sum([a["jobs_completed"] for a in agents])
    
    with col1:
        st.metric("🤖 Active Agents", active_agents, "All systems operational")
    with col2:
        st.metric("✅ Jobs Completed", total_jobs, "+23 today")
    with col3:
        st.metric("📊 Knowledge Nodes", 127, "+8 this week")
    with col4:
        st.metric("⏰ Scheduled Tasks", 12, "3 due today")
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Agent Activity")
        
        # Agent activity chart
        df_agents = pd.DataFrame(agents)
        fig = go.Figure(data=[
            go.Bar(
                x=df_agents['name'],
                y=df_agents['jobs_completed'],
                marker_color='#6366f1'
            )
        ])
        fig.update_layout(
            xaxis_title="Agent",
            yaxis_title="Jobs Completed",
            height=300,
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📋 Task Status Distribution")
        
        tasks = get_mock_tasks()
        status_counts = pd.DataFrame(tasks)['status'].value_counts()
        
        fig = go.Figure(data=[
            go.Pie(
                labels=status_counts.index,
                values=status_counts.values,
                marker_colors=['#10b981', '#f59e0b', '#6366f1']
            )
        ])
        fig.update_layout(height=300, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig, use_container_width=True)
    
    # Recent activity
    st.markdown("---")
    st.subheader("🕐 Recent Activity")
    
    activity_data = [
        {"time": "2 min ago", "agent": "Notion Agent", "action": "Synced 5 new thoughts to knowledge graph"},
        {"time": "5 min ago", "agent": "GitHub Agent", "action": "Created repository: nebula-dashboard"},
        {"time": "10 min ago", "agent": "Gmail Agent", "action": "Processed 3 new emails"},
        {"time": "15 min ago", "agent": "Google Calendar", "action": "Updated 2 scheduled events"},
    ]
    
    for activity in activity_data:
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 5])
            with col1:
                st.text(activity["time"])
            with col2:
                st.text(f"🤖 {activity['agent']}")
            with col3:
                st.text(activity["action"])

elif page == "🤖 Agents Monitor":
    st.markdown('<div class="main-header">🤖 Agents Monitor</div>', unsafe_allow_html=True)
    
    agents = get_mock_agents()
    
    # Search and filter
    col1, col2 = st.columns([3, 1])
    with col1:
        search = st.text_input("🔍 Search agents", placeholder="Enter agent name...")
    with col2:
        status_filter = st.selectbox("Status", ["All", "Active", "Inactive"])
    
    st.markdown("---")
    
    # Agent cards
    for agent in agents:
        if search and search.lower() not in agent["name"].lower():
            continue
        
        with st.expander(f"{'🟢' if agent['status'] == 'active' else '🔴'} {agent['name']}", expanded=False):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Status", agent["status"].upper())
            with col2:
                st.metric("Jobs Completed", agent["jobs_completed"])
            with col3:
                st.metric("Last Run", agent["last_run"])
            
            st.markdown(f"**Slug:** `{agent['slug']}`")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"▶️ Run Now", key=f"run_{agent['slug']}"):
                    st.success(f"Triggered {agent['name']}")
            with col2:
                if st.button(f"⚙️ Configure", key=f"config_{agent['slug']}"):
                    st.info(f"Configuration for {agent['name']}")

elif page == "🧠 Knowledge Graph":
    st.markdown('<div class="main-header">🧠 Knowledge Graph</div>', unsafe_allow_html=True)
    
    st.info("📊 Interactive knowledge graph visualization - Connect your thoughts, tasks, and ideas")
    
    # Graph visualization using plotly
    graph_data = get_mock_knowledge_graph()
    
    # Create network graph
    edge_trace = []
    for link in graph_data["links"]:
        source_node = next(n for n in graph_data["nodes"] if n["id"] == link["source"])
        target_node = next(n for n in graph_data["nodes"] if n["id"] == link["target"])
        
        edge_trace.append(
            go.Scatter(
                x=[source_node["id"], target_node["id"], None],
                y=[source_node["size"], target_node["size"], None],
                mode='lines',
                line=dict(width=link["value"], color='#cbd5e1'),
                hoverinfo='none'
            )
        )
    
    node_trace = go.Scatter(
        x=[node["id"] for node in graph_data["nodes"]],
        y=[node["size"] for node in graph_data["nodes"]],
        mode='markers+text',
        text=[node["label"] for node in graph_data["nodes"]],
        textposition="top center",
        marker=dict(
            size=[node["size"] for node in graph_data["nodes"]],
            color=['#6366f1' if n["group"] == "concept" else '#10b981' if n["group"] == "task" else '#f59e0b' 
                   for n in graph_data["nodes"]],
            line=dict(width=2, color='white')
        ),
        hovertemplate='<b>%{text}</b><extra></extra>'
    )
    
    fig = go.Figure(data=edge_trace + [node_trace])
    fig.update_layout(
        showlegend=False,
        hovermode='closest',
        margin=dict(b=0, l=0, r=0, t=0),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=600,
        plot_bgcolor='#f8fafc'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Legend
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("🔵 **Concepts** - Core ideas and systems")
    with col2:
        st.markdown("🟢 **Tasks** - Actionable items")
    with col3:
        st.markdown("🟡 **Ideas** - Future possibilities")
    
    st.markdown("---")
    
    # Add new node
    with st.expander("➕ Add New Node"):
        col1, col2 = st.columns(2)
        with col1:
            node_title = st.text_input("Title")
            node_type = st.selectbox("Type", ["Concept", "Task", "Idea"])
        with col2:
            node_content = st.text_area("Content")
            node_tags = st.text_input("Tags (comma separated)")
        
        if st.button("Create Node"):
            st.success(f"Created new {node_type}: {node_title}")

elif page == "📅 Task Scheduler":
    st.markdown('<div class="main-header">📅 Task Scheduler</div>', unsafe_allow_html=True)
    
    # Task list
    tasks = get_mock_tasks()
    
    # Add new task
    with st.expander("➕ Create New Task", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            task_title = st.text_input("Task Title")
            task_priority = st.selectbox("Priority", ["High", "Medium", "Low"])
        with col2:
            task_due = st.date_input("Due Date")
            task_status = st.selectbox("Status", ["Todo", "In Progress", "Done"])
        
        task_desc = st.text_area("Description")
        
        if st.button("Create Task"):
            st.success(f"Task created: {task_title}")
    
    st.markdown("---")
    
    # Filter tasks
    col1, col2, col3 = st.columns(3)
    with col1:
        status_filter = st.multiselect("Status", ["Todo", "In Progress", "Done"], default=["Todo", "In Progress"])
    with col2:
        priority_filter = st.multiselect("Priority", ["High", "Medium", "Low"], default=["High", "Medium", "Low"])
    with col3:
        sort_by = st.selectbox("Sort by", ["Due Date", "Priority", "Status"])
    
    # Task cards
    for task in tasks:
        if task["status"] not in status_filter or task["priority"] not in priority_filter:
            continue
        
        priority_color = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
        status_emoji = {"Todo": "⭕", "In Progress": "🔄", "Done": "✅"}
        
        with st.container():
            col1, col2, col3, col4 = st.columns([4, 2, 2, 2])
            
            with col1:
                st.markdown(f"### {status_emoji[task['status']]} {task['title']}")
            with col2:
                st.markdown(f"{priority_color[task['priority']]} **{task['priority']}**")
            with col3:
                st.markdown(f"📅 {task['due_date']}")
            with col4:
                if st.button("✏️ Edit", key=f"edit_{task['title']}"):
                    st.info(f"Editing {task['title']}")
            
            st.markdown("---")
    
    # Scheduled automations
    st.subheader("⚡ Scheduled Automations")
    
    automations = [
        {"name": "Daily Notion Sync", "schedule": "Every day at 9:00 AM", "status": "Active", "next_run": "Tomorrow 9:00 AM"},
        {"name": "Weekly Report", "schedule": "Every Monday at 10:00 AM", "status": "Active", "next_run": "Mon 10:00 AM"},
        {"name": "GitHub Backup", "schedule": "Every day at 11:00 PM", "status": "Active", "next_run": "Today 11:00 PM"},
    ]
    
    for auto in automations:
        with st.expander(f"⚡ {auto['name']} - {auto['status']}", expanded=False):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Schedule:** {auto['schedule']}")
                st.markdown(f"**Status:** {auto['status']}")
            with col2:
                st.markdown(f"**Next Run:** {auto['next_run']}")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("⏸️ Pause", key=f"pause_{auto['name']}"):
                    st.warning(f"Paused {auto['name']}")
            with col2:
                if st.button("✏️ Edit", key=f"edit_auto_{auto['name']}"):
                    st.info(f"Editing {auto['name']}")

elif page == "⚙️ Settings":
    st.markdown('<div class="main-header">⚙️ Settings</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🔗 Connections", "🔔 Notifications", "🎨 Appearance"])
    
    with tab1:
        st.subheader("Connected Apps")
        
        apps = [
            {"name": "Notion", "status": "Connected", "account": "nine.octo.2046@gmail.com"},
            {"name": "GitHub", "status": "Connected", "account": "nineocto2046"},
            {"name": "Gmail", "status": "Connected", "account": "nine.octo.2046@gmail.com"},
            {"name": "Netlify", "status": "Connected", "account": "nine.octo.2046@gmail.com"},
            {"name": "Telegram", "status": "Connected", "account": "@nineAI0246"},
        ]
        
        for app in apps:
            col1, col2, col3 = st.columns([2, 3, 1])
            with col1:
                st.markdown(f"**{app['name']}**")
            with col2:
                st.markdown(f"🟢 {app['status']} - {app['account']}")
            with col3:
                st.button("Disconnect", key=f"disconnect_{app['name']}")
            st.markdown("---")
    
    with tab2:
        st.subheader("Notification Preferences")
        
        st.checkbox("✅ Task completion notifications", value=True)
        st.checkbox("⚠️ Agent failure alerts", value=True)
        st.checkbox("📊 Daily activity summary", value=True)
        st.checkbox("📧 Email notifications", value=False)
        
        st.markdown("---")
        
        st.subheader("Notification Channels")
        notify_channel = st.multiselect(
            "Send notifications to:",
            ["Email", "Telegram", "Slack"],
            default=["Telegram"]
        )
    
    with tab3:
        st.subheader("Dashboard Theme")
        
        theme = st.radio("Color Theme", ["Light", "Dark", "Auto"])
        
        st.markdown("---")
        
        st.subheader("Dashboard Layout")
        
        col1, col2 = st.columns(2)
        with col1:
            st.checkbox("Show activity feed", value=True)
            st.checkbox("Show quick actions", value=True)
        with col2:
            st.checkbox("Compact view", value=False)
            st.checkbox("Show agent status", value=True)

st.markdown("---")
st.markdown("**Nebula Command Center** | Built with ❤️ for Nine Octo")
