#Homework 2 Assignment
constant1 = 1.371
constantminus1 = 0.371

dictCoefficients = {'Vision':              [1, 0.98, 0.89, 0.84, 0.75, 0.61],
                    'Hearing':             [1, 0.95, 0.89,0.8, 0.74, 0.61],
                    'Speech':              [1, 0.94, 0.89, 0.81, 0.68],
                    'Ambulation':          [1, 0.93, 0.86, 0.73, 0.65, 0.58],
                    'Dexterity':           [1, 0.95, 0.88, 0.76, 0.65, 0.56],
                    'Emotion':              [1, 0.95, 0.85, 0.64, 0.46],
                    'Cognition':            [1, 0.92, 0.95, 0.83, 0.6, 0.42],
                    'Pain':                 [1, 0.96, 0.9, 0.77, 0.55]};
#We want to build a specified function that looks @ health of user via the HUI3 chart stuff#

def superhealthyscore (vision, hearing, speech, ambulation, dexterity, emotion, cognition, pain):
#it's important to offer a description noted by 3 quotes. You should understand the code from anywhere
    """
:param vision: A range of abilities from level 1-6, level 1 being healthy vision, level 6 being unable to see at all
:param hearing: A range of abilities from level 1-6, level 1 being healthy hearing, level 6 being unable to hear at all
:param speech: A range of abilities from level 1-5, level 1 being normal speaking ability, level 5 being unable to
be understood at all
:param ambulation: A range of abilities from level 1-6, level 1 being normal walking ability level 6 being unable to
walk at all
:param dexterity: A range of abilities from level 1-6, level 1 being able to fully use 2 hands/ 10 fingers,
level 6 being unable to use fingers independently
:param emotion: A range of abilities from level 1-5, level 5 being unable so happy that life is not worthwhile
:param cognition: A range of abilities from level 1-6, level 1 able to remember most things, level 6 Unable to remember
anything at all, and unable to think or solve day to day problems.
:param pain: A range of abilities from level 1-5, level 1 free of pain and discomfort, level 5 severe pain that prevents most activities.
:return:
"""
    if not(vision in [1,2,3,4,5,6]):
        raise ValueError('Mobility level can take only values between 1-6')
    if not(hearing in [1,2,3,4,5,6]):
        raise ValueError('Self Care level can take only values between 1-6')
    if not(speech in [1,2,3,4,5]):
        raise ValueError('Usual Activity level can take only values between 1-5')
    if not(ambulation in [1,2,3,4,5,6]):
            raise ValueError('Usual Activity level can take only values between 1-6')
    if not(dexterity in [1,2,3,4,5,6]):
            raise ValueError('Usual Activity level can take only values between 1-6')
    if not(emotion in [1,2,3,4,5]):
            raise ValueError('Usual Activity level can take only values between 1-5')
    if not(cognition in [1,2,3,4,5,6]):
                raise ValueError('Usual Activity level can take only values between 1-6')
    if not(pain in [1,2,3,4,5]):
                    raise ValueError('Usual Activity level can take only values between 1-5')
#I could have probably used range here?? But i wasn't sure which values
# would be included or not so just stuck with the class example


#Formula from the website: (Dead - Perfect Health scale)   u* = 1.371 (b1 * b2 * b3 * b4 * b5 * b6 * b7 * b8) - 0.371
#remember to add controls to normalize the data

    multipliedvalue = dictCoefficients['Vision'][vision - 1] \
                    * dictCoefficients['Hearing'][hearing - 1] \
                    * dictCoefficients['Speech'][speech - 1] \
                    * dictCoefficients['Ambulation'][ambulation - 1] \
                    * dictCoefficients['Dexterity'][dexterity - 1] \
                    * dictCoefficients['Emotion'][emotion - 1] \
                    * dictCoefficients['Cognition'][cognition - 1] \
                    * dictCoefficients['Pain'][pain - 1]

    score = constant1 * multipliedvalue - constantminus1
    return score
