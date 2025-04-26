import os
import sys
import subprocess

try:
    from gtts import gTTS
except ImportError:
    print('❌ The "gTTS" package is not installed.')
    choice = input('💬 Do you want to install it now? (y/n): ').strip().lower()
    if choice == 'y':
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gTTS'])
            from gtts import gTTS
            print('✅ "gTTS" installed successfully.\n')
        except Exception as install_error:
            print(f'❌ Failed to install "gTTS": {install_error}')
            sys.exit(1)
    else:
        print('🚪 Exiting because "gTTS" is required.')
        sys.exit(1)

if len(sys.argv) < 2:
    print('❌ Usage: python script.py <input_text_file> [output_file_name]')
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2] if len(sys.argv) >= 3 else 'audio'

if not output_file.endswith('.mp3'):
    output_file += '.mp3'

try:
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f'Input file "{input_file}" not found.')

    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read().strip()

    if not text:
        raise ValueError('Input file is empty. Cannot generate audio.')

    tts = gTTS(text=text, lang='hi')
    tts.save(output_file)

    print(f'✅ Audio file "{output_file}" has been generated successfully.')

except FileNotFoundError as fnf_error:
    print(f'❌ Error: {fnf_error}')

except ValueError as val_error:
    print(f'❌ Error: {val_error}')

except Exception as e:
    print(f'❌ An unexpected error occurred: {e}')
