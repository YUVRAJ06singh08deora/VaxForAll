import smartpy as sp

class vaxForAll(sp.Contract):
    def __init__(self):
        self.init(
            patientMap = sp.map(),
            centerMap = sp.map(),
            factoryMap = sp.map(),
            factoryOrder = 0   
        )
        

    @sp.entry_point       
    def addPatient(self, params):
        uid = params.uid
        self.data.patientMap[uid] = sp.record(
            name = params.name, 
            age = params.age, 
            gender = params.gender, 
            number = params.number, 
            vName = '',
            v1 = False, 
            v2 = False, 
            v1Date = sp.timestamp_from_utc_now(),
            v2Date = sp.timestamp_from_utc_now(),
            v1Hospital = '', 
            v2Hospital = '', 
            v1Price = '', 
            v2Price = ''
        )
        
    def checkPatient(self, uid):
      	sp.verify(self.data.patientMap.contains(uid))

    @sp.entry_point
    def checkSlot(self, params):

        uidC = params.centerUID
        message = ""

        self.checkCenter(uidC)

        sp.if self.data.centerMap[uidC].slotAvailability[params.vaccName] >=1:
            message = "Slot Available"
        sp.else:
            message = "Slot not Available"

    @sp.entry_point
    def addCenter(self, params):
        uid = params.uid
        self.data.centerMap[uid] = sp.record(
            name = params.name,
            location = params.centLoc, 
            number = params.number,
            factory = params.factoryUID,
            vaccAvailability = {
                'Covaxin': 100,
                'Covishield': 100,
                'Sputnik-V': 100     
            },
            slotAvailability = {
                'Covaxin': 100,
                'Covishield': 100,
                'Sputnik-V': 100     
            }
        )

    def checkCenter(self, uid):
        sp.verify(self.data.centerMap.contains(uid))

    @sp.entry_point
    def getVacc(self, params):

        uidP = params.patientUID
        uidC = params.centerUID
        uidF = self.data.centerMap[uidC].factory

        self.checkCenter(uidC)
        self.checkPatient(uidP)

        
        sp.if self.data.centerMap[uidC].slotAvailability[params.vaccName] >=1:
            sp.if self.data.centerMap[uidC].vaccAvailability[params.vaccName] >= 1:
                self.data.patientMap[uidP].vName = params.vaccName
                self.data.patientMap[uidP].v1 = True
                self.data.patientMap[uidP].v1Hospital = self.data.centerMap[uidC].name
                self.data.patientMap[uidP].v1Price = 'subsidised'
                self.data.patientMap[uidP].v1Date = sp.timestamp_from_utc_now()

            sp.else:
                self.orderVacc(params)

    @sp.entry_point
    def orderVacc(self, params):

        uidC = params.centerUID
        uidF = self.data.centerMap[uidC].factory
        
        self.checkFactory(uidF)


        self.data.factoryOrder += 1

        self.data.factoryMap[uidF].orders.push(
            sp.record(
                orderNumber = self.data.factoryOrder,
                centerUID = uidC,
                vaccName = params.vaccName,
                quantity = 100
            )
        )

    @sp.entry_point
    def addFactory(self, params):
        uid = params.uid
        self.data.factoryMap[uid] = sp.record(
            name = params.name,
            location = params.factLoc, 
            number = params.number,
            availability = {
                'Covaxin': 100,
                'Covishield': 100,
                'Sputnik-V': 100     
            }, 
            productionCap = {
                'Covaxin': 100,
                'Covishield': 100,
                'Sputnik-V': 100     
            }, 
            orders = sp.list()
        )

    @sp.sub_entry_point
    def checkFactory(self, uid):
      	sp.verify(self.data.factoryMap.contains(uid))


    @sp.entry_point
    def updateStock(self, params):

        self.checkFactory(params.uid)

        self.data.factoryMap[params.uid].availability[params.vaccName] += params.quantity


@sp.add_test(name = "vax_slot_transfer")
def test():
    scenario = sp.test_scenario()

    user = sp.test_account("Test")
    
    vaxScene = vaxForAll()
    scenario += vaxScene
    
    scenario.h1("Add New User")
    scenario += vaxScene.addPatient(
        uid = "Adhar:0123456789", 
        name = "Bhavya Goel", 
        age = 20, 
        gender = "Male", 
        number = 70420897902, 
    )

    scenario.h2("Add New Factory")
    scenario += vaxScene.addFactory(
        uid = "Ind:0123456789", 
        name = "Bharat Biotech", 
        factLoc = "Bangalore India", 
        number = 70420897902, 
    )

    scenario.h3("Add New Hospital")
    scenario += vaxScene.addCenter(
        uid = "Med:0123456789", 
        name = "Bharat Biotech", 
        centLoc = "Bangalore India", 
        number = 70420897902, 
        factoryUID = "Ind:0123456789",
    )

    scenario += vaxScene.updateStock(
        uid = "Ind:0123456789",
        vaccName = 'Covaxin',
        quantity = 200
    )

    scenario += vaxScene.getVacc(
        patientUID = "Adhar:0123456789",
        centerUID = "Med:0123456789",
        vaccName = 'Covaxin'
    )
    
    scenario += vaxScene.orderVacc(
        centerUID = "Med:0123456789",
        vaccName = 'Covaxin'
    )

    scenario += vaxScene.checkSlot(
        centerUID = "Med:0123456789",
        vaccName = 'Covaxin'
    )

    scenario += vaxScene.addPatient(
        name = "Manthan Garg",
        gender = "Male",
        number = 9310055405,
        uid = "Adhar:9876543210",
        age = 19
    )

    scenario += vaxScene.addPatient(
        uid = "Adhar:01234569839", 
        name = "Yuvraj Singh", 
        age = 20, 
        gender = "Male", 
        number = 23764786293, 
    )

    # scenario.show(vaxScene.balance)