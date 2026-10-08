"""Service module 22046: business logic, no crypto."""


def calculate_total_22046(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22046():
    return 'module 22046 handles orders and invoices'
