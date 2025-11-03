from web.app import run_app
import os

# Start the server
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    run_app(host='0.0.0.0', port=port)
