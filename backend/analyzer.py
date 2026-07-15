def analyze_response(answer: str):
    """
    SurfBench Verification Analyzer v2
    Rule-Based Design Verification Analyzer
    """

    text = answer.lower()

    score = 0
    language = "Unknown"

    passed = []
    warnings = []
    suggestions = []

    # -----------------------------
    # Detect Language
    # -----------------------------
    if "uvm" in text:
        language = "UVM"
    elif "module" in text or "always_ff" in text:
        language = "SystemVerilog"

    # -----------------------------
    # Verification Rules
    # -----------------------------

    rules = [

        {
            "keyword": "uvm_monitor",
            "score": 10,
            "pass": "Extends uvm_monitor",
            "warn": "Monitor class not found",
            "suggest": "Extend uvm_monitor."
        },

        {
            "keyword": "uvm_component_utils",
            "score": 10,
            "pass": "Factory registration present",
            "warn": "Factory registration missing",
            "suggest": "Add `uvm_component_utils`."
        },

        {
            "keyword": "build_phase",
            "score": 10,
            "pass": "build_phase implemented",
            "warn": "build_phase missing",
            "suggest": "Create objects and retrieve config in build_phase."
        },

        {
            "keyword": "run_phase",
            "score": 10,
            "pass": "run_phase implemented",
            "warn": "run_phase missing",
            "suggest": "Monitor interface activity inside run_phase."
        },

        {
            "keyword": "uvm_config_db",
            "score": 10,
            "pass": "Uses uvm_config_db",
            "warn": "uvm_config_db missing",
            "suggest": "Retrieve virtual interface through config_db."
        },

        {
            "keyword": "analysis_port",
            "score": 10,
            "pass": "Analysis port declared",
            "warn": "Analysis port missing",
            "suggest": "Broadcast transactions using analysis_port."
        },

        {
            "keyword": "virtual",
            "score": 5,
            "pass": "Virtual interface detected",
            "warn": "Virtual interface missing",
            "suggest": "Declare a virtual interface."
        },

        {
            "keyword": "@(posedge",
            "score": 5,
            "pass": "Clock sampling detected",
            "warn": "Clock sampling missing",
            "suggest": "Sample DUT on a clock edge."
        },

        {
            "keyword": "write(",
            "score": 10,
            "pass": "Analysis write() used",
            "warn": "write() not found",
            "suggest": "Send transactions through analysis port."
        },

        {
            "keyword": "forever",
            "score": 5,
            "pass": "Continuous monitoring implemented",
            "warn": "No forever loop",
            "suggest": "Use forever loop inside run_phase."
        },

        {
            "keyword": "begin",
            "score": 5,
            "pass": "Structured code",
            "warn": "Code structure weak",
            "suggest": "Use begin/end blocks."
        },

        {
            "keyword": "new(",
            "score": 10,
            "pass": "Constructor found",
            "warn": "Constructor missing",
            "suggest": "Implement constructor."
        }

    ]

    for rule in rules:

        if rule["keyword"] in text:
            score += rule["score"]
            passed.append("✅ " + rule["pass"])
        else:
            warnings.append("⚠ " + rule["warn"])
            suggestions.append("💡 " + rule["suggest"])

    score = min(score, 100)

    return {

        "score": score,

        "language": language,

        "passed": passed,

        "warnings": warnings,

        "suggestions": suggestions

    }