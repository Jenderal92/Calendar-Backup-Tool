# Calendar Backup Tool  

![calendar-backup-tool Jenderal92](https://github.com/user-attachments/assets/e614e260-6374-442f-8434-064be0fe77cb)


The **Calendar Backup Tool** is designed to back up your Google Calendar to Google Drive in JSON format. This tool utilizes the **Google Calendar API** to fetch calendar data and the **Google Drive API** to upload the backup files into a dedicated folder on Google Drive.  

### **Features**  

1. **Secure Authentication**: Uses OAuth 2.0 for secure authentication with Google APIs.  
2. **Backup All Calendars**: Fetches all calendars from your Google account and saves them locally as JSON files.  
3. **Automatic Upload to Google Drive**: Automatically uploads backup files to a folder named `Calendar_Backups` in Google Drive.  
4. **Folder Creation**: Creates the backup folder in Google Drive if it does not already exist.  
5. **User-Friendly**: Fully automated process after authentication.  

---

### **How to Use**  

#### 1. **Setup Requirements**  
- Enable **Google Calendar API** and **Google Drive API** in the [Google Cloud Console](https://console.cloud.google.com/).  
- Download the OAuth 2.0 credentials file (`credentials.json`) from the Cloud Console.  

#### 2. **Install Dependencies**  
1. Ensure you're using Python 2.7.  
2. Install the required libraries using pip:  
   ```bash
   pip install --upgrade google-api-python-client oauth2client
   ```

#### 3. **Run the Tool**  
1. Place the `credentials.json` file in the same directory as the script.  
2. Execute the script:  
   ```bash
   python backup_calendar.py
   ```

3. A browser will open for authentication. Log in to your Google account and grant access.  

#### 4. **Results**  
- Backup JSON files will be created in the local directory.  
- Files will be uploaded to the `Calendar_Backups` folder on Google Drive.  

---

### **Folder Structure**  
- **credentials.json**: Your Google Cloud credentials file.  
- **token.json**: Authentication token automatically generated after the first login.  
- **backup_calendar.py**: The main script file.  

---
