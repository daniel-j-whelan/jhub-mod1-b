# imports
from flask import Flask, render_template, request
from api import query

# Flask creation
app = Flask(__name__)

# Home page
@app.route("/")
def index():
    return render_template("index.html")
    
# Forces page
@app.route("/forces", methods=['GET', 'POST'])
def forces(methods=["POST"]):
    
    force_id = None
    force_results = None
    officer_results = None
    
    url = "https://data.police.uk/api/forces"
    forces_list = query(url=url)

    if request.method == "POST":
        force_id = request.form.get("force_select").strip()
        url += f"/{force_id}"
        force_results = query(url=url)
        url += f"/people"
        officer_results = query(url=url)
    
    return render_template(
        "forces.html",
        forces_list=forces_list,
        force_id=force_id,
        force_results=force_results,
        officer_results=officer_results
        )

# Flask initialisation
if __name__ == "__main__":
    app.run()