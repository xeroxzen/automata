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


def extract_social_media_ids(column):
    social_media_ids = []

    for url in column:
        if pd.notna(url) and isinstance(url, str) and url.strip():
            url_parts = url.split('/')

            domain = url_parts[2] if len(url_parts) >= 3 else None
            social_media_id = extract_user_alias(url, domain)

            if domain in social_media_dict.values():
                social_media_ids.append(social_media_id)
            else:
                social_media_ids.append('')

        else:
            social_media_ids.append('')

    return social_media_ids


def main(csv_file):
    df = pd.read_csv(csv_file, encoding='utf-8')

    for domain_key in social_media_dict.values():
        domain_rows = df['personal_www'].str.contains(domain_key)
        if domain_rows.any():
            df[domain_key] = ''

    for idx, row in df.iterrows():
        social_media_id = extract_social_media_ids(row)
        domain = social_media_id[:-1] if social_media_id else None

        if domain in social_media_dict.values():
            df.at[idx, domain] = social_media_id.split('.com/')[-1]

    # Populate the IDs to the corresponding columns
    for domain, key in social_media_dict.items():
        df[key] = df['personal_www'].str.extract(f'{key}(.*)')

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
