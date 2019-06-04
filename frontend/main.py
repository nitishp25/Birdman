import click

@click.command()

def main():
    click.clear()
    venue_decided = click.prompt("Venue Decided? (y/n)")
    if(venue_decided=='y'):
        meetup_link = click.prompt("Meetup Link")
        poster_link = click.prompt("Poster Link")
        telegram_user = click.prompt("Telegram Username")
        talk = click.prompt("Talks Decided? (y/n)")
        if(talk=='y'):
            click.echo("\nProcessing ↑ (saving to .birdman/<date>/meetup.txt)")
            click.echo("\nJoin us for the next ILUG-D Meetup on <Date/Time> at <Venue>")
            click.echo("Event Page: " + meetup_link)
            c = click.prompt("\nDo you want to change? (y/n)")
            if(c=='y'):
                main()
            else:
                f = open("meetup.txt", "w+")
                f.write("Join us for the next ILUG-D Meetup on <Date/Time> at <Venue> \nEvent Page: " + meetup_link)
                f.close()
        # else talks not decided
        # announce CFP @ mailing list

    # else venue not decided
    # ask for admin approval
    # send email to POCs

if __name__ == "__main__":
    main()
