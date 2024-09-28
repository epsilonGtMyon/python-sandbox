class AjaxClient {
  async get(url, params) {
    const query = new URLSearchParams(params ?? {});
    
    const headers = new Headers();
    headers.append("X-Requested-With", "XMLHttpRequest");
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
    headers.append("X-Requested-With", "XMLHttpRequest");

    const resp = await fetch(`${url}`, {
      method: "POST",
      body: JSON.stringify(params),
      headers,
    });

    try {
      return await resp.json();
    } catch (err) {
      return null;
    }
  }
  
  async postReceiveStream(url, params) {
    const headers = new Headers();
    headers.append("Content-Type", "application/json");
    headers.append("X-Requested-With", "XMLHttpRequest");
    headers.append("accept", "text/event-stream");

    const resp = await fetch(`${url}`, {
      method: "POST",
      body: JSON.stringify(params),
      headers,
    });

    // とりあえずそのまま返す。
    return resp;
  }
}

const ajax = new AjaxClient();

function useAjax() {
  return ajax;
}

export { AjaxClient, useAjax };
