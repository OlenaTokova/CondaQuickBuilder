import streamlit as st
import sqlite3

def create_usertable():
    conn = sqlite3.connect('sqlite.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS contact_manager(Person_Name TEXT,Address TEXT,City TEXT,State TEXT,PostCode TEXT,Phone_Number TEXT,Email TEXT)')
    conn.close()

def add_contact_details(person_name, address, city, state, postcode, phone_number, email):
    conn = sqlite3.connect('sqlite.db')
    c = conn.cursor()
    c.execute('INSERT INTO contact_manager(Person_Name,Address,City,State,PostCode,Phone_Number,Email) VALUES (?,?,?,?,?,?,?)',(person_name, address, city, state, postcode, phone_number, email))
    conn.commit()
    conn.close()

def view_all_contacts():
    conn = sqlite3.connect('sqlite.db')
    c = conn.cursor()
    c.execute('SELECT * FROM contact_manager')
    data = c.fetchall()
    return data

def delete_contact(record_id):
    conn = sqlite3.connect('sqlite.db')
    c = conn.cursor()
    c.execute('DELETE FROM contact_manager WHERE rowid=?', (record_id,))
    conn.commit()
    conn.close()

def main():
    st.title("Contacts Manager")

    menu = ["Home","Add Contact","View Contacts","Delete Contact"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Add Contact":
        st.subheader("Add New Contact")
        person_name = st.text_input("Name")
        address = st.text_input("Address")
        city = st.text_input("City")
        state = st.text_input("State")
        postcode = st.text_input("Postcode")
        phone_number = st.text_input("Phone Number")
        email = st.text_input("Email")

        if st.button("Add Contact"):
            create_usertable()
            add_contact_details(person_name, address, city, state, postcode, phone_number, email)
            st.success("Added {} to Contacts".format(person_name))

        st.subheader("All Contacts")
        all_contacts = view_all_contacts()
        st.table(all_contacts)

    elif choice == "View Contacts":
        st.subheader("View Contacts")
        all_contacts = view_all_contacts()
        st.table(all_contacts)

    elif choice == "Delete Contact":
        st.subheader("Delete Contact")
        record_id = st.text_input("Enter the ID of the Contact to be deleted")
        if st.button("Delete Contact"):
            confirm_button = st.empty()
            cancel_button = st.empty()

            if confirm_button.button("Are you sure?"):
                delete_contact(record_id)
                st.success("Deleted Contact with ID {}".format(record_id))
                confirm_button.empty()
                cancel_button.empty()
            elif cancel_button.button("Cancel"):
                confirm_button.empty()
                cancel_button.empty()

if __name__ == "__main__":
    main()