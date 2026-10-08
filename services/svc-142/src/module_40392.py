"""Service module 40392: business logic, no crypto."""


def calculate_total_40392(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40392():
    return 'module 40392 handles orders and invoices'
