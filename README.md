Radar Data Processing Readme
This repository contains Python code for processing radar data obtained from a system. The code includes functions for parsing binary output from the radar, converting range profiles to distances, and visualizing the results. The main purpose of this code is to extract meaningful information from radar measurements, such as detecting objects and analyzing their movement.
Prerequisites
Make sure you have the following libraries installed:
NumPy
Matplotlib
Scikit-learn (for make_blobs)
You can install them using the following:
bash
Copy code
pip install numpy matplotlib scikit-learn

Getting Started
Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/your-username/your-repository.git
cd your-repository

Open the Python script where the radar data processing is implemented (your_script.py).
Specify the binary file path in the script:
python
Copy code
- specify the binary file path below
binDirPath = "path/to/your/binary/file"

Run the script. The radar data will be parsed, and the range profiles will be converted to distances. The script will generate a plot showing the variation in distances over frames.


Feel free to customize the script based on your specific use case and requirements.
**Functions**
parse_ADC(binDirPath) -> This function parses ADC data from the specified binary file directory (binDirPath) and returns a list of dictionaries, where each dictionary represents information for a specific frame.
convert_range_profile_to_distances(range_profile, fs=100e6/8, c0=3e8, S=170e12, num_ADC=256) -> 
This function takes a range profile as input and converts it to distances. It uses parameters such as sampling frequency (fs), speed of light (c0), sweep bandwidth (S), and number of ADC samples (num_ADC) to perform the conversion.
