import view
import model


def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.success_open()
            case 2:
                model.new_save_file()
                view.success_save()
            case 3:
                view.show_contacts(model.get_phone_book())
            case 4:
                new_contact = list(view.create_new_contact())
                model.add_new_contact(new_contact)
            case 5:
                clean = view.select_contact('Введите удаляемый контакт')
                contact = model.get_contact(clean)
                if contact:
                    confirm = view.delete_confirm(contact[0][0])
                    if confirm:
                        model.delete_contact(contact[0])
                elif contact == []:
                    view.empty_request()
                else:
                    view.many_request()
                view.success_del()
            case 6:
                name = view.select_contact('Введите изменяемый контакт')
                contact = model.get_contact(name)
                if contact:
                    changed_contact = view.change_contact()
                    model.change_contact(contact[1], list(changed_contact))
                elif contact == []:
                    view.empty_request()
                else:
                    view.many_request()
                view.success_chan()
            case 7:
                find = view.find_contact()
                result = model.search_contact(find)
                view.show_contacts(result)
                view.success_find()
            case 8:
                view.end_program()
                break
