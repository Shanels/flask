from app import app
from flask import Flask, jsonify
import os

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
