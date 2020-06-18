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
      for site_class in Pages.__subclasses__():
         if site in site_class.tags:
            Use_Pages = site_class
   else:
      Use_Pages = Pages 
   s = Use_Pages(name)
   s.downloadlinks()


@cli.command(help="Website to dowload from")
@click.argument("websitename")
def website(websitename):
    w = websitename
    w.downloadlinks()


@cli.command(help="list of accepted websites")
def sitelist():
   print("Sitename: Tags")
   print("==============")
   for pages_class in Pages.__subclasses__():
      print("{}: {}".format(*pages_class.tags))

if __name__ == '__main__':
   cli()