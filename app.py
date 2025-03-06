import sys
import os
import json
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Database Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'project_configurations.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------------------------
# Authentication Functions
# -------------------------
@app.before_request
def require_login():
    # Allow access to login and static files without authentication
    if request.endpoint not in ('login', 'static') and 'logged_in' not in session:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Replace 'YOUR_PASSWORD' with your actual password
        if request.form.get('password') == 'prjdb1234':
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            flash('Invalid password, please try again.', 'error')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# ===================
# Models
# ===================
class ProjectConfiguration(db.Model):
    __tablename__ = 'project_configurations'

    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(10), unique=True, nullable=False)
    project_stage = db.Column(db.Text)
    last_updated = db.Column(db.Text)
    description = db.Column(db.Text)

    feature_needs = db.relationship('ProjectFeatureNeeds', backref='project_config', uselist=False, cascade="all, delete")

    # Standards Compliance
    aspice_level = db.Column(db.Text)
    aspice_version = db.Column(db.Text)
    iso26262_level = db.Column(db.Text)
    iso26262_version = db.Column(db.Text)
    iso21448 = db.Column(db.Text)
    iso21434 = db.Column(db.Text)
    
    # Regulatory Compliance
    ncap_23 = db.Column(db.Boolean, default=False)
    ncap_26 = db.Column(db.Boolean, default=False)
    ncap_29 = db.Column(db.Boolean, default=False)
    gsr = db.Column(db.Boolean, default=False)
    gsr_v2 = db.Column(db.Boolean, default=False)
    gbt = db.Column(db.Boolean, default=False)
    
    # Camera/Packaging & Image Configuration
    frontal = db.Column(db.Boolean, default=False)
    offset_high_rvm = db.Column(db.Boolean, default=False)
    offset_low_cc = db.Column(db.Boolean, default=False)
    offset_low_ic = db.Column(db.Boolean, default=False)
    offset_high_ohc = db.Column(db.Boolean, default=False)
    fusion = db.Column(db.Boolean, default=False)
    camera_rotation = db.Column(db.Text)
    oms_dms = db.Column(db.Text)
    oms_iq_low = db.Column(db.Text)
    oms_iq_mid = db.Column(db.Text)
    oms_iq_high = db.Column(db.Text)
    bright_pupil = db.Column(db.Boolean, default=False)
    dark_pupil = db.Column(db.Boolean, default=False)
    smart_bright_pupil = db.Column(db.Boolean, default=False)
    nfov = db.Column(db.Boolean, default=False)
    wfov = db.Column(db.Boolean, default=False)
    
    #Seating Positions
    seat_driver = db.Column(db.Boolean, default=False)
    seat_mid = db.Column(db.Boolean, default=False)
    seat_pass = db.Column(db.Boolean, default=False)
    seat_2nd_row_mid = db.Column(db.Boolean, default=False)
    seat_2nd_row_drv = db.Column(db.Boolean, default=False)
    seat_2nd_row_pass = db.Column(db.Boolean, default=False)
    seat_3rd_row_mid = db.Column(db.Boolean, default=False)
    seat_3rd_row_drv = db.Column(db.Boolean, default=False)
    seat_3rd_row_pass = db.Column(db.Boolean, default=False)
    
    # Hardware/Platform
    ti_sitara = db.Column(db.Boolean, default=False)
    ti_tda4_entry = db.Column(db.Boolean, default=False)
    ti_tda4_low = db.Column(db.Boolean, default=False)
    ti_tda4_mid = db.Column(db.Boolean, default=False)
    ti_tda4_high = db.Column(db.Boolean, default=False)
    amd_zynq_ultrascale = db.Column(db.Boolean, default=False)
    qcm_sa81xx = db.Column(db.Boolean, default=False)
    qcm_sa86xx = db.Column(db.Boolean, default=False)
    renesas_v4h = db.Column(db.Boolean, default=False)
    fdm_occula_8_0 = db.Column(db.Boolean, default=False)
    fdm_occula_8_2 = db.Column(db.Boolean, default=False)
    fdm_occula_8_3 = db.Column(db.Boolean, default=False)
    ov_oax4600 = db.Column(db.Boolean, default=False)
    ambarella_cv25 = db.Column(db.Boolean, default=False)
    x86_64 = db.Column(db.Boolean, default=False)
    edme = db.Column(db.Boolean, default=False)
    ti_sitara_2tops_2gb_ram = db.Column(db.Boolean, default=False)
    ti_sitara_1tops_8gb_ram = db.Column(db.Boolean, default=False)
    renesas_rcar_v4h = db.Column(db.Boolean, default=False)
    
    # Operating Systems
    linux = db.Column(db.Boolean, default=False)
    qnx = db.Column(db.Boolean, default=False)
    pike_os = db.Column(db.Boolean, default=False)
    android = db.Column(db.Boolean, default=False)
    library = db.Column(db.Boolean, default=False)
    ghs_integrity = db.Column(db.Boolean, default=False)
    windows = db.Column(db.Boolean, default=False)
    peta_linux = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Project {self.project}>"

class ProjectFeatureNeeds(db.Model):
    __tablename__ = 'project_feature_needs'
    project = db.Column(db.String(10), db.ForeignKey('project_configurations.project'), primary_key=True)
    last_updated = db.Column(db.Text)
    
    # Cognitive Features
    cog_del_inattentive = db.Column(db.String(10))
    cog_del_disengaged = db.Column(db.String(10))
    cog_del_distracted = db.Column(db.String(10))
    cog_dil_drowsy = db.Column(db.String(10))
    cog_dil_microsleeping = db.Column(db.String(10))
    cog_dil_sleeping = db.Column(db.String(10))
    
    # Visual Recognition Features
    vis_gesture_head = db.Column(db.String(10))
    vis_activity_ahp = db.Column(db.String(10))
    vis_activity_handpos = db.Column(db.String(10))
    vis_activity_helditem = db.Column(db.String(10))
    vis_activity_oop = db.Column(db.String(10))
    vis_mouth_speak = db.Column(db.String(10))
    vis_mouth_laugh = db.Column(db.String(10))
    vis_mouth_cough = db.Column(db.String(10))
    vis_mouth_sneeze = db.Column(db.String(10))
    vis_mouth_yawn = db.Column(db.String(10))
    vis_smoke = db.Column(db.String(10))
    vis_phone = db.Column(db.String(10))
    vis_das_coarse = db.Column(db.String(10))
    vis_das_fine = db.Column(db.String(10))
    vis_das_ray = db.Column(db.String(10))
    vis_das_posture = db.Column(db.String(10))
    vis_fod_face = db.Column(db.String(10))
    vis_fod_mask = db.Column(db.String(10))
    vis_fod_eyemask = db.Column(db.String(10))
    vis_sod_childseat = db.Column(db.String(10))
    vis_sod_seatbelt = db.Column(db.String(10))
    vis_sod_height = db.Column(db.String(10))
    vis_sod_weight = db.Column(db.String(10))
    vis_sod_age = db.Column(db.String(10))
    vis_sod_gender = db.Column(db.String(10))
    vis_sod_presence_low = db.Column(db.String(10))
    vis_sod_presence_high = db.Column(db.String(10))
    vis_id_recognize_low = db.Column(db.String(10))
    vis_id_recognize_high = db.Column(db.String(10))
    vis_id_change = db.Column(db.String(10))
    vis_spoof = db.Column(db.String(10))
    vis_expr = db.Column(db.String(10))
    
    # Core Features
    core_bpt_coarse = db.Column(db.String(10))
    core_bpt_fine = db.Column(db.String(10))
    core_depth = db.Column(db.String(10))
    core_get_gaze = db.Column(db.String(10))
    core_get_eyelid = db.Column(db.String(10))
    core_ht_pose = db.Column(db.String(10))
    core_ht_landmarks = db.Column(db.String(10))
    core_ed = db.Column(db.String(10))
    core_aec = db.Column(db.String(10))
    core_fd = db.Column(db.String(10))
    core_ms = db.Column(db.String(10))
    
    # Utility Features
    util_cpose_cf = db.Column(db.String(10))
    util_cpose_imu = db.Column(db.String(10))
    util_video = db.Column(db.String(10))
    util_diag_stk = db.Column(db.String(10))
    util_diag_lbd = db.Column(db.String(10))
    util_diag_liq = db.Column(db.String(10))
    util_diag_cooa = db.Column(db.String(10))
    
    # Additional fields
    COG_DIL_INTOX = db.Column(db.String(10))
    COG_ES = db.Column(db.String(10))
    COG_OVERLOAD = db.Column(db.String(10))
    VIS_MOUTH_SPEECH = db.Column(db.String(10))
    VIS_SOD_HEALTH_PREG = db.Column(db.String(10))
    VIS_CLOTHING = db.Column(db.String(10))
    VIS_MOUTH_EATING_DRINKING = db.Column(db.String(10))
    SFC109 = db.Column(db.String(10))
    VIS_CABIN_OBJECT = db.Column(db.String(10))
    VIS_CABIN_STATE = db.Column(db.String(10))
    VIS_SPOOF_NOVELTY = db.Column(db.String(10))
    VIS_SOD_PETS = db.Column(db.String(10))
    VIS_SOD_CHILDSEAT_TYPE = db.Column(db.String(10))
    SFC115 = db.Column(db.String(10))
    SFC116 = db.Column(db.String(10))
    SFC117 = db.Column(db.String(10))
    VIS_SOD_HEALTH_HR = db.Column(db.String(10))
    SFC120 = db.Column(db.String(10))
    SFC121 = db.Column(db.String(10))
    SFC122 = db.Column(db.String(10))
    SFC123 = db.Column(db.String(10))
    SFC124 = db.Column(db.String(10))
    SFC125 = db.Column(db.String(10))
    SFC126 = db.Column(db.String(10))
    SFC127 = db.Column(db.String(10))
    SFC128 = db.Column(db.String(10))
    SFC129 = db.Column(db.String(10))
    SFC130 = db.Column(db.String(10))
    SFC131 = db.Column(db.String(10))
    SFC132 = db.Column(db.String(10))
    SFC133 = db.Column(db.String(10))
    SFC134 = db.Column(db.String(10))
    SFC135 = db.Column(db.String(10))
    SFC136 = db.Column(db.String(10))
    SFC137 = db.Column(db.String(10))
    SFC138 = db.Column(db.String(10))
    SFC139 = db.Column(db.String(10))
    SFC140 = db.Column(db.String(10))
    SFC141 = db.Column(db.String(10))
    SFC142 = db.Column(db.String(10))
    SFC143 = db.Column(db.String(10))
    SFC144 = db.Column(db.String(10))
    SFC145 = db.Column(db.String(10))

    def __repr__(self):
        return f"<FeatureNeeds {self.project}>"

LOG_FILE = os.path.join(basedir, "change_log.txt")

def log_changes(project, changes):
    """Logs changes made to a project."""
    log_entry = {
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "project": project.project,
        "changes": changes
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
        print(json.dumps(log_entry) + "\n")

def populate_fields(model, fields):
    for field in fields:
        if field == "id":
            continue  # Skip primary key

        form_value = request.form.get(field, None)

        if hasattr(model, field):
            column_type = type(getattr(model.__class__, field).property.columns[0].type)

            if column_type == db.Boolean:
                setattr(model, field, form_value.lower() == "true" if form_value else False)

            elif column_type == db.Integer:
                setattr(model, field, int(form_value) if form_value and form_value.isdigit() else None)

            elif column_type == db.String and form_value == "":
                setattr(model, field, None)  # Convert empty strings to None for nullable fields

            else:
                setattr(model, field, form_value)


# ===================
# Routes
# ===================
@app.route('/')
def index():
    projects = ProjectConfiguration.query.outerjoin(ProjectFeatureNeeds).all()
    project_stages = sorted(set(p.project_stage for p in projects if p.project_stage))
    return render_template('index.html', projects=projects, project_stages=project_stages)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        project_name = request.form.get("project")

        if ProjectConfiguration.query.filter_by(project=project_name).first():
            flash(f'Error: Project "{project_name}" already exists.', 'error')
            return redirect(url_for('add'))

        new_project = ProjectConfiguration(project=project_name)
        project_fields = {c.name for c in ProjectConfiguration.__table__.columns if c.name not in ["id", "project"]}
        populate_fields(new_project, list(project_fields))
        new_feature_needs = ProjectFeatureNeeds(project=project_name)
        feature_fields = {c.name for c in ProjectFeatureNeeds.__table__.columns if c.name != "project"}
        populate_fields(new_feature_needs, list(feature_fields))

        try:
            db.session.add(new_project)
            db.session.add(new_feature_needs)
            db.session.commit()
            flash('Project added successfully.', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding project: {str(e)}', 'error')

    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    project = ProjectConfiguration.query.get_or_404(id)

    # Separate fields for ProjectConfiguration and ProjectFeatureNeeds
    project_fields = {c.name for c in ProjectConfiguration.__table__.columns if c.name != "id"}
    feature_fields = {c.name for c in ProjectFeatureNeeds.__table__.columns if c.name != "id"}

    # Store old values for logging
    old_values = {}
    for field in request.form.keys():
        if field in project_fields:
            old_values[field] = getattr(project, field)
        elif project.feature_needs and field in feature_fields:
            old_values[field] = getattr(project.feature_needs, field)

    # Update fields
    populate_fields(project, project_fields)

    # Ensure feature_needs exists before updating it
    if not project.feature_needs:
        project.feature_needs = ProjectFeatureNeeds(project=project.project)

    populate_fields(project.feature_needs, feature_fields)

    project.last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Track changes for logging
    changes = {}
    for field in request.form.keys():
        new_value = None
        if field in project_fields:
            new_value = getattr(project, field)
        elif field in feature_fields:
            new_value = getattr(project.feature_needs, field)

        if old_values.get(field) != new_value:
            changes[field] = {"old": old_values.get(field), "new": new_value}

    if changes:
        log_changes(project, changes)

    try:
        db.session.commit()
        flash('Project updated successfully.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error updating project: {str(e)}', 'error')

    return redirect(url_for('index'))

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    project = ProjectConfiguration.query.get_or_404(id)
    try:
        db.session.delete(project)
        db.session.commit()
        flash('Project deleted successfully.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting project: {str(e)}', 'error')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=80, use_reloader=False)
