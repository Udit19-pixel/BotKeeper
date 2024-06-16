![image](https://github.com/Udit19-pixel/BotKeeper/assets/83877590/cd209c2e-5510-405b-9f95-4e0b650bb86c)
# BotKeeper

# Project Description
This project is a chatbot application developed with deep learning and a feed-forward neural network using PyTorch. It features a user-friendly system tray icon created with pystray for easy access. The application showcases advanced AI capabilities and seamless desktop integration.

# Project Requirements
- Python LTS version
- Tkinter for creating the container and overall design.
- pyTorch version == 2.0.1 (preferred)
- pystray version == 0.16.1 (preferred)
- nltk_utility : Machine learning toolkit

# Features

### The essential features of this project are -
- Tkinter GUI for intuitive interaction with delayed responses managed by scheduler.
- Utilizes PyTorch framework to enhance chatbot with advanced machine learning and using CUDA for GPU related hardware acceleration and faster computation of each subtask in the layers.
- NLTK integration empowers chatbot with robust natural language understanding.
- Introduces a delay in chatbot responses using a scheduler, simulating more natural conversation flow and enhancing user experience.
 - Using Docker to containerize the chatbot application, simplifying deployment and ensuring consistency across different environments.

# Project Structure and Build

## Directory Structure
- The Directory contains the python scripts for executing different component of the entire project. Since it's not a web application, gathering all the files in one folder will not cause a problem.
  
  <div align="center">
        <img src="https://github.com/Udit19-pixel/BotKeeper/blob/main/BotKeeper/Images/Project_Structure.png" alt="Project Structure" width="270" height="450">
  </div>

## Designing container
- Adding label, texts, scrollbar in the mainframe container for better design and a presentable UI using Tkinter's function.
- Setting up a textarea at the bottom of the container for allowing users to enter their messages.
- The messages are differentiated clearly so that user can understand what section of the container belongs to the reply given by the bot.
- All the above sections are defined in the app.py file alongside starting and stopping schedulers.

## JSON formatted segregation
- The intents.json file specifies how exactly the bot will be answer the query written by the user.
- Each label consists of "key-values" pair and are divided into categories called as "tag".
- Now, each "tag" is present with a set of "patterns" and "response" which helps the bot to understand what sort of pattern is it expecting and what response it can generate considering the response pair.

## Creating Neural network's Structure
- The Feedforward Neural Network are the simplest type of Artificial Neural Network which are used for variety of tasks such as classification problems. They process data on a single pass moving it from input layer to output layer without any feedback loops, through the hidden layers.
- In this project, for the sake of demonstration, three such hidden layers are created which refines the data as unit vectors for generating better results which each layer.
- Now, each layer consists of neurons which helps to transfer processed data from the preceding layer to the following layers, which is further done by an activation function (in my case, ReLU).
- The logic for this is defined in the model.py file.

## Processing and hardware acceleration
- The chat.py file defines how this computation is done and what can be selected as the closest answer/reply to what user is saying.
- Just to be clear, these vector values are resulted as probabilities and for my project, any output whose probability exceeds 0.75 becomes the most likely output.
- If no value is exceeding, then just tell the bot to return "I do not understand".
- Just to get faster results through this computation, we leverage pyTorch's CUDA library to change the device from CPU to GPU, if an external GPU is available, else continue using CPU.
- These responses are further loaded into a dictionary for each model_state. A numpy array is created for faster retrieval and compact size. A data.pth file is created when the computation is done which contains the serialised pyTorch state dictionary.

## Stemming and Tokenization
- In order to remove any extra and unwanted characters from the input given by the user, in the nltk_utility.py file, there are functions defined which inside this file like the tokenizer() and stemmer() which helps in creating indices for each word and using string's lowercase() function for uniformity.
- The function bag_of_words takes in the tokenized numpy array and initializes 1 to represent that all the words are equally likely.
- To establish this, I have used Porter_Stemmer which is one of the stuffing algorithm for performing the same task. 
 
## Finalizing the numpy array
- After the preprocessed numpy array is sent to the representation from the intents.json file, all extra items like punctuations and special characters gets removed.
- Thereafter, two sets of numpy array are creating for X_train and Y_train datasets which contain the above mentioned bag and labels.
- These values are divided into the batches of 8 for batch segregation and are feeded into the neural network using DataLoader and epochs which defines how many passes of dataset are to be made for refining.
- The torch.optim.Adam is the optimizer which helps in reaching the convergence point faster. This function takes in the learning rate.
- The crossEntropyLoss() method helps to compute the performance of the learning model.
- After every successive layer processing, the losses are accepted as input for the next layer and given a gradient value. All this computation is then stored in the data.pth file. Remember to run this file after every change made in the intents.json file. 

## Task Scheduling 
- The scheduler.py file contains the logic for generating a delayed response and showcasing the capabilities of threading in the Operating System.
- In the initializing method of this class, an empty array is taken an lock() function is called to achieve parallelism in threads. Then, After assigning a delay value in app.py file, adequate delay is generated, after which the next set is appended to the array.
- The tasks are scheduled on the basis of their respective thread processing time and sufficient delay is generated. 

## System Tray
- The System_tray.py file calls the start and stop scheduler methods which are called when the user clicks on them throw the system icons, present in the system tray.
- The start and stop container respectively calls the methods, after calling subprocesses for building and closing down docker container.
- The method icon.update_menu is called to create an icon of the program and the same is closed when the stop_container is called.

# Dockerizing Project
- The whole idea of dockerizing this project is to made it available for different type of environments so that it can run there too.
- First step is to create a requirements.txt file which contains the libraries needed for complete demonstration.
 ```
        pip freeze > requirements.txt
 ```
- The contents of this file will be :
```
    jsonschema==4.21.1
    jsonschema-specifications==2023.12.1
    nltk==3.8.1
    numpy==1.26.4
    pipreqs==0.5.0
    pystray==0.16.1
    tk==0.1.0
    torch==2.0.1
```
- The next step is to create dockerfile and docker-compose.yml files.
  - The Dockerfile begins with a base image sourced from Docker Hub, establishing the work directory, incorporating copy instructions, configuring runtime settings, exposing ports, and concluding with the execution command.

  - Docker-compose.yml serves to enhance comprehension of the Dockerfile by presenting its contents in a more accessible, human-readable format.

- Following will be the created docker image which can be seen in the Docker Desktop application.
  
    <div align="center">
        <img src="https://github.com/Udit19-pixel/BotKeeper/blob/main/BotKeeper/Images/Docker_%20image.png" alt="Docker image" width="600" height="350">
    </div>
    
# X11 Casting
- X11 Basics: X11, or X Window System, is a network-transparent window system that allows for graphical user interfaces on Unix-like operating systems, enabling GUIs for applications running on remote servers.

- Docker X11 Forwarding: To run GUI applications inside Docker containers, X11 forwarding is used to display the application's window on the host machine's screen, necessitating sharing the X11 socket with the container.

- Environment Variables: Setting the DISPLAY environment variable in the Docker container to host.docker.internal:0 allows the container to use the host's display server for rendering the GUI.

- Volume Mounting: Mounting /tmp/.X11-unix from the host to the container gives the container access to the X11 Unix socket, enabling communication with the host's X server.

- Security Considerations: Using xhost + on the host machine temporarily allows connections from all hosts, necessary for Docker to access the display but should be disabled (xhost -) after use for security reasons.

  <div align="center">
        <img src="https://github.com/Udit19-pixel/BotKeeper/blob/main/BotKeeper/Images/Docker_%20image.png" alt="Docker image" width="600" height="350">
        

  </div>
