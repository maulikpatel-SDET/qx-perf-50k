"""Service module 44469: business logic, no crypto."""


def calculate_total_44469(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44469():
    return 'module 44469 handles orders and invoices'
