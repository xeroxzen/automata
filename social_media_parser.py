import pandas as pd
import sys

# Dictionary of social media networks and their keys
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
}


def extract_user_alias(url, domain):
    if domain and domain in social_media_dict:
        if domain == 'vk.com':
            return social_media_dict[domain] + url.split('/id')[-1]
        else:
            return social_media_dict[domain] + url.split('/')[-1]
    return ''


def extract_social_media_ids(row):
    url = row['personal_www']

    if pd.notna(url) and url.strip():
        url_parts = url.split('/')

        domain = url_parts[2] if len(url_parts) >= 3 else None
        social_media_id = extract_user_alias(url, domain)

        if domain in social_media_dict:
            return social_media_id
        else:
            return ''

    return ''


def main(csv_file):
    df = pd.read_csv(csv_file, encoding='utf-8')

    # Create new columns for each social media domain
    for domain_key in social_media_dict.values():
        df[domain_key] = ''

    # Populate the new columns with social media IDs
    for _, row in df.iterrows():
        social_media_id = extract_social_media_ids(row)
        domain = social_media_id[:-1] if social_media_id else None

        if domain in social_media_dict.values():
            df.at[_, domain] = social_media_id

    new_csv_file = csv_file.replace('.csv', '_with_social_media_ids.csv')
    df.to_csv(new_csv_file, index=False)

    print(
        f"Social media IDs have been added, and the new CSV file has been saved at: {new_csv_file}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the CSV file path as an argument.")
        sys.exit(1)

    csv_file = sys.argv[1]
    main(csv_file)
