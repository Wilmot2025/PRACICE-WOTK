import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;

public class UserForm extends JFrame {
    private JTextField nameField;
    private JTextField emailField;
    private JTextField ageField;
    private JButton submitButton;

    public UserForm() {
        setTitle("User Registration Form");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(4, 2));

        add(new JLabel("Name:"));
        nameField = new JTextField();
        add(nameField);

        add(new JLabel("Email:"));
        emailField = new JTextField();
        add(emailField);

        add(new JLabel("Age:"));
        ageField = new JTextField();
        add(ageField);

        submitButton = new JButton("Submit");
        submitButton.addActionListener(new SubmitActionListener());
        add(submitButton);

        setVisible(true);
    }

    private class SubmitActionListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            try {
                String name = nameField.getText();
                String email = emailField.getText();
                int age = Integer.parseInt(ageField.getText());

                // Send data to servlet
                URL url = new URL("http://localhost:8080/JavaSwingServletProject/user");
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("POST");
                conn.setDoOutput(true);
                conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");

                String data = "name=" + URLEncoder.encode(name, "UTF-8") +
                              "&email=" + URLEncoder.encode(email, "UTF-8") +
                              "&age=" + age;

                try (OutputStream os = conn.getOutputStream()) {
                    os.write(data.getBytes());
                }

                int responseCode = conn.getResponseCode();
                if (responseCode == 200) {
                    JOptionPane.showMessageDialog(UserForm.this, "User submitted successfully!");
                } else {
                    JOptionPane.showMessageDialog(UserForm.this, "Error submitting user.");
                }

                conn.disconnect();
            } catch (Exception ex) {
                JOptionPane.showMessageDialog(UserForm.this, "Error: " + ex.getMessage());
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new UserForm());
    }
}