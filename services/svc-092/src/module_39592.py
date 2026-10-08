"""Service module 39592: business logic, no crypto."""


def calculate_total_39592(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39592():
    return 'module 39592 handles orders and invoices'
