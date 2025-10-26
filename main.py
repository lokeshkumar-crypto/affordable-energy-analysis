def affordable_energy_analysis(consumption, renewable, rate):
    total_cost = (consumption - renewable) * rate
    percent_renewable = (renewable / consumption) * 100
    return total_cost, percent_renewable

if __name__ == "__main__":
    # Read values from input.txt for automation
    with open("input.txt", "r") as f:
        lines = f.readlines()
    consumption = int(lines[0].split(":")[1])
    renewable = int(lines[1].split(":")[1])
    rate = float(lines[2].split(":")[1])
    cost, renewable_pct = affordable_energy_analysis(consumption, renewable, rate)
    with open("result.txt", "w") as f:
        f.write(f"Total Grid Energy Cost: {cost}\n")
        f.write(f"Percent Renewable Used: {renewable_pct:.2f}%\n")
    print("Analysis complete. Results saved to result.txt.")
