# TechSurf 2023 by ContentStack
Submission by Ankur Kumar Raj for problem statement 2.
## About me
A brief introduction about myself.
Hi, My name is Ankur Kumar Raj, I am a final year undergraduate at IIT Kanpur, my primary interests include competitive programming, machine learning and deep learning.
Officially registered email ID on unstop - mr.anon57@gmail.com
College Email ID - ankurkraj20@iitk.ac.in

## Problem Statement and Key Requirements
>Problem 2: Design & Develop an impressive tool that utilizes generative AI to generate content while maintaining the style and tone of previously written content.
>Key Requirements:
>●	Generative AI Implementation: Build a robust generative AI model capable of analyzing and understanding the nuances of existing content.
>●	Style and Tone Preservation: Ensure that the generated content aligns with the style and tone of previously written content, providing a consistent and coherent output.
>●	Contextual Understanding: Develop the tool to comprehend the context of the given title/headlines, enabling it to generate relevant and meaningful content.
>●	User-Friendly Interface: Create an intuitive and user-friendly interface that allows users to input their existing title/headlines and receive generated content that matches their writing style.
>●	Quality and Accuracy: Strive for high-quality and accurate content generation by fine-tuning and optimizing the generative AI model.

## Running it locally
I have deployed the app at https://techsurf2023.streamlit.app/, and you can access it directly from there, if you wish to run it locally kindly ensure that python >=3.9, and pip is installed and then take care of the following steps:-
(1) Clone this repository (https://github.com/ankurkraj/NextGenAIContentGenerator)
(2) In the terminal open the folder of this repository
(3) You will need OpenAI API Key and Serper API key to run it locally, in the deployed version I have already bought one and put it, but if you wish to run it locally in the folder of the repo kindly create a folder by the name of ".streamlit" -> then create a file by the name of "secrets.toml". In secrets.toml you would need to add two variables in the following manner

> openai_key = "YOUR_KEY"
> serper_api_key = "YOUR KEY

OpenAI API Key can be obtained from https://platform.openai.com/account/api-keys and the Serper API key from https://serper.dev/. In case you face any issues with obtaining the API key, you can mail me at mr.anon57@gmail.com and I will send you my keys which you can use for running it locally
(4) Run the following command 
`pip install requirements.txt`
(5) Then run the following command
`streamlit run main.py`
If everything workd out fine you should get a following message
![deploy](https://github.com/ankurkraj/NextGenAIContentGenerator/assets/84915395/6866b89e-c548-4eee-875c-2b1ebe503f3b)
Then you can click on any of the two links and it should be working alright from there.
