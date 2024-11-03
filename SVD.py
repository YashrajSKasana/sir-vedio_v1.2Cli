import subprocess as sp
from selenium.webdriver.common.by import By
from typing import Callable
import os

class download_video():
    FFMPEG: str = r".\Dependencies\FFmpeg-Sorce\ffmpeg-master-latest-win64-gpl-shared\bin\ffmpeg.exe"
    YT_DLP: str = r"Dependencies\Yt-Dlp-Sorce\yt-dlp.exe"

    def __init__(self, V_code: str, V_title: str) -> None:
        self.V_code = V_code
        self.V_title = V_title 
        self.audio_form, self.video_form = self.get_formate()
        self.pwsh_run = lambda cmd: sp.run(['powershell','-c', f"{cmd}"], shell=True)

    def get_formate(self) -> tuple[str, str]:

            extract_format: Callable[[str], tuple[str, str]] = lambda strings, query_str: next((s.split(' ')[0] for s in strings if query_str in s), "")
            with open("temp/temp.txt","w") as f:
                    sp.run(['pwsh','-c', f"{self.YT_DLP} -F https://player.vimeo.com/video/{self.V_code} --ffmpeg-location {self.FFMPEG}"], shell=True, text=True, stdout=f)

            with open("temp/temp.txt","r") as f:
                    l = list(filter(lambda line:"mp4" in line,f)) 
    
                    audio_form: str =extract_format(l,"audio only")
                    video_form: str = extract_format(l[::-1],"video only")

            return audio_form, video_form

    def create_temp_file_ytdlp(self, type: str) -> None:
        formate: str = {"V" : self.video_form, "A" : self.audio_form}.get(type)
        down_cmd: str = fr"{self.YT_DLP} -f {formate} 'https://player.vimeo.com/video/{self.V_code}'  --ffmpeg-location {self.FFMPEG} -o 'temp\temp_{type + "_" + self.V_title}.mp4'"
        self.pwsh_run(down_cmd)

    def merge_file_ffmpeg(self) -> None:
        self.pwsh_run(fr"{self.FFMPEG} -i 'temp/temp_A_{self.V_title}.mp4' -i 'temp/temp_V_{self.V_title}.mp4' -c copy 'output\Video_{self.V_title}.mp4'")

    def chick_down_sussed(self) -> bool:
        return os.path.exists(fr"output\Video_{self.V_title}.mp4")

def get_V_link(driver) -> str:
    element = driver.find_element(By.CSS_SELECTOR, "div.panel_video > iframe")
    return element.get_attribute('src')

def get_V_title(driver) -> str:
    element = driver.find_element(By.CSS_SELECTOR, "li#contentName > span")
    return element.text

@lambda fr:__name__ == "__main__" and fr()
def main() -> None:
    input_video_code: str = input("Enter video code: ")
    input_title: str = input("Enter A title for video: ")
    down_vid = download_video(input_video_code, input_title)
    down_vid.create_temp_file_ytdlp('A')
    down_vid.create_temp_file_ytdlp('V')
    down_vid.merge_file_ffmpeg()
    if down_vid.chick_down_sussed(): os.remove("temp\*")