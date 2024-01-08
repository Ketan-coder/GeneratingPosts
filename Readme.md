# Image Quote Generator

This Python script generates visually appealing image quotes by overlaying text on an image template. The script uses the OpenCV library to manipulate images and includes random quotes, fonts, and colors for variety.

## Examples
![Example first](Making_Posts/Quotes#1.jpg)
![Example second](Making_Posts/Quotes#2.jpg)
![Example third](Making_Posts/Quotes#3.jpg)

## Features

1. **Dynamic Content:**
   - The script dynamically selects a random quote, font, color, and template for each execution.

2. **Text Wrapping:**
   - Quotes are wrapped to fit the desired width, ensuring a visually appealing layout.

3. **Randomization:**
   - Randomly selects a quote, font, color, and template from predefined lists.

4. **Counting and Persistence:**
   - Maintains a count of generated images using a text file (`count.txt`).

## Usage

1. **Prerequisites:**
   - Ensure you have Python installed on your machine.
   - Install the required libraries using:

     ```bash
     pip install opencv-python textwrap3 tqdm
     ```

2. **Running the Script:**
   - Execute the script using the following command:

     ```bash
     python image_quote_generator.py
     ```

3. **Generated Images:**
   - The script generates an image with a quote overlay and saves it as `Quotes#<count>.jpg`.
   - The count is incremented and persisted in the `count.txt` file.

## Customization

- **Quotes:**
  - Customize the `quotes_list` variable with your favorite quotes.

- **Fonts:**
  - Extend the `fonts_list` variable with additional OpenCV font constants.

- **Colors:**
  - Add or modify color combinations in the `colors` variable.

- **Templates:**
  - Replace the `Template.jpg` image with your own template.

## Note

- The script uses a template (`Template.jpg`) and overlays text on it. You can replace this template with your own image.

- Adjust the script parameters, such as font sizes, positions, and color schemes, to match your preferences.

## Contributing

Contributions are welcome! Feel free to open issues for bug reports, feature requests, or general feedback. If you have improvements or new features to contribute, please submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.