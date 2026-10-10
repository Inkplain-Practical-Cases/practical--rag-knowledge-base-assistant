import json,logging
logger=logging.getLogger("rag.audit")
def service_log_query_event(status:str,citation_count:int)->None:
    # Privacy: raw queries, credentials and document bodies never enter event logs.
    logger.info(json.dumps({"event":"query_completed","status":status,"citation_count":citation_count}))
