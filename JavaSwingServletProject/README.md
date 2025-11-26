# Java Swing Servlet Project

This is a minimal project demonstrating Swing for GUI form design and event handling, JavaBeans for data modeling, and Servlets for server-side processing.

## Prerequisites
- Java JDK (version 8 or higher)
- Apache Tomcat (version 9 or higher)

## Build Instructions
1. Set up Tomcat: Download and install Apache Tomcat. Note the installation path (e.g., C:\apache-tomcat-9.x.x).

2. Compile the Java files:
   ```
   javac -cp "C:\path\to\tomcat\lib\servlet-api.jar" -d web/WEB-INF/classes src/*.java
   ```
   Replace `C:\path\to\tomcat` with your actual Tomcat path.

3. Deploy to Tomcat:
   - Copy the `web` folder to `TOMCAT_HOME/webapps/JavaSwingServletProject`
   - Or create a WAR file: `jar cvf JavaSwingServletProject.war -C web .` and place it in `TOMCAT_HOME/webapps`

4. Start Tomcat:
   - Run `TOMCAT_HOME/bin/startup.bat` (Windows) or `startup.sh` (Linux/Mac)

## Run Instructions
1. Ensure Tomcat is running (check http://localhost:8080).

2. Run the Swing application:
   ```
   java -cp src UserForm
   ```
   This will open the GUI form.

3. Fill in the form (Name, Email, Age) and click Submit. The data will be sent to the servlet at http://localhost:8080/JavaSwingServletProject/user, processed server-side, and a success message will be shown.

## Components
- `User.java`: JavaBean for user data
- `UserForm.java`: Swing GUI with form and event handling
- `UserServlet.java`: Servlet for processing form submissions
- `web.xml`: Servlet configuration

## Notes
- The servlet logs the received user data to the console.
- For production, add proper error handling, validation, and database integration.