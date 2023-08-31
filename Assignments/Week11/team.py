with open("hr_system.txt") as hr_file:
    for line in hr_file:
        line = line.strip()
        parts = line.split()
        name = parts[0]
        job_num = parts[1]
        job_title = parts[2]
        salary = int(parts[3])
        # print(
        #     f'Name: {name} (id: {job_num}), Title: {job_title} salary: ${salary/26:,.2f}')

        '''
        Change the program so that it generates bonuses for anyone who is an engineer. 
        For each of these employees, add $1000 to their paycheck amount.
        '''

        if job_title.capitalize() == 'Engineer':
            salary += 24000

        print(
            f'Name: {name} (id: {job_num}), Title: {job_title} salary: ${salary/24:,.2f}')
