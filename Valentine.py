import cv2
import numpy as np

def generate_valentine_card(name, message, image_path="heart.png"):
    
    heart_image = cv2.imread(image_path)
    if heart_image is None:
        print("Image not found! Please check the image path.")
        return
    
    card_height, card_width, _ = heart_image.shape
    card_height += 100
    card = np.ones((card_height, card_width, 3), dtype=np.uint8) * 255
    
    card[0:heart_image.shape[0], 0:heart_image.shape[1]] = heart_image
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7
    color_name = (0, 0, 255)  # Red color in BGR
    color_message = (255, 0, 255)  # Magenta color in BGR
    color_closing = (255, 0, 0)  # Blue color in BGR
    
    name_position = (20, heart_image.shape[0] + 20)
    message_position = (20, heart_image.shape[0] + 50)
    closing_position = (20, heart_image.shape[0] + 80)
    
    cv2.putText(card, f"Dear {name},", name_position, font, font_scale, color_name, 2)
    cv2.putText(card, message, message_position, font, font_scale, color_message, 2)
    cv2.putText(card, "With Love,", closing_position, font, font_scale, color_closing, 2)
    cv2.putText(card, "Your Secret Admirer", (closing_position[0], closing_position[1] + 30), font, font_scale, color_closing, 2)
    
    return card

# Example usage
name = "Tasha"
message = "Wishing you a day filled with love and happiness! Happy Valentine's Day!"
card = generate_valentine_card(name, message)
if card is not None:
    cv2.imshow("Valentine Card", card)  
