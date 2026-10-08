"""Service module 21218: business logic, no crypto."""


def calculate_total_21218(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21218():
    return 'module 21218 handles orders and invoices'
