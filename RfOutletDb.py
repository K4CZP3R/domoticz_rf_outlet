from RfOutlet import RfOutlet
from LogicResponse import LogicResponse

class RfOutletDb(object):
    def __init__(self, predefined_outlets: [RfOutlet]):
        self.rf_outlets = predefined_outlets
        self.rf_outlets: [RfOutlet]
    def get_outlets(self) -> [RfOutlet]:
        return self.rf_outlets
    def count_outlets(self):
        return len(self.rf_outlets)
    def add_outlet(self, new_outlet: RfOutlet) -> LogicResponse:
        for outlet in self.rf_outlets:
            outlet: RfOutlet

            if outlet.dom_id == new_outlet.dom_id:
                return LogicResponse(False, "This outlet already exists")
        
        self.rf_outlets.append(new_outlet)
    
    def get_outlet_by_dom_id(self, dom_id):
        for outlet in self.rf_outlets:
            outlet: RfOutlet
            if outlet.dom_id == dom_id:
                return LogicResponse(True, outlet)
        return LogicResponse(False, "Not found!")