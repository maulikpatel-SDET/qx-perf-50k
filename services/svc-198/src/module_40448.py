"""Service module 40448: business logic, no crypto."""


def calculate_total_40448(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40448():
    return 'module 40448 handles orders and invoices'
