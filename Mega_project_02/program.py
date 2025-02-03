import pyautogui
import time
import pyperclip
import requests
import json
# Step 1: Click on the icon
pyautogui.click(1284, 1047)
time.sleep(1)  # Wait for UI to respond

# Step 2: Drag to select text
pyautogui.moveTo(1026, 168)
pyautogui.mouseDown()
pyautogui.moveTo(1810, 722, duration=1)  # Smooth drag
pyautogui.mouseUp()

# Step 3: Copy to clipboard
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)  # Wait for clipboard to update
pyautogui.click(1766,665)

# Step 4: Retrieve text from clipboard
copied_text = pyperclip.paste()
print("Copied Text:", copied_text)

from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  model="openai/o1-preview",
  messages=[
    {
      "role": "you are prathamesh , he is tech inthusiast he is speak in hindi as well as english",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion)
print(completion.choices[0].message.content)
