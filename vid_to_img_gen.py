# pip install opencv-python
# python vid_to_img_gen.py --vid_input vid.mp4 --frame_skip 150
import cv2
import argparse
import os


def main(args):
    # Setting args
    image_counter = args.img_num
    output_dir = args.output_dir
    output_path = os.path.join(os.getcwd(), output_dir)
    frame_count = 0


    # Check if the image save folder exists
    if not os.path.exists(output_path):
        os.mkdir(output_path)


    # Create a VideoCapture object and read from input file
    # If the input is the camera, pass 0 instead of the video file name
    cap = cv2.VideoCapture(args.vid_input)
    
    # Check if camera opened successfully
    if not cap.isOpened(): 
        print("Error opening video stream or file")
    
    # Read until video is completed
    while(cap.isOpened()):
    # Capture frame-by-frame
        ret, frame = cap.read()
        
        if ret and not os.path.isfile(os.path.join(os.getcwd(), output_dir, f'img_{image_counter}.jpg')):
            if frame_count % int(args.frame_skip)==0:
                # Save the resulting frame
                cv2.imwrite(f'{output_path}/img_{image_counter}.jpg',frame)
                image_counter = image_counter + 1
                print(f'img_{image_counter}.jpg saved!')
            
            # Count the number of frames
            frame_count+=1
            if frame_count>50000:
                frame_count=0
                
        # Break the loop
        else: 
            break

    # When everything done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()
        



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_dir', default='images', help='folder to save the image')
    parser.add_argument('--img_num', default=0, help='image number to start')
    parser.add_argument('--vid_input', default=0, help='input video path')
    parser.add_argument('--frame_skip', default=30, help='input video path')
    
    args = parser.parse_args()
    
    main(args)