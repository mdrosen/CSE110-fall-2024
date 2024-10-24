
with open('BYU-I code\CSE110-Fall-2024\week6\hr_system.txt', 'r') as f:

    for line in f:
        line = line.strip()
        parts = line.split(" ")
        
        name = parts[0]
        id_number = parts[1]
        job_title = parts[2]
        salary = float(parts[3]) 
        paycheck = salary / 24 # Assuming they're paid twice a month.
        
        if job_title == "Engineer":
            paycheck += 1000
        
        print(f'Name: {name} (ID: {id_number}),  Title: {job_title} - ${paycheck:.2f}')

