# TechSurf 2023 by ContentStack
Submission by Ankur Kumar Raj for **Problem Statement 2**.
## About me
A brief introduction about myself.
<br> Hi, My name is **Ankur Kumar Raj**, I am a final year undergraduate at IIT Kanpur, my primary interests include competitive programming, machine learning and deep learning. </br>
<br> Officially registered email ID on unstop - mr.anon57@gmail.com </br>
<br> College Email ID - ankurkraj20@iitk.ac.in </br>
<br> You can read about the methodology of the code at [PROCESS.MD](https://github.com/ankurkraj/NextGenAIContentGenerator/blob/main/PROCESS.md). and the scope of improvement over at </br>
<br> 

## Problem Statement and Key Requirements
>**Problem 2**: Design & Develop an impressive tool that utilizes generative AI to generate content while maintaining the style and tone of previously written content.
><br> Key Requirements: </br>
><br> ●	Generative AI Implementation: Build a robust generative AI model capable of analyzing and understanding the nuances of existing content. </br>
><br> ●	Style and Tone Preservation: Ensure that the generated content aligns with the style and tone of previously written content, providing a consistent and coherent output. </br>
><br> ●	Contextual Understanding: Develop the tool to comprehend the context of the given title/headlines, enabling it to generate relevant and meaningful content. </br>
><br> ●	User-Friendly Interface: Create an intuitive and user-friendly interface that allows users to input their existing title/headlines and receive generated content that matches their writing style. </br>
><br> ●	Quality and Accuracy: Strive for high-quality and accurate content generation by fine-tuning and optimizing the generative AI model. </br>

## Running it locally
I have deployed the app at **https://techsurf2023.streamlit.app/**, and you can access it directly from there, if you wish to run it locally kindly ensure that python >=3.9, and pip is installed and then take care of the following steps:-
<br> (1) Clone this repository (https://github.com/ankurkraj/NextGenAIContentGenerator) </br>
<br> (2) In the terminal open the folder of this repository </br>
<br> (3) You will need OpenAI API Key and Serper API key to run it locally, in the deployed version I have already bought one and put it, but if you wish to run it locally in the folder of the repo kindly create a folder by the name of ".streamlit" -> then create a file by the name of "secrets.toml". In secrets.toml you would need to add two variables in the following manner </br>

>openai_key = "YOUR_KEY"
><br> serper_api_key = "YOUR KEY </br>

OpenAI API Key can be obtained from https://platform.openai.com/account/api-keys and the Serper API key from https://serper.dev/. In case you face any issues with obtaining the API key, you can mail me at mr.anon57@gmail.com and I will send you my keys which you can use for running it locally
<br> (4) Run the following command  </br>
`pip install requirements.txt`
<br> (5) Then run the following command </br>
`streamlit run main.py`
<br> If everything workd out fine you should get a following message</br>

![deploy](https://github.com/ankurkraj/NextGenAIContentGenerator/assets/84915395/6866b89e-c548-4eee-875c-2b1ebe503f3b)

Then you can click on any of the two links and it should be working alright from there.

## Results 
I just want to say that I thoroughly enjoyed the project and gave it my best to make it as good as possible. I have summarized all the steps and what I have done to make the project what it is today at Steps.md, the amount of research and efforts that I have put and the decisions that I have taken and the reasons behind them. There are additional points at futureworks.md, where I mention about the things that I would like to work on if I was given more time. Finally here are the results of the kind of response my model produces. I have two examples to present 
<br>**1st Example**</br>
<br>The point of the project was that my model should be able to understand the tone and context of the input and further create content based on that. To demonstrate my model's competence for this I have used a tone which is very casual, and hip-hoppish, the narrator here is talking about the writer F. Scott Fitzgerald in a very informal tone. Here is the prompt that I gave to it. </br>
>**_Yo, boy cool_dude93 is here to drop some lines on the greatest american writers of all time, and this one goes to my man F. Scott. Fitzgerald_**

<br>Let's see the kind of output that my model produced</br>

![cool_writer](https://github.com/ankurkraj/NextGenAIContentGenerator/assets/84915395/260ca8b2-4d74-4e2c-8dd9-a7a9fb22dc35)

The model was able to **maintain the tone**.

<br> **2nd Example** </br>
<br> What should make my model stand out among the many submissions that you receive is the **amazing visuals** that it produces. The following is the prompt that I gave to my model : </br>

> **_A very vivid history of printing, printing has had a very old history, but none of them has stood the test of time as well as the typewriter has_**

<br>This is the response it produces, notice the description that is present below the image, this was generated by the Generative AI model, which could be achieved by experimenting a lot and using very precise prompt techniques. This is the prompt that the model is using to send the Image generation model, and based on this particulat prompt DALLE2, produced the image relevant to the context</br>

![typewriter](https://github.com/ankurkraj/NextGenAIContentGenerator/assets/84915395/054fb42f-cbbe-4471-b0ad-0e666d9e1636)

## Features of my model
I have taken care all the points that was mentioned in the problem statement while preparing my model. Here are the features that I have been able to integrate into my model
<br> (1) It can accept in many formats like **PDF, DOCX, and raw text**, adding to the versatility of the model is the fact that it can recognize the **headings** from the given input(As requried by the problem statement) when given in PDF or DOCX format, and if the heading is not there, it will **generate one on its own**. </br>
<br> (2) There is an **image generation model** integrated with it, and the image generation model uses correct prompt to add a image relevant to the generated context. </br>
<br> (3) Everything is done by AI, I have used multplie **LLMs in chain**, leveraging the full potential of LLMs, **a LLM is responsible for generating a prompt for another LLM, which generates the image based on this prompt**. This makes the model utilize the full potential of GenerativeAI. </br>
<br> (4) The drawback of LLMs is that their vast knowledge is limited by time which they were trained in, **their information is limited**, to tackle this problem I have used the **Google Search API and the Wikipedia API**, to provide the model latest information. </br>
<br> (5) The model can understand inputs in **multiple languages**, I have tried using Hindi for the model and it works extremetly well for that too, although the responses produed are still in **English** though.</br>
<br> (6) The response are produced are **extremely well formatted** and relevant to the context that is given in input. The PDF produced is **aesthetically pleasing** and there has been no compromise with the quality of responses. </br>
<br> (7) **Well organized and modular code** - The coding style is very clean, and modular, all the tasks have been handeled by functions, the code has been separated in to four parts, main.py is the proimary frontend of the model, response creator holds that backend of the model, while pdf creator is responsible for creating PDF and output formatting, and document formatter for preprocessing the inputs of various formatsThe code is very **well commented** </br>.

