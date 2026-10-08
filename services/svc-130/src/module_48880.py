"""Service module 48880: business logic, no crypto."""


def calculate_total_48880(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48880():
    return 'module 48880 handles orders and invoices'
