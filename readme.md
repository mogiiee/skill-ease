
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
  cd skill-ease
```

Install dependencies

```bash
  pip3 install -r requirements.txt
```

## Authors

- [@mogiiee](https://www.github.com/mogiiee)
- [@SubhanuSRoy](https://www.github.com/SubhanuSRoy)
- [@chethanreddy123](https://www.github.com/chethanreddy123)


## Demo

you can check the working demo file [here](https://skillease.netlify.app/)

## Points to remember 
- The app is hosted on render and it might take some time to boot up slowly
- There are only a few credits we can get as students for free so dont go crazy with the requests
- If there are any errors you face while checking it out pls start a new issue. 

### Note
This is just the backend of the entire app for the rest of the content do check out the following repos
 - [repo 1](https://github.com/SubhanuSRoy/skill-ease)
 - [repo 2](https://github.com/chethanreddy123/Skill-a-thon)
 
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`USER_COLLECTION=`

`TOTAL_POSTS_COLLECTION=`

`TOTAL_JOBS_COLLECTION=`
## Screenshots

![Course creation](https://discord.com/channels/1075402466675392572/1079576374903320636/1079577229945741383)
![Course vide language converter](https://discord.com/channels/1075402466675392572/1079576374903320636/1079583105494548541)
![Updation](https://discord.com/channels/1075402466675392572/1079576374903320636/1079584478403510342)
![App homepage](https://discord.com/channels/1075402466675392572/1079576374903320636/1079584534699446294)
![Login](https://discord.com/channels/1075402466675392572/1079576374903320636/1079585181947666504)
![Signup](https://discord.com/channels/1075402466675392572/1079576374903320636/1079586244893356163)
![App Dashboard](https://discord.com/channels/1075402466675392572/1079576374903320636/1079586386497241160)
![Replies](https://discord.com/channels/1075402466675392572/1079576374903320636/1079586693868441680)
![courses](https://discord.com/channels/1075402466675392572/1079576374903320636/1079601237558829150)
![User flow](https://discord.com/channels/1075402466675392572/1079576374903320636/1079607028944732214)

## Tech Stack

**Client:** Gpt 3, FastAPI

**Server:** Uvicorn, FastAPI