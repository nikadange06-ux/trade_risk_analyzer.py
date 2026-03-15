# Simple Trade Risk Analyzer
# Beginner Python project for evaluating trading setups

entry = float(input("Enter entry price: "))
stop_loss = float(input("Enter stop loss price: "))
take_profit = float(input("Enter take profit price: "))

risk = entry - stop_loss
reward = take_profit - entry

if risk <= 0:
    print("Invalid trade setup. Stop loss must be below entry price.")
else:
    risk_reward_ratio = reward / risk

    print("\nTrade Analysis")
    print("Entry Price:", entry)
    print("Stop Loss:", stop_loss)
    print("Take Profit:", take_profit)
    print("Risk per unit:", round(risk, 2))
    print("Reward per unit:", round(reward, 2))
    print("Risk/Reward Ratio:", round(risk_reward_ratio, 2))

    if risk_reward_ratio >= 2:
        print("This trade setup looks reasonable based on risk/reward.")
    else:
        print("This trade setup may not be strong because the reward is low compared to the risk.")
