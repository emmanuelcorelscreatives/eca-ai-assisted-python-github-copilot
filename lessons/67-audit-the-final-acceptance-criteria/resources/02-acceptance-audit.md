# Acceptance audit

Contract reviewed: [link or location of the project's original contract]
Database or test-data context: [safe, disposable data used for checks]

Status key: verified = recorded evidence supports this clause; missing = observed behavior contradicts or lacks this clause; uncertain = sufficient evidence has not been gathered. Do not mark a row verified solely because the full test command passed.

| Requirement from original contract | Example to check and expected outcome | Evidence: observed result, inspected assertion, or reason not checked | Status | Follow-up |
| --- | --- | --- | --- | --- |
| Add: valid record | Use the documented add command; record expected save and response. | Not checked. | uncertain | Compare response and stored record with contract. |
| Add: invalid record | Use a contract-invalid input; expect the specified error and no new stored record. | Not checked. | uncertain | Check both response and storage. |
| Amount boundaries | Copy the project's actual limits; check valid, zero, precision-limit, and non-finite cases as applicable. | Not checked. | uncertain | Record each expected and observed outcome separately. |
| Date format and calendar validity | Copy required format; check a valid date and invalid calendar date. | Not checked. | uncertain | Compare add and filter date rules. |
| List and ordering | Include records with equal dates; record the required tie-break rule. | Not checked. | uncertain | Compare identifiers in returned order. |
| Category and date filters | Include records inside, outside, and on contracted boundaries. | Not checked. | uncertain | Write expected identifiers before observing results. |
| Overall and per-category summaries | Calculate exact expected totals from written input records. | Not checked. | uncertain | Compare included records and totals. |
| Delete: existing identifier | Expect only the selected record to disappear. | Not checked. | uncertain | Check remaining records. |
| Delete: missing identifier | Record expected message and process outcome. | Not checked. | uncertain | Compare both with observed behavior. |
| Restart persistence | Save, end the invocation, then retrieve through a fresh invocation using the same database. | Not checked. | uncertain | Record identifier and values before and after. |
| Storage failure | Copy the promised failure message and outcome; successful save must not be claimed. | Not checked. | uncertain | Locate suitable existing failure evidence or record the gap. |

For a mismatch, add the smallest reproducible input and actual outcome to the evidence cell, set status to missing, and name the correction needed. For an evidence gap, leave status uncertain and name the check needed. Split a row whenever one status would hide a different result within it.
