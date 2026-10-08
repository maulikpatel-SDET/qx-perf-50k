"""Service module 40651: business logic, no crypto."""


def calculate_total_40651(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40651():
    return 'module 40651 handles orders and invoices'
