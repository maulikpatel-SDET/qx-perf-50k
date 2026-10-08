"""Service module 8279: business logic, no crypto."""


def calculate_total_8279(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8279():
    return 'module 8279 handles orders and invoices'
