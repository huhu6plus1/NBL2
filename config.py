# 配置文件：监听频率、推送等参数

# Server酱推送 Key（用户提供）
SERVER_CHAN_KEY = "SCT282237TA-4sseGxqm4WrkvefyZLDe53M0"

# 监听设置
LINEUP_CHECK_INTERVAL_DEFAULT = 180  # 默认每3分钟监听一次
LINEUP_CHECK_INTERVAL_30MIN = 60     # 比赛前30分钟每1分钟
LINEUP_CHECK_INTERVAL_15MIN = 20     # 比赛前15分钟每20秒

# 推荐阈值
MIN_EV_THRESHOLD = 3.0  # 只有 EV >= 3% 时才触发推送
