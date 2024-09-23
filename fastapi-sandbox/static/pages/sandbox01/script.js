import { useAjax } from "../../script/ajax.js";

const ajax = useAjax();

const value01Elem = document.getElementById("value01")
const value02Elem = document.getElementById("value02")
const btnGetElem = document.getElementById("btnGet")



btnGetElem.addEventListener("click", async () => {
  const param = {
    value01: value01Elem.value,
    value02: value02Elem.value,
  }
  const resp = await ajax.get("/sandbox01/hello", param)
  console.log(resp)
})