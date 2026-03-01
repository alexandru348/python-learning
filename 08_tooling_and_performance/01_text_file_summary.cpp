// 01_text_file_summary.cpp

// This file is a tool for creating a summary who displays the total number of lines, the number of blank lines and the number of characters without spaces

#include<iostream> // for input and output
#include<fstream> // for working with files
#include<string> // for working with sequence of characters
#include<filesystem> // for working with folder / file paths

using namespace std; // for not writing the long form of std
namespace fs = std::filesystem; // alternative name for working with folder / file paths

int main() // the declaration of main function
{
    string file_path; // the file path as a sequence of characters

    cout << "Text file path (Enter = sample.txt): "; // display this text in the console, the user enters the path from the keyboard
    getline(cin, file_path); // read the input and store it into a variable

    if (file_path == "") // if the user didn't enter the file path
    {
        file_path = "sample.txt"; // set the file path
    }

    fs::path path(file_path); // file path
    cout << "file = " << path << endl; // display the file path in the console and move to the next line
    cout << "resolved = " << fs::absolute(path) << endl; // display the complete path in the console, and move to the next line
    cout << endl; // move to the next line

    if (fs::exists(path)) // if the file exists
    {
        cout << "This file exists." << endl; // display this text in the console and move to the next line
    }
    else  // if the file doesn't exist
    {
        cout << "This file does not exist." << endl; // display this text in the console and move to the next line
        return 0; // stop the program
    }
    if (fs::is_regular_file(path)) // if it is a file
    {
        cout << "This is a text file." << endl; // display this text in the console and move to the next line
    }
    else // if it is not a file
    {
        cout << "This path exists, but it is not a file." << endl; // display this text in the console and move to the next line
        return 0; // stop the program
    }
    cout << endl; // move to the next line

    ifstream fin(path); // opening the file for reading

    if (!fin.is_open()) // if the file couldn't be opened
    {
        cout << "The file could not be opened." << endl; // display this text in the console and move to the next line
    }
    else // if the file could be opened successfully
    {
        cout << "The file was opened successfully." << endl; // display this text in the console and move to the next line
    }
    cout << endl; // move to the next line

    string line; // line as a sequence of characters
    int line_count = 0; // the declaration of line counting
    int empty_line_count = 0; // the declaration of the empty line counting
    int char_count = 0; // the declaration of character counting

    while (getline(fin, line)) // read a line from the file and store it into a variable
    {
        line_count++; // line counting

        if (line.empty()) // if the line is empty
        {
            empty_line_count++; // empty line counting
        }
        for (int i = 0; i < line.size(); i++) // loop through the characters
        {
            if (line[i] != ' ') // if the character is not a space
            {
                char_count++; // counting characters without spaces
            }
        }
    }

    fin.close(); // closing the file

    cout << "Text file summary:" << endl; // display this text in the console and move to the next line
    cout << "Total lines: " << line_count << endl; // display this text in the console and move to the next line
    cout << "Empty lines: " << empty_line_count << endl; // display this text in the console and move to the next line
    cout << "Total characters: " << char_count << endl; // display this text in the console and move to the next line

    return 0; // stop the program
}