from agno.agent import Agent
from agno.models.ollama import Ollama

# Create agent once
agent = Agent(
    model=Ollama(id="llama3.2"),
    markdown=True,
    instructions="""
You are an intelligent assistant that converts video transcripts into structured study notes.

Rules:
- Use clear section headings
- Use bullet points
- Keep language concise
- Avoid repetition
- Highlight key ideas

Output Format:

# Title

## Topics Covered
- ...

## Detailed Notes
- ...

## Key Takeaways
- ...
"""
)

def generate_notes(transcript):
    # Prevent overload (important)
    transcript = transcript[:8000]

    response = agent.run(
    f"""
    Convert this transcript into structured notes.

    Transcript:
    {transcript}
    """
    )
    return response.content