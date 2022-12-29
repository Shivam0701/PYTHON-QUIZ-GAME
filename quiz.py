print("WELCOME TO mYqUiZ")
name=input("Type your name here: ")
start=input("Do you want to start the QUIZ? YES/NO: ")
if start=="yes" or start=="YES":
    print("ROUND:1,SPORTS ROUND")
    Q1="""Durand Cup is associated with?
    A.Swimming
    B.Foot ball
    C.TableTennis
    D. Hockey"""
    Q2="""Which among the following games was previously known as Mintonette?
    A.foot ball
    B.base ball
    C.volley ball
    D.hand  ball"""
    Q3="""Which country does Allyson Felix belong to?
    A.US
    B.Jamaica
    C.Kenya
    D. Nigeria"""
    Q4="""What is the duration of a Test Match?
    A.3days
    B.4days
    C.1day
    D.5days"""
    Q5="""Who is regarded as the most successful Indian test captain of Indian Cricket team?
    A.ViratKohli
    B.SunilGavaskar
    C.MSDhoni
    D.Sachin Tendulkar"""
    score=0
    questions={Q1:"B",Q2:"C",Q3:"A",Q4:"D",Q5:"C"}
    for i in questions:
        print(i)
        ans=input("enter you answer (A/B/C/D): ")
        if ans==questions[i]:
            score+=1
            print("correct",name,"your  current score is",score)
        else:
            print("OH ho! incorrect",name,"your current score is:",score)
    print("your score till now is: ",score)
    ROUND2=input("ARE YOU READY FOR THE NEXT ROUND?(yes/no) ")
    if ROUND2=="YES" or ROUND2=="yes":
        print("ROUND:2,PYTHON ROUND")
        Q6='''Who developed Python Programming Language?
        A. Wick van Rossum
        B. Rasmus Lerdorf
        C. Guido van Rossum
        D. Niene Stom'''

        Q7='''Which type of Programming does Python support?
        A. object-oriented programming
        B. structured programming
        C. functional programming
        D. all of the mentioned'''

        Q8=''' Is Python case sensitive when dealing with identifiers?
        A. no
        B. yes
        C. machine dependent
        D. none of the mentioned'''

        Q9= '''Which of the following is the correct extension of the Python file?
        A. .python
        B. .pl
        C. .py
        D. .p'''

        Q10='''Is Python code compiled or interpreted?
        A. Python code is both compiled and interpreted
        B. Python code is neither compiled nor interpreted
        C. Python code is only compiled
        D. Python code is only interpreted'''
        questions={Q6:"C",Q7:"D",Q8:"A",Q9:"C",Q10:"B"}
        for i in questions:
            print(i)
            ans=input("enter you answer (A/B/C/D): ")
            if ans==questions[i]:
                score+=1
                print("correct",name,"your  current score is",score)
            else:
                print("OH ho! incorrect",name,"your current score is:",score)
        print("your score till now is: ",score)
        ROUND3=input("ARE YOU READY FOR THE NEXT ROUND?(yes/no) ")
        if ROUND3=="YES" or ROUND3=="yes":
            print("ROUND:3,CURRENT AFFAIRS ROUND")
            Q11='''“Blue Book”, which was seen in the news, is the manual of which armed force/group?
            A. Central Reserve Police Force    
            B. Special Protection Group
            C. National Security Guard
            D. Indian Coast Guard'''
            Q12='''Which state/UT recognised Takht Damdama Sahib, as the fifth Takht of Sikhs?
            A. Punjab
            B. Delhi
            C. Bihar
            D. Uttar Pradesh'''
            Q13='''A new species of dwarf catfish named ‘Pseudolaguvia vespa’ was discovered in Milak River in which state?
            A. Assam
            B. Nagaland
            C. West Bengal
            D. Bihar'''
            Q14='''Who is the head of the committee set up by Union Home Ministry, to probe on Prime Minister’s Security Lapse?
            A. Sudhir Kumar Saxena
            B. Ajay Bushan Pandey
            C. Surjit Bhalla
            D. Ranjan Gogoi'''
            Q15='''Which state signed agreement with ‘National Dairy Development Board’ to create a Rs 2,000-crore Dairy joint venture?
            A. Punjab
            B. Assam
            C. Gujarat
            D. Arunachal Pradesh'''
            questions={Q11:"B",Q12:"B",Q13:"B",Q14:"A",Q15:"B"}
            for i in questions:
                print(i)
                ans=input("enter you answer (A/B/C/D): ")
                if ans==questions[i]:
                    score+=1
                    print("correct",name,"your  current score is",score)
                else:
                    print("OH ho! incorrect",name,"your current score is:",score)
            print("your score till now is: ",score)
            ROUND4=input("ARE YOU READY FOR THE NEXT ROUND?(yes/no) ")
            if ROUND4=="yes" or ROUND4=="YES":
                print("ROUND:4,ENVIRONMENTAL SCIENCE ROUND")
                Q16='''Which of these layers of the atmosphere consists of the ozone layer that is responsible for absorbing the Ultra-Violet (UV) light?
                A.Troposphere
                B.Mesosphere
                C.Stratosphere
                D.None of these'''
                Q17='''Which of these are essential non-metallic minerals?
                A.Coal, silica, clay, cement
                B.Iron, copper, aluminium, zinc
                C.Gold, platinum, silver
                D.Granite, limestone, marble'''
                Q18='''What is the estimated percentage of forest land that India should ideally have?
                A.15%
                B. 50%
                C. 44%
                D.33%'''
                Q19='''An extensive number of chains interlinked in an ecosystem forms a __________ together.
                A. Food chain
                B. Food web
                C.Carbon cycle
                D.Nitrogen cycle'''
                Q20=''' Which of these elements is considered to be the largest source of commercial energy consumption in the world?
                A. Nuclear
                B.Natural gas
                C.Oil
                D.Coal'''
                questions={Q16:"C",Q17:"A",Q18:"D",Q19:"B",Q20:"C"}
                for i in questions:
                    print(i)
                    ans=input("enter you answer (A/B/C/D): ")
                    if ans==questions[i]:
                        score+=1
                        print("correct",name,"your  current score is",score)
                    else:
                        print("OH ho! incorrect",name,"your current score is:",score)
                print("your score till now is: ",score)
                ROUND5=input("ARE YOU READY FOR THE NEXT ROUND?(yes/no) ")
                if ROUND5=="yes" or ROUND4=="YES":
                    print("ROUND:5,FOURIER SERIES ROUND")
                    Q21='''At the point of discontinuity, sum of the series is equal to ___________
                    A. 12[f(x+0)–f(x−0)]
                    B. 12[f(x+0)+f(x−0)]
                    C. 14[f(x+0)–f(x−0)]
                    D. 14[f(x+0)+f(x−0)]'''
                    Q22=''' Which of the following is not Dirichlet’s condition for the Fourier series expansion?
                    A. f(x) is periodic, single valued, finite
                    B. f(x) has finite number of discontinuities in only one period
                    C. f(x) has finite number of maxima and minima
                    D. f(x) is a periodic, single valued, finite'''
                    Q23='''4. If the function f(x) is even, then which of the following is zero?
                    A. an
                    b. bn
                    C.a0
                    D. nothing is zero'''
                    Q24='''If the function f(x) is odd, then which of the only coefficient is present?
                    A. an
                    B. bn
                    C. a0
                    D. everything is present'''
                    Q25=''' Find bn if the function f(x) = x2.
                    A. finite value
                    B. infinite value
                    C. zero
                    D. can’t be found'''
                    questions={Q21:"B",Q22:"D",Q23:"B",Q24:"B",Q25:"C"}
                    for i in questions:
                        print(i)
                        ans=input("enter you answer (A/B/C/D): ")
                        if ans==questions[i]:
                            score+=1
                            print("correct",name,"your  current score is",score)
                        else:
                            print("OH ho! incorrect",name,"your current score is:",score)
                    print(name,"your FINAL SCORE is: ",score)
                    print("THANK YOU FOR PLAYING",name)
                else:
                    print("oH hO! NOW YOU HAVE TO RESTART THIS GAME")
            else:
                print("oH hO! NOW YOU HAVE TO RESTART THIS GAME")
        else:
            print("oH hO! NOW YOU HAVE TO RESTART THIS GAME")
    else:
        print("oH hO! NOW YOU HAVE TO RESTART THIS GAME")
else:
    print("oH hO! TYPE YES TO START")
