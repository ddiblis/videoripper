import click
from .animefreak_shitway import Pages

@click.group()
def cli():
   pass

@cli.command(help= "download a full series") 
@click.argument("series") 
def dlseries(series):
   s = Pages(series)
   s.downloadlinks()

if __name__ == '__main__':
   cli()