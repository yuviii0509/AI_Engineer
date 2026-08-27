from Backend.llm import ask_llm


def match_resume(resume_data, job_description, system_prompt):

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": f"""
Resume:
{resume_data}

Job Description:
{job_description}
"""
        }
    ]

    result = ask_llm(messages)

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    return result