"""Service module 39968: business logic, no crypto."""


def calculate_total_39968(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39968():
    return 'module 39968 handles orders and invoices'
