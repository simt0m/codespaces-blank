from datetime import datetime, timedelta


now = datetime.now()
if now.hour < 17:
    due_date = now.replace(hour=18, minute=0, second=0, microsecond=0)
else:
    due_date = (now + timedelta(days=1)).replace(hour=18, minute=0, second=0, microsecond=0)
due_date_str = due_date.strftime("%Y-%m-%d %H:%M")


items_list = [
    {
        "ID": "1",
        "Type": "Headset",
        "Model": "Jabra Evolve2 65",
        "Features": "Wireless, ANC, USB-A",
        "Rate": 4.1,
        "RateCount": 10,
        "Status": "Available",
        "User": "n/a",
        "User email": "n/a",
        "Due by": "n/a",
        "Cost": "£126",
        "Short description": "High-quality wireless headset with Active Noise Cancellation and USB-A connectivity.",
    },
    {
        "ID": "2",
        "Type": "Headset",
        "Model": "Jabra Evolve2 65",
        "Features": "Wireless, ANC, USB-A",
        "Rate": 4.1,
        "RateCount": 10,
        "Status": "Available",
        "User": "n/a",
        "User email": "n/a",
        "Due by": "n/a",
        "Cost": "£126",
        "Short description": "High-quality wireless headset with Active Noise Cancellation and USB-A connectivity.",
    },
    {
        "ID": "3",
        "Type": "Headset",
        "Model": "Jabra Evolve2 65",
        "Features": "Wireless, ANC, USB-A",
        "Rate": 4.1,
        "RateCount": 10,
        "Status": "Being used",
        "User": "Joe Bloggs",
        "User email": "joeblogg@email.com",
        "Due by": due_date_str,
        "Cost": "£126",
        "Short description": "High-quality wireless headset with Active Noise Cancellation and USB-A connectivity.",
    },
    {
        "ID": "4",
        "Type": "Headset",
        "Model": "Jabra Evolve2 55",
        "Features": "Wireless, ANC, USB-C",
        "Rate": 2.9,
        "RateCount": 20,
        "Status": "Available",
        "User": "n/a",
        "User email": "n/a",
        "Due by": "n/a",
        "Cost": "£116",
        "Short description": "Ergonomically designed with ANC, offering both USB-C connection and wireless freedom.",
    },
    {
        "ID": "5",
        "Type": "Headset",
        "Model": "Jabra Evolve2 55",
        "Features": "Wireless, ANC, USB-C",
        "Rate": 2.9,
        "RateCount": 20,
        "Status": "Overdue",
        "User": "John Smith",
        "User email": "johnsmith@email.com",
        "Due by": due_date_str,
        "Cost": "£116",
        "Short description": "Ergonomically designed with ANC, offering both USB-C connection and wireless freedom.",
    },
    {
        "ID": "6",
        "Type": "Headset",
        "Model": "Jabra Evolve 40 Mono",
        "Features": "Wired, 3.5mm Jack, One-ear",
        "Rate": 3.7,
        "RateCount": 43,
        "Status": "Available",
        "User": "n/a",
        "User email": "n/a",
        "Due by": "n/a",
        "Cost": "£38",
        "Short description": "Wired, single-ear headset with 3.5mm jack, suitable for multi-tasking professionals.",
    },
    {
        "ID": "7",
        "Type": "Earpods",
        "Model": "Apple EarPods",
        "Features": "Wired, Lightning Connector, No mic",
        "Rate": 4.2,
        "RateCount": 13,
        "Status": "Being used",
        "User": "Jane Austin",
        "User email": "janeaustin@email.com",
        "Due by": due_date_str,
        "Cost": "£15.83",
        "Short description": "Classic wired EarPods with a lightning connector, delivering clear audio with a minimalistic design.",
    },
    {
        "ID": "8",
        "Type": "Earpods",
        "Model": "Apple EarPods",
        "Features": "Wired, Lightning Connector, No mic",
        "Rate": 4.2,
        "RateCount": 13,
        "Status": "Broken",
        "User": "n/a",
        "User email": "n/a",
        "Due by": "n/a",
        "Cost": "£15.83",
        "Short description": "Classic wired EarPods with a lightning connector, delivering clear audio with a minimalistic design.",
    },
    {
        "ID": "9",
        "Type": "Mouse",
        "Model": "Dell Optical Mouse MS116",
        "Features": "Wired, Black",
        "Rate": 4.4,
        "RateCount": 23,
        "Status": "Available",
        "User": "n/a",
        "User email": "n/a",
        "Due by": "n/a",
        "Cost": "£8.75",
        "Short description": "A dependable wired mouse, featuring a sleek design and smooth tracking.",
    },
    {
        "ID": "10",
        "Type": "Mouse",
        "Model": "Dell Wireless Mouse MS3320W",
        "Features": "Wireless, Black",
        "Rate": 3.1,
        "RateCount": 22,
        "Status": "Available",
        "User": "n/a",
        "User email": "n/a",
        "Due by": "n/a",
        "Cost": "£15.51",
        "Short description": "Versatile wireless mouse with a comfortable grip, ideal for both home and office use.",
    },
]