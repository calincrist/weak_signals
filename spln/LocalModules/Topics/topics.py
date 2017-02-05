from subprocess import Popen, STDOUT, PIPE
import logging
import json

logger = logging.getLogger('root')
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)

def run_command(command):
    p = Popen(command,
                     stdout=PIPE, stderr=STDOUT,
                     shell=True)
    return p.stdout
    # return iter(.read, b'')

def retrieve_topics(text):


    print(run_command('pwd').read())
    print(run_command('ls').read())

    api_key = 'b337f77af3b11496f1dff8bd9b38c1564100ed58'
    cmd = 'java -jar spln/LocalModules/Topics/run2.jar "' + api_key + '" "' + text + '"'
    print(cmd)
    cmd_result = run_command(cmd).read()

    try:
        # topics = json.loads(cmd_result)
        topics = {
            'topics' : cmd_result
        }
        return topics
    except (RuntimeError, TypeError, NameError, ValueError) as e:
        logger.error("Error: {0}".format(e))
        logger.error("---\n {0} ---\n".format(cmd_result))
        return {}

    pass
