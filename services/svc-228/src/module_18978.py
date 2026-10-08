"""Service module 18978: business logic, no crypto."""


def calculate_total_18978(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18978():
    return 'module 18978 handles orders and invoices'
