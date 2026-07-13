def analyze_response(answer: str):
    """
    Analyze AI-generated Design Verification code.
    Version 1 (Rule-Based)
    """

    score = 0
    checks = []

    text = answer.lower()

    # Detect Language
    if "module" in text or "logic" in text or "always_ff" in text:
        language = "SystemVerilog"
    elif "class" in text and "uvm" in text:
        language = "UVM"
    else:
        language = "Unknown"

    # Detect UVM Monitor
    if "uvm_monitor" in text:
        score += 20
        checks.append("✅ Extends uvm_monitor")
    else:
        checks.append("❌ uvm_monitor missing")

    if "build_phase" in text:
        score += 20
        checks.append("✅ build_phase found")
    else:
        checks.append("⚠️ build_phase missing")

    if "run_phase" in text:
        score += 20
        checks.append("✅ run_phase found")
    else:
        checks.append("⚠️ run_phase missing")

    if "uvm_config_db" in text:
        score += 20
        checks.append("✅ uvm_config_db used")
    else:
        checks.append("⚠️ uvm_config_db missing")

    if "analysis_port" in text:
        score += 20
        checks.append("✅ analysis_port declared")
    else:
        checks.append("⚠️ analysis_port missing")

    return {
        "score": score,
        "language": language,
        "checks": checks
    }