# Personal Media Tracker

The Personal Media Tracker project aims to design and develop a unified desktop application that allows users to track, organize, and review both movies and television shows within a single platform.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/sashaelle/media-tracker.git
   cd media-tracker
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the database setup (example):
   ```
   python code/database.py
   ```

## Requirements

- Python 3.6+
- pandas (automatically installed via requirements.txt)

## Features

### Create a Profile (Sasha)

The personal media tracker supports the ability to have up to 4 different personal profiles on a locally used version of the application.

To create a profile:

1. Open to PMT
2. Select the `Create Profile` button
3. Type in your profile name
4. Select `Create` to create profile and add your account to the database

### Tracking a Title (Jessa)

To track progress with media titles, PMT offers a watch status dropdown selection including: Not Watched, Watching, and Want to Watch.  

To track a title:
1. Open to PMT and select your profile
2. Search and select your desired title
3. Select one of the following options: `Not Watched`, `Watching`, `Want to Want`
4. Select `Save Entry` to save all selections to the database

### Review/Rate a Title (Jessa)

If the user wants to insert their opinion, PMT provides a numerical rating scale and text-based responses.

To rate a selected title in the `Title Details` window:
1. Open to PMT and select your profile
2. Search and select your desired title
3. Navigate under the Watch Status feature
4. Click a button between 1 (lowest) and 5 (highest) to rate the title
5. Select `Save Entry` to save all selections to the database

To review a selected title in the `Title Details` window:
1. Open to PMT and select your profile
2. Search and select your desired title
3. Naviagte under the Rating feature
4. Below the Rating buttons, enter any commentary you have for the selected title
5. Select `Save Entry` to save all selections to the database

### Export Tracked Titles (Sasha)

If it is desired to see all of tracked titles in one concise file, PMT offers the ability to export tracked titles in a nicely formatted .csv

1. Open PMT and select your profile
2. Below the list of tracked titles, select `Export Data`
3. Select the file on your desktop where you would like to save your file of tracked titles
4. Select `Save`
