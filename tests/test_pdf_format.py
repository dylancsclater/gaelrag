#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pytest
from pypdf import PdfReader
from pypdf.errors import PdfReadError

def test_is_pdf_format():
    file_path = '../data/inbound/gael.pdf'
    try:
        with open(file_path, 'rb') as file:
            pdf = PdfReader(file)
            assert pdf.is_encrypted == False
    except PdfReadError:
        pytest.fail(f"The file at {file_path} is not in PDF format.")


# In[ ]:




