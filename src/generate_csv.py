import os
import pandas as pd

def read_reviews_from_folder(folder_path, label):
    data = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, encoding='utf-8') as f:
                content = f.read().strip()
                data.append(content)
    return data

def save_reviews_to_csv(base_path, output_csv_path, folders_labels):
    all_reviews = []
    all_labels = []
    for folder_rel, label in folders_labels:
        folder_abs = os.path.join(base_path, folder_rel)
        reviews = read_reviews_from_folder(folder_abs, label)
        all_reviews.extend(reviews)
        all_labels.extend([label] * len(reviews))

    df = pd.DataFrame({
        'id': range(len(all_reviews)),
        'review': all_reviews,
        'label': all_labels
    })
    df.to_csv(output_csv_path, index=False, encoding='utf-8')
    print(f"Saved {output_csv_path} with {len(df)} entries.")

def save_urls_to_csv(base_path, filenames_labels, output_csv_path):
    urls = []
    labels = []
    for filename, label in filenames_labels:
        file_path = os.path.join(base_path, filename)
        with open(file_path, encoding='utf-8') as f:
            for line in f:
                urls.append(line.strip())
                labels.append(label)
    df = pd.DataFrame({
        'id': range(len(urls)),
        'url': urls,
        'label': labels
    })
    df.to_csv(output_csv_path, index=False, encoding='utf-8')
    print(f"Saved {output_csv_path} with {len(df)} entries.")

def save_vocab_to_csv(vocab_path, output_csv_path):
    with open(vocab_path, encoding='utf-8') as f:
        words = [line.strip() for line in f.readlines()]
    df = pd.DataFrame({
        'id': range(len(words)),
        'word': words
    })
    df.to_csv(output_csv_path, index=False, encoding='utf-8')
    print(f"Saved vocabulary to {output_csv_path}.")

def save_embedding_scores_to_csv(score_path, output_csv_path):
    with open(score_path, encoding='utf-8') as f:
        scores = [float(line.strip()) for line in f.readlines()]
    df = pd.DataFrame({
        'id': range(len(scores)),
        'score': scores
    })
    df.to_csv(output_csv_path, index=False, encoding='utf-8')
    print(f"Saved embedding scores to {output_csv_path}.")

if __name__ == "__main__":
    OUTPUT_DIR = "./data"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    BASE_PATH = "./aclImdb"

    # Train set
    save_reviews_to_csv(BASE_PATH + "/train", os.path.join(OUTPUT_DIR, "train.csv"), [
        ("neg", 0),
        ("pos", 1),
        ("unsup", -1)
    ])

    # Test set
    save_reviews_to_csv(BASE_PATH + "/test", os.path.join(OUTPUT_DIR, "test.csv"), [
        ("neg", 0),
        ("pos", 1)
    ])

    # URLs
    save_urls_to_csv(BASE_PATH + "/train", [
        ("urls_neg.txt", 0),
        ("urls_pos.txt", 1),
        ("urls_unsup.txt", -1)
    ], os.path.join(OUTPUT_DIR, "train_urls.csv"))

    save_urls_to_csv(BASE_PATH + "/test", [
        ("urls_neg.txt", 0),
        ("urls_pos.txt", 1)
    ], os.path.join(OUTPUT_DIR, "test_urls.csv"))

    # Vocabulary and scores
    save_vocab_to_csv(os.path.join(BASE_PATH, "imdb.vocab"), os.path.join(OUTPUT_DIR, "vocab.csv"))
    save_embedding_scores_to_csv(os.path.join(BASE_PATH, "imdbEr.txt"), os.path.join(OUTPUT_DIR, "embedding_scores.csv"))
