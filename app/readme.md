
# Skillease

This project is a web application that allows users to automatically create a transcript of a video by uploading the video. It also allows users to change the audio of the video and produce a new video with a changed voiceover. The application also has a section where a mentor can update his/her details and post courses that users can enroll in and watch in multiple languages at once.

# Usage

## Transcript Creation
To create a transcript of a video, the user needs to upload the video to the application. The application will then use Google Speech-to-Text API to generate a transcript of the video. Once the transcript is generated, the user can download it in the form of a text file.

## Voiceover Change
To change the audio of the video, the user needs to upload the video to the application and also upload the new audio file that they want to use for the voiceover. The application will then use FFmpeg to replace the audio of the video with the new audio file. Once the new video is generated, the user can download it.

## Mentor Section
The mentor section of the application allows mentors to update their details, such as name, email address, and profile picture. The mentor can also post courses that users can enroll in and watch in multiple languages at once.
## Contributing
If you would like to contribute to this project, please fork the repository and create a pull request. We welcome all contributions!
## Run Locally
Clone the project

```bash
  git clone https://github.com/mogiiee/skill-a-thon.git
```

Go to the project directory

```bash
  cd skill-a-thon
```

Install dependencies

```bash
  pip3 install -r requirements.txt
```