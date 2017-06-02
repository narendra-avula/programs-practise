__author__ = 'narendra'
'''
Objective
Today, we're delving into Inheritance. Check out the Tutorial tab for learning materials and an instructional video!

Task
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has  parameters:
A string, .
A string, .
An integer, .
An integer array (or vector) of test scores, .
A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:
Grading.png

Input Format

The locked stub code in your editor calls your Student class constructor and passes it the necessary arguments. It also calls the calculate method (which takes no arguments).

You are not responsible for reading the following input from stdin:
The first line contains , , and , respectively. The second line contains the number of test scores. The third line of space-separated integers describes .

Constraints

Output Format

This is handled by the locked stub code in your editor. Your output will be correct if your Student class constructor and calculate() method are properly implemented.

Sample Input

Heraldo Memelli 8135627
2
100 80
Sample Output

 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O
Explanation

This student had  scores to average:  and . The student's average grade is . An average grade of  corresponds to the letter grade , so our calculate() method should return the character'O'.
'''

class Person:

    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber

class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        avg = sum(self.scores) / len(self.scores)
        if avg >= 90:
            return 'O'
        elif avg >= 80:
            return 'E'
        elif avg >= 70:
            return 'A'
        elif avg >= 55:
            return 'P'
        elif avg >= 40:
            return 'D'
        else:
            return 'T'

line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input()) # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()


'''
Java
class Student extends Person {
    private int[] testScores;

    Student(String firstName, String lastName, int identification, int[] scores){
        super(firstName, lastName, identification);
        this.testScores = scores;
    }

    public char calculate() {
        int average = 0;
        for(int i = 0; i < testScores.length; i++){
            average += testScores[i];
        }
        average = average / testScores.length;

        if(average >= 90) {
            return 'O'; // Outstanding
        }
        else if(average >= 80) {
            return 'E'; // Exceeds Expectations
        }
        else if(average >= 70) {
            return 'A'; // Acceptable
        }
        else if(average >= 55) {
            return 'P'; // Poor
        }
        else if(average >= 40) {
            return 'D'; // Dreadful
        }
        else {
            return 'T'; // Troll
        }
    }
}

C++
class Student :  public Person{
    private:
        vector<int> testScores;
    public:
        Student(string firstName, string lastName, int identification, vector<int> scores) : Person(firstName, lastName, identification) {
            this->testScores = scores;
        }

        char calculate() {
            int average = 0;
            for(int i = 0; i < testScores.size(); i++) {
                average += testScores[i];
            }
            average = average / testScores.size();

            if(average >= 90) {
                return 'O'; // Outstanding
            }
            else if(average >= 80) {
                return 'E'; // Exceeds Expectations
            }
            else if(average >= 70) {
                return 'A'; // Acceptable
            }
            else if(average >= 55) {
                return 'P'; // Poor
            }
            else if(average >= 40) {
                return 'D'; // Dreadful
            }
            else {
                return 'T'; // Troll
            }
        }
};
C Sharp
class Student : Person{
    private int[] testScores;

    /*
    *   Class Constructor
    *   Parameters:
    *   firstName - A string denoting the Person's first name.
    *   lastName - A string denoting the Person's last name.
    *   id - An integer denoting the Person's ID number.
    *   scores - An array of integers denoting the Person's test scores.
    */
    public Student(string firstName, string lastName, int identification, int[] scores){
            this.firstName = firstName;
            this.lastName = lastName;
            this.id = identification;
            this.testScores = scores;
    }

    /*
    *   Method Name: Calculate
    *   Return: A character denoting the grade.
    */
    public char Calculate(){
        // Note: Sum() uses the System.Linq import
        int average = testScores.Sum();

        average = average / testScores.Length;

        if(average >= 90){
            return 'O'; // Outstanding
        }
        else if(average >= 80){
            return 'E'; // Exceeds Expectations
        }
        else if(average >= 70){
            return 'A'; // Acceptable
        }
        else if(average >= 55){
            return 'P'; // Poor
        }
        else if(average >= 40){
            return 'D'; // Dreadful
        }
        else{
            return 'T'; // Troll
        }
    }
}
JavaScript
class Student extends Person {

    constructor(firstName, lastName, identification, scores) {
        super(firstName, lastName, identification);
        this.testScores = scores;
    }

    calculate() {
        let average = this.testScores.reduce(
            function(a, b) {
                return a + b
            },
            0
        ) / this.testScores.length

        if (average >= 90) {
            return 'O'
        }
        else if(average >= 80) {
            return 'E'
        }
        else if(average >= 70) {
            return 'A'
        }
        else if(average >= 55) {
            return 'P'
        }
        else if(average >= 40) {
            return 'D'
        }
        else {
            return 'T'
        }
    }
}
Python 2/3
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.testScores = scores

    def calculate(self):
        average = 0
        for i in self.testScores:
            average += i

        average = average / len(self.testScores)

        if(average >= 90):
            return 'O' # Outstanding
        elif(average >= 80):
            return 'E' # Exceeds Expectations
        elif(average >= 70):
            return 'A' # Acceptable
        elif(average >= 55):
            return 'P' # Poor
        elif(average >= 40):
            return 'D' # Dreadful
        else:
            return 'T' # Troll
Ruby
class Student <Person
    def initialize(firstName, lastName, id, scores)
        super(firstName, lastName, id)
        @scores = scores
    end
    def calculate()
        sumScores = 0.to_i
        @scores.each do |x|
            sumScores = sumScores + Integer(x)
        end
        average = sumScores / @scores.count

        if(average >= 90)
            return 'O' # Outstanding
        elsif(average >= 80)
            return 'E' # Exceeds Expectations
        elsif(average >= 70)
            return 'A' # Acceptable
        elsif(average >= 55)
            return 'P' # Poor
        elsif(average >= 40)
            return 'D' # Dreadful
        else
            return 'T' # Troll
        end
    end
end
Swift
// Class Student
class Student: Person {
	var testScores: [Int]

	// Write the Student class initializer
	init(firstName: String, lastName: String, identification: Int, scores: [Int]) {
		self.testScores = scores;
		super.init(firstName: firstName, lastName: lastName, identification: identification);
	}

	// Write the calculate method
	func calculate() -> String {
		var average = 0;
		for i in testScores {
			average += i;
		}
		average = average / testScores.count;

		if(average >= 90) {
			return "O"; // Outstanding
		}
		else if(average >= 80) {
			return "E"; // Exceeds Expectations
		}
		else if(average >= 70) {
			return "A"; // Acceptable
		}
		else if(average >= 55) {
			return "P"; // Poor
		}
		else if(average >= 40) {
			return "D"; // Dreadful
		}
		else {
			return "T"; // Troll
		}
	}

} // End of class Student

'''