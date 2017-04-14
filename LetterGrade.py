#!/usr/bin/python
# -*- coding: UTF-8 -*-
def average(numbers):
    '''
    Method to calc the average between a list of numbers.
    :param numbers: List of numbers
    :return: return a integer with the average.
    '''
    total = sum(numbers)
    total = float(total)
    average = total / len(numbers)
    return (average)

def getAverage(student):
    """
    Method to calc the weight of each average and sum it.
    :param student: A dictionary with all grades schollar of a student
    :return: return the final average of a student.
    """
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return (0.1 * homework) + (0.3 * quizzes) + (0.6 * tests)

def getLetterGrade(score):
    """
    Method to return the letter grade schollar of a student.
    :param score: A integer with the final grade schollar of a student.
    :return: return the final letter grade schollar.
    """
    if score >= 90:
        finalScore = 'A'
    elif score >= 80:
        finalScore = 'B'
    elif score >= 70:
        finalScore = 'C'
    elif score >= 60:
        finalScore = 'D'
    else:
        finalScore = 'F'
    return finalScore

def getClassAverage(students):
    """
    Method to get the average of the final grade schollar of all students in the classroom
    :param students: A Dictionary of students with all grades schollar
    :return: return the classroom average
    """
    results = []
    for student in students:
        results.append(getAverage(student))
    return average(results)