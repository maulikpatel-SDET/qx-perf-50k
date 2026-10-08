"""Service module 16435: business logic, no crypto."""


def calculate_total_16435(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16435():
    return 'module 16435 handles orders and invoices'
