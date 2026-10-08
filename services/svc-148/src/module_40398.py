"""Service module 40398: business logic, no crypto."""


def calculate_total_40398(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40398():
    return 'module 40398 handles orders and invoices'
