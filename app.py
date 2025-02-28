from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'project_configurations.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class ProjectConfiguration(db.Model):
    __tablename__ = 'project_configurations'
    
    cameras = {
    "1": {"left": 460, "top": 70, "width": 120, "height": 77},
    "2": {"left": 442, "top": 180, "width": 155, "height": 49},
    "3": {"left": 294, "top": 360, "width": 58, "height": 28},
    "4": {"left": 438, "top": 320, "width": 166, "height": 68},
    "5": {"left": 219, "top": 245, "width": 63, "height": 122}
    }

    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(100), nullable=False)
    project_stage = db.Column(db.String(50))
    last_updated = db.Column(db.String(50))
    description = db.Column(db.Text)

    # Cognitive Features
    cog_del_inattentive = db.Column("COG-DEL-INATTENTIVE", db.String(10))
    cog_del_disengaged = db.Column("COG-DEL-DISENGAGED", db.String(10))
    cog_del_distracted = db.Column("COG-DEL-DISTRACTED", db.String(10))
    cog_dil_drowsy = db.Column("COG-DIL-DROWSY", db.String(10))
    cog_dil_microsleeping = db.Column("COG-DIL-MICROSLEEPING", db.String(10))
    cog_dil_sleeping = db.Column("COG-DIL-SLEEPING", db.String(10))

    # Visual Recognition Features
    vis_gesture_head = db.Column("VIS-GESTURE-HEAD", db.String(10))
    vis_activity_ahp = db.Column("VIS-ACTIVITY-AHP", db.String(10))
    vis_activity_handpos = db.Column("VIS-ACTIVITY-HANDPOS", db.String(10))
    vis_activity_helditem = db.Column("VIS-ACTIVITY-HELDITEM", db.String(10))
    vis_activity_oop = db.Column("VIS-ACTIVITY-OOP", db.String(10))
    vis_mouth_speak = db.Column("VIS-MOUTH-SPEAK", db.String(10))
    vis_mouth_laugh = db.Column("VIS-MOUTH-LAUGH", db.String(10))
    vis_mouth_cough = db.Column("VIS-MOUTH-COUGH", db.String(10))
    vis_mouth_sneeze = db.Column("VIS-MOUTH-SNEEZE", db.String(10))
    vis_mouth_yawn = db.Column("VIS-MOUTH-YAWN", db.String(10))
    vis_smoke = db.Column("VIS-SMOKE", db.String(10))
    vis_phone = db.Column("VIS-PHONE", db.String(10))
    vis_das_coarse = db.Column("VIS-DAS-COARSE", db.String(10))
    vis_das_fine = db.Column("VIS-DAS-FINE", db.String(10))
    vis_das_ray = db.Column("VIS-DAS-RAY", db.String(10))
    
    # Standard Compliance
    aspice_level = db.Column(db.Text)
    aspice_version = db.Column(db.Text)
    iso26262_level = db.Column(db.Text)
    iso26262_version = db.Column(db.Text)
    iso21448 = db.Column(db.Text)
    iso21434 = db.Column(db.Text)
    
    # Regulatory Compliance
    ncap_23 = db.Column(db.Text)
    ncap_26 = db.Column(db.Text)
    ncap_29 = db.Column(db.Text)
    gsr = db.Column(db.Text)
    gsr_v2 = db.Column( db.Text)
    gbt = db.Column(db.Text)

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

    # Packaging Configuration
    frontal = db.Column(db.Text)
    offset_high = db.Column(db.Text)
    offset_low = db.Column(db.Text)
    overhead = db.Column(db.Text)
    fusion = db.Column(db.Text)
    camera_rotation = db.Column(db.Text)
    oms_dms = db.Column(db.Text)
    oms_iq_high = db.Column(db.Text)
    oms_iq_mid = db.Column(db.Text)
    oms_iq_high = db.Column(db.Text)
    bright_pupil = db.Column(db.Text)
    dark_pupil = db.Column(db.Text)
    smart_bright_Pupil = db.Column(db.Text)
    nfov = db.Column(db.Text)
    wfov = db.Column(db.Text)
    seating_positions = db.Column(db.Text)
    
    def __repr__(self):
        return f"<Project {self.project}>"

# Home route: List all configurations using the ORM.
@app.route('/')
def index():
    projects = ProjectConfiguration.query.all()
    project_stages = sorted(set(project.project_stage for project in projects if project.project_stage))  # Get unique stages
    return render_template('index.html', projects=projects, project_stages=project_stages)

# Helper function to populate project attributes from form back to the database
def populate_project_from_form(project):
    field_mapping = {
        "project": "project",
        "project_stage": "project_stage",
        "description": "description",
        # Cognitive Features
        "cog_del_inattentive": "cog_del_inattentive",
        "cog_del_disengaged": "cog_del_disengaged",
        "cog_del_distracted": "cog_del_distracted",
        "cog_dil_drowsy": "cog_dil_drowsy",
        "cog_dil_microsleeping": "cog_dil_microsleeping",
        "cog_dil_sleeping": "cog_dil_sleeping",
        # Visual Recognition Features
        "vis_gesture_head": "vis_gesture_head",
        "vis_activity_ahp": "vis_activity_ahp",
        "vis_activity_handpos": "vis_activity_handpos",
        "vis_activity_helditem": "vis_activity_helditem",
        "vis_activity_oop": "vis_activity_oop",
        "vis_mouth_speak": "vis_mouth_speak",
        "vis_mouth_laugh": "vis_mouth_laugh",
        "vis_mouth_cough": "vis_mouth_cough",
        "vis_mouth_sneeze": "vis_mouth_sneeze",
        "vis_mouth_yawn": "vis_mouth_yawn",
        "vis_smoke": "vis_smoke",
        "vis_phone": "vis_phone",
        "vis_das_coarse": "vis_das_coarse",
        "vis_das_fine": "vis_das_fine",
        "vis_das_ray": "vis_das_ray",
        # Standards Compliance
        "aspice_level": "aspice_level",
        "aspice_version": "aspice_version",
        "iso26262_level": "iso26262_level",
        "iso26262_version": "iso26262_version",
        "iso21448": "iso21448",
        "iso21434": "iso21434",
        # Regulatory Compliance
        "ncap_23": "ncap_23",
        "ncap_26": "ncap_26",
        "ncap_29": "ncap_29",
        "gsr": "gsr",
        "gsr_v2": "gsr_v2",
        "gbt": "gbt",
        # Hardware/Platform
        "ti_sitara": "ti_sitara",
        "ti_tda4_entry": "ti_tda4_entry",
        "ti_tda4_low": "ti_tda4_low",
        "ti_tda4_mid": "ti_tda4_mid",
        "ti_tda4_high": "ti_tda4_high",
        "amd_zynq_ultrascale": "amd_zynq_ultrascale",
        "qcm_sa81xx": "qcm_sa81xx",
        "qcm_sa86xx": "qcm_sa86xx",
        "renesas_v4h": "renesas_v4h",
        "fdm_occula_8_0": "fdm_occula_8_0",
        "fdm_occula_8_2": "fdm_occula_8_2",
        "fdm_occula_8_3": "fdm_occula_8_3",
        "ov_oax4600": "ov_oax4600",
        "ambarella_cv25": "ambarella_cv25",
        "x86_64": "x86_64",
        "edme": "edme",
        "ti_sitara_2tops_2gb_ram": "ti_sitara_2tops_2gb_ram",
        "ti_sitara_1tops_8gb_ram": "ti_sitara_1tops_8gb_ram",
        "renesas_rcar_v4h": "renesas_rcar_v4h",
        # Camera Configuration
        "frontal": "Frontal",
        "offset_High": "Offset_High",
        "offset_Low": "Offset_Low",
        "overhead": "Overhead",
        "fusion": "Fusion",
        "camera_Rotation": "Camera_Rotation",
        "oms_dms": "OMS_DMS_Both",
        "oms_iq_low": "OMSIQ_LOW",
        "oms_iq_mid": "OMSIQ_MID",
        "oms_iq_high": "OMSIQ_HIGH",
        "bright_pupil": "Bright_Pupil",
        "dark_pupil": "Dark_Pupil",
        "smart_bright_pupil": "Smart_Bright_Pupil",
        "nfov": "NFOV",
        "wfov": "WFOV",
        "seating_positions": "Seating_Positions",
        # Operating System Fields (Newly Added)
        "linux": "Linux",
        "qnx": "QNX",
        "pike_os": "Pike_OS",
        "android": "Android",
        "library": "NA",
        "ghs_integrity": "GHS_Integrity",
        "windows": "Windows",
        "peta_linux": "PetaLinux",
    }

    for form_field, model_attr in field_mapping.items():
        setattr(project, model_attr, request.form.get(form_field, None))


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        try:
            new_project = ProjectConfiguration()
            populate_project_from_form(new_project)

            db.session.add(new_project)
            db.session.commit()
            flash('Project added successfully.', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding project: {str(e)}', 'error')

    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    project = ProjectConfiguration.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            populate_project_from_form(project)
            project.last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Update timestamp
            db.session.commit()
            flash('Project updated successfully.', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating project: {str(e)}', 'error')

    return

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
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=80, use_reloader=False)
