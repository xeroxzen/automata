import pandas as pd
import sys

social_media_dict = {
    'apple': 'apple',
    'facebook': 'facebook',
    'battlenet': 'battlenet',
    'aim': 'aim',
    'mailru': 'mailru',
    'ok': 'ok',
    'twitter': 'twitter',
    'roblox': 'roblox',
    'google': 'google',
    'vk': 'vk',
    'steam': 'steam',
    'leagueoflegends': 'leagueoflegends',
    'discord': 'discord',
    'icq': 'icq',
    'snapchat': 'snapchat',
    'instagram': 'instagram',
    'youtube': 'youtube',
    'telegram': 'telegram',
    'linkedin': 'linkedin',
    'yim': 'yim',
    'skype': 'skype',
    'github': 'github',
    'twitch': 'twitch',
    'spotify': 'spotify',
    'xbox': 'xbox',
    'reddit': 'reddit',
    'tiktok': 'tiktok',
    'flattr': 'flattr',
    'qq': 'qq',
    'openid.mail': 'mailru'
}


def extract_social_media_ids(df):
    for domain, key in social_media_dict.items():
        df[key] = df['personal_www'].str.extract(f'{key}(.*)')

    return df


if __name__ == '__main__':
    csv_file = sys.argv[1]
    df = pd.read_csv(csv_file, encoding='utf-8')

    df = extract_social_media_ids(df)

    new_csv_file = csv_file.replace(
        '.csv', '_with_social_media_ids_minimal_approach.csv')
    df.to_csv(new_csv_file, index=False)

    print(
        f"Social media IDs have been added, and the new CSV file has been saved at: {new_csv_file}")
