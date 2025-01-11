#import file_operation
from menu import menu_root,menu_view,view_param_dialog,menu_after_view,new_note_dialog,menu_after_new_note,menu_for_repit_add,menu_edit_del,inp_key_for_edi_del
from gtf_func_16 import view_on_disp, add_book,view_for_edi_del,edit_katal, del_katal

if __name__ == "__main__":

      print(60 * "_")
      print("Добро пожаловать в Каталог книг!")

      #print(file_operation.file_matrix())

      while True:

            choice_1 = menu_root()

            match choice_1:

                  case "1":

                        choice_1_1 = menu_view()

                        if choice_1_1 == "7":
                              continue

                        choice_view,find = view_param_dialog(choice_1_1)

                        view_on_disp(choice_view, find)

                        choice_after_view = menu_after_view()

                        if choice_after_view == "0":
                              break

                        elif choice_after_view == "1":
                              continue

                  case "2":

                        while True:

                              new_note = new_note_dialog()

                              chek = ""
                              while True:

                                    chek = menu_after_new_note()

                                    if chek == "1":

                                          add_book(new_note)

                                          break
                                    elif chek == "0" or chek == "2":
                                          break
                                    print("Вы не ввели корректное значение пункта меню. Повторите ввод.")

                              if chek == "1":

                                    chek_repit_add_book = menu_for_repit_add()

                                    if chek_repit_add_book == "1":
                                          continue
                                    elif chek_repit_add_book == "2":
                                          break

                              elif chek == "0":
                                    continue
                              elif chek == "2":
                                    break

                  case "3":

                        choice_3_1 = menu_edit_del('edit')

                        if choice_3_1 == "7":
                              continue

                        choice_view, find = view_param_dialog(choice_3_1)

                        view_for_edi_del(choice_view,find)

                        key_edi = inp_key_for_edi_del('edit')

                        edit_katal(key_edi)

                        choice_after_view = menu_after_view()

                        if choice_after_view == "0":
                              break

                        elif choice_after_view == "1":
                              continue

                  case "4":

                        choice_4_1 = menu_edit_del('delete')

                        if choice_4_1 == "7":
                              continue

                        choice_view, find = view_param_dialog(choice_4_1)

                        view_for_edi_del(choice_view, find)

                        key_del = inp_key_for_edi_del('delete')

                        del_katal(key_del)

                        choice_after_view = menu_after_view()

                        if choice_after_view == "0":
                              break

                        elif choice_after_view == "1":
                              continue

                  case "5":
                        break













