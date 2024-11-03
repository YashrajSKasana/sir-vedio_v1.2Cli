from SVD import download_video, get_V_link, get_V_title
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from re import findall

first_time: bool = True
def download(driver) -> None:
    globel first_time
    if first_time:
        input("Please press 'Enter Key' after luging in the website :)\n")
    first_time = False
    want_to_down_V: bool = (input("Do you want to download a video (y/n): ").lower() == "y")
    if want_to_down_V: 
        input("navigate to the desired video and press 'Enter Key' to download: ")
        try:
            down_vid = download_video(findall(r"\d{9}", get_V_link(driver))[0], get_V_title(driver))
        except NoSuchElementException:
            input("[Error]: Program is not able to find the element. You might be on wrong page please navigate to the video that you want ot download (if problem is still thar then Please contact yashraj): ")
            download(driver)
            return

        print("Downloading Audio file")
        down_vid.create_temp_file_ytdlp('A')
        print("Downloading Video file")
        down_vid.create_temp_file_ytdlp('V')
        print("merging Audio and Video files")
        down_vid.merge_file_ffmpeg()
        print("Download Completed!!!")

        if down_vid.chick_down_sussed():
            os.remove("temp/*")
        else:
            print("[Error]: Sorry, some thing went wrong during download process please contact yashraj.")

        download(driver)

@lambda fn:__name__ == "__main__" and fn()
def main() -> str:
    driver = webdriver.Chrome()
    driver.get("https://courses.thetestingacademy.com/courses/software-tester-blueprint/dashboard")
    download(driver)    
