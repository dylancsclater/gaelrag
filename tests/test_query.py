#!/usr/bin/env python
# coding: utf-8

# In[25]:


import logging
import pytest
import sys
from dotenv import load_dotenv
import os
from pinecone import Pinecone
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
)
from llama_index.vector_stores.pinecone import PineconeVectorStore

# Load environment variables from .env file
load_dotenv()

pinecone_api_key = os.environ.get('PINECONE_API_KEY')

@pytest.fixture(scope="module")
def pinecone_api_key():
    return os.environ.get('PINECONE_API_KEY')

@pytest.fixture(scope="module")
def pinecone_index(pinecone_api_key):
    if pinecone_api_key is None:
        pytest.skip("PINECONE_API_KEY environment variable is not set.")
    pinecone = Pinecone(api_key=pinecone_api_key)
    return PineconeVectorStore(pinecone.Index("gael"))

def test_pinecone_connection(pinecone_api_key):
    assert pinecone_api_key is not None, "PINECONE_API_KEY is not set."

def test_llama_index_query(pinecone_index):
    vector_store = pinecone_index
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
    query_engine = index.as_query_engine()
    response = query_engine.query("What is attention and why do I need it?")
    assert response is not None, "Query to LlamaIndex did not return a response."


# In[ ]:




