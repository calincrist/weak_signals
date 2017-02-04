import json
from watson_developer_cloud import AlchemyLanguageV1


def get_ner(sample):
    # replace the api_key when trial expires with a new one
    alchemy_language = AlchemyLanguageV1(api_key='c8d252337e2eddb7d0775771f4a4de96d89b8a6c')
    jsonOutput = {}
    i = 1
    news = {}

    print(sample)

    for element in sample:
        catAnatomy = []
        catAnniversary = []
        catAutomobile = []
        catCity = []
        catCompany = []
        catContinent = []
        catCountry = []
        catCrime = []
        catDegree = []
        catDrug = []
        catEntertainmentAward = []
        catFacility = []
        catFieldTerminology = []
        catFinancialMarketIndex = []
        catGeographicFeature = []
        catHealthCondition = []
        catHoliday = []
        catJobTitle = []
        catMovie = []
        catMusicGroup = []
        catNaturalDisaster = []
        catOperatingSystem = []
        catOrganisation = []
        catPerson = []
        catPrintMedia = []
        catProduct = []
        catProffesionalDegree = []
        catRadioProgram = []
        catRadioStation = []
        catRegion = []
        catSport = []
        catSportingEvent = []
        catStateOrCounty = []
        catTechnology = []
        catTelevisionShow = []
        catTelevisionStation = []
        catEmailAddress = []
        catTwitterHandle = []
        catHashtag = []
        catIPAddress = []
        catQuantity = []
        catMoney = []

        jsonResponse = json.loads(json.dumps(alchemy_language.entities(text=element)))
        jsonEntities = jsonResponse["entities"]
        for item in jsonEntities:
            if (item.get("type") == "Anatomy"):
                catAnatomy.append(item.get("text"))
            elif (item.get("type") == "Anniversary"):
                catAnniversary.append(item.get("text"))
            elif (item.get("type") == "Automobile"):
                catAutomobile.append(item.get("text"))
            elif (item.get("type") == "City"):
                catCity.append(item.get("text"))
            elif (item.get("type") == "Company"):
                catCompany.append(item.get("text"))
            elif (item.get("type") == "Continent"):
                catContinent.append(item.get("text"))
            elif (item.get("type") == "Country"):
                catCountry.append(item.get("text"))
            elif (item.get("type") == "Crime"):
                catCrime.append(item.get("text"))
            elif (item.get("type") == "Degree"):
                catDegree.append(item.get("text"))
            elif (item.get("type") == "Drug"):
                catDrug.append(item.get("text"))
            elif (item.get("type") == "EntertainmentAward"):
                catEntertainmentAward.append(item.get("text"))
            elif (item.get("type") == "Facility"):
                catFacility.append(item.get("text"))
            elif (item.get("type") == "FieldTerminology"):
                catFieldTerminology.append(item.get("text"))
            elif (item.get("type") == "FinancialMarketIndex"):
                catFinancialMarketIndex.append(item.get("text"))
            elif (item.get("type") == "GeographicFeature"):
                catGeographicFeature.append(item.get("text"))
            elif (item.get("type") == "HealthCondition"):
                catHealthCondition.append(item.get("text"))
            elif (item.get("type") == "Holiday"):
                catHoliday.append(item.get("text"))
            elif (item.get("type") == "JobTitle"):
                catJobTitle.append(item.get("text"))
            elif (item.get("type") == "Movie"):
                catMovie.append(item.get("text"))
            elif (item.get("type") == "MusicGroup"):
                catMusicGroup.append(item.get("text"))
            elif (item.get("type") == "NaturalDisaster"):
                catNaturalDisaster.append(item.get("text"))
            elif (item.get("type") == "OperatingSystem"):
                catOperatingSystem.append(item.get("text"))
            elif (item.get("type") == "Organization"):
                catOrganisation.append(item.get("text"))
            elif (item.get("type") == "Person"):
                catPerson.append(item.get("text"))
            elif (item.get("type") == "PrintMedia"):
                catPrintMedia.append(item.get("text"))
            elif (item.get("type") == "Product"):
                catProduct.append(item.get("text"))
            elif (item.get("type") == "ProffesionalDegree"):
                catProffesionalDegree.append(item.get("text"))
            elif (item.get("type") == "RadioProgram"):
                catRadioProgram.append(item.get("text"))
            elif (item.get("type") == "RadioStation"):
                catRadioStation.append(item.get("text"))
            elif (item.get("type") == "Region"):
                catRegion.append(item.get("text"))
            elif (item.get("type") == "Sport"):
                catSport.append(item.get("text"))
            elif (item.get("type") == "SportingEvent"):
                catSportingEvent.append(item.get("text"))
            elif (item.get("type") == "StateOrCounty"):
                catStateOrCounty.append(item.get("text"))
            elif (item.get("type") == "Technology"):
                catTechnology.append(item.get("text"))
            elif (item.get("type") == "TelevisionShow"):
                catTelevisionShow.append(item.get("text"))
            elif (item.get("type") == "TelevisionStation"):
                catTelevisionStation.append(item.get("text"))
            elif (item.get("type") == "EmailAddress"):
                catEmailAddress.append(item.get("text"))
            elif (item.get("type") == "TwitterHandle"):
                catTwitterHandle.append(item.get("text"))
            elif (item.get("type") == "Hashtag"):
                catHashtag.append(item.get("text"))
            elif (item.get("type") == "IPAddress"):
                catIPAddress.append(item.get("text"))
            elif (item.get("type") == "Quantity"):
                catQuantity.append(item.get("text"))
            elif (item.get("type") == "Money"):
                catMoney.append(item.get("text"))
            else:
                print(item.get("text") + "-" + item.get("type") + "\n")
        newName = "news" + str(i)
        newsEntities = {}
        if catAnatomy:
            newsEntities["Anatomy"] = catAnatomy
        if catAnniversary:
            newsEntities["Anniversary"] = catAnniversary
        if catAutomobile:
            newsEntities["Automobile"] = catAutomobile
        if catCity:
            newsEntities["City"] = catCity
        if catCompany:
            newsEntities["Company"] = catCompany
        if catContinent:
            newsEntities["Continent"] = catContinent
        if catCountry:
            newsEntities["Country"] = catCountry
        if catCrime:
            newsEntities["Crime"] = catCrime
        if catDegree:
            newsEntities["Degree"] = catDegree
        if catDrug:
            newsEntities["Drug"] = catDrug
        if catEntertainmentAward:
            newsEntities["EntertainmentAward"] = catEntertainmentAward
        if catFacility:
            newsEntities["Facility"] = catFacility
        if catFieldTerminology:
            newsEntities["FieldTerminology"] = catFieldTerminology
        if catFinancialMarketIndex:
            newsEntities["FinancialMarketIndex"] = catFinancialMarketIndex
        if catGeographicFeature:
            newsEntities["GeographicFeature"] = catGeographicFeature
        if catHealthCondition:
            newsEntities["HealthCondition"] = catHealthCondition
        if catHoliday:
            newsEntities["Holiday"] = catHoliday
        if catJobTitle:
            newsEntities["JobTitle"] = catJobTitle
        if catMovie:
            newsEntities["Movie"] = catMovie
        if catMusicGroup:
            newsEntities["MusicGroup"] = catMusicGroup
        if catNaturalDisaster:
            newsEntities["NaturalDisaster"] = catNaturalDisaster
        if catOperatingSystem:
            newsEntities["OperatingSystem"] = catOperatingSystem
        if catOrganisation:
            newsEntities["Organization"] = catOrganisation
        if catPerson:
            newsEntities["Person"] = catPerson
        if catPrintMedia:
            newsEntities["PrintMedia"] = catPrintMedia
        if catProduct:
            newsEntities["Product"] = catProduct
        if catProffesionalDegree:
            newsEntities["ProffesionalDegree"] = catProffesionalDegree
        if catRadioProgram:
            newsEntities["RadioProgram"] = catRadioProgram
        if catRadioStation:
            newsEntities["RadioStation"] = catRadioStation
        if catRegion:
            newsEntities["Region"] = catRegion
        if catSport:
            newsEntities["Sport"] = catSport
        if catSportingEvent:
            newsEntities["SportingEvent"] = catSportingEvent
        if catStateOrCounty:
            newsEntities["StateOrCounty"] = catStateOrCounty
        if catTechnology:
            newsEntities["Technology"] = catTechnology
        if catTelevisionShow:
            newsEntities["TelevisionShow"] = catTelevisionShow
        if catTelevisionStation:
            newsEntities["TelevisionStation"] = catTelevisionStation
        if catEmailAddress:
            newsEntities["EmailAddress"] = catEmailAddress
        if catTwitterHandle:
            newsEntities["TwitterHandle"] = catTwitterHandle
        if catHashtag:
            newsEntities["Hashtag"] = catHashtag
        if catIPAddress:
            newsEntities["IPAddress"] = catIPAddress
        if catQuantity:
            newsEntities["Quantity"] = catQuantity
        if catMoney:
            newsEntities["Money"] = catMoney
        news[newName] = newsEntities
        i = i + 1
    jsonOutput["NER"] = news
    print(json.dumps(jsonOutput, sort_keys=True, indent=4, separators=(',', ': ')))
    return json.dumps(jsonOutput)