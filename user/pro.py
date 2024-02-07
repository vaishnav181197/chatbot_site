from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('jarvis', logic_adapters=['chatterbot.logic.BestMatch',

{'import_path': 'chatterbot.logic.BestMatch', 
'default_response': 'I am sorry, but I do not understand.',
'maximum similarity_threshold': 0.90}])

def chatbotfun(qstn):

    trainer = ListTrainer(bot)

    trainer.train([
    "Can you tell me the name of the institution",
    "Government polytechnic college.",

    "Please provide me with the address.",
    "Govt.Polytechnic College, Nedumkandam,idukki",

    "what about the district and city?",
    "kerala,nedumkandam",

    "Could you please explain about the college",
    """Government Polytechnic College, Nedumkandam is one,
    among the leading technical institutions in highrange since its venture in 1999
    Within a short span of time since its emergence GPTC has become successful in
    establishing itself as a leading premier professional educational institution by
    providing its excellence in the field of technology. It is a matter of immense pride
    that students who crossed the threshold of this pioneer institute are now placed in
    responsible and highly coveted positions all over the world and are contributing
    substantially in various fields""",

    "What courses and activities are available",
    "Computer engineering,Computer hardware engineering,Electronics engineering",

    "What is the sanctioned strength",
    "60",

    "Please let me know about the class times",
    "09:30 AM to 03:50 PM",

    "let me know about office timings",
    "09:00 AM to 05:00 PM",

    "How about the holidays",
    "all saturday & Govt holidays",

    "Please provide me with your contact information",
    "GPTC Nedumkandam,idukki,kerala,685553 ,Phone : 04868 - 234082 ,gptcnedumkandam@yahoo.co.in, info@gptcnedumkandam.ac.in",

    "What facilities are available there in the institution",
    """Library : Thiru Mahatma Gandhi said, the present day university is
    nothing but a cluster of books. Our library is working as an example for
    the above saying.
    Our Polytechnic College Library possesses many books in an ordered
    manner of various disciplines. It is computerized for the benefit of the
    students and is working 12 hours per day. Books are arranged with the
    retrieve time of less than 1 minute.
    We are providing book bank facilities to the students, thereby; students
    from low financial background can take text books for all their subjects
    with the due period of one semester. In accordance with the objective of
    the College, the library aims to develop a comprehensive collection of
    documents useful for researchers, the faculty and the student community.\n

    ○ Health club : A Healthy mind in a Healthy body so goes the adage.
    The Health Club is home to an ultra modern gymnasium in appropreate
    area, to the needs of the fitness enthusiasts. The staff and students are free
    to use the gymnasium, after class hours under the tutelage of professional
    trainers. The state-of-the-art equipments available include bench press,
    peck deck, bicep curl, lateral pulley and body twister machines.\n

    ○ Hostel : We provide excellent hostel facility for girls is taken care of by
    dedicated concerned staff. Affectionate discipline, tasty food at moderate
    rates and neat rooms with modern sanitation and professional laundry
    services are provided.Hostel Mess based on the dividing system and rent
    as per government norm(Rs.105 per month).\n

    ○ Canteen : We have canteen facility for accession to the students for their
    welfare at all time through out the year.It can accommodate more than
    50 students at a time. It caters the needs of the students of various
    backgrounds. We ensure the foods in neat and affordable rate. Foods
    provided are delicious, tasty and digestive. A month-end-payment facility
    is provided if need.\n

    ○ Auditorium : Our Polytechnic have auditorium which is situated in
    college campus. It is fully electrically furnished with sound system.
    Students cultural activities and PTA association meetings are held on here.

    ○ Transport : The college has a fleet of new bus to cater the transportation
    needs of students and staffs. It is servicing from Nedumkandam to and
    from college. The transportation wing always aims for safety of the
    students and staffs and hence experienced driver is employed to do this
    service.The facility is monthly or daily.""",

    "which is the affiliated university",
    "state board of technical education,kerala",

    "What type of institution is this",
    "government",

    "Please provide me with additional admission details",
    "http://gptcnedumkandam.ac.in/",

    ])

    rply=bot.get_response(qstn)
    # print(qstn)

    return rply