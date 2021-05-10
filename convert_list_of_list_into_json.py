import datetime

res= [('nikita.malviya09@futuregenerali.in','ernikitamalviya@gmail.com', datetime.datetime(2021, 4, 15, 13, 50, 17, 27000), '[External]Network vpn access', 
        '<html><head>\r\n\r\n</head>\r\n<body>\r\n<p><span style="background-color: #ffff99;">*** CAUTION : This email is originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. ***<', 
        'Server Management', 'Access Request', 'Port Opening'),
         ('nikita.malviya09@futuregenerali.in','ernikitamalviya@gmail.com', datetime.datetime(2021, 4, 15, 13, 50, 17, 27000), '[External]Network vpn access', '<html><head>\r\n\r\n</head>\r\n<body>\r\n<p><span style="background-color: #ffff99;">*** CAUTION : This email is originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. ***<', 'Server Management', 'Access Request', 'Port Opening'),
          ('nikita.malviya09@futuregenerali.in','ernikitamalviya@gmail.com', datetime.datetime(2021, 4, 15, 13, 50, 17, 27000), '[External]Network vpn access', '<html><head>\r\n\r\n</head>\r\n<body>\r\n<p><span style="background-color: #ffff99;">*** CAUTION : This email is originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. ***<', 'Server Management', 'Access Request', 'Port Opening'),
          ('nikita.malviya09@futuregenerali.in','ernikitamalviya@gmail.com', datetime.datetime(2021, 4, 15, 13, 50, 17, 27000), '[External]Network vpn access', '<html><head>\r\n\r\n</head>\r\n<body>\r\n<p><span style="background-color: #ffff99;">*** CAUTION : This email is originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. ***<', 'Server Management', 'Access Request', 'Port Opening'),
           ('nikita.malviya09@futuregenerali.in','ernikitamalviya@gmail.com', datetime.datetime(2021, 4, 18, 18, 41, 45, 673000), '[External]New server for AI projects development', '<html><head>\r\n\r\n</head>\r\n<body>\r\n<p><span style="background-color: #ffff99;">*** CAUTION : This email is originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. ***<', 'Server Management', 'Access Request', 'Port Opening'), 
           ('nikita.malviya09@futuregenerali.in','ernikitamalviya@gmail.com', datetime.datetime(2021, 4, 15, 13, 50, 17, 27000), '[External]Network vpn access', '<html><head>\r\n\r\n</head>\r\n<body>\r\n<p><span style="background-color: #ffff99;">*** CAUTION : This email is originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. ***<', 'Server Management', 'Access Request', 'Port Opening'), 
           ('nikita.malviya09@futuregenerali.in','ernikitamalviya@gmail.com', datetime.datetime(2021, 4, 18, 18, 41, 45, 673000), '[External]New server for AI projects development', '<html><head>\r\n\r\n</head>\r\n<body>\r\n<p><span style="background-color: #ffff99;">*** CAUTION : This email is originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. ***<', 'Server Management', 'Access Request', 'Port Opening')]


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