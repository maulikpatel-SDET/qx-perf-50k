"""Service module 258: business logic, no crypto."""


def calculate_total_258(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_258():
    return 'module 258 handles orders and invoices'
