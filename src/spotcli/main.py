import typer
from typing import Annotated

app = typer.Typer(no_args_is_help=True)

def main() -> None:
    app()

@app.command()
def saludar(name: str = "") -> None:
    print(f"Bienvenida a SpotCLI {name}")

@app.command()
def version() -> None:
    print("SpotCLI 0.1.0")
    
@app.command()
def play(query: str) -> None:
    clean_query = query.strip()
    if clean_query:
        print(f"Simulación: reproducir {clean_query}")
    else:
        raise typer.BadParameter("El argumento no puede ser vacio.")
    
@app.command()
def volume(n: int) -> None:
    if n in range(101):
        print(f"Volumen a {n}")
    else:
        raise typer.BadParameter("Numero debe ser de 0 al 100")
        

if __name__ == "__main__":
    main()