"""Service module 14697: business logic, no crypto."""


def calculate_total_14697(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14697():
    return 'module 14697 handles orders and invoices'
