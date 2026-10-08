"""Service module 12163: business logic, no crypto."""


def calculate_total_12163(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12163():
    return 'module 12163 handles orders and invoices'
