# LED Control Project (TWIG)
## Overview
This project realizes a Python application for controlling LEDs to display various patterns and stock market information. It allows the user to control the TWIG device's LED strip and matrix through a series of HTTP requests. The system can display various color patterns and can even show real-time stock market data (of AAPL) with visual indicators of market performance.
## Features
- Basic LED color control (RGBW for strip, RGB for matrix)
- Pattern generation across both the LED strip and matrix
- Alternating color patterns
- Stock market data visualization
  - Shows stock symbols (AAPL)
  - Displays percentage changes with appropriate colors (green for gains, red for losses)
  - Shows directional arrows based on magnitude of change
## Usage
### Basic Functions
1. Send Custom Colors to TWIG
   ```python
   send_request(colors)
   ```
2. Turn off TWIG device
   ```python
   turn_off()
   ```
### Requirements
1. Requirement 1 (requirement1())
  Cycles all light strip LEDs through blue, red, and green colors with a 1-second delay between each color.
2. Requirement 2 (requirement2())
  Similar to Requirement 1 but specifically targets the matrix (256 LEDs) rather than the strip.
3. Requirement 3 (requirement3())
  Creates an alternating pattern of two colors (maize and blue) across both the strip and matrix.
4. Requirement 4a (requirement4a())
  Creates a checkerboard pattern that alternates between two colors, with the pattern inverting every second.
5. Requirement 4b (requirement4b())
  Alternates between all maize and all blue across the entire LED system every second.
6. Requirement 6 (requirement6(stock_symbol))
  Displays real-time stock information:
   - Shows the stock symbol
   - Displays the percentage change with appropriate color (green for positive, red for negative)
   - Shows directional arrows based on the magnitude of the change:
     - Up arrow for changes > 1%
     - 45° arrow for changes between 0% and 1%
     - -45° arrow for changes between -1% and 0%
     - Down arrow for changes < -1%
