# UTS Handbook V2

## Project Introduction

This project is for Assessment Task 3 for 41043 Natural Language Processing at UTS. [UTS Handbook](https://www.handbook.uts.edu.au/) is the web resource for finding information about degrees, majors, sub-majors, subjects, etc. The goal of this project is to recreate the UTS Handbook website with the following features:

1. **Subject Search**: Users can search for a subject by typing in a query in natural language using the search bar. To do this we will be a semantic search engine using text embeddings and vector search.

2. **RPL Helper**: RPL (Recognition of Prior Learning) is a process students need to go through when changing degrees. The RPL Helper will suggest subjects a student has already completed (that aren't explicitly required/recommended by their degree), that could be added to their RPL submission. *Note: This feature will become even more useful when we add subject data from other Universities.* This feature will be built using the text embeddings generated from the previous feature, in combination with similarity search.
