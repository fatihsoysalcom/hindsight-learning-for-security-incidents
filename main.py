#!/usr/bin/env python3

import re

class SecurityKnowledgeBase:
    """Manages a knowledge base of past security incidents and lessons learned."""
    def __init__(self):
        # The knowledge base stores past incidents, their root causes, and lessons learned.
        # This simulates the 'permanent knowledge' derived from post-incident analyses.
        self.incidents = [
            {
                "id": 1,
                "description": "SQL injection vulnerability found in user login form due to unsanitized input.",
                "root_cause": "Lack of input validation and use of string concatenation in SQL queries.",
                "keywords": ["sql", "injection", "login", "input validation", "unsanitized"],
                "lesson_learned": "Always use parameterized queries or ORMs for database interactions. Implement strict input validation and sanitization for all user inputs.",
                "mitigation_action": "Refactor login query to use prepared statements."
            },
            {
                "id": 2,
                "description": "Cross-Site Scripting (XSS) detected in comment section, allowing arbitrary script execution.",
                "root_cause": "Unescaped user-generated content rendered directly in HTML.",
                "keywords": ["xss", "script", "comment", "html", "unescaped"],
                "lesson_learned": "Escape all user-generated content before rendering it in HTML. Implement Content Security Policy (CSP) headers.",
                "mitigation_action": "Apply HTML entity encoding to all user comments before display."
            },
            {
                "id": 3,
                "description": "Weak password policy led to a successful brute-force attack on an admin account.",
                "root_cause": "Insufficient password complexity requirements and lack of account lockout mechanisms.",
                "keywords": ["password", "brute-force", "admin", "weak policy", "account lockout"],
                "lesson_learned": "Enforce strong password policies (length, complexity). Implement account lockout after multiple failed attempts and rate limiting on login.",
                "mitigation_action": "Update password policy, add rate limiting and account lockout features."
            }
        ]

    def add_incident(self, description, root_cause, lesson_learned, mitigation_action, keywords):
        """Adds a new incident and its lessons to the knowledge base."""
        new_id = len(self.incidents) + 1
        self.incidents.append({
            "id": new_id,
            "description": description,
            "root_cause": root_cause,
            "keywords": keywords,
            "lesson_learned": lesson_learned,
            "mitigation_action": mitigation_action
        })
        print(f"[KB] New lesson added to knowledge base (ID: {new_id}).")

    def analyze_new_incident(self, new_incident_description):
        """Analyzes a new incident against past experiences (hindsight learning)."""
        print(f"\n--- Analyzing New Incident ---")
        print(f"New Incident: '{new_incident_description}'")
        
        matched_lessons = []
        new_incident_description_lower = new_incident_description.lower()

        # This loop simulates the 'hindsight' aspect: looking back at past incidents
        # to find relevant lessons for the current situation.
        for incident in self.incidents:
            # Simple keyword matching to find similarities.
            # In a real system, this would involve more advanced NLP or pattern matching.
            for keyword in incident["keywords"]:
                if re.search(r'\b' + re.escape(keyword) + r'\b', new_incident_description_lower):
                    matched_lessons.append(incident)
                    break # Found a match for this incident, move to the next historical incident
        
        if matched_lessons:
            print("\n[HINDSIGHT] Similar past incidents found! Applying lessons learned:")
            for lesson in matched_lessons:
                print(f"  - Past Incident ID {lesson['id']}: {lesson['description']}")
                print(f"    Root Cause: {lesson['root_cause']}")
                print(f"    Lesson Learned: {lesson['lesson_learned']}")
                print(f"    Suggested Mitigation: {lesson['mitigation_action']}")
        else:
            # If no direct match, it's an opportunity for new learning.
            print("\n[HINDSIGHT] No direct match found in past incidents. This is a new learning opportunity.")
            print("  Conduct a thorough post-incident analysis to identify root cause and document lessons learned.")
            print("  Consider adding this incident to the knowledge base for future reference.")


# --- Main execution --- #
if __name__ == "__main__":
    kb = SecurityKnowledgeBase()

    # Example 1: A new incident similar to a known SQL Injection
    kb.analyze_new_incident("A web application form is vulnerable to database manipulation through user input.")

    # Example 2: A new incident similar to a known XSS
    kb.analyze_new_incident("User comments are displaying raw HTML tags and scripts, leading to potential client-side attacks.")

    # Example 3: A new incident with no direct match, representing a new learning opportunity
    kb.analyze_new_incident("A critical zero-day vulnerability was exploited in a newly deployed container orchestration system.")

    # Example 4: Adding a new lesson to the knowledge base after a new incident analysis
    print("\n--- Simulating a new lesson being learned and added ---")
    new_incident_desc = "A recent phishing campaign successfully compromised several employee credentials due to lack of MFA."
    new_root_cause = "Employees not trained on phishing detection, and multi-factor authentication not enforced."
    new_lesson = "Implement mandatory phishing awareness training. Enforce MFA for all critical systems and user accounts."
    new_mitigation = "Deploy MFA across the organization and conduct regular security awareness training."
    new_keywords = ["phishing", "mfa", "credentials", "training", "compromise"]
    kb.add_incident(new_incident_desc, new_root_cause, new_lesson, new_mitigation, new_keywords)

    # Example 5: Re-analyzing an incident that now has a match after new learning
    kb.analyze_new_incident("An employee reported a suspicious email asking for login details, which could lead to credential compromise.")

    print("\n--- End of demonstration ---")
