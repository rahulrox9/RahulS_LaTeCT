import gradio as gr
import pandas as pd
import joblib

def classify_lamproites(input_filepath):
    model = joblib.load('final_rf.joblib')
    
    geochemical_data = pd.read_csv(input_filepath)
    
    required_features = model.feature_names_in_
    model_input = geochemical_data[required_features]
    
    geochemical_data['Tectonic_Setting'] = model.predict(model_input)
    
    output_filepath = 'classified_lamproites.csv'
    geochemical_data.to_csv(output_filepath, index=False)
    
    return output_filepath

interface = gr.Interface(
    fn=classify_lamproites,
    inputs=gr.File(label="Upload Geochemical Data (CSV format)"),
    outputs=gr.File(label="Download Classified Data (CSV format)"),
    title="LaTeCT: Lamproite Tectonic Classification Tool",
    description="Upload a CSV file containing whole rock trace element data. The application will return the dataset appended with the predicted tectonic settings."
)

if __name__ == "__main__":
    interface.launch()
