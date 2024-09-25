import chainlit as cl
from image_analyzer import analyze_image

@cl.on_chat_start
async def start():
    await cl.Message(content="Welcome to the Image Analyzer! Please upload an image and provide a question about it.").send()

@cl.on_message
async def main(message: cl.Message):
    # Check if there's an image attachment
    if not message.elements:
        await cl.Message(content="Please upload an image and provide a question about it.").send()
        return

    image = message.elements[0]
    if image.type != "image":
        await cl.Message(content="The uploaded file is not an image. Please try again with an image file.").send()
        return

    # Get the user's question about the image
    question = message.content.strip()
    if not question:
        await cl.Message(content="Please provide a question about the image.").send()
        return

    # Analyze the image with the user's question
    async with cl.Step("Analyzing image..."):
        result = analyze_image(question, image.path)

    # Send the analysis result
    await cl.Message(content=f"Analysis result: {result}").send()

if __name__ == "__main__":
    cl.run()
