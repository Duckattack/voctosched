import logging

from ..base import ExportHandler
from fahrplan.model.schedule import Schedule
from hacks import noexcept
from util import write_output


log = logging.getLogger(__name__)


class OdtSetcardsExportHandler(ExportHandler):
    @noexcept(log)
    def run(self, schedule: Schedule) -> bool:
        path = self.config["path"]
        for day in schedule.days:
            print(day)
        #content = schedule.to_xml(extended=False)
        #return write_output(path, content)
