from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models import user
from flask_app.models import team

@app.route('/all-teams/')
def display_teams():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data={
            'id' : session['user_id']
        }
        logged_in_user = user.User.get_user_by_id(data)
        return render_template('all_teams.html', logged_in_user = logged_in_user)


@app.route('/create/team/')
def create_team_page():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id' : session['user_id']
        }
        logged_in_user = user.User.get_user_by_id(data)
        return render_template('create_team.html', logged_in_user = logged_in_user)


@app.route('/create/team/form/')
def create_team():
    is_valid = team.Team.validate_team(request.form)
    if not is_valid:
        return redirect('/')
    else:
        team_data = {
            'name' : request.form['name']
        }
        club = team.Team.save_team(team_data)
        if not club:
            flash('Please enter in valid info.')
            return redirect('/')
        else:
            return redirect('/dashboard/')

@app.route('/team/<int:team_id>/view/')
def view_team(team_id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id' : session['user_id']
        }
        team_data = {
            'id' : team_id
        }
        logged_in_user = user.User.get_user_by_id(data)
        all_users = user.User.get_all_users()
        club = team.Team.get_a_team(team_data)
        return render_template('view_team.html', logged_in_user = logged_in_user, club = club, all_users = all_users)
