from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


# graphing the data
@app_route('/')
def home():
    data = [
        (10)
        (20)
        (15)
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("graph.html", labels=labels, values=values)