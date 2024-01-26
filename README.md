
    <h1>Image Processing Script</h1>

    <p>This Python script is designed to process images within a specified directory. It offers functionality to resize images and create thumbnails while maintaining aspect ratios and considering image orientations.</p>

    <h2>Functions</h2>

    <h3><code>eh_imagem(nome_arquivo)</code></h3>
    <ul>
        <li><strong>Description:</strong> Checks if a file has an image extension.</li>
        <li><strong>Parameters:</strong>
            <ul>
                <li><code>nome_arquivo</code>: Name of the file.</li>
            </ul>
        </li>
        <li><strong>Returns:</strong> <code>True</code> if the file has an image extension, otherwise <code>False</code>.</li>
    </ul>

    <!-- Reduzir Foto Function -->
    <h3><code>reduzir_foto(input_dir, output_dir, ext='.jpg')</code></h3>
    <ul>
        <!-- Description -->
        <li><strong>Description:</strong> Resizes images within the specified input directory and saves them to the output directory.</li>
        <!-- Parameters -->
        <li><strong>Parameters:</strong>
            <ul>
                <li><code>input_dir</code>: Path to the directory containing the original images.</li>
                <li><code>output_dir</code>: Path to the directory where resized images will be saved.</li>
                <li><code>ext</code>: Extension for the output images (default is '.jpg').</li>
            </ul>
        </li>
        <!-- Process -->
        <li><strong>Process:</strong>
            <ol>
                <li>Retrieves a list of image files from the input directory.</li>
                <li>Iterates through each image file, opens it, and adjusts orientation if necessary.</li>
                <li>Resizes the image while maintaining the aspect ratio to fit within a maximum width of 3840 pixels.</li>
                <li>Saves the resized image to the output directory with reduced quality.</li>
            </ol>
        </li>
    </ul>

    <!-- Criar Thumbnail Function -->
    <h3><code>criar_tumbnail(input_dir, output_dir, ext='.jpg')</code></h3>
    <ul>
        <!-- Description -->
        <li><strong>Description:</strong> Creates thumbnails of images within the specified input directory and saves them to the output directory.</li>
        <!-- Parameters -->
        <li><strong>Parameters:</strong>
            <ul>
                <li><code>input_dir</code>: Path to the directory containing the original images.</li>
                <li><code>output_dir</code>: Path to the directory where thumbnails will be saved.</li>
                <li><code>ext</code>: Extension for the output thumbnails (default is '.jpg').</li>
            </ul>
        </li>
        <!-- Process -->
        <li><strong>Process:</strong>
            <ol>
                <li>Checks if the output directory exists; if not, creates it.</li>
                <li>Retrieves a list of image files from the input directory.</li>
                <li>Iterates through each image file, opens it, and creates a thumbnail with a fixed size of 290x290 pixels.</li>
                <li>Saves the thumbnail image to the output directory with reduced quality.</li>
            </ol>
        </li>
    </ul>

    <!-- Play Function -->
    <h3><code>play()</code></h3>
    <ul>
        <!-- Description -->
        <li><strong>Description:</strong> Orchestrates the image processing operations.</li>
        <!-- Process -->
        <li><strong>Process:</strong>
            <ol>
                <li>Specifies the input directory and output directories for resized images and thumbnails.</li>
                <li>Calls <code>reduzir_foto()</code> to resize images.</li>
                <li>Prints a message indicating the completion of image resizing.</li>
                <li>Calls <code>criar_tumbnail()</code> to create thumbnails.</li>
            </ol>
        </li>
    </ul>

    <h2>Usage</h2>

    <ol>
        <li>Ensure that you have Python installed on your system.</li>
        <li>Install the required dependencies using <code>pip install Pillow piexif</code>.</li>
        <li>Place your images in the specified input directory.</li>
        <li>Run the script, and it will process the images as per the defined functions.</li>
    </ol>

    <h2>Note</h2>

    <ul>
        <li>The script supports images with extensions: 'png', 'jpg', 'JPG', 'PNG', and 'heic'.</li>
        <li>It uses the Python Imaging Library (PIL) and piexif library for image processing and handling EXIF data.</li>
        <li>Adjustments for image orientations are made based on EXIF metadata when available.</li>
    </ul>

    <p>Feel free to modify the script according to your specific requirements or integrate it into your projects.</p>

