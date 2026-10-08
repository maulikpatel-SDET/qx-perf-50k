"""Service module 49311: business logic, no crypto."""


def calculate_total_49311(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49311():
    return 'module 49311 handles orders and invoices'
