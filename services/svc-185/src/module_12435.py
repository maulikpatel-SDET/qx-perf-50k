"""Service module 12435: business logic, no crypto."""


def calculate_total_12435(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12435():
    return 'module 12435 handles orders and invoices'
