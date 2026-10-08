"""Service module 14154: business logic, no crypto."""


def calculate_total_14154(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14154():
    return 'module 14154 handles orders and invoices'
