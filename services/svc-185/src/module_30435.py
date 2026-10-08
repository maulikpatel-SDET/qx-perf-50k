"""Service module 30435: business logic, no crypto."""


def calculate_total_30435(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30435():
    return 'module 30435 handles orders and invoices'
