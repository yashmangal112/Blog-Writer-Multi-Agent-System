from crewai import Crew
from tasks import plan_task, write_task, edit_task
import gradio as gr

# Initialize Crew with agents and their tasks
blog_crew = Crew(
    agents=[plan_task.agent, write_task.agent, edit_task.agent],
    tasks=[plan_task, write_task, edit_task],
    verbose=True
)

# Function to run the blog creation workflow
def generate_blog(topic):
    if not topic or topic.strip() == "":
        return "❌ Error: Please enter a valid topic for the blog post."
    if len(topic.strip()) < 5:
        return "❌ Error: The topic is too short. Please provide a more detailed topic."

    print(f"Starting the Blog Writer Multi-Agent System for topic: {topic}")
    try:
        inputs = {"topic": topic}
        result = blog_crew.kickoff(inputs=inputs)
        print("Blog content creation completed!")
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"❌ Error: Failed to generate the blog post. Please try again with a different topic."

# Gradio Interface
def gradio_interface(topic):
    blog_content = generate_blog(topic)
    return blog_content

# Create Gradio app
interface = gr.Interface(
    fn=gradio_interface,
    inputs=gr.Textbox(lines=2, placeholder="Enter the topic for your blog post...", label="Blog Topic"),
    outputs=gr.Textbox(lines=20, label="Generated Blog Post"),
    title="AI-Powered Blog Writer",
    description="A Multi-Agent System for Automated Content Creation. Enter a topic, and the system will generate a blog post for you!"
)

# Run the Gradio app
if __name__ == "__main__":
    interface.launch()