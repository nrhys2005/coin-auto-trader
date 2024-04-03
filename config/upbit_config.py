# API 기본 주소
base_url = 'https://api.upbit.com'

## 자산
# 계좌 전체 조회 API
accounts_api_url = '/v1/accounts'

## 주문
# 주문 가능 정보
orders_chance = 'v1/orders/chance/?market={market}'
# 개별 주문 조회 및 주문 취소 접수
order = '/v1/order'
# 주문 리스트 조회 및 주문하기
orders = '/v1/orders'


## 서비스 정보
# 입출금 현황(실제 서비스 상태 보다 수 분 정도 지연되어 반영될 수 있으니 거래 전략의 일부로 사용하지 마시기를 바랍니다.)
status_wallet = '/v1/status/wallet'


## 시세 종목 조회
# 마켓 조회
market_all = '/v1/market/all'

## 시세 캔들 조회
# 분 캔들
cancel_minutes = '/v1/candles/minutes/{unit}'
# 일 캔들
cancel_days = '/v1/candles/days/{unit}'
# 주 캔들
cancel_weeks = '/v1/candles/weeks/{unit}'
# 월 캔들
cancel_months = '/v1/candles/motnhs/{unit}'