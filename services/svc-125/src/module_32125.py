"""Service module 32125: business logic, no crypto."""


def calculate_total_32125(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32125():
    return 'module 32125 handles orders and invoices'
