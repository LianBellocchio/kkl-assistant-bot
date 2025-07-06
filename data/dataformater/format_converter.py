import json
from datetime import datetime

def parse_form_data(data):
    # Diccionario para almacenar la información de los usuarios
    users_info = {}

    for entry in data:
        birth_date = entry.get("Birth date", "")
        age = calculate_age(birth_date)
        user_key = entry.get('First Name', 'Unknown') + entry.get('Last Name', '')

        user_info = {
            "nombre": f"{entry.get('First Name', '')} {entry.get('Last Name', '')}",
            "informacion-basica": (
                f"Edad: {age} años, Nacionalidad: {entry.get('Nationality', '')}, "
                f"País de residencia: {entry.get('Country of residence', '')}, "
                f"Signo zodiacal: {entry.get('Zodiac sign', '')}, "
                f"Color favorito: {entry.get('favorite color', '')}, "
                f"Twitter: {entry.get('Twitter user', '')}, "
                f"Instagram: {entry.get('Instagram user', '')}, "
                f"TikTok: {entry.get('TikTok user ', '')}"
            ),
            "contenido-disponible": (
                f"DILDO: {'Sí' if entry.get('dildo', 'FALSE') == 'TRUE' else 'No'}, "
                f"ROLEPLAY: {'Sí' if entry.get('roleplay', 'FALSE') == 'TRUE' else 'No'}, "
                f"ASS PLAY: {'Sí' if entry.get('ass play', 'FALSE') == 'TRUE' else 'No'}, "
                f"CUM: {'Sí' if entry.get('cum', 'FALSE') == 'TRUE' else 'No'}, "
                f"DANCE / TWERK: {'Sí' if entry.get('dance twerk', 'FALSE') == 'TRUE' else 'No'}, "
                f"FOOT FETISH: {'Sí' if entry.get('foot fetish', 'FALSE') == 'TRUE' else 'No'}"
            ),
            "agenda-videollamadas": (
                f"Disponible para videollamadas {entry.get('Where will the call be made? Whatsapp, facetime, zoom... ', '')} "
                f"de {entry.get('Duration', 'N/A')}"
            ),
            "tarifas": (
                f"Custom Videos: ${entry.get('CUSTOM VIDEOS', 'N/A')}, "
                f"Videollamadas: ${entry.get('VIDEOCALLS', 'N/A')}, "
                f"Otros precios: {entry.get('VIDEO PRICES', 'N/A')}"
            ),
            "no_hare": (
                f"Lo que no hago: {entry.get('what are you NOT willing to do on a custom video? ', 'N/A')}"
            )
        }
        users_info[user_key] = user_info

    return users_info

def calculate_age(birth_date_str):
    if not birth_date_str:
        return "N/A"
    try:
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    except ValueError:
        return "N/A"

# Ejemplo de datos (debes reemplazar esto con la entrada real)
data = [
    {
        "Submission ID": "RBeyJv",
        "Respondent ID": "EPg00r",
        "Submitted at": "2024-03-05 17:53:18",
        "First Name": "Graziela",
        "Last Name": "Mourao Rocha",
        "Birth date": "1999-12-21",
        "Zodiac sign": "Sagitarius",
        "Country of residence": "United States",
        "Nationality": "Brazilian",
        "favorite color": "Black",
        "Twitter user": "eugrazimourao",
        "Instagram user": "Grazimourao",
        "TikTok user ": "Grazimourao_",
        "bust, waist and hip measurements": "P / P / P",
        "underwear size": "P",
        "favorite sexual position": "Dog",
        "CUSTOM VIDEOS": "30",
        "DURATION": "5/ 10 min",
        "Select those are you willing to do on a custom": "DILDO, ROLEPLAY, ASS PLAY, CUM, DANCE / TWERK, FOOT FETISH",
        "dildo": "TRUE",
        "roleplay": "TRUE",
        "ass play": "TRUE",
        "cum": "TRUE",
        "dance twerk": "TRUE",
        "foot fetish": "TRUE",
        "what are you NOT willing to do on a custom video? ": "I don’t do squirt",
        "VIDEOCALLS": "100",
        "Duration": "20 min",
        "Where will the call be made? Whatsapp, facetime, zoom... ": "Whatsapp",
        "VIDEO PRICES": "10",
        "B/G": "15",
        "B/B OR G/G": "15",
        "3SUM": "20",
        "ORGY": "40",
        "RANDOM QUESTIONS, KEEPING THE SAME SCRIPT WITH ALL": "White",
        "Do you like men or women more?": "Men",
        "What videos would you like to record that you haven't recorded yet?": "Gangbang",
        "Desired sexual fantasy": "Sex in public/ sex with a vouyer watching",
        "Favorite music to listen to and dance to": "Gorah - Nitefreak, Emmanuel Jal",
        "Where would your perfect vacation be?": "Bali / Playa del Carmen / Italy",
        "Top 3 favorite series": "Breaking Bad / How to get away with Murder / La casa de Papel",
        "Countries you know, what are your favorites": "Brasil/ USA / Mexico/ Egypt/ Greece/ Holanda / Belgium/ Croacia/ England/ Arab Emirates\nFavorites: Mexico/ USA / Croacia / Greece",
        "How long has your longest relationship lasted": "3 relations / 1 girl, 2 boys\nMaximum 2 years relationship ",
        "What do you enjoy most about sex?": "I like to feel at ease, have a strong grip and feel that the person is part of my body. I like being touched on all the points on my body.",
        "How do you choose who you record the videos with? (This is to have a solid answer to give to all the fans who get intense about why she/he  records with other men and they don't)": "I choose a person who I feel attracted to and want to have sex with. I also choose professional people who look good on cameras, who can have sex and record at the same time.",
        "Do you have any sexual fetishes?": "Me and other mens, sex in public, men with suit, men doing any exercise or cooking",
        "EXTRA INFO ABOUT YOU, DONT MISS THIS ONE. ": ""
    },
    {
        "Submission ID": "AWzgko",
        "Respondent ID": "dAz0ay",
        "Submitted at": "2024-04-01 13:56:19",
        "First Name": "Sabrina",
        "Last Name": "Alvarado",
        "Birth date": "1983-12-24",
        "Zodiac sign": "Capricorn",
        "Country of residence": "United States",
        "Nationality": "Costa Rican ",
        "favorite color": "Gray and pink",
        "Twitter user": "Marcelatinbabe",
        "Instagram user": "Itsmarcelababe",
        "TikTok user ": "Marcelatinbabe",
        "bust, waist and hip measurements": "36F",
        "underwear size": "S",
        "favorite sexual position": "Missionary",
        "CUSTOM VIDEOS": "100 and up (depending on request)",
        "DURATION": "5mins or so",
        "Select those are you willing to do on a custom": "DILDO, SQUIRT, ROLEPLAY, ASS PLAY, CUM, DANCE / TWERK, FOOT FETISH",
        "dildo": "TRUE",
        "roleplay": "TRUE",
        "ass play": "TRUE",
        "cum": "TRUE",
        "dance twerk": "TRUE",
        "foot fetish": "TRUE",
        "what are you NOT willing to do on a custom video? ": "Things that aren’t allowed on OF. Nothing gross or painful.",
        "VIDEOCALLS": "150",
        "Duration": "10",
        "Where will the call be made? Whatsapp, facetime, zoom... ": "Snapchat",
        "VIDEO PRICES": "$15-$50",
        "B/G": "$30 - $80",
        "B/B OR G/G": "$30 - $80",
        "3SUM": "$40 - $100",
        "ORGY": "$75+",
        "RANDOM QUESTIONS, KEEPING THE SAME SCRIPT WITH ALL": "I have a bbc obsession, but I don’t discriminate, love both. ",
        "Do you like men or women more?": "Both",
        "What videos would you like to record that you haven't recorded yet?": "Haven’t thought about this yet.",
        "Desired sexual fantasy": "Massage with happy endings\nGG orgy",
        "Favorite music to listen to and dance to": "I love many types of music, from rock to hip hop to reggaeton and bachata. Depends on what mood I’m in.",
        "Where would your perfect vacation be?": "Hawaii",
        "Top 3 favorite series": "Breaking Bad\nGame of thrones\nFriends",
        "Countries you know, what are your favorites": "USA + Puerto Rico, Colombia, Brazil, Costa Rica, Mexico, UK, Spain, France, Portugal, Iceland, Bahamas, Dominican Republic.\nMy favorites so far, Costa Rica and France. ",
        "How long has your longest relationship lasted": "15 years. ",
        "What do you enjoy most about sex?": "The passion, the connection. I’m very sensual and the orgasms are amazing too 😅",
        "How do you choose who you record the videos with? (This is to have a solid answer to give to all the fans who get intense about why she/he  records with other men and they don't)": "Most of my tapes were people I’ve dated, or friends of mine. I don’t shoot content with other people often, and definitely don’t shoot with random ppl either. ",
        "Do you have any sexual fetishes?": "I don’t know if these are fetishes or kinks or what but, here you go..\nBBC\nLesbian\nMassage with ending \nMommy role play.,\nDominant and submissive.",
        "EXTRA INFO ABOUT YOU, DONT MISS THIS ONE. ": "If you are not sure about something just ask me. It’s the best way to get things going ☺️\nI’m goofy, and very sweet, call ppl papi and mi amor, bread and chocolate are my weakness. I am divorced, have 2 grown kids, I’m very family oriented, been on playboy, hmm not sure what else lol"
    },
    {
        "Submission ID": "P8Lkv0",
        "Respondent ID": "VlR4Wg",
        "Submitted at": "2024-04-13 18:10:59",
        "First Name": "Thony",
        "Last Name": "Grey",
        "Birth date": "1999-04-28",
        "Zodiac sign": "Taurus",
        "Country of residence": "France",
        "Nationality": "Frances",
        "favorite color": "Rouge",
        "Twitter user": "Thonygrey_",
        "Instagram user": "Thony_grey",
        "TikTok user ": "Thony_grey",
        "bust, waist and hip measurements": "M",
        "underwear size": "Medium ",
        "favorite sexual position": "Doggy / Amazone / Reverse cowgirl",
        "CUSTOM VIDEOS": "200",
        "DURATION": "10",
        "Select those are you willing to do on a custom": "DILDO, ROLEPLAY, ASS PLAY, CUM, DANCE / TWERK, MUSCLE WORSHIP, FOOT FETISH",
        "dildo": "TRUE",
        "roleplay": "TRUE",
        "ass play": "TRUE",
        "cum": "TRUE",
        "dance twerk": "TRUE",
        "foot fetish": "TRUE",
        "what are you NOT willing to do on a custom video? ": "I’m doing what it needs me to do, I have no limits if the ammount is good enough ",
        "VIDEOCALLS": "200",
        "Duration": "15",
        "Where will the call be made? Whatsapp, facetime, zoom... ": "FaceTime / Skype ",
        "VIDEO PRICES": "Depende de lo que hago entre 6.69$ y 39.99$ ",
        "B/G": "Entre 8.99$ las muy viejas y 39.99$",
        "B/B OR G/G": "Depende de lo reciente o de la acción entre 8.99$ y 100$ ",
        "3SUM": "If I’d do it depende con quien o como cada video tiene su precio proprio",
        "ORGY": "Igual que por el threesome",
        "RANDOM QUESTIONS, KEEPING THE SAME SCRIPT WITH ALL": "I love them all no preferences ",
        "Do you like men or women more?": "More women but I’m doing gay for pay and sometimes I can enjoy it ",
        "What videos would you like to record that you haven't recorded yet?": "No tengo ni idea habría que pensarlo ",
        "Desired sexual fantasy": "Trying New experiences like threesomes ",
        "Favorite music to listen to and dance to": "Should - Love tonight ",
        "Where would your perfect vacation be?": "Las Vegas USA",
        "Top 3 favorite series": "Smallville - Las Vegas - NCIS enquêtes spéciale ",
        "Countries you know, what are your favorites": "USA COLOMBIA ALEMAÑA SUISSA ITALIA FRANCIA ESPAÑA MEXICO UKRANIA REINO UNIDO BELGICA y mi favorito sería ESTADOS UNIDOS ",
        "How long has your longest relationship lasted": "3 years ",
        "What do you enjoy most about sex?": "Making my partner cum first before my own pleasure, I’m taking pleasure in my partner’s pleasure ",
        "How do you choose who you record the videos with? (This is to have a solid answer to give to all the fans who get intense about why she/he  records with other men and they don't)": "I shoot with sucesfull people or people that are very good looking and easygoing ",
        "Do you have any sexual fetishes?": "Squirt and milk from womens with big titties ",
        "EXTRA INFO ABOUT YOU, DONT MISS THIS ONE. ": "I’m willing to do almost whatever if the ammount is good enough, and I have no limits, except kissing guys else than this it’s limitless "
    }
]

# Convertir los datos
converted_data = parse_form_data(data)

# Guardar el resultado en un archivo JSON
with open('usuarios.json', 'w', encoding='utf-8') as f:
    json.dump(converted_data, f, ensure_ascii=False, indent=4)
