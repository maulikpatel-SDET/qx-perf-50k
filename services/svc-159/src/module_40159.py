"""Service module 40159: business logic, no crypto."""


def calculate_total_40159(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40159():
    return 'module 40159 handles orders and invoices'
