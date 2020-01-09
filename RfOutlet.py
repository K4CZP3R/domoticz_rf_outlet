class RfOutlet(object):
    def __init__(self, dom_id, rf_id, state, executed):
        self.rf_id = rf_id
        self.state = state
        self.executed = executed
        self.dom_id = dom_id
        self.state_changed_at = 0
        