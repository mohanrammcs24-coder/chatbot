from sentence_transformers import SentenceTransformer, util
from data import faq_data
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

questions = [item["question"] for item in faq_data]
question_embeddings = model.encode(questions, convert_to_tensor=True)

def get_response(user_input):
    user_embedding = model.encode(user_input, convert_to_tensor=True)

    
    similarities = util.cos_sim(user_embedding, question_embeddings)[0]

    best_match_index = similarities.argmax().item()
    best_score = similarities[best_match_index].item()

    if best_score > 0.5:
        return faq_data[best_match_index]["answer"]

    return "Sorry, I didn’t understand that. Can you rephrase?"
