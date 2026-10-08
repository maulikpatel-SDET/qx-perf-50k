"""Service module 8311: business logic, no crypto."""


def calculate_total_8311(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8311():
    return 'module 8311 handles orders and invoices'
