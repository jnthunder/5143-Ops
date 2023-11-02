"""The sort command is a tool for sorting file contents and printing the result in standard output. Reordering a file's contents numerically 
    or alphabetically and arranging information in ascending or descending order.
    commad sort [flag] filename has flags...   
"""
import csv

#will perform an alphanumerical sort in ascending/descending
# order if no flags are given
def sort(**kwargs):
    # Load data 
    lists = list()
    #filename = ""
    filename = kwargs.get('params')

    # for n in fn:
    #     filename += n

    #print(filename[0])

    if filename == 0:
        with open(filename[0], 'r') as f:
            for line in f:
                lists.append(line.rstrip().split())
                return lists
        
    else:
        print(filename[0])
        with open(filename[0], 'r') as f:
            for line in f:
                lists.append(line.rstrip().split())

                # Sort data
                results = sorted(lists)
                # Write to a file
                with open(filename[1], 'w') as f:
                    writer = csv.writer(f, delimiter='\t')
                    writer.writerows(results)
                    return writer
    
    # Sort data
    #Iterable required. The sequence to sort, list, dictionary, tuple etc.
    #sorted(iterable, 
    # key= Optional. A Function to execute to decide the order. 
    # Default is None, 
    # reverse= Optional. A Boolean. False will sort ascending, True will sort descending. 
    # Default is False)
#     return sorted(lists)

# #sort prints std output, unless specified to print to file 
# def sortToFile(infilename, outfilename):
#     # Load data 
#     lists = list()

#     with open(infilename, 'r') as f:
#         for line in f:
#             lists.append(line.rstrip().split())

#     # Sort data
#     results = sorted(lists)
#     # Write to a file
#     with open(outfilename, 'w') as f:
#         writer = csv.writer(f, delimiter='\t')
#         writer.writerows(results)
