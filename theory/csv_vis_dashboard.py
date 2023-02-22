import pandas as pd
import plotly.express as px

# Load the incident data from a CSV file or database
incident_data = pd.read_csv('incident_data.csv')

# Group the data by incident type and calculate the total count and severity level
incidents_by_type = incident_data.groupby('type').agg({'severity': 'mean', 'incident_id': 'count'}).reset_index()

# Create a bar chart showing the total number of incidents by type
fig1 = px.bar(incidents_by_type, x='type', y='incident_id', title='Total Incidents by Type')

# Create a scatter plot showing the average severity level of incidents by type
fig2 = px.scatter(incidents_by_type, x='type', y='severity', size='incident_id', title='Severity by Type')

# Load the investigation data from a CSV file or database
investigation_data = pd.read_csv('investigation_data.csv')

# Group the data by status and calculate the total count
investigations_by_status = investigation_data.groupby('status').agg({'investigation_id': 'count'}).reset_index()

# Create a pie chart showing the distribution of investigations by status
fig3 = px.pie(investigations_by_status, values='investigation_id', names='status', title='Investigations by Status')

# Display the charts in a dashboard layout using the Plotly subplots function
dashboard = px.subplots(fig1, fig2, fig3)
dashboard.show()
