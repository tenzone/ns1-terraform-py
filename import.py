import json
from ns1 import NS1

api = NS1(apiKey='o1ZUt7O44pqTEEwnStbA')

def GetZoneInfo():
    print("Please enter the zone name")
    global zone
    zone = input("> ")
    zoneDef = api.loadZone(zone)
    double = str(zoneDef.data).replace("'", '"')
    valid = json.dumps(zoneDef.data, sort_keys=True, indent=4)
    global data
    data = json.loads(valid)
    
     #print(data["records"][2])
    
    
def getRecords():
    str(data["records"][2]["type"]).replace("'", '"')
    print("Which Record Type do You want? (A, MX, NS, ALIAS, CNAME, SPF, TXT, SRV)")
    recordType = input("> ")
    # len(data["records"])
    recordImport = []
    tf_TTL = []
    tf_Type = []
    tf_Answers = []
    tf_Domain = []
    
    
    # for n in range(0, len(data["records"])):
    #     if data["records"][n]["type"] == recordType:
    #         record = data["records"][n]["domain"]
    #         recordEdit = record
    #         recordImport.append(recordEdit)
    
    for recordzz in data["records"]:
        if recordzz["type"] == recordType:
            record = recordzz["domain"]
            recordEdit = record
            recordImport.append(recordEdit)
    
    target = open(f'{zone}_{recordType}', 'w+')
    hcl = open(f'{zone}_{recordType}.tf', 'w+')
    
    for item in recordImport:
        stringed = str(item)
        replaced = item.replace(".", "_")
        target.write(f'ns1_record.{recordType}_{replaced},{zone}/{stringed}/{recordType}\n')
        # print(f'ns1_record.{recordType}_{replaced},{zone}/{stringed}/{recordType}')
        
    for x in range(0, len(data["records"])):
        if data["records"][x]["type"] == recordType: 
            recordZone = data["zone"]
            recordTTL = data["records"][x]["ttl"]
            recordType = data["records"][x]["type"]
            recordAnswers = data["records"][x]["short_answers"]
            recordDomain = data["records"][x]["domain"]
            tf_TTL.append(recordTTL)
            tf_Type.append(recordType)
            tf_Answers.append(recordAnswers)
            tf_Domain.append(recordDomain)
    tfDomain_ = [w.replace('.', '_') for w in tf_Domain]
    
    for z in range(0, len(tf_Domain)):
        answers = ""
        for ans in tf_Answers[z]:
            answers += f'\n\t\tanswer = \"{ans}\"'
        test = f"resource \"ns1_record\" \"{tf_Type[z]}_{tfDomain_[z]}\" ~\n\tzone = \"{recordZone}\"\n\tttl = {tf_TTL[z]}\n\ttype = \"{tf_Type[z]}\"\n\tdomain = \"{tf_Domain[z]}\"\n\n\tanswers = ~{answers}\n  !\n!\n\n"
        rep1 = test.replace("~", "{")
        rep2 = rep1.replace("!", "}")
        # print(rep2)
        hcl.write(rep2)
    
    target.close()
    hcl.close()

GetZoneInfo()
getRecords()