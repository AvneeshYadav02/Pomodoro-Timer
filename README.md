# Pomodoro Timer

This project is a simple, customizable Pomodoro timer application built with Python and the tkinter library. It's designed to help you stay focused on your work by structuring your time into work and break intervals.

Features

    Pomodoro Technique: Follows the classic Pomodoro method with predefined work and break durations.

    Work/Break Cycles: Alternates between a 25-minute work session, a 5-minute short break, and a 20-minute long break after every four work sessions.

    Visual Interface: A clean, minimalist user interface with a timer displayed over a tomato image.

    Interactive Controls: Start and Reset buttons for easy control of the timer.

    Progress Tracking: A checkmark indicator that appears for each completed work session to help you track your progress.

How to Install and Run

To run this application, you only need Python installed on your system.
The project uses the tkinter library, which is included by default with most Python installations.

    Clone the Repository (or download the files).

    Navigate to the Project Directory in your terminal.

    Run the script:
    Bash

    python main.py

How to Use

    Click the "START" button to begin a work session. The timer will start counting down, and the heading will change to "WORK TIME."

    After each 25-minute work session, a short break of 5 minutes will begin automatically. The heading will change to "SHORT BREAK," and a checkmark will appear.

    After every four work sessions, the timer will initiate a 20-minute long break. The heading will change to "LONG BREAK."

    To stop the timer at any time, click the "RESET" button. This will reset the timer, the heading, and the checkmarks.

Customization

You can easily adjust the duration of the work and break periods by editing the main.py file. The following constants can be changed to your preference:

    WORK_MIN: The duration of a work session in minutes.

    SHORT_BREAK_MIN: The duration of a short break in minutes.

    LONG_BREAK_MIN: The duration of a long break in minutes.
