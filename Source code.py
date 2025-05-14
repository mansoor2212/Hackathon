from graphviz import Digraph
# Create a new directed graph
dot = Digraph(comment='Colour Detection Flowchart')
dot.attr(rankdir='TB') # TB = Top to Bottom, LR = Left to Right

# Define nodes (shapes can be specified)
# Oval for Start/End
dot.node('A', 'Start', shape='oval')
dot.node('J', 'End', shape='oval')

# Parallelogram for Input/Output
dot.node('B', 'Input Image', shape='parallelogram')
dot.node('I', 'Output Results', shape='parallelogram')

# Rectangle for Processes
dot.node('C', 'Pre-processing\n(Resize, Noise Reduction, Colour Space Conversion)', shape='box')
dot.node('D', 'Select Region of Interest (ROI)\n(Optional)', shape='box')
dot.node('F', 'Extract Colour Information', shape='box')
dot.node('G', 'Process/Analyze Colour Data\n(Averaging, Counting, Mapping to Names)', shape='box')

# Diamond for Decision/Method Choice
dot.node('E', 'Colour Identification/Quantization Method\n(Pixel Iteration, Masking, Clustering, Histogram)', shape='diamond')


# Define edges (connections between nodes)
dot.edge('A', 'B')  # Start -> Input Image
dot.edge('B', 'C')  # Input Image -> Pre-processing
dot.edge('C', 'D')  # Pre-processing -> Select ROI
dot.edge('D', 'E')  # Select ROI -> Colour Identification Method
# If ROI is skipped, Pre-processing can go directly to Colour Identification
# You could add an alternative path or just keep it sequential for simplicity here.
# For a more complex flowchart, you'd add more decision logic.
dot.edge('E', 'F')  # Colour Identification Method -> Extract Colour Info
dot.edge('F', 'G')  # Extract Colour Info -> Process/Analyze Data
dot.edge('G', 'I')  # Process/Analyze Data -> Output Results
dot.edge('I', 'J')  # Output Results -> End

# --- Optional: Add a "bypass" for the ROI step if it's truly optional ---
# This makes the graph slightly more complex to draw simply.
# For this example, we'll keep the main flow.
# An alternative is to have an edge from 'C' directly to 'E' labeled "Skip ROI"
# Specify output format and render the graph
# You can render to PDF, PNG, SVG, etc.
try:
    dot.render('colour_detection_flowchart', view=True, format='png')
    print("Flowchart 'colour_detection_flowchart.png' generated successfully.")
    print("It should open automatically if view=True and a viewer is available.")
except Exception as e:
    print(f"Error rendering flowchart: {e}")
    print("Make sure Graphviz is installed and in your system's PATH.")
