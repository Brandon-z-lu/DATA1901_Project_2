import os
import time
import schedule

start_time = time.time()


def count_files_in_folder(folder_path):
    return len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]) - 1


def count_valid_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len([line for line in lines if not line.startswith("#") and not line.strip() == ""])


def progress_report():
    current_time = time.time()
    elapsed_time = current_time - start_time

    m = count_files_in_folder("csv_cache")
    n = count_valid_lines("main1_INPUT.txt")
    progress = (m / n) * 100
    num_hashes = int(progress)
    num_spaces = 100 - num_hashes

    if elapsed_time == 0:
        speed = 0
    else:
        speed = m / (elapsed_time / 60)  # files/min

    if speed == 0:
        eta = 24 * 60
    else:
        eta = (n - m) / speed  # minutes

    eta_hours = int(eta // 60)
    eta_minutes = int(eta % 60)

    print(f"{time.strftime('%H:%M:%S')} Progress report:")
    print(f"Speed: {speed:.2f} files/min")
    print(f"ETA: {eta_hours} hours {eta_minutes} minutes")
    print(f"{progress:.2f}% ({m}/{n} files)")
    print(f"{'#' * num_hashes}{' ' * num_spaces}")


progress_report()

# Schedule the progress_report function to run every 10 minutes
schedule.every(5).minutes.do(progress_report)

# Keep the script running and execute the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
