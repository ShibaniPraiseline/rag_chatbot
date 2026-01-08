import numpy as np
from ingest.embedder import embedding_model


def retrieve_top_k(query, index, chunks, top_k=3):
    """
    Retrieve top-k most relevant chunks for a query.
    """
    query_embedding = embedding_model.encode(
        [query],
        convert_to_numpy=True
    )

    distances, indices = index.search(
        np.array(query_embedding),
        top_k
    )

    return [chunks[i] for i in indices[0]]


def build_context(chunks):
    """
    Combine retrieved chunks into a single context string.
    """
    return "\n\n".join(chunks)
