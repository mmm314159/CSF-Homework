# Name: Branddon Gordon
# Evergreen Login: Gorbra14
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)
# Homework 4: DNA analysis (Part 2)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)



# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0



for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of GC and AT base pairs
gc_count = 0
at_count = 0
# Number of individual A,C,G and T nucleotides
a_count = 0
c_count = 0
g_count = 0
t_count = 0


# for each base pair in the string,
for bp in seq:
           
    if bp == 'A':
        a_count = a_count + 1
        at_count = at_count + 1
        total_count = total_count + 1
    elif bp == 'C':
        c_count = c_count + 1
        gc_count = gc_count + 1
        total_count = total_count + 1
    elif bp == 'G':
        g_count = g_count + 1
        gc_count = gc_count + 1
        total_count = total_count + 1
    elif bp == 'T':
        t_count = t_count + 1
        at_count = at_count + 1
        total_count = total_count + 1


# divide the gc_count by the total_count
gc_content = float(gc_count) / float(total_count)
at_content = float(at_count) / float(total_count)
acgt_ratio = float(at_count) / float(gc_count)


# Print the answer
print 'GC-content:', gc_content
print 'AT-content:', at_content
print 'A-count:', a_count
print 'C-count:', c_count
print 'G-count:', g_count
print 'T_count:', t_count
print 'Sum count of A, C, G, T:', a_count+c_count+g_count+t_count
print 'Total count:', total_count
print 'Seq length:', len(seq)
print 'AT/GC ratio:', acgt_ratio



    
if gc_content > 0.6:
    print 'High GC content'

elif gc_content < 0.4:
    print 'Low GC content:'
        
else:
    print 'Moderate GC content'


