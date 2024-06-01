# app.py
import streamlit as st
import pygame
import pyttsx3

# Function to simulate the game
def simulate_game():
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Simulation")

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (400, 300), 30)
        pygame.display.update()

    pygame.quit()

# Function to speak text
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Streamlit UI
def main():
    st.title("Simulation App")

    st.write("Press the button to simulate the game.")
    if st.button("Simulate Game"):
        simulate_game()

    st.write("Enter text below to hear it spoken aloud.")
    text_input = st.text_input("Enter text:")
    if st.button("Speak"):
        speak(text_input)

if __name__ == "__main__":
    main()
