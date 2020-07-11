/**
 * 末尾にスラッシュがない状態の遷移を実行しようとした場合、
 * 強制定期に末尾スラッシュありにリダイレクトする
 *
 */
export default function ({ route, redirect }) {
  if (route.path.slice(-1) !== '/') {
    redirect(301, route.path + '/')
  }
}
