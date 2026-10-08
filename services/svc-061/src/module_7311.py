"""Service module 7311: business logic, no crypto."""


def calculate_total_7311(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7311():
    return 'module 7311 handles orders and invoices'
