import pandas as pd

def create_synthetic_data():
    """Create data for cruise ships' economy."""
    data = {
        'Ship Name': ['Ocean Voyager', 'Sea Explorer', 'Wave Rider', 'Sunset Dream', 'Star Cruiser'],
        'Passenger Capacity': [2000, 1800, 2200, 2500, 2100],
        'Ticket Revenue': [3000000, 2500000, 3500000, 4000000, 3200000],  # in dollars
        'Additional Revenue': [500000, 400000, 600000, 700000, 650000],  # in dollars
        'Operating Cost': [2500000, 2300000, 2800000, 3000000, 2700000]  # in dollars
    }
    df = pd.DataFrame(data)
    print("cruise ship economy data created successfully!")
    return df

def filter_data(df, column, value):
    """Filter the data based on a column and value."""
    try:
        filtered_df = df[df[column] == value]
        if filtered_df.empty:
            print(f"No records found for {column} = {value}")
        else:
            print(f"\nFiltered Data (where {column} = {value}):")
            print(filtered_df)
    except KeyError:
        print(f"Error: Column '{column}' does not exist in the data.")
    except Exception as e:
        print(f"An unexpected error occurred while filtering data: {e}")

def calculate_profit(df):
    """Calculate the profit for each ship and display statistics."""
    try:
        df['Profit'] = df['Ticket Revenue'] + df['Additional Revenue'] - df['Operating Cost']
        print("\nProfit Calculations for each Ship:")
        print(df[['Ship Name', 'Profit']])
        
        avg_profit = df['Profit'].mean()
        max_profit = df['Profit'].max()
        min_profit = df['Profit'].min()
        
        print("\nProfit Statistics:")
        print(f"Average Profit: ${avg_profit:,.2f}")
        print(f"Maximum Profit: ${max_profit:,.2f}")
        print(f"Minimum Profit: ${min_profit:,.2f}")
    except KeyError as e:
        print(f"Error: {e}. One or more columns are missing.")
    except Exception as e:
        print(f"An unexpected error occurred while calculating profit: {e}")

def main():
    print("Welcome to the Cruise Ship Economy Data Analysis Program with Error Handling!")
    
    # Load data
    data = create_synthetic_data()
    
    # Main interactive loop
    while True:
        print("\nMenu Options:")
        print("1 - View Data")
        print("2 - Filter Data by Column")
        print("3 - Calculate Profit and Statistics")
        print("4 - Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                print("\nData Preview:")
                print(data)
                
            elif choice == 2:
                column = input("Enter the column name to filter by (e.g., 'Ship Name', 'Passenger Capacity'): ")
                value = input(f"Enter the value to filter by for column '{column}': ")
                
                # Try converting value to an appropriate type if needed
                if column == 'Passenger Capacity':
                    value = int(value)
                elif column in ['Ticket Revenue', 'Additional Revenue', 'Operating Cost']:
                    value = float(value)
                
                filter_data(data, column, value)
                
            elif choice == 3:
                calculate_profit(data)
                
            elif choice == 4:
                print("Exiting program. Goodbye!")
                break
                
            else:
                print("Invalid choice. Please select a valid option.")
                
        except ValueError:
            print("Error: Please enter a valid integer for your choice.")
        except Exception as e:
            print(f"An unexpected error occurred in the menu: {e}")
        finally:
            print("End of current operation.")

# Run the main function
if __name__ == "__main__":
    main()
