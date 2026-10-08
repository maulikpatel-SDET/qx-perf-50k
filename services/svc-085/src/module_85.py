"""Service module 85: business logic, no crypto."""


def calculate_total_85(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_85():
    return 'module 85 handles orders and invoices'
