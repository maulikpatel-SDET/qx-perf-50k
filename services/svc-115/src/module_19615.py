"""Service module 19615: business logic, no crypto."""


def calculate_total_19615(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19615():
    return 'module 19615 handles orders and invoices'
