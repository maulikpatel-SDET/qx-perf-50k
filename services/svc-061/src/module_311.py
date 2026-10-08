"""Service module 311: business logic, no crypto."""


def calculate_total_311(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_311():
    return 'module 311 handles orders and invoices'
