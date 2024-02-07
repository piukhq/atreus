import click


@click.command(name="_post_onboards")
def post_onboards(file):
    from atreus.squaremeal import _post_onboards

    print(_post_onboards())


@click.command(name="post_offboards")
def post_offboards():
    from atreus.squaremeal import _post_offboards

    print(_post_offboards())
