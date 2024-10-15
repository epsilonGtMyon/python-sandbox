from fastapi import APIRouter, Request

router = APIRouter(prefix = "/sandbox04")

# starlette.middleware.sessions.SessionMiddleware を利用しセッションを実現
# このミドルウェアはセッションの内容をCookieに書き出している。
# サーバーはステートレスだが、書き込む情報の量が増えるとCookieのサイズが大きくなる。

@router.get("/current_count")
async def current_count(request: Request):

  # countup
  count = request.session.get("count", 0)
  request.session["count"] = count

  return {
    "count": count
  }

@router.post("/count_up")
async def count_up(request: Request):

  # countup
  count = request.session.get("count", 0)
  count += 1
  request.session["count"] = count

  return {
    "count": count
  }

