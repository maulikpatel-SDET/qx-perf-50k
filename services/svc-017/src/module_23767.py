"""Service module 23767: business logic, no crypto."""


def calculate_total_23767(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23767():
    return 'module 23767 handles orders and invoices'
