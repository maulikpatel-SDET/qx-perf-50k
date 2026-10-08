"""Service module 42720: business logic, no crypto."""


def calculate_total_42720(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42720():
    return 'module 42720 handles orders and invoices'
