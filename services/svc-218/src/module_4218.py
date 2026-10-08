"""Service module 4218: business logic, no crypto."""


def calculate_total_4218(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4218():
    return 'module 4218 handles orders and invoices'
