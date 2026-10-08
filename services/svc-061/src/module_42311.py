"""Service module 42311: business logic, no crypto."""


def calculate_total_42311(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42311():
    return 'module 42311 handles orders and invoices'
