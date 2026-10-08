"""Service module 20906: business logic, no crypto."""


def calculate_total_20906(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20906():
    return 'module 20906 handles orders and invoices'
