from description_audit_driver import main

# Define your paths
LEXICON_PATH = "/Users/oliviabuck/Desktop/data_audit_project/description-audit/lexicons/lexicons.csv"
OUTPUT_PATH = "output"
EAD_PATH = "NONE"  # or "NONE"
# MARCXML_PATH = "morgan_marc_xml/PeelAll20241120.xml"  # or "NONE"
MARCXML_PATH = "/Users/oliviabuck/Desktop/data_audit_project/description-audit/morgan_marc_xml/PeelAll20241120_2.xml"  # or "NONE"
# MARCXML_PATH = "/Users/oliviabuck/Desktop/data_audit_project/description-audit/source_data/sample_marcxml"

# Call the main function
if __name__ == "__main__":
    main(
        lexicon_csv_path=LEXICON_PATH,
        lexicon_test="ALL",  # or specific columns like "offensive_terms_slurs"
        hatebase_include=1,  # 0 or 1
        output_path=OUTPUT_PATH,
        ead_path=EAD_PATH,
        marcxml_path=MARCXML_PATH
    )
