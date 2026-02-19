#!/bin/bash
# Activate venv
source /Users/matgriffin/UKBinCollectionData/.venv/bin/activate

# Fetch JSON and generate ICS directly to iCloud
python3 uk_bin_collection/uk_bin_collection/collect_data.py \
  SouthNorfolkCouncil \
  "https://collections-southnorfolk.azurewebsites.net/calendar.aspx" \
  -u 2630112976 \
  | python3 create_ics_12mo.py
