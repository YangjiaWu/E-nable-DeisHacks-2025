from openai import OpenAI
import pandas as pd

def prompt_just_text(description, prompt):
  client = OpenAI()

  response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
          # I got all of these images from the top rated example of each type that I could find on imgflip
          {
            "type": "text", "text": prompt
          },
          {
            "type": "text", "text": "Please with response with just 1-3 words"
          },
        {"type": "text", "text": description},
      ],
    }
  ],
  max_tokens=20,
  )

  print(response.choices[0].message.content)
  

description = "This is a wrist-powered device. To use this design, the user must have a functional wrist and enough palm to push against..."

# prompt_just_text(description)