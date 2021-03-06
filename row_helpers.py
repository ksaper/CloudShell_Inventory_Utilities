class AutoloadRow:
    def __init__(self, row):
        # set ignore
        if str(row[0].value).upper().strip() == 'Y':
            self.ignore = True
        else:
            self.ignore = False

        # check if it's update
        if str(row[1].value).upper().strip() == 'Y':
            self.update = True
        else:
            self.update = False

        # set autoload
        if str(row[2].value).upper().strip() == 'Y':
            self.autoload = True
        else:
            self.autoload = False

        self.parent = str(row[3].value).strip()
        self.name = str(row[4].value).strip()
        if self.parent:
            self.fullname = '%s/%s' % (self.parent, self.name)
        else:
            self.fullname = self.name

        self.resource_family = row[5].value.strip()
        self.resource_model = row[6].value.strip()
        self.domain = []
        dom_list = str(row[7].value)
        temp = dom_list.split(',')
        for each in temp:
            self.domain.append(each.strip())
        self.address = str(row[8].value).strip()
        self.folder_path = row[9].value.strip()
        self.connection_type = row[10].value.strip()
        self.user = row[11].value.strip()
        self.password = str(row[12].value).strip()
        self.enable_password = str(row[13].value).strip()
        self.description = str(row[14].value).strip()
        self.driver_name = row[15].value.strip()
        self.snmp_version = str(row[16].value).strip()
        self.snmp_read_str = str(row[17].value).strip()
        self.location = str(row[18].value).strip()
        if str(row[19].value).upper().strip() == 'Y':
            self.enable_snmp = True
        else:
            self.enable_snmp = False
        if str(row[20].value).upper().strip() == 'Y':
            self.under_pwr_mgmt = True
        else:
            self.under_pwr_mgmt = False
        if self.name != '' and \
                self.address != '' and \
                self.resource_family != '' and \
                self.resource_model != '':
            self.valid = True
        else:
            self.valid = False


class SetAttributesRow:
    def __init__(self, row, attribute_list):
        # set ignore
        if str(row[0].value).upper().strip() == 'Y':
            self.ignore = True
        else:
            self.ignore = False

        self.name = row[1].value.strip()
        self.attributes = dict()
        n = 2
        for h in attribute_list:
            # blank check handled in the set_attributes method
            self.attributes[h] = str(row[n].value).strip()
            n += 1


class SetConnectionsRow:
    def __init__(self, row):
        if str(row[0].value).upper().strip() == 'Y':
            self.ignore = True
        else:
            self.ignore = False
            
        if row[1].value == '':
            self.point_a = None
        else:
            self.point_a = row[1].value.strip()

        if row[2].value == '':
            self.point_b = None
        else:
            self.point_b = row[2].value.strip()


class CustomAttributeRow:
    def __init__(self, row):
        if str(row[0].value).upper().strip() == 'Y':
            self.ignore = True
        else:
            self.ignore = False

        self.model_name = row[1].value.strip()
        self.attribute_name = row[2].value.strip()
        self.default_value = row[3].value.strip()


class SelectionHelper:
    def __init__(self):
        self.create_and_load = False
        self.set_attributes = False
        self.set_connections = False
        self.list_connections = False
        self.add_custom_attributes = False
        self.inventory_report = False
        self.user_report = False
        self.update_users = False


class UserUpdateRow:
    def __init__(self, row):
        if str(row[0].value).upper().strip() == 'Y':
            self.ignore = True
        else:
            self.ignore = False

        self.user = row[1].value.strip()
        self.email = row[2].value.strip()

        if str(row[3].value).upper().strip() == 'N':
            self.active = False
        else:
            self.active = True

        if len(row[4].value) > 0:
            self.add_groups = str(row[4].value).split(',')
        else:
            self.add_groups = []

        if len(row[5].value) > 0:
            self.remove_groups = str(row[5].value).split(',')
        else:
            self.remove_groups = []

        self.max_reservation = str(row[6].value).strip()
        self.max_duration = str(int(row[7].value) * 60)
