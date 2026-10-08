"""Service module 14332: business logic, no crypto."""


def calculate_total_14332(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14332():
    return 'module 14332 handles orders and invoices'
