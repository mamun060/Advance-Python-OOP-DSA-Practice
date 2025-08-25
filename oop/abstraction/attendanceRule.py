from abc import ABC, abstractmethod
from datetime import datetime 

class AttendanceRule(ABC):
    @abstractmethod
    def applyRule(self, check_in: datetime, check_out: datetime):
        pass 

class NormalRule(AttendanceRule):
    def applyRule(self, check_in: datetime, check_out: datetime):
        return f"Present (on time)"

class LateRule(AttendanceRule):
    def applyRule(self, check_in, check_out):
        officeStart = datetime( check_in.year, check_in.month, check_in.day, 9, 0, 0)
        if check_in > officeStart:
            return f"Late (Checked in at {check_in.strftime('%H:%M:%S')})"
        return f"Present (Checked in at {check_in.strftime('%H:%M:%S')})"

class OvertimeRule(AttendanceRule):
    def applyRule(self, check_in: datetime, check_out: datetime):
        return f"Overtime (Checked in at {check_in.strftime('%H:%M:%S')}, Checked out at {check_out.strftime('%H:%M:%S')})"
    

def process_attendance(rule: AttendanceRule, check_in: datetime, check_out: datetime):
    result = rule.applyRule(check_in, check_out)
    print(result)

in_time = datetime(2023, 3, 15, 8, 30, 0)
out_time = datetime(2023, 3, 15, 17, 30, 0)

process_attendance(NormalRule(), in_time, out_time)
process_attendance(LateRule(), in_time, out_time)
process_attendance(OvertimeRule(), in_time, out_time)