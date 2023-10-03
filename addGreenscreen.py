from moviepy.editor import VideoFileClip, ColorClip, CompositeVideoClip

# Ruta del video de entrada
input_file = 'originalFootage.avi'

# Cargar el video de entrada
clip = VideoFileClip(input_file, has_mask=True)

# Crear un clip de fondo verde del mismo tamaño que el video de entrada
green_background = ColorClip(size=clip.size, color=(0, 255, 0), duration=clip.duration)

# Combinar el video de entrada con el fondo verde
final_clip = CompositeVideoClip([green_background.set_position('center'), clip.set_position('center')])

# Guardar el resultado
output_file = 'videoWithGreenscreen.mp4'
final_clip.write_videofile(output_file, codec='libx264')
