const API_BASE_URL = "http://127.0.0.1:5000/api";

async function getAccessToken() {
  const token = localStorage.getItem("access_token");
  const expires = localStorage.getItem("token_expiry");

  if (!token || Date.now() > parseInt(expires || 0)) {
    // Try refreshing the token
    const refreshed = await refreshAccessToken();
    return refreshed;
  }
  return token;
}

async function refreshAccessToken() {
  const refresh = localStorage.getItem("refresh_token");
  if (!refresh) return null;

  const res = await fetch(`${API_BASE_URL}/auth/refresh`, {
    method: "POST",
    headers: { Authorization: `Bearer ${refresh}` },
  });

  if (res.ok) {
    const data = await res.json();
    localStorage.setItem("access_token", data.access_token);
    localStorage.setItem("token_expiry", Date.now() + 15 * 60 * 1000); // 15min
    return data.access_token;
  } else {
    logoutUser();
    return null;
  }
}

function logoutUser() {
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
  localStorage.removeItem("token_expiry");
  window.location.href = "login.html";
}
