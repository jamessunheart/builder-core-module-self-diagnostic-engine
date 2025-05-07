import datetime

class SelfDiagnosticEngine:
    """
    A diagnostic tool that runs automated self-checks to identify communication,
    integration, and optimization issues in Builder Core systems.
    """

    def __init__(self):
        self.last_run = None
        self.diagnostics_log = []

    def run_diagnostics(self):
        """
        Run all core system checks and return a prioritized list of issues with clarity.
        """
        now = datetime.datetime.utcnow()
        self.last_run = now
        results = {
            "timestamp": now.isoformat(),
            "issues": [],
            "recommendations": []
        }

        # Example checks — these should be expanded
        if not self.check_github_token_permissions():
            results["issues"].append("GitHub token permissions may be misconfigured.")
            results["recommendations"].append("Ensure token includes repo access and write permissions.")

        if not self.check_api_schema_alignment():
            results["issues"].append("API calls do not fully match latest schema.")
            results["recommendations"].append("Update API call formats to match OpenAPI spec.")

        self.diagnostics_log.append(results)
        return results

    def check_github_token_permissions(self):
        # Placeholder — replace with actual token validation logic
        return True

    def check_api_schema_alignment(self):
        # Placeholder — simulate API schema check
        return True

    def get_log(self):
        return self.diagnostics_log
