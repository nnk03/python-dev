import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")


@app.cell
def _():
    helloWorld = 'Hello World!'
    return (helloWorld,)


@app.cell
def _(helloWorld):
    print( helloWorld )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

