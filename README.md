# Natural Language Processing for Text Summarization

## Poster
![img](https://github.com/ACM-Research/NLP-Summarizer/blob/master/poster.JPG)

## Objective
As Natural Language Processing models and tools are becoming more powerful and precise, automated text summarization to extract critical information out of bodies of text has become more practical and important in a world surrounded by information. Researchers in NLP are constantly refining their tools and models to becoming the state of the art, but summarization models are often pigeonholed into a theme of text. We seek to analyze how different models perform summarization on varying corpora of text and to understand the comparative strengths and weaknesses that impact summarization performance. 
## Models
Summarization models can be broken into two types depending on how they generate summaries. 

- **Extractive summarization** is a type of summarization where words within the body of text are chosen to be part of the summary.
For example, extractive summarization is similar to highlighting important information when reading a paper and combining the highlighted parts of text to create a summary.

- **Abstractive summarization** models learn an internal language representation of the text to create its own unique human-like summarizations. For example, reading a piece of text and writing a summary in your own words is a type of abstractive summarization.  

The models we will analyze include:
* BERT (extractive)
* spaCy (extractive)
* t5 (abstractive)
* ERNIE (abstractive)
* Pegasus (abstractive)

## Tools/Resources

### Text Evaluation
[ROUGE](https://github.com/andersjo/pyrouge/tree/master/tools/ROUGE-1.5.5) - Recall-Oriented Understudy for Gisting Evaluation. Generally it is a set of metrics for evaluating summarization of texts

[pyRouge](https://pypi.org/project/rouge/) - Python wrapper for the ROUGE summarization evaluation package.

### Text Statistical Analysis
[textstat](https://pypi.org/project/textstat/) - Python package to calculate statistics from text to determine readability, complexity and grade level of a particular corpus.

### Natural Language Processing
[spaCy](https://spacy.io/) - Open source package used to perform information extraction and build natural language understanding systems for NLP analysis.

## Contributors
- [Adithya Viswanathan](https://github.com/AdithyaViswanathan1)
- [Dylan Trang](https://github.com/Trippt1c)
- [Fawaz Khurram](https://github.com/fawazkhurram)
- [Rick Gao](https://github.com/rickgao12)
- [Varun Joshi](https://github.com/varuncj02)
- [Brian Nguyen](https://github.com/briannoogin) - Research Lead
