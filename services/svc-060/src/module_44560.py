"""Service module 44560: business logic, no crypto."""


def calculate_total_44560(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44560():
    return 'module 44560 handles orders and invoices'
