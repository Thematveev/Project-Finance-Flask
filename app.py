from flask import Flask
from routes import main_page, dashboard, export


app = Flask(__name__)
app.secret_key = "123"

app.register_blueprint(main_page.page)
app.register_blueprint(dashboard.page, url_prefix="/dashboard")
app.register_blueprint(export.page, url_prefix="/export")


if __name__ == "__main__":
    app.run(debug=True)