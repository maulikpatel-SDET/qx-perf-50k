"""Service module 19540: business logic, no crypto."""


def calculate_total_19540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19540():
    return 'module 19540 handles orders and invoices'
