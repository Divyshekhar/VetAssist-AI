from calendar_service import create_event
from db import save_appointment

def book_appointment(owner_name, pet_name, date, time):
    appointment_data = {
        "owner_name": owner_name,
        "pet_name": pet_name,
        "date": date,
        "time": time
    }
    result = create_event(owner_name, pet_name, date, time)
    if result["success"]:
        save_appointment(appointment_data)
        event_link = result.get("event_link", "No Event link present")
        return f"""
        ✅ Appointment booked!

        🐶 Pet: {pet_name}
        👤 Owner: {owner_name}
        📅 Date: {date}
        ⏰ Time: {time}

        📍 Event: {event_link}
        """
    else:
        return result["message"]
