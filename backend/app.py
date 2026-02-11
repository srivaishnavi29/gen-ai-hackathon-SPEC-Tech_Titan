from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from curriculum_generator import generate_curriculum
from pdf_generator import generate_pdf
import os
import json
from datetime import datetime
import webbrowser
import threading
import time

app = Flask(__name__)
CORS(app)

@app.route("/api/generate-curriculum", methods=["POST"])
def api_generate_curriculum():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    result = generate_curriculum(data)
    return jsonify(result)

@app.route("/api/download-pdf", methods=["POST"])
def download_pdf():
    try:
        data = request.get_json()
        if not data or 'curriculum' not in data:
            return jsonify({"error": "No curriculum data provided"}), 400
        
        # Create temp file with proper Windows handling
        import tempfile
        import os
        
        # Generate unique temp filename
        fd, filepath = tempfile.mkstemp(suffix='.pdf', prefix='curriculum_')
        os.close(fd)  # Critical for Windows - close file descriptor immediately
        
        try:
            # Generate PDF
            generate_pdf(data['curriculum'], filepath)
            
            # Verify file was created
            if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
                raise Exception("PDF file was not created or is empty")
            
            # Send file with proper headers for immediate download
            response = send_file(
                filepath,
                mimetype='application/pdf',
                as_attachment=True,
                download_name=f"Curriculum_{data['curriculum'].get('program_title', 'Learning_Plan').replace(' ', '_')}.pdf",
                max_age=0  # Prevent caching
            )
            
            # Schedule cleanup after response is sent
            @response.call_on_close
            def cleanup():
                try:
                    if os.path.exists(filepath):
                        os.remove(filepath)
                        print(f"✓ Cleaned up temp file: {filepath}")
                except Exception as e:
                    print(f"Warning: Failed to cleanup temp file: {e}")
            
            print(f"✓ PDF generated successfully: {filepath}")
            return response
            
        except Exception as e:
            # Cleanup on failure too
            if os.path.exists(filepath):
                os.remove(filepath)
            raise e
            
    except Exception as e:
        error_msg = f"PDF download failed: {str(e)}"
        print(f"\n{'='*60}")
        print("PDF DOWNLOAD ERROR")
        print(error_msg)
        print(f"{'='*60}\n")
        return jsonify({"error": error_msg}), 500
    
    
@app.route("/")
def home():
    try:
        with open("frontend/index.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Frontend not found. Please create frontend/index.html", 404

def open_browser():
    """Open browser after 2 seconds (server ready ayina tarvatha)"""
    time.sleep(2)
    webbrowser.open("http://localhost:5000")

if __name__ == "__main__":
    os.makedirs("frontend", exist_ok=True)
    
    # Auto-open browser in separate thread
    threading.Thread(target=open_browser, daemon=True).start()
    
    app.run(host="127.0.0.1", port=5000, debug=False)
