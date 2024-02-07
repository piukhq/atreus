import click


@click.command(name="accounthistory")
@click.option("--auth", help="Auth token")
@click.option("--givex-number", help="Givex number")
def givex_accounthistory(auth: str, givex_number: str):
    from atreus.givex.givex import account_history

    print(account_history(auth=auth, givex_number=givex_number))


@click.command(name="accountlookup")
@click.option("--auth", help="Auth token")
@click.option("--givex-number", help="Givex number")
def givex_accountlookup(auth: str, givex_number: str):
    from atreus.givex.givex import account_lookup

    print(account_lookup(auth=auth, givex_number=givex_number))
