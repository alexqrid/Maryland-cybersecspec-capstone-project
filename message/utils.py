from django.db import connection


def dbdump():
    cur = connection.cursor()
    cur.execute(
        """SELECT username, first_name, last_name,
           encode(secret_question,'hex') as secret_question, 
           encode(secret_answer,'hex') as secret_answer
           from user_user
            """)
    users = []
    for i in cur:
        users.append(dict(zip({j.name: "" for j in cur.description}, i)))

    cur.execute(
        """select b.username sender, 
                c.username recipient ,encode(content,'hex') as content ,created_at from chat_message a 
                    join user_user b on a.sender_id = b.id 
                    join user_user c on recipient_id = c.id""")

    messages = []
    for i in cur:
        temp = list(i)
        temp[-1] = temp[-1].strftime('%Y-%m-%d %H:%M:%S')
        messages.append(dict(zip({j.name: "" for j in cur.description}, temp)))

    return (users, messages)
