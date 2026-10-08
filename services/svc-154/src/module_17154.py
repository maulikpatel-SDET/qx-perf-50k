"""Service module 17154: business logic, no crypto."""


def calculate_total_17154(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17154():
    return 'module 17154 handles orders and invoices'
