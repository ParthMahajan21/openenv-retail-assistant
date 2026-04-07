def grade_easy(output):
    return 1.0 if "refund" in output.lower() else 0.0


def grade_medium(output):
    score = 0
    if "sorry" in output.lower():
        score += 0.5
    if "help" in output.lower() or "assist" in output.lower():
        score += 0.5
    return score


def grade_hard(output):
    score = 0
    if "clean" in output.lower():
        score += 0.5
    if "insight" in output.lower() or "analysis" in output.lower():
        score += 0.5
    return score