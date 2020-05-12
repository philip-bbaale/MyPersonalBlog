from . import email
from flask import redirect, url_for, flash
from flask_mail import Message
from .. import mail, MAIL_USERNAME
from .forms import subscription_form


@email.route("/subscribe")
def subscribe():
    form = subscription_form()
    if form.validate_on_submit():
        subemail = form.email.data
        msg = Message('Hey there.',recipients = subemail)
        msg.html = '<h2>Welcome to YourQuote.</h2> <p>YourBlog is a personal blogging website where you can create and share your opinions and other users can read and comment on them. Additionally, add a feature that displays random quotes to inspire your users.</p>'
        mail.send(msg)
        flash('You have been added to our subscription', 'success')
        return redirect(url_for('main.home'))

    return redirect(url_for('main.home'))
