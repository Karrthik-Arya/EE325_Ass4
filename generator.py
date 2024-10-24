import pandas as pd
import numpy as np
import streamlit as st

def generate_xy(lambda_val=10000, p_val=0.01, num_samples=20):

  x_values = np.random.poisson(lam=lambda_val, size=num_samples)
  y_values = [np.random.binomial(n=x, p=p_val) for x in x_values]

  df = pd.DataFrame({'Insurers': x_values, 'Claims': y_values})
  return df


def main():
    st.title("Data Generator")

    lambda_val = st.text_input("Enter Lamnda:", value=10000)
    p_val = st.text_input("Enter p:", value=0.01)
    num_samples = st.text_input("Enter no. of samples:", value=20)


    if st.button("Generate Data"):
        if lambda_val and p_val and num_samples:
            df = generate_xy(float(lambda_val), float(p_val), int(num_samples))
            st.write("Generated DataFrame:")
            st.write(df)

            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Data as CSV",
                data=csv,
                file_name='generated_dataframe.csv',
                mime='text/csv',
            )
        else:
            st.error("Please provide all inputs.")

if __name__ == "__main__":
    main()
