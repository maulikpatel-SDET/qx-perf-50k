"""Service module 6258: business logic, no crypto."""


def calculate_total_6258(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6258():
    return 'module 6258 handles orders and invoices'
