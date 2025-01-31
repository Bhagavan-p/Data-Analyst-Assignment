from flask import Flask, render_template
import logging
from analytics import get_analytics_data

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
error_log = logging.getLogger('error_logger')
error_log.addHandler(logging.FileHandler('logs/error.log'))

@app.route('/')
def dashboard():
    """
    Route to render the admin dashboard with analytics data.
    """
    try:
        # Fetch analytics data
        analytics_data = get_analytics_data()
        logging.info("Dashboard rendered successfully.")
        return render_template('dashboard.html', data=analytics_data)
    except Exception as e:
        error_log.error(f"Error in dashboard route: {e}")
        return "An error occurred. Please check the logs."

if __name__ == '__main__':
    app.run(debug=True)