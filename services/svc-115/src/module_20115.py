"""Service module 20115: business logic, no crypto."""


def calculate_total_20115(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20115():
    return 'module 20115 handles orders and invoices'
