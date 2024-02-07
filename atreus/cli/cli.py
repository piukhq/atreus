import click

from atreus.cli.amex import amex_merchant_search
from atreus.cli.givex import givex_accounthistory, givex_accountlookup
from atreus.cli.stonegate import stonegate_find_by_email, stonegate_find_by_member_number
from atreus.cli.visa import (
    visa_gettransaction,
    visa_helloworld,
    visa_merchant_group,
    visa_merchant_search,
    visa_offer_community,
)


@click.group()
def cli() -> None:
    pass


@cli.group(name="amex")
def amex() -> None:
    pass


@cli.group(name="givex")
def givex() -> None:
    pass


@cli.group(name="stonegate")
def stonegate() -> None:
    pass


@cli.group(name="visa")
def visa() -> None:
    pass


amex.add_command(amex_merchant_search)
givex.add_command(givex_accounthistory)
givex.add_command(givex_accountlookup)
stonegate.add_command(stonegate_find_by_email)
stonegate.add_command(stonegate_find_by_member_number)
visa.add_command(visa_helloworld)
visa.add_command(visa_gettransaction)
visa.add_command(visa_merchant_group)
visa.add_command(visa_merchant_search)
visa.add_command(visa_offer_community)

if __name__ == "__main__":
    cli()
