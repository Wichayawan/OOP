class ContraceList(list):
    def search(self, phone):
        matching_contracts = []
        for c in self:
            if phone in c.phone:
                matching_contracts.append(c)
        return matching_contracts
    

    