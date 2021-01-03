from prometheus_client import Counter, Histogram, Summary


class Model:
    captcha_content_created = Counter('desecapi_captcha_content_created', 'number of times captcha content created',['kind'])
    autodelegation_created = Counter('desecapi_autodelegation_created', 'number of autodelegations added')
    autodelegation_deleted = Counter('autodelegation_deleted', 'number of autodelegations deleted')
    email_queued = Histogram('desecapi_messages_queued', 'number of emails queued', ['reason', 'user', 'lane'], buckets=[0, 1, float("inf")])


class View:
    dynDNS12_domain_not_found = Counter('desecapi_dynDNS12_domain_not_found', 'number of times dynDNS12 domain is not found')


class Crypto:
    key_encryption_success = Counter('desecapi_key_encryption_success', 'number of times key encryption was successful', ['context'])
    key_decryption_success = Counter('desecapi_key_decryption_success', 'number of times key decryption was successful', ['context'])


class ExceptionHandlers:
    database_unavailable = Counter('desecapi_database_unavailable', 'number of times database was unavailable')


class Pdns:
    request_success = Counter('desecapi_pdns_request_success', 'number of times pdns request was successful', ['method', 'status'])
    keys_fetched = Counter('desecapi_pdns_keys_fetched', 'number of times pdns keys were fetched')


class ChangeTracker:
    catalog_updated = Counter('desecapi_pdns_catalog_updated', 'number of times pdns catalog was updated successfully')


class Throttling:
    failure = Counter('desecapi_throttle_failure', 'number of requests throttled', ['method', 'scope', 'user'])


class Serializer:
    rrset_list_init = Counter('desecapi_rrset_list_serializer', 'number of times RRsetListSerializer was initialized')


class Replication:
    axfr_transfer_time = Summary('desecapi_replication_axfr_transfer_time', 'Time waited to transfer AXFR')
    axfr_parse_time = Summary('desecapi_replication_axfr_parse_time', 'Time used to parse AXFR')
