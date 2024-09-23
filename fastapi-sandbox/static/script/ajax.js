class AjaxClient {
  async get(url, params) {
    const query = new URLSearchParams(params ?? {});
    
    const headers = new Headers();
    const resp = await fetch(`${url}?${query.toString()}`, {
      method: "GET",
      headers,
    });

    try {
      return await resp.json();
    } catch (err) {
      return null;
    }
  }

  async post(url, params) {
    const headers = new Headers();
    headers.append("Content-Type", "application/json");

    const resp = await fetch(`${url}`, {
      method: "POST",
      body: JSON.stringify(params),
      headers
    });

    try {
      return await resp.json();
    } catch (err) {
      return null;
    }
  }
}

const ajax = new AjaxClient();

function useAjax() {
  return ajax;
}

export { AjaxClient, useAjax };
