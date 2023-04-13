import subprocess
import time


def main():
    start_time = time.time()
    end_time = start_time + 30 * 60  # 30 minutes in seconds
    interval = 3 * 60  # 3 minutes in seconds

    while time.time() < end_time:
        # Run R script
        subprocess.run(
            ["Rscript", "min_working_example-before_graph_analysis_Apr12.r"])

        # Run Python script
        subprocess.run(["python3", "if_analysis_works.py"])

        # Sleep for 3 minutes
        time.sleep(interval)

    finish_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(finish_time, "Done!")


if __name__ == "__main__":
    main()
