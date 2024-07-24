import streamlit as st
import json
import os

st.set_page_config(
    page_title="The Mosaic Mind of AI",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for fonts and body
st.markdown('<style>div.block-container{padding-top:0.5rem;}</style>', unsafe_allow_html=True)

white_color = "#fff"
h1 = "1.8rem"
h2 = "1.5rem"
h3 = "1.1rem"
p = "0.9rem"

font_css = f"""
<style>
    body {{
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: black;
        color: white;
    }}
    .title-box {{
        padding: 10px;
        margin: 10px;
        background-color: #000;
        color: {white_color};
        border-radius: 10px;
        box-shadow: 0.4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease-in-out;
    }}
    h1 {{
        font-family: 'Helvetica Neue', Arial, sans-serif !important;
        font-size: {h1};
        font-weight: bold;
        font-stretch: condensed;
        margin: 0;
        letter-spacing: 0.08rem;
    }}
    h2 {{
        font-family: 'Helvetica Neue', Arial, sans-serif !important;
        font-size: {h2};
        font-weight: bold;
        font-stretch: condensed;
        letter-spacing: 0.02rem;
    }}
    h3 {{
        font-family: 'Helvetica Neue', Arial, sans-serif !important;
        font-size: {h3};
        font-weight: bold;
        font-stretch: condensed;
        letter-spacing: 0.01rem;
        color: #edcce8;
    }}
    h5, p {{
        font-family: 'Helvetica Neue', Arial, sans-serif !important;
        color: #85888c;
        font-size: {p};
    }}
    @media (max-width: 480px) {{
        .title-box {{
            padding: 10px;
            margin: 10px;
        }}
        h1 {{
            font-size: 1.4rem;
        }}
    }}
    h2 {{
        font-family: 'Helvetica Neue', Arial, sans-serif !important;
        font-size: {h2};
        font-weight: bold;
        font-stretch: condensed;
        letter-spacing: 0.02rem;
    }}
    h3 {{
        font-family: 'Helvetica Neue', Arial, sans-serif !important;
        font-size: {h3};
        font-weight: bold;
        font-stretch: condensed;
        letter-spacing: 0.01rem;
    }}
    h5, p {{
        font-family: 'Helvetica Neue', Arial, sans-serif !important;
        color: #dbdbdb;
        font-size: {p};
    }}
</style>
"""

st.markdown(font_css, unsafe_allow_html=True)

# Path to JSON data
json_file_path = 'graph_data.json'  # Make sure this path is correct

# Read the JSON graph data
with open(json_file_path, 'r') as json_file:
    graph_data = json.load(json_file)

# Convert JSON data to string and insert it directly into the HTML template
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>'Pride and Prejudice' Social Architecture</title>
    <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
    <style>
        body, html {{
            margin: 0;
            padding: 0;
            height: 100%;
            width: 100%;
            overflow: hidden;
        }}
        #mynetwork {{
            width: 100%;
            height: 100vh;
            border: none;
        }}
        .css-1v3fvcr, .css-18e3th9, .css-1d391kg {{
            padding: 0;
            margin: 0;
        }}
    </style>
</head>
<body>
<div id="mynetwork"></div>
<script>
    document.addEventListener('DOMContentLoaded', function () {{
        const container = document.getElementById('mynetwork');
        const data = {json.dumps(graph_data)};
        const options = {{
            nodes: {{
                shape: 'dot',
                size: 20,
                font: {{
                    size: 15,
                    color: 'white',
                }}
            }},
            edges: {{
                width: 2
            }},
            physics: {{
                barnesHut: {{
                    gravitationalConstant: -30000
                }}
            }}
        }};
        const network = new vis.Network(container, data, options);
        window.addEventListener('resize', function () {{
            network.fit();
        }});
    }});
</script>
</body>
</html>
"""

# Function to display the HTML in Streamlit
def main():
    st.title("'Pride and Prejudice' Social Architecture")
    st.subheader("Collection of ML Projects Created by [Fay Cai](https://www.faycai.com)")
    st.write("Read <Pride and Prejudice> in [AI Vision](https://www.faycai.com) | More Info about this [Graphic Network Model](https://www.faycai.com/data-science/the-mosaic-mind-of-ai-app)")

    st.components.v1.html(html_content, height=800, scrolling=True)


if __name__ == '__main__':
    main()
