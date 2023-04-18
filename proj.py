import openai
import json
import os
import landslide # api for slides

# set up API key

key =  os.getenv("GPT")
openai.api_key = key

# define prompt for GPT-3
topic = input("Enter the topic of the presentation:")
class_name = input("Enter the class name: ")

prompt = "Write a bullet-point slideshow about ${topic} for a ${class_name} class."
"Create 15 slides. Write a title for each slide, and each slide should have at most 5 bullet points."
"Please format the entire thing in Markdown format, with each slide title being a markkdown `#` header. "
"Each slide should be separated by a `---`. Please place the Markdown in a code block so I can copy-paste it. " 
"Don't write an outline for slides;  write the content for them."

# set parameters for API request
model_engine = "text-davinci-003"
params = {
    "prompt": prompt,
    "temperature": 0.5,
    "max_tokens": 100,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0
}

try:
    # generate text using GPT-3
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=params["max_tokens"],
        temperature=params["temperature"],
        top_p=params["top_p"],
        frequency_penalty=params["frequency_penalty"],
        presence_penalty=params["presence_penalty"]
    )
    # print the generated text
    print(response.choices[0].text.strip())
  
except openai.APIError as e: 
    print("OpenAI API error: ", e)
