from flask import jsonify, render_template
import asyncpg

from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)