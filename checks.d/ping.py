from checks import AgentCheck
import os

'''
This is for demostration purposes only.
Because of the nature of ping, it could result in a very long running check if there are excessive timeouts.
Long running checks could potentially result in other metrics and checks being skipped.
'''

class PingCheck(AgentCheck):
    def check(self, instance):
        hostnames = ["google.com", "datadog.com", "1.1.1.1"]
        for host in hostnames:
            res = os.system("ping " + host + " -W 1 -c 1")
            self.log.info("host: %s - res: %d" % (host, res))
            if res != 0:
                res = 2
                self.gauge('network.ping.can_connect', 0, tags=['ping_host:'+host])
            self.service_check('network.ping', status=res, tags=['ping_host:'+host])
            self.gauge('network.ping.can_connect', 1, tags=['ping_host:'+host])
