from models import db
from models import Telephone, Contact, Company, Organization, Deal, Link, Project, Sprint, Task, Comment, Message
from faker import Faker

fake = Faker()


def do_fixtures():
    global db

    def newuser():
        phonenumber = fake.phone_number()
        firstname = fake.first_name()
        lastname = fake.last_name()
        phoneobj = Telephone(number=phonenumber)
        email = fake.email()
        u = Contact(firstname=firstname, lastname=lastname, email=email)
        u.telephones = [phoneobj]
        db.session.add(phoneobj)

        u.comments = [newcomment() for i in range(2)]
        u.tasks = [newtask() for i in range(2)]
        u.messages = [newmsg() for i in range(2)]
        db.session.add(u)
        return u

    def newcompany():
        companyname = fake.company()
        companyemail = fake.company_email()
        description = fake.catch_phrase()
        company = Company(name=companyname, email=companyemail,
                          description=description)
        companyphone = Telephone(number=fake.phone_number())
        company.telephones = [companyphone]
        company.owner = newuser()
        db.session.add(company)
        company.comments = [newcomment() for i in range(5)]
        company.messages = [newmsg() for i in range(20)]

        db.session.add(companyphone)
        return company

    def neworg():
        orgname = fake.company() + "org"
        orgemail = fake.company_email()
        description = fake.catch_phrase()

        org = Organization(name=orgname, email=orgemail,
                           description=description)
        org.comments = [newcomment() for i in range(5)]
        org.tasks = [newtask() for i in range(5)]
        org.messages = [newmsg() for i in range(20)]

        db.session.add(org)
        return org

    def newproj():
        projname = fake.name() + "proj"
        projdesc = fake.paragraph()
        proj = Project(name=projname, description=projdesc)
        proj.comments = [newcomment() for i in range(5)]
        proj.tasks = [newtask() for i in range(5)]
        proj.messages = [newmsg() for i in range(20)]
        db.session.add(proj)
        return proj

    def newdeal():

        dealname = fake.name() + "deal"
        dealamount = 5000
        deal = Deal(name=dealname, amount=dealamount)
        deal.comments = [newcomment() for i in range(5)]
        deal.tasks = [newtask() for i in range(5)]
        deal.messages = [newmsg() for i in range(5)]
        db.session.add(deal)
        return deal

    def newcomment():
        com = Comment(name=fake.sentence(4),
                      content=fake.paragraph())
        db.session.add(com)
        return com

    def newtask():
        t = Task(title=fake.sentence(5), content=fake.paragraph(),
                 remarks=fake.paragraph())
        t.comments = [newcomment() for i in range(10)]
        db.session.add(t)
        return t

    def newmsg():
        m = Message(title=fake.sentence(5), content=fake.paragraph())
        db.session.add(m)
        return m

    for i in range(5):
        u = newuser()

        com = newcompany()
        proj = newproj()
        org = neworg()

    db.session.commit()
