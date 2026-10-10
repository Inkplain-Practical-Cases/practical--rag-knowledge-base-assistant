# A tiny synthetic corpus. Do not insert real secrets.
CORPUS=[
 {"id":"kb-1","title":"Remote Work","text":"Employees can work remotely up to three days per week. Manager approval is required for a fourth remote day."},
 {"id":"kb-2","title":"Expense Policy","text":"Reimbursements require a receipt. Expense claims over 500 EUR require manager approval."},
 {"id":"kb-3","title":"Incident Response","text":"Report a security incident to the security team within one hour. Rotate exposed credentials immediately."}
]
def provider_documents()->list[dict]:
    return [dict(d) for d in CORPUS]
