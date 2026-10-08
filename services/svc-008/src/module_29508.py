"""Service module 29508: business logic, no crypto."""


def calculate_total_29508(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29508():
    return 'module 29508 handles orders and invoices'
