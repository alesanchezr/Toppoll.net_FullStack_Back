from models import db, Users, Polls, Voters_Table, Chats
from datetime import datetime, timedelta
import utils
def run():

    Chats.query.delete()             #Arrange the deletes in the opposite order of the models
    Voters_Table.query.delete()   
    Polls.query.delete()
    Users.query.delete()
    
    # MYSQL database for gitpod
    db.session.execute("ALTER TABLE chats AUTO_INCREMENT = 1")
    db.session.execute("ALTER TABLE polls AUTO_INCREMENT = 1")
    db.session.execute("ALTER TABLE users AUTO_INCREMENT = 1")
    db.session.execute("ALTER TABLE voters_table AUTO_INCREMENT = 1")
 
    # POSTGRES database for heroku
    # db.session.execute("ALTER SEQUENCE chats_id_seq RESTART")
    # db.session.execute("ALTER SEQUENCE polls_id_seq RESTART")
    # db.session.execute("ALTER SEQUENCE users_id_seq RESTART")
    # db.session.execute("ALTER SEQUENCE voters_table_id_seq RESTART")

    now = datetime.utcnow()

    ##################
    #     USERS
    ##################
    Issac = Users(
        first_name = 'Issac',
        last_name = 'Alleyne',
        username = 'kolis10',
        password = utils.sha256('Awesom3'),
        date_of_birth = '10/22/1994',
        email = 'issacalleyne@gmail.com'
    )
    db.session.add(Issac)
    Naz = Users(
        first_name = 'Nhinhoshxhy',
        last_name = 'Desprez',
        username = 'Naz',
        password = utils.sha256('HHH'),
        date_of_birth = '1/2/1999',
        email = 'noztril@gmail.com'
    )
    db.session.add(Naz)
    Chouerlee = Users(
        first_name = 'Chouerlee',
        last_name = 'Victor',
        username = 'Curly-Fry',
        password = utils.sha256('Fry'),
        date_of_birth = '10/12/1997',
        email = 'curly@gmail.com'
    )
    db.session.add(Chouerlee)
    Zion = Users(
        first_name = 'Zion',
        last_name = 'Raymond',
        username = 'Coder',
        password = utils.sha256('Zee'),
        date_of_birth = '1/33/1998',
        email = 'coderzee@gmail.com'
    )
    db.session.add(Zion)
    Rajae = Users(
        first_name = 'Rajae',
        last_name = 'Lindsay',
        username = 'Rager',
        password = utils.sha256('$$'),
        date_of_birth = '4/4/1996',
        email = 'ceo?@gmail.com'
    )
    db.session.add(Rajae)
    Anthony = Users(
        first_name = 'Anthony',
        last_name = 'Smith',
        username = 'Tony',
        password = utils.sha256('Dez'),
        date_of_birth = '1/23/1995',
        email = 'anthony@gmail.com'
    )
    Hernan = Users(
        first_name = 'Hernan',
        last_name = 'Garcia',
        username = 'Garcia Sausage',
        password = utils.sha256('geek'),
        date_of_birth = '5/17/1984',
        email = 'hgs@gmail.com'
    )
    db.session.add(Hernan)
    Ms_Achille = Users(
        first_name = 'Classified',
        last_name = 'Achille',
        username = 'Boss Mom',
        password = utils.sha256('off-center'),
        date_of_birth = '5/17/1978',
        email = 'gotoclass@gmail.com'
    )
    db.session.add(Ms_Achille)

    ##################
    #     POLLS
    ##################
    db.session.add(Polls(
        creator_user = Chouerlee,
        poll_question = "What's the best way to travel?",
        poll_description = "A luxury cruise, flying first class, a glamourous bullet train, a scenic drive through the country; which getaway sounds best to you?",
        info_link = "",
        image_link = "https://images.pexels.com/photos/776030/pexels-photo-776030.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
        option1 = "Boat",
        option2 = "Plane",
        option3 = "Train",
        option4 = "Drive Myself"
    ))
    db.session.add(Polls(
        creator_user = Issac,
        poll_question = "Is the government hiding aliens in area 51?",
        poll_description = "If there were aliens, we'd know about it now, right? Or would we?",
        info_link = "",
        image_link = "https://images.pexels.com/photos/365625/pexels-photo-365625.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
        option1 = "I'm a believer",
        option2 = "Conspiracy Theories aren't my thing",
        option3 = "The Government is hiding something, just not aliens",
        option4 = "The Government would never lie to us. Ever."
    ))
    db.session.add(Polls(
        creator_user = Naz,
        poll_question = "Should the drinking age be lowered to 18?",
        poll_description = "The drinking age is 21 everywhere in the United States, but are 18 year olds mature enough to drink responsibly?",
        info_link = "https://drinkingage.procon.org/",
        image_link = "https://images.pexels.com/photos/696218/pexels-photo-696218.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
        option1 = "Yes",
        option2 = "No, it's fine the way it is",
        option3 = "It should be raised"
    ))
    db.session.add(Polls(
        creator_user = Zion,
        poll_question = "Is revenge cheating justified?",
        poll_description = "If you're cheated on, you're hurt, angry, and feel disrespected, and rightfully so. But do you cheat back",
        info_link = "",
        image_link = "https://images.pexels.com/photos/3694011/pexels-photo-3694011.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
        option1 = "Yes, they have it coming",
        option2 = "No, two wrongs won't make things right"
    ))
    db.session.add(Polls(
        creator_user = Rajae,
        poll_question = "Which is the better sport?",
        poll_description = "Sports are a part of everyday life, whether you prefer to play, watch or both. These three are some of the most popular in America, so how do they stack against each other?",
        info_link = "",
        image_link = "https://i2.wp.com/digiday.com/wp-content/uploads/2014/10/naenae.gif?resize=320%2C240&ssl=1",
        option1 = "Football. The American Version",
        option2 = "Basketball",
        option3 = "Baseball; there's a reason it's called America's Pastime.",
        option4 = "I don't really watch these"
    ))
    db.session.add(Polls(
        creator_user = Anthony,
        poll_question = "What element would you want to control?",
        poll_description = "Manipulating the elements is a standard superpower to have, but often quite powerful. If you could choose one of these four elements, which would you master?",
        info_link = "",
        image_link = "https://images.pexels.com/photos/1118873/pexels-photo-1118873.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
        option1 = "Water",
        option2 = "Earth",
        option3 = "Fire",
        option4 = "Air"
    ))
    db.session.add(Polls(
        creator_user = Hernan,
        poll_question = "If you could travel in time, what would you want to see?",
        poll_description = "A world far off or long forgotten, time travel has much appeal, but is it for you?",
        info_link = "",
        image_link = "https://images.pexels.com/photos/552598/pexels-photo-552598.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
        option1 = "The past",
        option2 = "The future",
        option3 = "There is enough in the present"
    ))
    db.session.add(Polls(
        creator_user = Ms_Achille,
        poll_question = "If you could have one of these superpowers, which one would you choose?",
        poll_description = "We've all dreamt of having superpowers and being more than ordinary; which of these abilities fits you best?",
        info_link = "",
        image_link = "https://images.pexels.com/photos/346796/pexels-photo-346796.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
        option1 = "Invisibility",
        option2 = "Super Strength",
        option3 = "Flight",
        option4 = "Telekinesis"
    ))
    db.session.add(Polls(
        creator_user = Naz,
        poll_question = "Is this website visually appealing?",
        poll_description = "The person who designed it went crazy on every little detail, but honestly you don't have to like it, tell us what you think.",
        info_link = "",
        image_link = "https://images.pexels.com/photos/57690/pexels-photo-57690.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
        option1 = "It looks very good",
        option2 = "It's okay",
        option3 = "Not great, TBH",
        option4 = "I honestly don't care"
    ))

    ##################
    #  VOTERS_TABLE
    ##################

    db.session.add(Voters_Table(
        user_id = 1,
        poll_id = 1,
        username = "kolis10",
        poll_name = "What's the best way to travel?",
        option_picked = "Boat"
    ))
    db.session.add(Voters_Table(
        user_id = 2,
        poll_id = 1,
        username = "Naz",
        poll_name = "What's the best way to travel?",
        option_picked = "Boat"
    ))
    db.session.add(Voters_Table(
        user_id = 3,
        poll_id = 1,
        username = "Curly-Fry",
        poll_name = "What's the best way to travel?",
        option_picked = "Plane"
    ))
    db.session.add(Voters_Table(
        user_id = 4,
        poll_id = 1,
        username = "Coder",
        poll_name = "What's the best way to travel?",
        option_picked = "Drive Myself"
    ))
    db.session.add(Voters_Table(
        user_id = 5,
        poll_id = 1,
        username = "Rager",
        poll_name = "What's the best way to travel?",
        option_picked = "Boat"
    ))
    db.session.add(Voters_Table(
        user_id = 6,
        poll_id = 1,
        username = "Tony",
        poll_name = "What's the best way to travel?",
        option_picked = "Plane"
    ))
    db.session.add(Voters_Table(
        user_id = 7,
        poll_id = 1,
        username = "Garcia Sausage",
        poll_name = "What's the best way to travel?",
        option_picked = "Drive Myself"
    ))
    db.session.add(Voters_Table(
        user_id = 8,
        poll_id = 1,
        username = "Boss Mom",
        poll_name = "What's the best way to travel?",
        option_picked = "Plane"
    ))
    #########################################
    db.session.add(Voters_Table(
        user_id = 1,
        poll_id = 2,
        username = "kolis10",
        poll_name = "Is the government hiding aliens in area 51?",
        option_picked = "The Government is hiding something, just not aliens"
    ))
    db.session.add(Voters_Table(
        user_id = 2,
        poll_id = 2,
        username = "Naz",
        poll_name = "Is the government hiding aliens in area 51?",
        option_picked = "I'm a believer"
    ))
    db.session.add(Voters_Table(
        user_id = 3,
        poll_id = 2,
        username = "Curly-Fry",
        poll_name = "Is the government hiding aliens in area 51?",
        option_picked = "Conspiracy Theories aren't my thing"
    ))
    db.session.add(Voters_Table(
        user_id = 4,
        poll_id = 2,
        username = "Coder",
        poll_name = "Is the government hiding aliens in area 51?",
        option_picked = "The Government would never lie to us. Ever."
    ))
    db.session.add(Voters_Table(
        user_id = 5,
        poll_id = 2,
        username = "Rager",
        poll_name = "Is the government hiding aliens in area 51?",
        option_picked = "The Government would never lie to us. Ever."
    ))
    db.session.add(Voters_Table(
        user_id = 6,
        poll_id = 2,
        username = "Tony",
        poll_name = "Is the government hiding aliens in area 51?",
        option_picked = "I'm a believer"
    ))
    db.session.add(Voters_Table(
        user_id = 7,
        poll_id = 2,
        username = "Garcia Sausage",
        poll_name = "Is the government hiding aliens in area 51?",
        option_picked = "I'm a believer"
    ))
    db.session.add(Voters_Table(
        user_id = 8,
        poll_id = 2,
        username = "Boss Mom",
        poll_name = "Is the government hiding aliens in area 51?",
        option_picked = "The Government is hiding something, just not aliens"
    ))
    ######################################
    db.session.add(Voters_Table(
        user_id = 1,
        poll_id = 3,
        username = "kolis10",
        poll_name = "Should the drinking age be lowered to 18?",
        option_picked = "It should be raised"
    ))
    db.session.add(Voters_Table(
        user_id = 2,
        poll_id = 3,
        username = "Naz",
        poll_name = "Should the drinking age be lowered to 18?",
        option_picked = "Yes"
    ))
    db.session.add(Voters_Table(
        user_id = 3,
        poll_id = 3,
        username = "Curly-Fry",
        poll_name = "Should the drinking age be lowered to 18?",
        option_picked = "No, it's fine the way it is"
    ))
    db.session.add(Voters_Table(
        user_id = 4,
        poll_id = 3,
        username = "Coder",
        poll_name = "Should the drinking age be lowered to 18?",
        option_picked = "Yes"
    ))
    db.session.add(Voters_Table(
        user_id = 5,
        poll_id = 3,
        username = "Rager",
        poll_name = "Should the drinking age be lowered to 18?",
        option_picked = "No, it's fine the way it is"
    ))
    db.session.add(Voters_Table(
        user_id = 6,
        poll_id = 3,
        username = "Tony",
        poll_name = "Should the drinking age be lowered to 18?",
        option_picked = "No, it's fine the way it is"
    ))
    db.session.add(Voters_Table(
        user_id = 7,
        poll_id = 3,
        username = "Garcia Sausage",
        poll_name = "Should the drinking age be lowered to 18?",
        option_picked = "Yes"
    ))
    db.session.add(Voters_Table(
        user_id = 8,
        poll_id = 3,
        username = "Boss Mom",
        poll_name = "Should the drinking age be lowered to 18?",
        option_picked = "It should be raised"
    ))
    #######################################
    db.session.add(Voters_Table(
        user_id = 1,
        poll_id = 4,
        username = "kolis10",
        poll_name = "Is revenge cheating justified?",
        option_picked = "No, two wrongs won't make things right"
    ))
    db.session.add(Voters_Table(
        user_id = 2,
        poll_id = 4,
        username = "Naz",
        poll_name = "Is revenge cheating justified?",
        option_picked = "Yes, they have it coming"
    ))
    db.session.add(Voters_Table(
        user_id = 3,
        poll_id = 4,
        username = "Curly-Fry",
        poll_name = "Is revenge cheating justified?",
        option_picked = "Yes, they have it coming"
    ))
    db.session.add(Voters_Table(
        user_id = 4,
        poll_id = 4,
        username = "Coder",
        poll_name = "Is revenge cheating justified?",
        option_picked = "Yes, they have it coming"
    ))
    db.session.add(Voters_Table(
        user_id = 5,
        poll_id = 4,
        username = "Rager",
        poll_name = "Is revenge cheating justified?",
        option_picked = "No, two wrongs won't make things right"
    ))
    db.session.add(Voters_Table(
        user_id = 6,
        poll_id = 4,
        username = "Tony",
        poll_name = "Is revenge cheating justified?",
        option_picked = "Yes, they have it coming"
    ))
    db.session.add(Voters_Table(
        user_id = 7,
        poll_id = 4,
        username = "Garcia Sausage",
        poll_name = "Is revenge cheating justified?",
        option_picked = "No, two wrongs won't make things right"
    ))
    db.session.add(Voters_Table(
        user_id = 8,
        poll_id = 4,
        username = "Boss Mom",
        poll_name = "Is revenge cheating justified?",
        option_picked = "Yes, they have it coming"
    ))
    ###########################################
    db.session.add(Voters_Table(
        user_id = 1,
        poll_id = 5,
        username = "kolis10",
        poll_name = "Which is the better sport?",
        option_picked = "Football. The American Version"
    ))
    db.session.add(Voters_Table(
        user_id = 2,
        poll_id = 5,
        username = "Naz",
        poll_name = "Which is the better sport?",
        option_picked = "Basketball"
    ))
    db.session.add(Voters_Table(
        user_id = 3,
        poll_id = 5,
        username = "Curly-Fry",
        poll_name = "Which is the better sport?",
        option_picked = "I don't really watch these"
    ))
    db.session.add(Voters_Table(
        user_id = 4,
        poll_id = 5,
        username = "Coder",
        poll_name = "Which is the better sport?",
        option_picked = "Basketball"
    ))
    db.session.add(Voters_Table(
        user_id = 5,
        poll_id = 5,
        username = "Rager",
        poll_name = "Which is the better sport?",
        option_picked = "I don't really watch these"
    ))
    db.session.add(Voters_Table(
        user_id = 6,
        poll_id = 5,
        username = "Tony",
        poll_name = "Which is the better sport?",
        option_picked = "Basketball"
    ))
    db.session.add(Voters_Table(
        user_id = 7,
        poll_id = 5,
        username = "Garcia Sausage",
        poll_name = "Which is the better sport?",
        option_picked = "Baseball; there's a reason it's called America's Pastime."
    ))
    db.session.add(Voters_Table(
        user_id = 8,
        poll_id = 5,
        username = "Boss Mom",
        poll_name = "Which is the better sport?",
        option_picked = "Football. The American Version"
    ))
    ######################################
    db.session.add(Voters_Table(
        user_id = 1,
        poll_id = 6,
        username = "kolis10",
        poll_name = "What element would you want to control?",
        option_picked = "Earth"
    ))
    db.session.add(Voters_Table(
        user_id = 2,
        poll_id = 6,
        username = "Naz",
        poll_name = "What element would you want to control?",
        option_picked = "Air"
    ))
    db.session.add(Voters_Table(
        user_id = 3,
        poll_id = 6,
        username = "Curly-Fry",
        poll_name = "What element would you want to control?",
        option_picked = "Water"
    ))
    db.session.add(Voters_Table(
        user_id = 4,
        poll_id = 6,
        username = "Coder",
        poll_name = "What element would you want to control?",
        option_picked = "Water"
    ))
    db.session.add(Voters_Table(
        user_id = 5,
        poll_id = 6,
        username = "Rager",
        poll_name = "What element would you want to control?",
        option_picked = "Fire"
    ))
    db.session.add(Voters_Table(
        user_id = 6,
        poll_id = 6,
        username = "Tony",
        poll_name = "What element would you want to control?",
        option_picked = "Fire"
    ))
    db.session.add(Voters_Table(
        user_id = 7,
        poll_id = 6,
        username = "Garcia Sausage",
        poll_name = "What element would you want to control?",
        option_picked = "Air"
    ))
    db.session.add(Voters_Table(
        user_id = 8,
        poll_id = 6,
        username = "Boss Mom",
        poll_name = "What element would you want to control?",
        option_picked = "Fire"
    ))
    ######################################
    db.session.add(Voters_Table(
        user_id = 1,
        poll_id = 7,
        username = "kolis10",
        poll_name = "If you could travel in time, what would you want to see?",
        option_picked = "The past"
    ))
    db.session.add(Voters_Table(
        user_id = 2,
        poll_id = 7,
        username = "Naz",
        poll_name = "If you could travel in time, what would you want to see?",
        option_picked = "There is enough in the present"
    ))
    db.session.add(Voters_Table(
        user_id = 3,
        poll_id = 7,
        username = "Curly-Fry",
        poll_name = "If you could travel in time, what would you want to see?",
        option_picked = "There is enough in the present"
    ))
    db.session.add(Voters_Table(
        user_id = 4,
        poll_id = 7,
        username = "Coder",
        poll_name = "If you could travel in time, what would you want to see?",
        option_picked = "The past"
    ))
    db.session.add(Voters_Table(
        user_id = 5,
        poll_id = 7,
        username = "Rager",
        poll_name = "If you could travel in time, what would you want to see?",
        option_picked = "The future"
    ))
    db.session.add(Voters_Table(
        user_id = 6,
        poll_id = 7,
        username = "Tony",
        poll_name = "If you could travel in time, what would you want to see?",
        option_picked = "The past"
    ))
    db.session.add(Voters_Table(
        user_id = 7,
        poll_id = 7,
        username = "Garcia Sausage",
        poll_name = "If you could travel in time, what would you want to see?",
        option_picked = "There is enough in the present"
    ))
    db.session.add(Voters_Table(
        user_id = 8,
        poll_id = 7,
        username = "Boss Mom",
        poll_name = "If you could travel in time, what would you want to see?",
        option_picked = "The future"
    ))
    ######################################
    db.session.add(Voters_Table(
        user_id = 1,
        poll_id = 8,
        username = "kolis10",
        poll_name = "If you could have one of these superpowers, which one would you choose?",
        option_picked = "Telekinesis"
    ))
    db.session.add(Voters_Table(
        user_id = 2,
        poll_id = 8,
        username = "Naz",
        poll_name = "If you could have one of these superpowers, which one would you choose?",
        option_picked = "Super Strength"
    ))
    db.session.add(Voters_Table(
        user_id = 3,
        poll_id = 8,
        username = "Curly-Fry",
        poll_name = "If you could have one of these superpowers, which one would you choose?",
        option_picked = "Flight"
    ))
    db.session.add(Voters_Table(
        user_id = 4,
        poll_id = 8,
        username = "Coder",
        poll_name = "If you could have one of these superpowers, which one would you choose?",
        option_picked = "Flight"
    ))
    db.session.add(Voters_Table(
        user_id = 5,
        poll_id = 8,
        username = "Rager",
        poll_name = "If you could have one of these superpowers, which one would you choose?",
        option_picked = "Super Strength"
    ))
    db.session.add(Voters_Table(
        user_id = 6,
        poll_id = 8,
        username = "Tony",
        poll_name = "If you could have one of these superpowers, which one would you choose?",
        option_picked = "Invisibility"
    ))
    db.session.add(Voters_Table(
        user_id = 7,
        poll_id = 8,
        username = "Garcia Sausage",
        poll_name = "If you could have one of these superpowers, which one would you choose?",
        option_picked = "Telekinesis"
    ))
    db.session.add(Voters_Table(
        user_id = 8,
        poll_id = 8,
        username = "Boss Mom",
        poll_name = "If you could have one of these superpowers, which one would you choose?",
        option_picked = "Invisibility"
    ))


    ##################
    #     CHATS
    ##################

    db.session.add(Chats(
        poll_id = 1,
        username = "kolis10",
        message = "'Sup",
        created_at = now + timedelta(minutes=1)
    ))
    db.session.add(Chats(
        poll_id = 1,
        username = "Naz",
        message = "Konichiwa",
        created_at = now + timedelta(minutes=2)
    ))
    db.session.add(Chats(
        poll_id = 1,
        username = "Curly-Fry",
        message = "Hey",
        created_at = now + timedelta(minutes=3)
    ))
    db.session.add(Chats(
        poll_id = 1,
        username = "Coder",
        message = "Dude",
        created_at = now + timedelta(minutes=4)
    ))
    db.session.add(Chats(
        poll_id = 1,
        username = "Rager",
        message = "Yo",
        created_at = now + timedelta(minutes=5)
    ))
    db.session.add(Chats(
        poll_id = 1,
        username = "Tony",
        message = "Hi",
        created_at = now + timedelta(minutes=6)
    ))
    ############################################
    db.session.add(Chats(
        poll_id = 2,
        username = "Naz",
        message = "Konichiwa, kolis10",
        created_at = now + timedelta(minutes=1)
    ))
    db.session.add(Chats(
        poll_id = 2,
        username = "kolis10",
        message = "'Sup, Naz",
        created_at = now + timedelta(minutes=2)
    ))
    db.session.add(Chats(
        poll_id = 2,
        username = "Tony",
        message = "Hi, Curly-Fry",
        created_at = now + timedelta(minutes=3)
    ))
    db.session.add(Chats(
        poll_id = 2,
        username = "Rager",
        message = "Yo, Coder",
        created_at = now + timedelta(minutes=4)
    ))
    db.session.add(Chats(
        poll_id = 2,
        username = "Coder",
        message = "Dude, Rager",
        created_at = now + timedelta(minutes=5)
    ))
    db.session.add(Chats(
        poll_id = 2,
        username = "Curly-Fry",
        message = "Hey, Tony",
        created_at = now + timedelta(minutes=6)
    ))
    db.session.commit()
    return 'seeds ran successfully'