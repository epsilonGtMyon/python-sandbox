import { useAjax } from "../../script/ajax.js";

const ajax = useAjax();

const countElem = document.getElementById("count");
const countUpElem = document.getElementById("countUp");

countUpElem.addEventListener("click", async () => {
  const param = {};
  const resp = await ajax.post("/sandbox04/count_up", param);

  countElem.textContent = resp.count;
});


const resp = await ajax.get("/sandbox04/current_count", {});
countElem.textContent = resp.count;

