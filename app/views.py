from app import app
from app.models import Dept, Course, Section, SectionToTime
from flask import render_template
from scheduling import Schedulizer


@app.route('/')
@app.route('/index')
def index():
    deptList = Dept.query.order_by('name')
    courseList = Course.query.order_by('name')
    sectionList = Section.query.order_by('id')
    return render_template('index.html', depts=deptList, courses=courseList, sections=sectionList)


@app.route('/schedule')
def schedule():
    sch = Schedulizer(Course.query.all())
    sch.generate_schedules()
    return render_template('schedule_ext.html', schlist=sch.sched_list)
