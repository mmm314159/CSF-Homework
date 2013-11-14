# Name: Branddon Gordon
# Evergreen Login: Gorbra14
# Programming as a Way of Life
# Homework 5: Election prediction

import csv
import os
import time

def read_csv(path):
    """
    Reads the CSV file at path, and returns a list of rows. Each row is a
    dictionary that maps a column name to a value in that column, as a string.
    """
    output = []
    for row in csv.DictReader(open(path)):
        output.append(row)
    return output


################################################################################
# Problem 1: State edges
################################################################################

def row_to_edge(row):
    """
    Given an election result row or poll data row, returns the Democratic edge
    in that state.
    """
    return float(row["Dem"]) - float(row["Rep"])  

def state_edges(election_result_rows):
    
    """
    Given a list of election result rows, returns state edges.
    The input list does has no duplicate states;
    that is, each state is represented at most once in the input list.
    """

    print{((election_result_rows)[0]['State']) : (row_to_edge((election_result_rows)[0])) , 
    ((election_result_rows)[1]['State']) : (row_to_edge((election_result_rows)[1])) , 
    ((election_result_rows)[2]['State']) : (row_to_edge((election_result_rows)[2])) , 
    ((election_result_rows)[3]['State']) : (row_to_edge((election_result_rows)[3])) , 
    ((election_result_rows)[4]['State']) : (row_to_edge((election_result_rows)[4])) , 
    ((election_result_rows)[5]['State']) : (row_to_edge((election_result_rows)[5])) , 
    ((election_result_rows)[6]['State']) : (row_to_edge((election_result_rows)[6])) , 
    ((election_result_rows)[7]['State']) : (row_to_edge((election_result_rows)[7])) , 
    ((election_result_rows)[8]['State']) : (row_to_edge((election_result_rows)[8])) , 
    ((election_result_rows)[9]['State']) : (row_to_edge((election_result_rows)[9])) , 
    ((election_result_rows)[10]['State']) : (row_to_edge((election_result_rows)[10])) , 
    ((election_result_rows)[11]['State']) : (row_to_edge((election_result_rows)[11])) , 
    ((election_result_rows)[12]['State']) : (row_to_edge((election_result_rows)[12])) , 
    ((election_result_rows)[13]['State']) : (row_to_edge((election_result_rows)[13])) , 
    ((election_result_rows)[14]['State']) : (row_to_edge((election_result_rows)[14])) , 
    ((election_result_rows)[15]['State']) : (row_to_edge((election_result_rows)[15])) , 
    ((election_result_rows)[16]['State']) : (row_to_edge((election_result_rows)[16])) , 
    ((election_result_rows)[17]['State']) : (row_to_edge((election_result_rows)[17])) , 
    ((election_result_rows)[18]['State']) : (row_to_edge((election_result_rows)[18])) , 
    ((election_result_rows)[19]['State']) : (row_to_edge((election_result_rows)[19])) , 
    ((election_result_rows)[20]['State']) : (row_to_edge((election_result_rows)[20])) , 
    ((election_result_rows)[21]['State']) : (row_to_edge((election_result_rows)[21])) , 
    ((election_result_rows)[22]['State']) : (row_to_edge((election_result_rows)[22])) , 
    ((election_result_rows)[23]['State']) : (row_to_edge((election_result_rows)[23])) , 
    ((election_result_rows)[24]['State']) : (row_to_edge((election_result_rows)[24])) , 
    ((election_result_rows)[25]['State']) : (row_to_edge((election_result_rows)[25])) , 
    ((election_result_rows)[26]['State']) : (row_to_edge((election_result_rows)[26])) , 
    ((election_result_rows)[27]['State']) : (row_to_edge((election_result_rows)[27])) , 
    ((election_result_rows)[28]['State']) : (row_to_edge((election_result_rows)[28])) , 
    ((election_result_rows)[29]['State']) : (row_to_edge((election_result_rows)[29])) , 
    ((election_result_rows)[30]['State']) : (row_to_edge((election_result_rows)[30])) , 
    ((election_result_rows)[31]['State']) : (row_to_edge((election_result_rows)[31])) , 
    ((election_result_rows)[32]['State']) : (row_to_edge((election_result_rows)[32])) , 
    ((election_result_rows)[33]['State']) : (row_to_edge((election_result_rows)[33])) , 
    ((election_result_rows)[34]['State']) : (row_to_edge((election_result_rows)[34])) , 
    ((election_result_rows)[35]['State']) : (row_to_edge((election_result_rows)[35])) , 
    ((election_result_rows)[36]['State']) : (row_to_edge((election_result_rows)[36])) , 
    ((election_result_rows)[37]['State']) : (row_to_edge((election_result_rows)[37])) , 
    ((election_result_rows)[38]['State']) : (row_to_edge((election_result_rows)[38])) , 
    ((election_result_rows)[39]['State']) : (row_to_edge((election_result_rows)[39])) , 
    ((election_result_rows)[40]['State']) : (row_to_edge((election_result_rows)[40])) , 
    ((election_result_rows)[41]['State']) : (row_to_edge((election_result_rows)[41])) , 
    ((election_result_rows)[42]['State']) : (row_to_edge((election_result_rows)[42])) , 
    ((election_result_rows)[43]['State']) : (row_to_edge((election_result_rows)[43])) , 
    ((election_result_rows)[44]['State']) : (row_to_edge((election_result_rows)[44])) , 
    ((election_result_rows)[45]['State']) : (row_to_edge((election_result_rows)[45])) , 
    ((election_result_rows)[46]['State']) : (row_to_edge((election_result_rows)[46])) , 
    ((election_result_rows)[47]['State']) : (row_to_edge((election_result_rows)[47])) , 
    ((election_result_rows)[48]['State']) : (row_to_edge((election_result_rows)[48])) , 
    ((election_result_rows)[49]['State']) : (row_to_edge((election_result_rows)[49])) , 
    ((election_result_rows)[50]['State']) : (row_to_edge((election_result_rows)[50]))}
    


################################################################################
# Problem 2: Find the most recent poll row
################################################################################

def earlier_date(date1, date2):
    """
    Given two dates as strings (formatted like "Oct 06 2012"), returns True if 
    date1 is after date2.
    """
    return (time.strptime(date1, "%b %d %Y") < time.strptime(date2, "%b %d %Y"))

def most_recent_poll_row(poll_rows, pollster, state):
    """
    Given a list of poll data rows, returns the most recent row with the
    specified pollster and state. If no such row exists, returns None.
    """
    #TODO: Implement this function
    pass


################################################################################
# Problem 3: Pollster predictions
################################################################################

def unique_column_values(rows, column_name):
    """
    Given a list of rows and the name of a column (a string), returns a set
    containing all values in that column.
    """
    #TODO: Implement this function
    pass

def pollster_predictions(poll_rows):
    """
    Given a list of poll data rows, returns pollster predictions.
    """
    #TODO: Implement this function
    pass

            
################################################################################
# Problem 4: Pollster errors
################################################################################

def average_error(state_edges_predicted, state_edges_actual):
    """
    Given predicted state edges and actual state edges, returns
    the average error of the prediction.
    """
    #TODO: Implement this function
    pass

def pollster_errors(pollster_predictions, state_edges_actual):
    """
    Given pollster predictions and actual state edges, retuns pollster errors.
    """
    #TODO: Implement this function
    pass


################################################################################
# Problem 5: Pivot a nested dictionary
################################################################################

def pivot_nested_dict(nested_dict):
    """
    Pivots a nested dictionary, producing a different nested dictionary
    containing the same values.
    The input is a dictionary d1 that maps from keys k1 to dictionaries d2,
    where d2 maps from keys k2 to values v.
    The output is a dictionary d3 that maps from keys k2 to dictionaries d4,
    where d4 maps from keys k1 to values v.
    For example:
      input = { "a" : { "x": 1, "y": 2 },
                "b" : { "x": 3, "z": 4 } }
      output = {'y': {'a': 2},
                'x': {'a': 1, 'b': 3},
                'z': {'b': 4} }
    """
     #TODO: Implement this function
    pass


################################################################################
# Problem 6: Average the edges in a single state
################################################################################

def average_error_to_weight(error):
    """
    Given the average error of a pollster, returns that pollster's weight.
    The error must be a positive number.
    """
    return error ** (-2)

# The default average error of a pollster who did no polling in the
# previous election.
DEFAULT_AVERAGE_ERROR = 5.0

def pollster_to_weight(pollster, pollster_errors):
    """"
    Given a pollster and a pollster errors, return the given pollster's weight.
    """
    if pollster not in pollster_errors:
        weight = average_error_to_weight(DEFAULT_AVERAGE_ERROR)
    else:
        weight = average_error_to_weight(pollster_errors[pollster])
    return weight


def weighted_average(items, weights):
    """
    Returns the weighted average of a list of items.
    
    Arguments:
    items is a list of numbers.
    weights is a list of numbers, whose sum is nonzero.
    
    Each weight in weights corresponds to the item in items at the same index.
    items and weights must be the same length.
    """
    assert len(items) > 0
    assert len(items) == len(weights)
    #TODO: Implement this function
    pass


def average_edge(pollster_edges, pollster_errors):
    """
    Given pollster edges and pollster errors, returns the average of these edges
    weighted by their respective pollster errors.
    """
    #TODO: Implement this function
    pass

    
################################################################################
# Problem 7: Predict the 2012 election
################################################################################

def predict_state_edges(pollster_predictions, pollster_errors):
    """
    Given pollster predictions from a current election and pollster errors from
    a past election, returns the predicted state edges of the current election.
    """
    #TODO: Implement this function
    pass
    

################################################################################
# Electoral College, Main Function, etc.
################################################################################

def electoral_college_outcome(ec_rows, state_edges):
    """
    Given electoral college rows and state edges, returns the outcome of
    the Electoral College, as a map from "Dem" or "Rep" to a number of
    electoral votes won.  If a state has an edge of exactly 0.0, its votes
    are evenly divided between both parties.
    """
    ec_votes = {}               # maps from state to number of electoral votes
    for row in ec_rows:
        ec_votes[row["State"]] = float(row["Electors"])

    outcome = {"Dem": 0, "Rep": 0}
    for state in state_edges:
        votes = ec_votes[state]
        if state_edges[state] > 0:
            outcome["Dem"] += votes
        elif state_edges[state] < 0:
            outcome["Rep"] += votes
        else:
            outcome["Dem"] += votes/2.0
            outcome["Rep"] += votes/2.0
    return outcome


def print_dict(dictionary):
    """
    Given a dictionary, prints its contents in sorted order by key.
    Rounds float values to 8 decimal places.
    """
    for key in sorted(dictionary.keys()):
        value = dictionary[key]
        if type(value) == float:
            value = round(value, 8)
        print key, value


def main():
    """
    Main function, which is executed when election.py is run as a Python script.
    """
    # Read state edges from the 2008 election
    edges_2008 = state_edges(read_csv("data/2008-results.csv"))
    
    # Read pollster predictions from the 2008 and 2012 election
    polls_2008 = pollster_predictions(read_csv("data/2008-polls.csv"))
    polls_2012 = pollster_predictions(read_csv("data/2012-polls.csv"))
    
    # Compute pollster errors for the 2008 election
    error_2008 = pollster_errors(polls_2008, edges_2008)
    
    # Predict the 2012 state edges
    prediction_2012 = predict_state_edges(polls_2012, error_2008)
    
    # Obtain the 2012 Electoral College outcome
    ec_2012 = electoral_college_outcome(read_csv("data/2012-electoral-college.csv"),
                                        prediction_2012)
    
    print "Predicted 2012 election results:"
    print_dict(prediction_2012)
    print
    
    print "Predicted 2012 Electoral College outcome:"
    print_dict(ec_2012)
    print    


# If this file, election.py, is run as a Python script (such as by typing
# "python election.py" at the command shell), then run the main() function.
if __name__ == "__main__":
    main()
