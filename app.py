import streamlit as st
from pytezos import pytezos

def welcome():
    return "Welcome All"

def addPatient():
  name = st.text_input("Enter your Full Name")
  number = st.number_input("Enter your Phone Number", step=1, min_value=1)
  age = st.number_input("Enter your Age", step=1, min_value=1)
  gender = st.text_input("Male/Female/Prefer Not Say")
  uid = st.text_input("Enter your UID")


  if st.button("Register Now"):
    pytezos = pytezos.using(shell = 'https://florencenet.smartpy.io', key='edskRd4QGqLTZFjP7H1wHYc7FJ7kv8Ds7HYfJR9dp7eeCVP5RyG6ZJKTJhmzZyjkfNyXtoWTuvxT2UT2VxWgFrGJcWLZKHrU5j')
    contract = pytezos.contract('KT1Tvgcmu9L36RQPH451dVF57H2xcDAWnq42')

    contract.addPatient(age = age, gender = gender, name = name, number = number, uid = uid).with_amount(0).as_transaction().fill().sign().inject()   

def addFactory():
  name = st.text_input("Enter your Full Name")
  number = st.number_input("Enter Phone Number of your Industrial Complex", step=1, min_value=1)
  factLoc = st.text_input("Write Complete Address of your Industrial Complex")
  uid = st.text_input("Enter UID of your Industrial Complex")


  if st.button("Register Now"):
    pytezos = pytezos.using(shell = 'https://florencenet.smartpy.io', key='edskRd4QGqLTZFjP7H1wHYc7FJ7kv8Ds7HYfJR9dp7eeCVP5RyG6ZJKTJhmzZyjkfNyXtoWTuvxT2UT2VxWgFrGJcWLZKHrU5j')
    contract = pytezos.contract('KT1Tvgcmu9L36RQPH451dVF57H2xcDAWnq42')

    contract.addFactory(factLoc = factLoc, name = name, number = number, uid = uid).with_amount(0).as_transaction().fill().sign().inject()

def addCenter():
  name = st.text_input("Enter your Full Name")
  number = st.number_input("Enter Phone Number of your Medical Complex", step=1, min_value=1)
  centLoc = st.text_input("Write Complete Address of your Medical Complex")
  uid = st.text_input("Enter UID of your Medical Complex")
  factoryUID = st.text_input("Enter UID of your allied Factory")

  if st.button("Register Now"):
    pytezos = pytezos.using(shell = 'https://florencenet.smartpy.io', key='edskRd4QGqLTZFjP7H1wHYc7FJ7kv8Ds7HYfJR9dp7eeCVP5RyG6ZJKTJhmzZyjkfNyXtoWTuvxT2UT2VxWgFrGJcWLZKHrU5j')
    contract = pytezos.contract('KT1Tvgcmu9L36RQPH451dVF57H2xcDAWnq42')

    contract.addCenter(centLoc = centLoc, name = name, number = number, uid = uid, factoryUID = factoryUID).with_amount(0).as_transaction().fill().sign().inject()

def checkSlot():
  centerUID = st.text_input("Enter UID of the Vaccination Center")
  vaccName = st.text_input("Covaxin/Covishield/Sputnik-V")

  if st.button("Check"):
    pytezos = pytezos.using(shell = 'https://florencenet.smartpy.io', key='edskRd4QGqLTZFjP7H1wHYc7FJ7kv8Ds7HYfJR9dp7eeCVP5RyG6ZJKTJhmzZyjkfNyXtoWTuvxT2UT2VxWgFrGJcWLZKHrU5j')
    contract = pytezos.contract('KT1Tvgcmu9L36RQPH451dVF57H2xcDAWnq42')

    contract.checkSlot(centerUID = centerUID, vaccName = vaccName).with_amount(0).as_transaction().fill().sign().inject()

def orderVacc():
  centerUID = st.text_input("Enter UID of the Vaccination Center")
  vaccName = st.text_input("Covaxin/Covishield/Sputnik-V")

  if st.button("Place Order Now"):
    pytezos = pytezos.using(shell = 'https://florencenet.smartpy.io', key='edskRd4QGqLTZFjP7H1wHYc7FJ7kv8Ds7HYfJR9dp7eeCVP5RyG6ZJKTJhmzZyjkfNyXtoWTuvxT2UT2VxWgFrGJcWLZKHrU5j')
    contract = pytezos.contract('KT1Tvgcmu9L36RQPH451dVF57H2xcDAWnq42')

    contract.orderVacc(centerUID = centerUID, vaccName = vaccName).with_amount(0).as_transaction().fill().sign().inject()

def updateStock():
  uid = st.text_input("Enter UID of the Factory")
  quantity = st.text_input("Quantity of Vaccine")
  vaccName = st.text_input("Covaxin/Covishield/Sputnik-V")

  if st.button("Update"):
    pytezos = pytezos.using(shell = 'https://florencenet.smartpy.io', key='edskRd4QGqLTZFjP7H1wHYc7FJ7kv8Ds7HYfJR9dp7eeCVP5RyG6ZJKTJhmzZyjkfNyXtoWTuvxT2UT2VxWgFrGJcWLZKHrU5j')
    contract = pytezos.contract('KT1Tvgcmu9L36RQPH451dVF57H2xcDAWnq42')

    contract.updateStock(centerUID = centerUID, vaccName = vaccName, quantity = quantity).with_amount(0).as_transaction().fill().sign().inject()

def getVacc():
  centerUID = st.text_input("Enter UID of the Vaccination Center")
  patiendUID = st.text_input("Enter your UID")
  vaccName = st.text_input("Covaxin/Covishield/Sputnik-V")

  if st.button("Confirm"):
    pytezos = pytezos.using(shell = 'https://florencenet.smartpy.io', key='edskRd4QGqLTZFjP7H1wHYc7FJ7kv8Ds7HYfJR9dp7eeCVP5RyG6ZJKTJhmzZyjkfNyXtoWTuvxT2UT2VxWgFrGJcWLZKHrU5j')
    contract = pytezos.contract('KT1Tvgcmu9L36RQPH451dVF57H2xcDAWnq42')

    contract.getVacc(centerUID = centerUID, vaccName = vaccName, patiendUID = patiendUID).with_amount(0).as_transaction().fill().sign().inject()


def main():
    
    st.set_page_config(page_title="VaxForAll")
   
    st.title("@VaxForAll")
    st.markdown(
        """<div style="background-color:#e1f0fa;padding:10px">
                    <h1 style='text-align: center; color: #304189;font-family:Helvetica'><strong>
                    Vaccine For All</strong></h1></div><br>""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """<p style='text-align: center;font-family:Helvetica;'>
                   This project greatly decreases any chances of misuse of the vaccine. As Our country is facing a shortage of vaccine due to some unfaithful people who are responsible for lots of innocent deaths So to bring these malpractices to an end becomes our priority. We tried to help our nation by building a website that helps to track all the information of covid vaccine through blockchain technology.</p>""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """<h3 style='text-align: center; color: white; font-family:'Lato';font-family:Helvetica;'>
                   The proposed solution is going to help our nation overcome our vaccine shortage problem
by keeping all the information decentralized and available to all. #VaxForAll.
                   </h3>""",
        unsafe_allow_html=True,
    )

    st.sidebar.title("Choose your entry point")
    st.sidebar.markdown("Select the entry point accordingly:")

    algo = st.sidebar.selectbox(
        "Select the Option", options=[
          "Register Patient",
          "Register Factory",
          "Register Vaccination Center",
          "Check Slot Availability",
          "Order Vaccine from Allied Factory",
          "Book Vaccination Slot",
          "Update Factory Stock Availability"
          ]
    )

    if algo == "Register Patient":
        addPatient()

    if algo == "Register Factory":
        addFactory()

    if algo == "Register Vaccination Center":
        addCenter()

    if algo == "Check Slot Availability":
        checkSlot()

    if algo == "Order Vaccine from Allied Factory":
        orderVacc()  

    if algo == "Book Vaccination Slot":
        getVacc()

    if algo == "Update Factory Stock Availability":
        updateStock()
   
if __name__ == "__main__":
  main()