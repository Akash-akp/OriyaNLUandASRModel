<h1 align="center">Oriya NLU and ASR Model</h1>
<p align="center"> This is a virtual assitant chatbot with which you can talk in oriya language </p>

# How to use this file 
- After cloning it in you local environment, create a virtal python environment
  ```
  python -m venv .\venv
  ```
- Activate the virtual environment
  ```
  source venv/bin/activate
  ```
- Install rasa library
  ### In Windows
  ```
  pip install rasa
  ```
  ### In Mac
  ```
  pip3 install rasa
  ```
- Train the rasa model
  ```
  rasa train
  ```
- Use this command to activate rasa chatbot on web
  ```
  rasa run -m model --enable-api --cors "*"
  ```
- Open the index.html file
