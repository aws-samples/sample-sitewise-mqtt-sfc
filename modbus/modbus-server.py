import csv
import time
import threading
import random
from pymodbus.server import StartAsyncTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock
import asyncio

def read_csv_data(filename):
    """
    Read the CSV data and return it as a dictionary where keys are
    the address and values are the corresponding register values.
    """
    data = {}
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            address = int(row['address'])
            data[address] = row
    return data

def create_modbus_data_block(csv_data):
    """
    Create a Modbus data block from the CSV data.
    """
    data = dict()
    for item_key in csv_data.keys():
        value = int(csv_data[item_key]['value'])
        data[item_key] = value
    
    store = ModbusSequentialDataBlock(3, csv_data)
    return store

async def update_modbus_data(context, csv_data):
    """
    Update the Modbus register values over time from the CSV file.
    This will be run in a separate thread to update the registers every few seconds.
    """
    while True:
        await asyncio.sleep(10)
        # Read the CSV data
        
        for item_key in csv_data.keys():
            min, max= (csv_data[item_key]['range']).split(';')
            if min == max :
                #skip static value
                continue
            value = random.randrange(int(min), int(max))
            print(item_key, [value])
            context[1].setValues( 3, item_key, [value])

        print("Updated Modbus registers")
        

async def start_modbus_server(csv_file):
    """
    Start the Modbus TCP server and expose the data from a CSV file.
    """
    # Read initial CSV data
    print("reading file")
    csv_data = read_csv_data(csv_file)

    # Create Modbus data block from CSV data
    #data_block = create_modbus_data_block(csv_data)
    
    print("preparing the storage")
    data_block = create_modbus_data_block(csv_data)
    
    # Create a Modbus slave context using the data block
    store = ModbusSlaveContext(
        hr=data_block  # Holding Registers (hr) to expose
    )

    context = ModbusServerContext(slaves=store, single=True)
    
    asyncio.create_task(update_modbus_data(context, csv_data))

    # Create and start the Modbus TCP server
    print("Modbus TCP Server is running and updating registers over time...")
    server = await StartAsyncTcpServer(context, framer='socket')


    # Start the Modbus server and serve indefinitely
    #await server.serve_forever()

if __name__ == "__main__":
    csv_file = 'data.csv'  # Replace with the path to your CSV file
    asyncio.run(start_modbus_server(csv_file))