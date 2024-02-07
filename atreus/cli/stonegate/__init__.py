import click


@click.command(name="find-by-email")
@click.option("--email", help="Email")
def stonegate_find_by_email(email: str):
    from atreus.stonegate.stonegate import find_by_email

    print(find_by_email(email=email))


@click.command(name="find-by-member-number")
@click.option("--member-number", help="Member number")
def stonegate_find_by_member_number(member_number: str):
    from atreus.stonegate.stonegate import find_by_member_number

    print(find_by_member_number(member_number=member_number))
