"""Service module 49279: business logic, no crypto."""


def calculate_total_49279(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49279():
    return 'module 49279 handles orders and invoices'
