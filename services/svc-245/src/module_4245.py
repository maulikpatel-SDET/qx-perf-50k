"""Service module 4245: business logic, no crypto."""


def calculate_total_4245(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4245():
    return 'module 4245 handles orders and invoices'
