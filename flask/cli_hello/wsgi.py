from flask import Flask
import click

app = Flask(__name__)


@app.cli.command()
def hello():
    click.echo("Hello World")
    

if __name__ == '__main__':
    app.run()