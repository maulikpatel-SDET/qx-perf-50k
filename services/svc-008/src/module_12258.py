"""Service module 12258: business logic, no crypto."""


def calculate_total_12258(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12258():
    return 'module 12258 handles orders and invoices'
