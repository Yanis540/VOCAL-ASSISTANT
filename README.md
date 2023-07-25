# VOCAL ASSISTANT
<p>
  This project allows to use the full Power of AI. I used for this the Whisper model for speech to text recognition. 
  Then used the ChatGPT 3.5 - Turbo Model just to get the answers by streaming it directly. Then used the Bark model 
  to generate Audio from the answer. One problem i want to mention is that i ran this on my PC which for some reason 
  did not want to use the GPU, if it's you case then it will be very slow. So just make sure you run this on a GPU.
  <br />
  <br />
  <br />
  Don't hesitate to modify the code. For example the <strong>ask_stream</strong> function can be modified to <strong>display and launch audio for each word</strong>.
</p> 

  ```python
    def ask_stream() 
      ... 
      for response in openai.ChatCompletion.create(...): 
        #Code 
      text_to_audio(full_answer)
      #Display word by word to get Typing effect
  ```

<p>
  Can be changed to 
</p>

 ```python
    def ask_stream() 
      ... 
      for response in openai.ChatCompletion.create(...): 
        #Code 
        text_to_audio(answer_word)
        #Display word 
  ```
