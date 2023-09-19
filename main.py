import subprocess
import os


def extract_frames_from_video(video_path, output_folder):
    # 確保輸出目錄存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 使用 ffmpeg 提取圖片
    command = [
        './ffmpeg',
        '-i', video_path,
        # 將每一幀儲存為 frame0001.png, frame0002.png, ...
        os.path.join(output_folder, 'frame%04d.png')
    ]
    subprocess.run(command)


if __name__ == '__main__':
    video_path = 'test.mp4'
    output_folder = 'output'
    extract_frames_from_video(video_path, output_folder)
