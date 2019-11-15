import random, pendulum, uuid


class ServiceNowSearch(object):

    def __init__(self):
        self.search_list = []


    def get(self, random_keyword=None):
        root_url = 'https://dev{}.service-now.com'.format(random.randint(10000,90000))
        return_dict = { 
            'active': random.choice(['true', 'false']),
            'activity_due': pendulum.now().add(days=random.randint(0,30)).to_iso8601_string(),
            'additional_assignee_list': '',
            'approval': 'not requested',
            'approval_history': '',
            'approval_set': '',
        }
        random_id = uuid.uuid1().hex
        return_dict['assigned_to'] = {
            'link': '{}/api/now/table/sys_user/5137153cc611227c000bbd1bd8cd2007'.format(root_url, random_id),
            'value': '{}'.format(random_id)
        }
        random_id = uuid.uuid1().hex
        return_dict['assignment_group'] = {
            'link': '{}/api/now/table/sys_user_group/{}'.format(root_url, random_id),
            'value': '{}'.format(random_id)
        }
        return_dict['business_duration'] = pendulum.now(1).to_iso8601_string()
        random_id = uuid.uuid1().hex
        return_dict['business_service'] = {
            'link': '{}/api/now/table/cmdb_ci_service/{}'.format(root_url, random_id),
            'value': '{}'.format(random_id)
        }
        return_dict['business_stc'] = '28800'
        return_dict['calendar_duration'] = '1970-01-02 04:23:17'
        return_dict['calendar_stc'] =  '102197'
        random_id = uuid.uuid1().hex
        return_dict['caller_id'] = {
            'link': '{}/api/now/table/sys_user/{}'.format(root_url, random_id),
            'value': '{}'.format(random_id)
        }
        return_dict['category'] = 'inquiry'
        return_dict['caused_by'] = ''
        return_dict['child_incidents'] = '0'
        return_dict['close_code'] = random.choice(['Open', 'In-Progress'] * 5 + ['Solved (Permanently)', 'Closed/Resolved by Caller', 'Solved (Work Around)'])
        if return_dict['close_code'] in ('Open', 'In-Progress'):
            return_dict['close_notes'] = ''
            return_dict['closed_at'] = ''
        else:
            return_dict['close_notes'] = 'This incident is resolved.'
            return_dict['closed_at'] = pendulum.now().add(days=random.randint(0,30)).to_iso8601_string()
            random_id = uuid.uuid1().hex
            return_dict['closed_by'] = {
                'link': '{}/api/now/table/sys_user/{}'.format(root_url, random_id),
                'value': '{}'.format(random_id)
            }
            return_dict['resolved_at'] =  return_dict['closed_at']
            random_id = uuid.uuid1().hex
            return_dict['resolved_by'] = {
                'link': '{}/api/now/table/sys_user/{}'.format(root_url, random_id),
                'value': '{}'.format(random_id)
            }
        random_id = uuid.uuid1().hex
        return_dict['closed_by'] = {
            'link': '{}/api/now/table/cmdb_ci/{}'.format(root_url, random_id),
            'value': '{}'.format(random_id)
        }
        return_dict['comments'] = '' if random_keyword is None else random_keyword
        return_dict['comments_and_work_notes'] = '' if random_keyword is None else random_keyword
        random_id = uuid.uuid1().hex
        return_dict['company'] = {
            'link': '{}/api/now/table/core_company/{}'.format(root_url, random_id),
            'value': '{}'.format(random_id)
        }
        return_dict['contact_type'] = 'self-service'
        return_dict['contract'] = ''
        return_dict['correlation_display'] = ''
        return_dict['correlation_id'] = ''
        return_dict['delivery_plan'] = ''
        return_dict['delivery_task'] = ''
        return_dict['description'] = 'I am unable to connect to the {}. It appears to be down.'.format('email server' if random_keyword is None else random_keyword)
        return_dict['due_date'] = ''
        return_dict['escalation'] = '0'
        return_dict['expected_start'] = ''
        return_dict['follow_up'] = ''
        return_dict['group_list'] = ''
        return_dict['hold_reason'] = ''
        return_dict['impact'] = '2'
        return_dict['incident_state'] = random.randint(1,7)
        return_dict['knowledge'] = ''
        return_dict['location'] = ''
        return_dict['made_sla'] = random.choice(['true', 'false'])
        return_dict['notify'] = '1'
        return_dict['number'] = 'INC000{}'.format(random.randint(1,1000))
        return_dict['opened_at'] = pendulum.now().subtract(days=random.randint(0,15)).to_iso8601_string()
        random_id = uuid.uuid1().hex
        return_dict['opened_by'] = {
            'link': '{}/api/now/table/sys_user/{}'.format(root_url, random_id),
            'value': '{}'.format(random_id)
        }
        return_dict['order'] = ''
        return_dict['parent'] = ''
        return_dict['parent_incident'] = ''
        return_dict['priority'] = random.randint(1,5)
        return_dict['problem_id'] = ''
        return_dict['reassignment_count'] = random.randint(1,5)
        return_dict['reopen_count'] = ''
        return_dict['reopened_by'] = ''
        return_dict['reopened_time'] = ''
        return_dict['rfc'] = ''
        return_dict['service_offering'] = ''
        return_dict['severity'] = random.randint(1,5)
        return_dict['short_description'] = 'Unable to connect to {}'.format('email' if random_keyword is None else random_keyword)
        return_dict['sla_due'] = ''
        return_dict['state'] = random.randint(1,7)
        return_dict['subcategory'] = 'email'
        return_dict['sys_class_name'] = 'incident'
        return_dict['sys_created_by'] = 'employee'
        return_dict['sys_created_on'] = pendulum.now().subtract(days=random.randint(0,7)).to_iso8601_string()
        return_dict['sys_domain'] = {
            'link': '{}/api/now/table/sys_user_group/global'.format(root_url),
            'value': 'global'
        }
        return_dict['sys_domain_path'] = '/'
        return_dict['sys_id'] = uuid.uuid1().hex
        return_dict['sys_mod_count'] = random.randint(1,16)
        return_dict['sys_tags'] = ''
        return_dict['sys_updated_by'] = 'employee'
        return_dict['sys_updated_on'] = pendulum.now().subtract(hours=random.randint(0,7)).to_iso8601_string()
        return_dict['time_worked'] = ''
        return_dict['upon_approval'] = 'processed'
        return_dict['upon_reject'] = 'cancel'
        return_dict['urgency'] = random.randint(1,5)
        return_dict['user_input'] = '' if random_keyword is None else random_keyword
        return_dict['watch_list'] = ''
        return_dict['work_end'] = ''
        return_dict['work_notes'] = '' if random_keyword is None else random_keyword
        return_dict['work_notes_list'] = '' if random_keyword is None else random_keyword
        return_dict['work_start'] = ''

        return return_dict


print(ServiceNowSearch().get(random_keyword='CrowdStrike'))