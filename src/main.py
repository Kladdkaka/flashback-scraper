import typer
import scrape

app = typer.Typer()
app.add_typer(scrape.app, name="scrape")

if __name__ == "__main__":
    app()