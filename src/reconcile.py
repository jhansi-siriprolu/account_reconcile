import recordlinkage
from src.preprocess import preprocess_data

def match_transactions(bank_raw, ledger_raw):
    bank = preprocess_data(bank_raw, source='bank')
    ledger = preprocess_data(ledger_raw, source='ledger')
    indexer = recordlinkage.Index()
    indexer.block('date')
    candidate_links = indexer.index(bank, ledger)
    compare = recordlinkage.Compare()
    compare.exact('transaction_type', 'transaction_type', label='type')
    compare.string('clean_desc', 'clean_desc', method='jarowinkler', threshold=0.85, label='desc')
    compare.numeric('amount', 'amount', offset=5, label='amount')
    features = compare.compute(candidate_links, bank, ledger)
    clf = recordlinkage.LogisticRegressionClassifier()
    clf.fit(features)
    predictions = clf.predict(features)
    return predictions, features

def evaluate_model(predictions, features, true_links=None):
    if true_links:
        evaluator = recordlinkage.Evaluation(true_links, predictions)
        return {
            "precision": evaluator.precision(),
            "recall": evaluator.recall(),
            "f1": evaluator.fscore()
        }
    return {"matched_pairs": len(predictions)}