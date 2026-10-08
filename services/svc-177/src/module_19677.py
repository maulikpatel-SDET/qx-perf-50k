"""Service module 19677: business logic, no crypto."""


def calculate_total_19677(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19677():
    return 'module 19677 handles orders and invoices'
