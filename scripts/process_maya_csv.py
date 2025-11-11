#!/usr/bin/env python3
"""
Process Maya Eiendom CSV actor data into JSON format
Handles multiline CSV fields
"""

import csv
import json
import sys
import re
from pathlib import Path

def clean_number(value):
    """Extract number from strings like 'NOK 87 mill.' or '0.3% av kjede'"""
    if not value or value == '-':
        return None

    # Remove NOK, mill., %, etc
    cleaned = re.sub(r'[^\d.,\-]', '', value)
    cleaned = cleaned.replace(',', '')

    try:
        return float(cleaned) if cleaned else None
    except ValueError:
        return None

def parse_revenue(value):
    """Parse revenue like 'NOK 87 mill.'"""
    if not value or value == '-':
        return None

    match = re.search(r'(\d+(?:\.\d+)?)\s*mill', value, re.IGNORECASE)
    if match:
        return float(match.group(1))

    # Try direct number
    num = clean_number(value)
    return num

def parse_percent(value):
    """Parse percentage like '0.3% av kjede' or '0.2%'"""
    if not value or value == '-':
        return None

    match = re.search(r'([\d.]+)%', value)
    if match:
        return match.group(1)

    return None

def process_csv(csv_file, output_file):
    """Process CSV and create actor JSON"""

    actors = []
    category_counts = {}

    with open(csv_file, 'r', encoding='utf-8') as f:
        # Use csv.reader to handle multiline fields properly
        reader = csv.reader(f)

        for row in reader:
            # Skip empty rows
            if not row or len(row) < 6:
                continue

            # Extract fields (based on the structure we saw)
            rank = row[0] if len(row) > 0 else ""
            navn = row[1] if len(row) > 1 else ""
            actor_type = row[2] if len(row) > 2 else ""
            adresse = row[3] if len(row) > 3 else ""
            kommune = row[4] if len(row) > 4 else ""
            omsetning_raw = row[5] if len(row) > 5 else ""
            kjede_prosent_raw = row[6] if len(row) > 6 else ""
            yoy_vekst_raw = row[7] if len(row) > 7 else ""
            ansatte_lokalt_raw = row[8] if len(row) > 8 else ""
            ansatte_kjede_raw = row[9] if len(row) > 9 else ""
            kjede_lokasjoner_raw = row[10] if len(row) > 10 else ""
            markedsandel_raw = row[11] if len(row) > 11 else ""

            # Skip if no name
            if not navn or navn.strip() == '':
                continue

            # Parse values
            omsetning = parse_revenue(omsetning_raw)
            kjede_prosent = parse_percent(kjede_prosent_raw)
            yoy_vekst = clean_number(yoy_vekst_raw)
            ansatte_lokalt = int(clean_number(ansatte_lokalt_raw) or 0)
            ansatte_kjede = int(clean_number(ansatte_kjede_raw) or 0)
            kjede_lokasjoner = int(clean_number(kjede_lokasjoner_raw) or 0)
            markedsandel = clean_number(markedsandel_raw)

            actor = {
                "rank": rank.strip(),
                "navn": navn.strip(),
                "type": actor_type.strip(),
                "adresse": adresse.strip(),
                "kommune": kommune.strip(),
                "omsetning": omsetning,
                "kjedeProsent": kjede_prosent,
                "yoyVekst": yoy_vekst,
                "ansatteLokalt": ansatte_lokalt,
                "ansatteKjede": ansatte_kjede,
                "kjedeLokasjoner": kjede_lokasjoner,
                "markedsandel": markedsandel
            }

            actors.append(actor)

            # Count categories
            if actor_type:
                category_counts[actor_type] = category_counts.get(actor_type, 0) + 1

    # Create output structure
    output = {
        "eiendomId": Path(output_file).stem,
        "actors": actors,
        "categoryStats": category_counts,
        "metadata": {
            "totalActors": len(actors),
            "categories": len(category_counts),
            "generatedDate": "2025-11-11T18:00:00Z",
            "source": f"Place Analysis CSV - {csv_file}"
        }
    }

    # Write JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"✓ Processed {len(actors)} actors")
    print(f"✓ Found {len(category_counts)} categories")
    print(f"✓ Output written to {output_file}")

    # Print top 5 categories
    if category_counts:
        print("\nTop categories:")
        for cat, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  - {cat}: {count} actors")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 process_maya_csv.py <csv_file> <output_file>")
        sys.exit(1)

    csv_file = sys.argv[1]
    output_file = sys.argv[2]

    process_csv(csv_file, output_file)
