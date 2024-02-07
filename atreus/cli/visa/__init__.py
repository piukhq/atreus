import click


@click.command(name="helloworld")
@click.option("--auth", help="Auth token")
def visa_helloworld(auth: str):
    from atreus.visa import VisaHelloWorld

    VisaHelloWorld(auth=auth)


@click.command(name="merchant-search")
@click.option("--auth", help="Auth token")
@click.option("--community-code", help="Community code")
@click.option("--merchant-name", help="Merchant name")
@click.option("country-code", help="Country code")
@click.option("--postal-code", help="Postal code")
def visa_merchant_search(auth: str, community_code: str, merchant_name: str, country_code: str, postal_code: str):
    from atreus.visa import VisaGetMerchant

    print(
        VisaGetMerchant(
            auth=auth,
            community_code=community_code,
            merchant_name=merchant_name,
            country_code=country_code,
            postal_code=postal_code,
        )
    )


@click.command(name="get-transaction")
@click.option("--auth", help="Auth token")
@click.option("--transaction-amount", help="Transaction amount")
@click.option("--transaction-date", help="Transaction date")
@click.option("--user-key", help="User key")
@click.option("--community-code", help="Community code")
def visa_gettransaction(auth: str, transaction_amount: str, transaction_date: str, user_key: str, community_code: str):
    from atreus.visa import VisaGetTransaction

    print(
        VisaGetTransaction(
            auth=auth,
            transaction_amount=transaction_amount,
            transaction_date=transaction_date,
            user_key=user_key,
            community_code=community_code,
        )
    )


@click.command(name="merchant-group")
@click.option("--auth", help="Auth token")
@click.option("--community-code", help="Community code")
def visa_merchant_group(auth: str, community_code: str):
    from atreus.visa import VisaSearchMerchantGroup

    print(VisaSearchMerchantGroup(auth=auth, community_code=community_code))


@click.command(name="offer-community")
@click.option("--auth", help="Auth token")
@click.option("--community-code", help="Community code")
def visa_offer_community(auth: str, community_code: str):
    from atreus.visa import VisaOfferCommunity

    print(VisaOfferCommunity(auth=auth, community_code=community_code))
