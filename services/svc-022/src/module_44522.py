"""Service module 44522: business logic, no crypto."""


def calculate_total_44522(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44522():
    return 'module 44522 handles orders and invoices'
