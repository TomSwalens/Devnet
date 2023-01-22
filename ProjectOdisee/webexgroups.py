import xlrd   # library to manage excel spreadsheets
import json

wb = xlrd.open_workbook("webex_groups.xlsx")
sheet = wb.sheet_by_index(0)

member_dict = {"group": "x", "person_name": "y", "email":"z"}
member_list = [member_dict]


def find_all_persons_and_groups(xlf):
    ### READ EXCEL FILE AND RETURN NUMBER OF ROWS
    wb = xlrd.open_workbook("webex_groups.xlsx")
    sheet = wb.sheet_by_index(0)
    number_rows = sheet.nrows
    all_members = []
    for r in range(number_rows):
        if r > 0: ### first row contains columns names
            COL_A =  sheet.cell_value(r, 0)  #### column A
            COL_B =  sheet.cell_value(r, 1)  #### column B
            COL_C =  sheet.cell_value(r, 2)  #### column C
            member_dict["group"] = COL_A
            member_dict["person_name"]  = COL_B 
            member_dict["email"] = COL_C
            all_members.append(member_dict.copy())     
    return all_members

member_list = find_all_persons_and_groups("webex_groups.xlsx")

def make_list_of_groups(member_list):    
    all_groups = []
    mem = None
    for rec in member_list:
        g = rec["group"]
        if mem != g:
            all_groups.append(g)
        mem = g
    all_groups.pop()
    return all_groups

#group_list  = make_list_of_groups(member_list) 


def attach_members_to_groups(group_name, membr_list):        
    membr_dict         = {}
    all_group_members  = [membr_dict]
    #print(loc_group)
    for membr in membr_list:
        if membr["group"] == group_name:
            if membr["person_name"] != None:
                membr_dict["person_name"]  = membr["person_name"]
                membr_dict["email"] = membr["email"]
                #print(member_dict)
                all_group_members.append(membr_dict.copy())
    return all_group_members


def main():
    member_list = find_all_persons_and_groups("webex_groups.xlsx")
    group_list  = make_list_of_groups(member_list)  
    all_members = []
    groups_struc = []
    for group_rec in group_list:
        all_members = attach_members_to_groups(group_rec, member_list)
        del all_members[0] #### delete the first element, which is a copy of the last element
        group_dict = { "group": {"group_name": group_rec , "members": all_members }} 
        groups_struc["groups"].append(group_dict) # updated 18JAN2022
    js_groups = json.dumps(groups_struc)
    

#### execute main() when called directly        
if __name__ == '__main__':
    main()


