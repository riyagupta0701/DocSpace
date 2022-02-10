from fileinput import filename
from unicodedata import category
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Upload, Workspace
from . import db
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        if 'createForm' in request.form:
            wsName = request.form.get('workSpaceName')
            wsDesc = request.form.get('workSpaceDesc')

            if wsName != "" and wsDesc != "":
                new_workspace = Workspace(workSpaceName=wsName, workSpaceDesc=wsDesc, workSpaceAdminID=current_user.id)
                db.session.add(new_workspace)
                db.session.commit()

        if 'uploadDocsForm' in request.form:
            file = request.files['file']

            new_upload = Upload(filename=file.filename, data=file.read(), uploadedBy=current_user.id)
            db.session.add(new_upload)
            db.session.commit()

    return render_template('profile.html', name = current_user.name, user=current_user)