import cv2
import mediapipe as mp
import pickle
import os

def create_dataset():
    # Import the mediapipe model for hand landmarks detection. Static images
    mp_hands = mp.solutions.hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

    # Path where all the data is stored
    DATA_PATH = "./data"
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)

    expressions = []
    labels = []

    print("Loading data...")

    print("Processing data...")

    for expression_dir in os.listdir(DATA_PATH):
        for sample_dir in os.listdir(os.path.join(DATA_PATH, expression_dir)):
            sample = []
            # Loop from 0 to 19, so that all the features are in order.
            for i in range(20):
                time_step = []

                # Added two lists to normalize the position of the hand in the frame
                norm_x = []
                norm_y = []
                count = 0

                filename = os.path.join(DATA_PATH, expression_dir, sample_dir, str(i) + ".jpg")

                # Load the image and then convert it from BGR to RGB
                img = cv2.imread(filename)
                rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                # Process the image to obtain the landmarks position (x,y)
                results = mp_hands.process(rgb_img)

                # Loop through all the landmarks
                for hand_landmarks in results.multi_hand_landmarks:
                    if len(results.multi_handedness) == 1:

                        for j in range(len(hand_landmarks.landmark)):

                            x = hand_landmarks.landmark[j].x
                            y = hand_landmarks.landmark[j].y

                            # Save the coordinates for a future normalization
                            norm_x.append(x)
                            norm_y.append(y)

                        for j in range(len(hand_landmarks.landmark)):

                            x = hand_landmarks.landmark[j].x
                            y = hand_landmarks.landmark[j].y

                            # NORMALIZATION
                            x = x - min(norm_x)
                            y = y - min(norm_y)

                            # Save the coordinates as features in our time_step
                            time_step.append(x)
                            time_step.append(y)

                        # Save the time steps into our sample expression
                        sample.append(time_step)

                    else:

                        if count < 21:

                            for j in range(len(hand_landmarks.landmark)):
                                x = hand_landmarks.landmark[j].x
                                y = hand_landmarks.landmark[j].y

                                # Save the coordinates for a future normalization
                                norm_x.append(x)
                                norm_y.append(y)

                            for j in range(len(hand_landmarks.landmark)):

                                x = hand_landmarks.landmark[j].x
                                y = hand_landmarks.landmark[j].y

                                # NORMALIZATION
                                x = x - min(norm_x)
                                y = y - min(norm_y)

                                # Save the coordinates as features in our time_step
                                time_step.append(x)
                                time_step.append(y)

                                count += 1

                            # Save the time steps into our sample expression
                            sample.append(time_step)

            # Save the sample of the expression into the expression list
            expressions.append(sample)
            # Save the label of the expression
            labels.append(expression_dir)

    print("Data processed SUCCESSFULLY!")

    print("Saving data...")

    # Store the dataset into a pickle file
    f = open("expressions.pickle", "wb")
    pickle.dump({'expressions': expressions, 'labels': labels}, f)
    f.close()

    print("Data saved SUCCESSFULLY!")





