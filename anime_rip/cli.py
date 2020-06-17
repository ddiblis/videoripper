import click
from . import Pages

@click.group()
def cli():
   pass

@cli.command(help= "download a full series") 

@click.option("--site", default=None)

@click.argument("name") 
def series(name, site):
   if site is not None:
      for pages_class in Pages.__subclasses__():
         if site in pages_class.tags:
            Use_Pages = pages_class
   else:
      Use_Pages = Pages 
   s = Use_Pages(name)
   s.downloadlinks()

@cli.command(help="website to download from")
@click.argument("sitename")
def website(sitename):
   w = sitename
   w.downloadlinks()

@cli.command(help="list of accepted websites")
def sitelist():
   print("Sitename: Tags")
   print("============")
   for pages_class in Pages.__subclasses__():
      print("{}: {}".format(*pages_class.tags))

if __name__ == '__main__':
   cli()