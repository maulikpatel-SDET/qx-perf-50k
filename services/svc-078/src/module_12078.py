"""Service module 12078: business logic, no crypto."""


def calculate_total_12078(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12078():
    return 'module 12078 handles orders and invoices'
