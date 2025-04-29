import csv
import uuid
from faker import Faker
import random

fake = Faker()
Faker.seed(42)

def generate_vcard_entry(start_id, contact_id):
    rows = []
    uid = str(uuid.uuid4()) + ".vcf"
    fn = fake.name()
    last, first = fn.split()[-1], fn.split()[0]
    tel_entries = [fake.phone_number() for _ in range(random.randint(1, 3))]
    email = fake.email()

    rows.append((start_id, 'UID', uid))
    start_id += 1

    if random.random() > 0.1:
        rows.append((start_id, 'FN', fn))
        start_id += 1
        rows.append((start_id, 'N', f"{last};{first};;;"))
        start_id += 1

    for tel in tel_entries:
        rows.append((start_id, 'TEL', tel))
        start_id += 1

    if random.random() > 0.3:
        rows.append((start_id, 'EMAIL', email))
        start_id += 1

    if random.random() > 0.6:
        rows.append((start_id, 'ORG', fake.company()))
        start_id += 1

    if random.random() > 0.7:
        rows.append((start_id, 'TITLE', fake.job()))
        start_id += 1

    if random.random() > 0.8:
        rows.append((start_id, 'ADR', fake.address().replace('\n', ';')))
        start_id += 1

    return rows, start_id

def generate_synthetic_vcards(output_file, num_contacts=2000):
    current_id = 1
    all_rows = [("id", "name", "value")]

    for contact_id in range(num_contacts):
        rows, current_id = generate_vcard_entry(current_id, contact_id)
        all_rows.extend(rows)

    with open(output_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(all_rows)

    print(f"Synthetic file generated: {output_file}")

# Example usage
generate_synthetic_vcards("synthetic_vcards.csv", num_contacts=100000)
