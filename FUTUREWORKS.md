# Future improvements
## Current Ideas
There are certain ideas that I tried to implement but I simply could'nt beacuse of the restrictions of time, and the 
idea not working in the first try and interference with the quality of outputs. Here are the ideas:
<br> (1) **Google Image Search** - I used google images to search for images relevant to the context. But there were some
issues that I faced, formost of it, it was simply not AI generated. The project was about Content generation through
AI, and these images were not generally AI generated. Also the reason I did not use it was because it was distorting the 
outputs of the PDF. I tried editing the images using image genration model and giving it a touch of AI, but the model was 
not able to do that very well. So, I would love to explore this part. </br>
<br> (2) **User Interface** - I wanted to make a more sophisiticated user interface and application using Django, but the time was limited and since the
problem statement stated that the quality of the outputs should be top-notch, I decided to spent most of my time in Prompt
Engineering, and could not give it a lot of time. </br>
<br> (3) **Data backed content** - I wanted to make the content more useful backing it up by data and graphs ,but they would not fit in
all kind of contexts and the model outputs with this feature were inconsistent. So, I decided to remove this idea. I would love to make this feature
more consistent and this is guaranteed to give better results. </br>
<br> (4) Better cloud deployment - I wanted to deploy it on the cloud using AWS, but I was constantly getting some errors, and since the time was
not so much, I dropped this idea. This would give the model a stable deploy, and a CI/CD pipeline would allow continuous optimizations. </br>

## Future Ideas
These are the ideas that I did not try to implement and kept it for future plans :
<br> (1) **Open Source Models** - Even though the costs did'nt support hosting and fine tuning an open source models, it would be worth
a shot to try them, if the scale of the project was bigger. </br>
<br> (2) Just 4 days ago, **GPT-3.5-turbo was released to allow finetuning**, the cost associated with fine-tuning is also not a lot, for
our tasl, this would have beenmn very good, and also the api is hosted on their platform, so we would'nt have to deal with hosting the 
model, but since there were only 5 days left for the deadline. I decided not to dive into this. </br>
<br> (3) Currently the **number of tokens** of the model is limited by the OpenAI API, I would have loved to work on increasing the limits,
by trying out various preprocessing techniques. This would have added further to the functionality of the app. </br>
<br> (4) **Latency Issues** - The model takes about 1.5 minutes to prepare the content, this is alot and lot of this can be optimized 
using , **multhreading**, if given more time I would have given this a shot.</br>
