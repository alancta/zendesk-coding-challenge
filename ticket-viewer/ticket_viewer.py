

def view_all_tickets():
    """
    This function is executed when the user wants to view all single ticket. 
    """
    choice = ''
    while choice != 'm':
        print("\n***** View all tickets *****")
        print('Options:')
        print('[1] View all tickets')
        print('[2] View one ticket')
        choice = input('Enter an option (or <m> to return to main menu.):')


def view_single_ticket():
    """
    This function is executed when the user wants to view a single ticket. 
    The user is prompted for the specific ticket ID they want to view.
    """
    choice = ''
    while choice != 'm':
        print("\n***** View SINGLE ticket *****")
        choice = input('Enter ticket ID (or <m> to return to main menu.):')


def display_main_menu():
    """
    This function displays the main menu options
    """
    choice = ''
    while choice != 'q':
        print('\n***********************************************')
        print('*********  Welcome to Ticket Viewer!  *********')
        print('***********************************************')
        print('Main Menu')
        print('Options:')
        print('[1] View all tickets')
        print('[2] View single ticket')
        choice = input('Enter an option (or enter <q> to quit):')
        if choice == '1':
            view_all_tickets()
        elif choice == '2':
            view_single_ticket()
        elif choice == 'q':
            exit
        else:
            print(
                "Invalid input. Please pick from the available options.")


def main():
    """
    This function calls the display_main_menu function which kicks off the ticket viewer app.
    """
    display_main_menu()


if __name__ == '__main__':
    main()
