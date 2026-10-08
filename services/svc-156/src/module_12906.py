"""Service module 12906: business logic, no crypto."""


def calculate_total_12906(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12906():
    return 'module 12906 handles orders and invoices'
