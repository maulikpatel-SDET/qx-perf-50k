"""Service module 14074: business logic, no crypto."""


def calculate_total_14074(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14074():
    return 'module 14074 handles orders and invoices'
