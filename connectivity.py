from openai import OpenAI
import os
try:
    print("✅ Environment ready. Connecting to Ollama...")

    # Connect to local Ollama (no paid API key needed)
    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"   # required by the library, but ignored by Ollama
    )
    ### FIRST PROMPT 
    prompt1 = "What is prompt engineering? Answer in one sentence."
    print(f"\nPrompt: {prompt1}")

    response = client.chat.completions.create(
        model="llama3.2",          # change to phi3 or gemma2:2b if you pulled those
        messages=[
            {
                "role": "user",
                "content": prompt1
            }
        ]
    )

    answer1 = response.choices[0].message.content
    print("\nResponse:")
    print(answer1)

    ### SECOND PROMPT
    prompt2 = "What is the capital of INDIA?"
    print(f"\nPrompt: {prompt2}")
    
    response = client.chat.completions.create(
               model="llama3.2",          # change to phi3 or gemma2:2b if you pulled those
               messages=[
                {
                    "role": "user",
                    "content": prompt2
                }
            ]
        )
    
    answer2 = response.choices[0].message.content
    print("\nResponse:")
    print(answer2)
    ### THIRD PROMPT
    prompt3 = "What is a Research Paper in one line?"
    print(f"\nPrompt: {prompt3}")
    response = client.chat.completions.create(
                   model="llama3.2",          # change to phi3 or gemma2:2b if you pulled those
                   messages=[
                    {
                        "role": "user",
                        "content": prompt3
                    }
                ]
            )
        
    answer3 = response.choices[0].message.content
    print("\nResponse:")
    print(answer3)

    print("\n✅ Connectivity verified successfully with three prompts.")


except Exception as e:
    print(f"❌ Error: {e}")
    print("\nMake sure Ollama is running and the model is downloaded.")
    print("Run: ollama serve")
    print("Then: ollama pull llama3.2")

