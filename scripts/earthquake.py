import click
from xml.etree.ElementTree import ParseError
from src.recent_earthquake import RecentEarthquake
from src.earthquake_felt import EarthquakeFelt

__author__ = "Faishal Risfandi"

@click.group()
def main():
    """
    CLI sederhana untuk menampilkan info gempa berdasarkan data Badan Meteorologi, Klimatologi, dan Geofisika.
    """
    pass


@main.command()
# @click.option('--expanded', '-x', is_flag=True, help="Expanded mode", default=False)
def terkini():
    """Info gempa terkini dengan magnitudo 5.0 SR"""
    try:
        click.echo(RecentEarthquake())
    except ParseError as e:
        click.echo(e.msg, "| Cannot retrieve data from server!")


@main.command()
def dirasakan():
    """Info 20 gempa bumi yang dirasakan"""
    try:
        click.echo(EarthquakeFelt())
    except ParseError as e:
        click.echo(e.msg, "| Cannot retrieve data from server!")

