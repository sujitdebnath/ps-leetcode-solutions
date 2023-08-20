import pandas as pd

def email_validity_check(email):
    if '@' not in email:
        return False
    else:
        email_list = email.split('@')
        prefix, domain = email_list[0], email_list[1]

        if domain != 'leetcode.com':
            return False
        elif not prefix[0].isalpha():
            return False
        else:
            for ch in prefix[1:]:
                if (not ch.isalpha()) and (not ch.isdigit()) and (ch not in ['_', '.', '-']):
                    return False
            return True

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    users['valid_email'] = users.apply(lambda x: email_validity_check(x['mail']), axis=1)
    users                = users[users['valid_email'] == True]

    return users[['user_id', 'name', 'mail']]