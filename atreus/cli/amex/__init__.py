import click


@click.command(name="merchant-search")
@click.option("--auth", help="Auth token")
@click.option("--postal-code", help="Postal code")
@click.option("--merchant-name", help="Merchant name")
@click.option("--street", help="Street")
@click.option("--city", help="City")
@click.option("--state", help="State")
def amex_merchant_search(auth: str, postal_code: str, merchant_name: str, street: str, city: str, state: str):
    from atreus.amex.route import amex_merchant_search

    print(
        amex_merchant_search(
            auth=auth, postal_code=postal_code, merchant_name=merchant_name, street=street, city=city, state=state
        )
    )
