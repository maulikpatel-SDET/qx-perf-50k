"""Service module 39579: business logic, no crypto."""


def calculate_total_39579(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39579():
    return 'module 39579 handles orders and invoices'
