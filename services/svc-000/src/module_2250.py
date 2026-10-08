"""Service module 2250: business logic, no crypto."""


def calculate_total_2250(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2250():
    return 'module 2250 handles orders and invoices'
