
    # prints the menu to the terminal that servers as the main interface to the user.
    # all the options listed are the ones that are valid to choose from.
    # not all actions can be made towards particular columns, so exceptions must be raised to prevent errors.    
    def menu(self):
        ans = 0
        ##############################[ User Actions ]##############################
        while(ans != 3):
            valid = False
            options = ['Load Data', 'Exploring Data', 'Data Analysis', 'Quit']
            options_length = len(options)

            exploring_options = ['List All Columns', 'Drop Columns', 'Describe Columns', 
                'Search Element in Column', 'Count Distinct Value', 'Sort Column', 
                'Print first 100, 1000, or 5000 Rows', 'Back to Main Menu']
            exploring_options_length = len(exploring_options)

            try: 
                print(MAKE_BLUE, '\nMain Menu:\n**********', RESET)

                for i in range(options_length):
                    print(MAKE_BLUE, '(', i+1, ') ', options[i], RESET)

                while(valid == False):
                    print(MAKE_CYAN, '\nWhat would you like to do? (1 - '+ str(options_length) +'): ', RESET)
                    ans = int(input())
                    if ans < 1 or ans > options_length:
                        print(MAKE_RED, 'Number given isn\'t valid, please try again', RESET)
                    else:
                        valid = True
                # this is so that the answer follows the list counting system which starts at 0
                ans -= 1

                ##############################[ User Actions ]##############################

                # Load Data Set
                if ans == 0:
                    print(MAKE_BLUE, '\nLoad data set:\n**************', RESET)

                    self.filename = self.file_input()
                    time = self.get_time()
                    total_time = self.load_file(self.filename)

                    time = self.get_time()
                    total_columns = len(self.columns_as_lists)
                    print(MAKE_GREEN, "[", time, "] Total Columns Read: ", total_columns, RESET)

                    time = self.get_time()
                    total_rows = len(self.columns_as_lists[0])
                    print(MAKE_GREEN, "[", time, "] Total Rows Read: ", total_rows, RESET)

                    print(MAKE_YELLOW, "File loaded successfully! time to load ", total_time, RESET)

                # Exploring Data
                
                
                
###############################################################################################################################                
############################# INCLUDED  and self.filename != "" ###############################################################
###############################################################################################################################
                if ans == 1 and self.filename != "":
                    print('\n')
                    choice = 0
                    while(choice != 7):
                        valid = False
                        print(MAKE_BLUE, '\n(', ans+1, ') ', options[ans], ':\n************************', RESET)

                        for i in range(exploring_options_length):
                            print(MAKE_BLUE, '(', i+1, ') ', exploring_options[i], RESET)

                        while(valid == False):
                            print(MAKE_CYAN, '\nWhat would you like to do? (1 - '+ str(exploring_options_length) +'): ', RESET)
                            choice = int(input())

                            if choice < 1 or choice > exploring_options_length:
                                print(MAKE_RED, 'Number given isn\'t valid, please try again', RESET)
                            else:
                                valid = True

                        choice -= 1
                        
                        # list all columns
                        if choice == 0:
                            print(MAKE_BLUE, '\n(', choice+1, ') ', exploring_options[choice], ': ****************', RESET)

                            self.print_column_names()
                        
                        # drop columns
                        if choice == 1:
                            print(MAKE_BLUE, '\n(', choice+1, ') ', exploring_options[choice], ': \n****************', RESET)

                            if self.size <= 1:
                                raise Exception("At least 1 column must remain in the dataset.")
                            
                            option = 0
                            self.print_column_names()

                            while option < 1 or option > self.size:
                                print(MAKE_CYAN, "Enter a column to drop (1 - "+ str(self.size) +"): ", RESET)
                                option = int(input())

                            column_dropped_header = self.columns_as_lists[option-1][0]
                            self.drop_column(option)

                            print(MAKE_GREEN, 'Column', column_dropped_header, 'was dropped.', RESET)
                        
                        # describe columns
                        if choice == 2:
                            print(MAKE_BLUE, '\n(', choice+1, ') ', exploring_options[choice], ': \n**********************', RESET)
                            
                            option = self.choose_column()

                            chosen_column_header = self.columns_as_lists[option][0]
                            self.list_for_chosen_column(option)

                            time = self.get_time()
                            start = time
                            print(MAKE_GREEN, "[", time, "]", chosen_column_header, RESET)
                            print(MAKE_GREEN, "\nColumn Stats:\n==============", RESET)

                            print(MAKE_GREEN, "Count: ", len(self.chosen_column), RESET)
                            print(MAKE_GREEN, "Unique: ", self.unique(self.chosen_column), RESET)

                            mean = self.mean(self.chosen_column)
                            if mean == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine mean.', RESET)
                            else:
                                print(MAKE_GREEN, "Mean: ", mean, RESET)

                            median = self.median(self.chosen_column)
                            if median == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine median.', RESET)
                            else:
                                print(MAKE_GREEN, "Median: ", median, RESET)

                            mode = self.mode(self.chosen_column)
                            if mode == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine mode.', RESET)
                            else:
                                print(MAKE_GREEN, "Mode: ", mode, RESET)

                            sd = self.standard_deviation(self.chosen_column)
                            if sd == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine standard deviation.', RESET)
                            else:
                                print(MAKE_GREEN, "Standard Deviation (SD): ", sd, RESET)
                            
                            variance = self.variance(self.chosen_column)
                            if variance == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine variance.', RESET)
                            else:
                                print(MAKE_GREEN, "Variance: ", variance, RESET)

                            min = self.minimum(self.chosen_column)
                            if min == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine minimum.', RESET)
                            else:
                                print(MAKE_GREEN, "Minimum: ", min, RESET)    

                            max = self.maximum(self.chosen_column)
                            if max == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine maximum.', RESET)
                            else:
                                print(MAKE_GREEN, "Maximum: ", max, RESET)   

                            per20 = self.percentile_20(self.chosen_column)
                            if per20 == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine 20th percentile.', RESET)
                            else:
                                print(MAKE_GREEN, "20 Percentile (P20): ", per20, RESET)   

                            per40 = self.percentile_40(self.chosen_column)
                            if per40 == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine 40th percentile.', RESET)
                            else:
                                print(MAKE_GREEN, "40 Percentile (P40): ", per40, RESET)

                            per50 = self.percentile_50(self.chosen_column)
                            if per50 == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine 50th percentile.', RESET)
                            else:
                                print(MAKE_GREEN, "50 Percentile (P50): ", per50, RESET)

                            per60 = self.percentile_60(self.chosen_column)
                            if per60 == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine 60th percentile.', RESET)
                            else:
                                print(MAKE_GREEN, "60 Percentile (P60): ", per60, RESET)

                            per80 = self.percentile_80(self.chosen_column)
                            if per80 == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine 80th percentile.', RESET)
                            else:
                                print(MAKE_GREEN, "80 Percentile (P80): ", per80, RESET)

                            end = self.get_time()

                            total_time = end - start
                            print(MAKE_YELLOW, "Stats printed successfully! time to process is ", total_time, RESET)

                        # search element in column
                        if choice == 3:
                            print(MAKE_BLUE, '(', choice+1, ') ', exploring_options[choice], '\n****************', RESET)
                            
                            option = self.choose_column()

                            chosen_column_header = self.columns_as_lists[option][0]
                            for i in range(self.size):
                                if i == option:
                                    print(MAKE_CYAN, 'The distinct values of', self.columns_as_lists[i][0], 'are: ', RESET)
                                    distinct_list = self.unique(self.columns_as_lists[i][1:])

                                    for value in distinct_list:
                                        print(MAKE_MAGENTA, value, RESET)

                            self.list_for_chosen_column(option)
                            count = 0

                            print(MAKE_CYAN, 'Enter element to Search: \n', RESET)
                            value = input()
                            start = self.get_time()
                            # three for loops with try blocks so that ints, floats, and strings
                            # will be counted
                            for i in range(len(self.chosen_column)):   
                                try:
                                    if int(value) == self.chosen_column[i]:
                                        count += 1
                                except:
                                    break

                            if count < 1:
                                for i in range(len(self.chosen_column)):
                                    try:
                                        if float(value) == self.chosen_column[i]:
                                            count += 1
                                    except:
                                        break
                            if count < 1:
                                for i in range(len(self.chosen_column)):
                                    try:
                                        if value == self.chosen_column[i]:
                                            count += 1
                                    except:
                                        break
                            
                            end = self.get_time()
                            total_time = end - start
                            if count > 0:
                                print(MAKE_GREEN, '[', total_time, ']', value, 'was found', count, 'times.', RESET)
                                print(MAKE_YELLOW, 'Search was successful! time to search was ', total_time, RESET)
                            else:
                                print(MAKE_RED, '[', time, '] Element was not found, search unsuccessful', RESET)
                            
                            print('\n')

                        # count distinct value
                        if choice == 4:
                            print(MAKE_BLUE, '(', choice+1, ') ', exploring_options[choice], ':\n******************************', RESET)

                            option = self.choose_column()

                            total_time, distinct_value, count = self.count_distinct_value(option)
                            time = self.get_time()

                            if count > 0:
                                print(MAKE_GREEN, '[', time, '] The amount of times', distinct_value, 'is in the data is', count, 'time(s).', RESET)
                                print(MAKE_YELLOW, 'Total time to count distinct value ', total_time, RESET)
                            else:
                                print(MAKE_RED, '[', time, '] Element was not found in data', RESET)
                        
                        # sort column
                        if choice == 5:
                            print(MAKE_BLUE, '(', choice+1, ') ', exploring_options[choice], ':\n********************', RESET)

                            num = self.choose_column()
                            self.sort_column(num)
                        
                        # print first 100, 1000, or 5000 rows
                        if choice == 6:
                            print(MAKE_BLUE, '(', choice+1, ') ', exploring_options[choice], ':\n********************', RESET)

                            self.print_rows()


                #analysis
                
                
                
###############################################################################################################################                
############################# INCLUDED  and self.filename != "" ###############################################################
###############################################################################################################################
                if ans == 2 and self.filename != "":
                    print(MAKE_BLUE, '(', ans+1, ') ', exploring_options[ans], ':\n******************************', RESET)
                    self.print_analysis()
#########################################################################################################################



                if ans == 3:
                    print(MAKE_MAGENTA, '\nThank you for testing our program! :)\n', RESET)
                    
                    
#########################################################################################################################                    
################ NEW IF STATEMENT ERROR MESSAGE #########################################################################
#########################################################################################################################
                if ans > 0 and ans < 3 and self.filename == "":
                    print(MAKE_RED, "LOAD DATA REQUIRED", RESET)
#########################################################################################################################




            except ValueError:
                print(MAKE_RED, 'The column you chose does not include integers or floats for this action.', RESET)

            except Exception as ex:
                print(MAKE_RED, ex, RESET)


    
