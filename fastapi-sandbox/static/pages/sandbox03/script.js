import { useAjax } from "../../script/ajax.js";

const ajax = useAjax();

const btnStreamingElem = document.getElementById("btnStreaming");
const responseAreaElem = document.getElementById("responseArea");

/**
 * レスポンスエリアのクリア
 */
function clearResponseArea() {
  while (responseAreaElem.firstChild) {
    responseAreaElem.removeChild(responseAreaElem.firstChild);
  }
}


/**
 * レスポンスエリアにメッセージ追加
 * 
 * @param {String} message 
 */
function appendResponseArea(message) {
  const div = document.createElement("div")
  div.textContent = message

  responseAreaElem.append(div)
}

btnStreamingElem.addEventListener("click", async () => {

  clearResponseArea()

  const param = {};
  const resp = await ajax.postReceiveStream("/sandbox03/streaming", param);

  const reader = resp.body.getReader();
  const decoder = new TextDecoder();
  while (true) {
    const r = await reader.read();
    if (r.done) {
      console.log("done!");
      break;
    }

    const decoded = decoder.decode(r.value);
    appendResponseArea(decoded)
  }
});
