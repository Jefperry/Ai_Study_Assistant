document.getElementById("login-btn")?.addEventListener("click", async () => {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const res = await fetch(`${API_BASE_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  const data = await res.json();
  if (data.access_token && data.refresh_token) {
    localStorage.setItem("access_token", data.access_token);
    localStorage.setItem("refresh_token", data.refresh_token);
    localStorage.setItem("token_expiry", Date.now() + 15 * 60 * 1000); // 15min
    window.location.href = "index.html";
  } else {
    document.getElementById("login-msg").innerText = data.error || "Login failed";
  }
});

document.getElementById("logout-btn")?.addEventListener("click", async () => {
  const access = localStorage.getItem("access_token");
  if (access) {
    await fetch(`${API_BASE_URL}/auth/logout`, {
      method: "POST",
      headers: { Authorization: `Bearer ${access}` },
    });
  }
  logoutUser();
});
