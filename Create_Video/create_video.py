import os
import imageio

# Libary from progress bar
from tqdm import tqdm

def creator_video(path, output_name_video, fps_ = 30, reverse_ = False):
  """
  @path -> путь к папке с фотографиями (одного разрешения и в алфавитномм пордяке)
  @output_name_video -> название выходного видео
  @fps_ -> количество кадров в секунду
  @reverse_ -> включение обратного порядка в видео
  """
  fileList = []
  
  for file in os.listdir(path):
      complete_path = path + '/'+ file
      fileList.append(complete_path)
  
  fileList.sort(reverse = reverse_)
  
  writer = imageio.get_writer(output_name_video, fps = fps_)
  
  for im in tqdm(fileList):
    writer.append_data(imageio.imread(im))
  
  writer.close()
  print('Success create video!!!')


import imageio
# Libary from progress bar
from tqdm import tqdm

def creator_video_from_list(image_list, output_name_video, fps_ = 30, reverse_ = False):
  """
  @image_list -> массив картинок
  @output_name_video -> название выходного видео
  @fps_ -> количество кадров в секунду
  @reverse_ -> включение обратного порядка в видео
  """
  
  writer = imageio.get_writer(output_name_video, fps = fps_)
  if reverse_:
    image_list.reverse()

  for im in tqdm(image_list):
    writer.append_data(im)

  writer.close()
  print('Success create video!!!')