"""Service module 38435: business logic, no crypto."""


def calculate_total_38435(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38435():
    return 'module 38435 handles orders and invoices'
