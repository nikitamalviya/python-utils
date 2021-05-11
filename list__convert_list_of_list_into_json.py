import datetime

res= [('nikitamalviya@gmail.com','ernikitamalviya09@gmail.com', datetime.datetime(2021, 4, 15, 13, 50, 17, 27000), 'dummy sncksn', 'dummy text', 'dummy ancm', 'dummy hbakjn', 'dummy jhssn'),
         ('nikitamalviya@gmail.com','ernikitamalviya@gmail.com', datetime.datetime(2021, 4, 15, 13, 50, 17, 27000), 'dummy sdsncksn', 'dummy ajdn', 'dummy bs', 'dummy ajbd', 'dummy aja'),
          ('nikitamalviya@gmail.com','ernikitamalviya@gmail.com', datetime.datetime(2021, 4, 15, 13, 50, 17, 27000), 'dummy ajkdb', 'dummy ahd', 'dummy ankd', 'dummy jakjdm', 'dummy adna'),
          ('nikitamalviya@gmail.com','ernikitamalviya@gmail.com', datetime.datetime(2021, 4, 15, 13, 50, 17, 27000), 'dummy abjcsm', 'dummy ads', 'dummy whdw', 'dummy wiwm', 'dummy whe'),
           ('nikitamalviya@gmail.com','ernikitamalviya@gmail.com', datetime.datetime(2021, 4, 18, 18, 41, 45, 673000), 'dummy hakdn', 'dummy ahis', 'dummy wiuyr', 'dummy wyeh', 'dummy wyh'), 
           ('nikitamalviya@gmail.com','ernikitamalviya@gmail.com', datetime.datetime(2021, 4, 15, 13, 50, 17, 27000), 'dummy nkjsn', 'dummy hdki', 'dummy wydhw', 'dummy wyeqjs', 'dummy ajd'), 
           ('nikitamalviya@gmail.com','ernikitamalviya@gmail.com', datetime.datetime(2021, 4, 18, 18, 41, 45, 673000), 'dummy dhsjbam', 'dummy weucb', 'dummy wuh', 'dummy wyged', 'dummy wugd')]


def convert_list_of_list_into_json(res):
    '''
    @param res : list of list 
    @param data : output dictionary
    @param index : dict key as index 
    '''
    data = {}
    index = 0
    for entry in res:
        data[index] = {'outlookaccountname':res[index][0],
            'sender':res[index][1],
            'emaildatetime':datetime.datetime.strptime(str(res[index][2]), '%Y-%m-%d %H:%M:%S.%f'),
            'emailsubject':res[index][3],
            'displayemail':res[index][4],
            'predictedservice':res[index][5],
            'predicted_category_verified':res[index][6],
            'predictedsubcategory':res[index][7]
            }
        index += 1
    return(data)


print(convert_list_of_list_into_json(res))
