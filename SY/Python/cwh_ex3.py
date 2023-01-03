 #Make a program to which works like KBC contest.

import random

questions = [ 
    "The International Literacy Day is observed on \nA. Sep 8 \nB. Nov 28 \nC. May 2 \nD. Sep 22\n",
    "The language of Lakshadweep. a Union Territory of India, is \nA. Tamil \nB. Hindi \nC. Malayalam \nD. Telugu\n",
    "In which group of places the Kumbha Mela is held every twelve years? \nA. Ujjain. Purl; Prayag. Haridwar \nB. Prayag. Haridwar, Ujjain,. Nasik \nC. Rameshwaram. Purl, Badrinath. Dwarika \nD. Chittakoot, Ujjain, Prayag,'Haridwar\n",
    "Bahubali festival is related to \nA. Islam \nB. Hinduism \nC. Buddhism \nD. Jainism\n",
    "Which day is observed as the World Standards  Day? \nA. June 26 \nB. Oct 14 \nC. Nov 15 \nD. Dec 2\n",
    "Which of the following was the theme of the World Red Cross and Red Crescent Day? \nA. 'Dignity for all - focus on women' \nB. Dignity for all - focus on Children' \nC. Focus on health for all' \nD. Nourishment for all-focus on children'\n",
    "September 27 is celebrated every year as \nA. Teachers' Day \nB. National Integration Day \nC. World Tourism Day \nD. International Literacy Day\n",
    "Who is the author of 'Manas Ka-Hans' ? \nA. Khushwant Singh \nB. Prem Chand \nC. Jayashankar Prasad \nD. Amrit Lal Nagar\n",
    "The death anniversary of which of the following leaders is observed as Martyrs' Day? \nA. Smt. Indira Gandhi \nB. PI. Jawaharlal Nehru \nC. Mahatma Oandhi \nD. Lal Bahadur Shastri\n",
    "Who is the author of the epic 'Meghdoot'? \nA. Vishakadatta \nB. Valmiki \nC. Banabhatta \nD. Kalidas\n",
    "'Good Friday' is observed to commemorate the event of \nA. birth of Jesus Christ \nB. birth of' St. Peter \nC. crucification 'of Jesus Christ \nD. rebirth of Jesus Christ\n",
    "Who is the author of the book 'Amrit Ki Ore'? \nA. Mukesh Kumar \nB. Narendra Mohan \nC. Upendra Nath \nD. Nirad Choudhary\n",
    "Which of the following is observed as Sports Day every year? \nA. 22nd April \nB. 26th  july \nC. 29th August \nD. 2nd October\n",
    "World Health Day is observed on \nA. Apr 7 \nB. Mar 6 \nC. Mat I5 \nD. Apr 28\n",
    "Pongal is a popular festival of which state? \nA. Karnataka \nB. Kerala \nC. Tamil Nadu \nD. Andhra Pradesh\n",
    "Ghototkach in Mahabharat was the son of \nA. Duryodhana \nB. Arjuna \nC. Yudhishthir \nD. Bhima\n",
    "Which of the following Muslim festivals is based on the 'Holy Quran' ? \nA. Id -ul-Zuha \nB. Id -ul-Fitr \nC. Bakri-id \nD. Moharram\n",
    "Van Mahotsav was started by \nA. Maharshi Karve \nB. Bal Gangadhar Tiiak \nC. K.M, Munshi \nD. Sanjay Gandhi\n",
    "The first month of the Indian national calendar is \nA. Magha \nB. Chaitra \nC. Ashadha \nD. Vaishakha\n",
    "Which of the following is not a dance from Kerala? \nA. Kathakali \nB. Mohiniattam \nC. Ottan Thullal \nD. Yaksha Gana\n",
    "The festival of Nabanna is celebrated predominatly in \nA. Andhra Pradesh \nB. Rajasthan \nC. Kamataka \nD. Orissa\n",
    "Rath Yatra is famous festival at \nA. Ayodhya \nB. Mathura \nC. Dwaraka \nD. Puri\n",
    "Onam is the main festival of \nA. Tamil Nadu \nB. Karnataka \nC. Andhra Pradesh. \nD. Kerala\n",
    "The Lalit Kala Academy is devoted to the promotion of \nA. Dance & Drama \nB. Fine Arts \nC. Literature \nD. Music\n",
    "Which one of the following is essentially a solo dance? \nA. Kuchipudi \nB. Kathak \nC. Manipuri \nD. Mohiniattam\n",
    "Which of the followiing is a folk dance of India? \nA. Kathakali \nB. Mohiniattam \nC. Garba \nD. Manipuri\n",
    "Central Salt and Marine Chemicals Research Institute is located at \nA. Ahmedabad \nB. Bhavnagar. \nC. Gandhinagar \nD. Panaji\n",
    "The Krithi system was perfected and Carnatic music was given by \nA. Arunagirinathan \nB. Purandaradasa \nC. Shyama Shastri \nD. Swati Tirunal\n",
    "In which two dance forms the Krishna legends occupy the place of pride? 1. Bharatnatyam   2 Odissi  3  Manipuri 4 Kathakali \nA. 1 and 2 \nB. 1 and 4 \nC. 2 and 3 \nD. 3 and 4\n",
    "Nandyal is situated in \nA. Karnataka \nB. AndhraPradesh \nC. Maharashtra \nD. Madhya Pradesh\n"
]

answers = [
    "A", "C", "B", "D", "B", "B", "C", "D", "C", "D", "C", "B", "C", "A", "C", "D", "A", "C", "B", "D", "D", "D", "D", "B", "D", "C", "D", "D", "B", "A"
]

reech = 1000

for x in range(10) :
    rand = random.randint(0,29)
    print(questions[rand])
    ans = input("Your answer here: ")
    if(ans.upper() == answers[rand]):
        print("Sahi Jawab!")
        reech += reech*2
        print("Aap jeet gae hai ", reech, " rupaee!\n\n" )
    else:
        print("Galat Jawab! Aap haar gae. Sahi jawab tha ", answers[rand], ". Khelne ke liye dhanyavaad. Alvida!")
        break

