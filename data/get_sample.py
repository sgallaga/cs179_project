import json

with open("data/yelp_academic_dataset_review.json" , "r", encoding="utf-8") as infile, open("data/sample_reviews.json", "w", encoding="utf-8") as outfile:
    for i, line in enumerate(infile):
        if i == 1000:
            break
        outfile.write(line)