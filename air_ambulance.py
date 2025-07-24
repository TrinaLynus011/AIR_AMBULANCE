import traci, math, csv

sumoCmd = ["sumo-gui", "-c", "simulation.sumocfg"]

MAX_ALT = 700  # target altitude (ft)
CRUISE_SPEED = 10
LOG_CSV = "altitude_log.csv"

with open(LOG_CSV, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["step", "x", "y", "altitude_ft"])

def main():
    traci.start(sumoCmd)
    step = 0
    x = y = altitude = 0.0
    jlist = traci.junction.getIDList()
    target = traci.junction.getPosition(jlist[len(jlist)//2])

    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()

        if altitude < MAX_ALT:
            altitude += 10
            state = "climbing"
        else:
            dx, dy = target[0] - x, target[1] - y
            d = math.hypot(dx, dy) or 1
            x += dx / d * CRUISE_SPEED
            y += dy / d * CRUISE_SPEED
            state = "cruising" if d > 5 else "arrived"

        print(f"Step {step}: {state} | x={x:.1f}, y={y:.1f}, alt={altitude:.1f}")
        with open(LOG_CSV, "a", newline="") as f:
            csv.writer(f).writerow([step, x, y, altitude])

        step += 1
        if state == "arrived":
            break

    traci.close()

if __name__ == "__main__":
    main()
