import subprocess
import time

'''
:param: 
interval = 10 seconds until 30 seconds

:return:
1. RUN if_analysis_works.py
2. RUN min_working_example-before_graph_analysis_Apr12.r to write in "csv/"
3. Wait for 2.  to finish and buffer tiem interval = 10 seconds
4. repeat from 1.

(trimming down)
'''


def main():
    start_time = time.time()
    end_time = start_time + 30 * 60  # 30 minutes in seconds
    interval = 10  # 3 minutes in seconds

    i = 1
    while time.time() < end_time:
        # Run Python script
        subprocess.run(["python3", "if_analysis_works.py"])
        print("if_analysis_works.py DONE! On to min_working_example-before_graph_analysis_Apr12.r")

        # Run R script
        subprocess.run(
            ["Rscript", "min_working_example-before_graph_analysis_Apr12.r"])
        print("min_working_example-before_graph_analysis_Apr12.r DONE! Sleeping for 30s!")

        # Sleep for 3 minutes
        time.sleep(interval)
        i += 1
        print("Sleep done! Iteration #{i}!")

    finish_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(finish_time, "Done!")


if __name__ == "__main__":
    main()
