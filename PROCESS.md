#Process
<br> I would here like to discuss the process which the model went through in its making, the choices that I made and the places which took most time and effort.</br>
##Model Choice
<br> choosing the right model for these kind of tasks was very important ,and I made the decision to use th GPT-3.5 turbo model,
I wanted to use an open source model, but did'nt. Here are the reasons for my model choice</br>
<br> (1) GPT-3.5-turbo is the best in class, as it was said in the problem statement that the quality of the model should be top notch and there should not be any compromise with that, I decided to use the OpenAI's GPT-3.5-turbo.</br>
<br> (2) I would have loved to experiment with open source model, but for such a small scale project the cost seemed too high for an open source model considering that they are not tailor made for this task, and there would be
investment associated with fine-inference, and hosting . Taking all of this into consideration open source model were not guaranteed to give results better than that of GPT-3.5-turbo, and the cost associate with fine-tuning,
inference and hosting simply made it not worth the task.</br>
<br> (3) My previous experience with GPT-3.5-turbo, I have previously done a internship in Generative AI and I know the potential of GPT-3.5, so I knew that I just need to know the right tools to use it correctly,
and it will give me the correct outputs, because of this I have spend most of my time in Prompt Engineering rather than Fine - Tuning.</br>

##Model Response Design
<br> The design of model response involved multiple steps and they are listed below:</br>
<br> (1) The first step involved taking the input it could be taken in any format PDF,DOCX, or raw text, so I had to create an interface for that along with a heading parser to parse the heading incase it was given in input. </br>
<br> (2) Instruction Prompting - Prompting the model to produce the right kind of response by making it aware of its purpose, this was done through system prompting.</br>
<br> (3) Few shot prompting and rewarding - Use of the few shot prompting by using the input of the user and rewarding the model, prompted the model to produce that kind of response, and this I feel was the key of the project, this made the model
learn about the kind of style.</br>
<br> (4) Heading recognization - If heading was not given, it was generated and the search apis were used to extract information about this and this gave the model latest information that it used.</br>
<br> (5) Tone recognition - Again tone was recognized by giving the model some examples, and this helped in establishing the overall mood the output.</br>

##Image generation 
<br> I felt that this is the one idea that would make my stand out among all the other submissions, and I worked diligently on this. Here is how I did it:</br>
<br> (1) I used a few example to a llm, and told it that its purpose was to generate prompts for DALLE2 image generation model.</br>
<br> (2) Then the model was fed the heading, and it was asked to generate a prompt for DALLE2, the instruction prompting here was done very carefully which led to such appealing and amazing images</br>

##Formatting
<br> This was the most challenging part, to format a PDF of unknown content. Here is how I implemented it:</br>
<br> (1) I used output parsers to output some useless text and use fpdf2 library to carefully outline the text</br>
<br> (2) This took a lot of my time and I believe it gave my project the aesthetics that it currently has, and is apparent in the result. </br>

<br>**Overall, the area where I had to spend most of my time was in prompt engineering, the amazing outputs that my model presents, and the vivdly abstract images
are a result of rigorous prompt engineering**</br>
