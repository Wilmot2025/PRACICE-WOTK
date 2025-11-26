import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class UserServlet extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        // Read form parameters
        String name = request.getParameter("name");
        String email = request.getParameter("email");
        String ageStr = request.getParameter("age");

        try {
            int age = Integer.parseInt(ageStr);

            // Create User bean
            User user = new User(name, email, age);

            // Process the user (for demo, just log it)
            System.out.println("Received user: " + user);

            // Send response
            response.setContentType("text/html");
            PrintWriter out = response.getWriter();
            out.println("<html><body>");
            out.println("<h1>User Submitted Successfully</h1>");
            out.println("<p>" + user.toString() + "</p>");
            out.println("</body></html>");
        } catch (NumberFormatException e) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid age");
        }
    }
}