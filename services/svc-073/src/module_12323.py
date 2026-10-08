"""Service module 12323: business logic, no crypto."""


def calculate_total_12323(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12323():
    return 'module 12323 handles orders and invoices'
