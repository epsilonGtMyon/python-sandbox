class AjaxClient {
  async get(url, params) {
    const query = new URLSearchParams(params ?? {});
    const resp = await fetch(`${url}?${query.toString()}`, {
      method: "GET",
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
  return ajax
}

export {
  AjaxClient,
  useAjax
}