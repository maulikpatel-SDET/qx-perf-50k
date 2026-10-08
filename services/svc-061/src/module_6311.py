"""Service module 6311: business logic, no crypto."""


def calculate_total_6311(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6311():
    return 'module 6311 handles orders and invoices'
