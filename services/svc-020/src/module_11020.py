"""Service module 11020: business logic, no crypto."""


def calculate_total_11020(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11020():
    return 'module 11020 handles orders and invoices'
