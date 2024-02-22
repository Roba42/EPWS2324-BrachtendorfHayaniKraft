from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

# Check if environment variables for Azure Vision API are set
try:
    endpoint = os.environ["VISION_ENDPOINT"]
    key = os.environ["VISION_KEY"]
except KeyError:
    print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
    print("Set them before running this sample.")
    exit()

# Create an instance of the Image Analysis client
client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

# Function to extract accessibility information of an element
def get_accessibility_info(element):
    accessible_name = element.get_attribute("aria-label") or element.text.strip()
    role = element.get_attribute("role") or element.tag_name
    return accessible_name, role

# Function to extract images without alt attributes
def extract_images_without_alt(driver):
    images_without_alt = []
    images = driver.find_elements(By.TAG_NAME, "img")
    for img in images:
        alt_text = img.get_attribute("alt")
        if not alt_text:
            img_url = img.get_attribute("src")
            images_without_alt.append(img_url)
    return images_without_alt

# Function to analyze images
def analyze_images(images_without_alt):
    captions = []
    for img_url in images_without_alt:
        # Analyze the image and extract caption
        result = client.analyze_from_url(
            image_url=img_url,
            visual_features=[VisualFeatures.CAPTION]
        )
        if result.caption is not None:
            captions.append((img_url, result.caption.text, result.caption.confidence))
    return captions

# Function to create HTML report
def create_html_report(focused_elements_info, captions):
    with open("accessibility_report.html", "w") as file:
        file.write("<!DOCTYPE html>\n")
        file.write("<html lang='en'>\n<head>\n")
        file.write("<meta charset='UTF-8'>\n")
        file.write("<title>Accessibility Audit Report</title>\n")
        file.write("</head>\n<body>\n")
        file.write("<h1>Accessibility Audit Report</h1>\n")
        
        # Display images without alt attributes
        file.write("<h2>Images without alt attributes</h2>\n")
        if images_without_alt:
            for img_src in images_without_alt:
                file.write(f"<p><img src='{img_src}' style='height: 100px;' /> No alt attribute</p>\n")
        else:
            file.write("<p>All images have alt attributes.</p>\n")

        file.write("<h2>Captions for images without alt attributes</h2>\n")
        for img_url, caption, confidence in captions:  # Display captions and confidence
            file.write(f"<p><img src='{img_url}' style='height: 100px;' /> Caption: {caption}, Confidence: {confidence:.4f}</p>\n")

        # Display focusable elements order
        file.write("<h2>Focusable Elements Order</h2>\n")
        file.write("<ol>\n")
        for name, role in focused_elements_info:
            file.write(f"<li>{role} - '{name}'</li>\n")
        file.write("</ol>\n")

        file.write("</body>\n</html>")

# Start a new Chrome WebDriver session
driver = webdriver.Chrome()
driver.get("https://roba42.github.io/test/")

# Extract images without alt attributes
images_without_alt = extract_images_without_alt(driver)

# Analyze images without alt attributes and extract captions
captions = analyze_images(images_without_alt)

# Speichern der Informationen zu den fokussierten Elementen
focused_elements_info = []

# Extract accessibility information of focusable elements
for _ in range(10):  # Simulate tab navigation
    driver.switch_to.active_element.send_keys(Keys.TAB)
    time.sleep(0.5)  # Wait for focus change
    active_element = driver.switch_to.active_element
    accessible_name, role = get_accessibility_info(active_element)
    focused_elements_info.append((accessible_name, role))

# Create HTML report
create_html_report(focused_elements_info, captions)

# Cleanup
driver.quit()

print("Accessibility report generated and saved as 'accessibility_report.html'.")
