"""Service module 15163: business logic, no crypto."""


def calculate_total_15163(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15163():
    return 'module 15163 handles orders and invoices'
