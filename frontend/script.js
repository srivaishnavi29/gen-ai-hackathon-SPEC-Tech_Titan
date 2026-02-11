document.getElementById("curriculumForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const form = e.target;
    const data = {
        skill: form.skill.value,
        level: form.level.value,
        semesters: form.semesters.value,
        weekly_hours: form.weekly_hours.value,
        industry: form.industry.value
    };

    const res = await fetch("/api/generate-curriculum", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    const result = await res.json();
    document.getElementById("result").textContent = JSON.stringify(result, null, 2);
});