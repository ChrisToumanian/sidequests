import random

class Magic8Ball:
    @staticmethod
    def toss():
        responses = [
            "IT IS CERTAIN",
            "IT IS DECIDEDLY SO",
            "WITHOUT A DOUBT",
            "YES DEFINITELY",
            "YOU MAY RELY ON IT",
            "AS I SEE IT, YES",
            "MOST LIKELY",
            "OUTLOOK GOOD",
            "YES",
            "SIGNS POINT TO YES",
            "REPLY HAZY, TRY AGAIN",
            "ASK AGAIN LATER",
            "BETTER NOT TELL YOU NOW",
            "CANNOT PREDICT NOW",
            "CONCENTRATE AND ASK AGAIN",
            "DON'T COUNT ON IT",
            "MY REPLY IS NO",
            "MY SOURCES SAY NO",
            "OUTLOOK NOT SO GOOD",
            "VERY DOUBTFUL"
        ]
        answer = random.randint(0,19)
        response = responses[answer]
        
        return response
