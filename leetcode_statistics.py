import pandas as pd
import os


def find_all_topics():
    return [dir for dir in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(), dir))]

def find_all_solutions(topic_name):
    abs_dir_path = os.path.join(os.getcwd(), topic_name)

    return [file for file in os.listdir(abs_dir_path) if os.path.isfile(os.path.join(abs_dir_path, file))]

def calculate_unique_solution_count(solution_list):
    solution_num_set = set()

    for solution in solution_list:
        solution_num = solution.split('_')[0]

        if "-todo" not in solution:
            solution_num_set.add(solution_num)
    
    return len(solution_num_set)

def find_todo_list(solution_list):
    todo_solution_list = list()

    for solution in solution_list:
        if "-todo" in solution:
            todo_solution_list.append(solution)
    
    return todo_solution_list


if __name__ == '__main__':
    all_topics      = find_all_topics()
    all_columns     = ["Solved", "To-Do", "Dup Solved", "# of Files"]
    final_dataframe = pd.DataFrame(columns=all_columns, index=all_topics)
    todo_dict       = dict()

    for topic in all_topics:
        all_solution_list = find_all_solutions(topic)
        all_todo_sol_list = find_todo_list(all_solution_list)

        final_dataframe.at[topic, all_columns[0]] = calculate_unique_solution_count(all_solution_list)
        final_dataframe.at[topic, all_columns[1]] = len(all_todo_sol_list)
        final_dataframe.at[topic, all_columns[2]] = len(all_solution_list) - final_dataframe.at[topic, all_columns[0]] - len(all_todo_sol_list)
        final_dataframe.at[topic, all_columns[3]] = len(all_solution_list)

        if all_todo_sol_list:
            todo_dict[topic] = all_todo_sol_list
    
    print("----------------- Leetcode Statistics -----------------\n")
    final_dataframe.loc['Total'] = final_dataframe.sum()
    print(final_dataframe)
    print("\n-------------------------------------------------------")

    if todo_dict:
        print("\n--------------------- To-Do List ---------------------")
        for topic in todo_dict.keys():
            print("{} ({}) => {}".format(topic, len(todo_dict[topic]), (", ").join(todo_dict[topic])))
        print("------------------------------------------------------")
