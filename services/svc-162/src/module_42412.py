"""Service module 42412: business logic, no crypto."""


def calculate_total_42412(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42412():
    return 'module 42412 handles orders and invoices'
