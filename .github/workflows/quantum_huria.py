from pyqpanda3.core import QCircuit, H, CNOT, QProg, measure, CPUQVM
from pyqpanda3.qcloud import QCloudService, LogOutput
import pyqpanda3.qcloud as qcloud

api_key = ""  # ضع مفتاحك هنا

service = QCloudService(api_key)
service.setup_logging(LogOutput.CONSOLE)

backend = service.backend("origin_wukong")
chip_info = backend.chip_info()

circuit = QCircuit(2)
circuit << H(0)
circuit << CNOT(0, 1)

prog = QProg()
prog << circuit

for i in range(2):
    prog << measure(i, i)

options = qcloud.QCloudOptions()
result = backend.run(prog, 1000, options).result()

print("نتيجة التشفير الكمي:")
print(result.get_counts())
