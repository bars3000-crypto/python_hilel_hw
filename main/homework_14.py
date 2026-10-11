import time
import random
import threading

files = ["photo.jpg", "document.pdf", "video.mp4", "archive.zip", "music.mp3"]

def download_file(file_name):
    print(f"Початок завантаження {file_name}...")
    sleep_time = random.uniform(1, 3)
    time.sleep(sleep_time)
    print(f"Завершено: {file_name}")

if __name__ == "__main__":
    print("--- ПОСЛІДОВНЕ ЗАВАНТАЖЕННЯ ---")
    start_seq = time.perf_counter()

    for file in files:
        download_file(file)

    end_seq = time.perf_counter()
    seq_time = end_seq - start_seq
    print(f"Час послідовного завантаження: {seq_time:.2f} сек\n")

    print("--- ПАРАЛЕЛЬНЕ ЗАВАНТАЖЕННЯ ---")
    start_threads = time.perf_counter()

    threads = []
    for file in files:
        thread = threading.Thread(target=download_file, args=(file,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_threads = time.perf_counter()
    threads_time = end_threads - start_threads
    print(f"Час паралельного завантаження: {threads_time:.2f} сек\n")

    diff = seq_time - threads_time
    print("--- РЕЗУЛЬТАТИ ---")
    print(f"Послідовно: {seq_time:.2f} сек.")
    print(f"Паралельно: {threads_time:.2f} сек.")
    print(f"Різниця: {diff:.2f} сек.")