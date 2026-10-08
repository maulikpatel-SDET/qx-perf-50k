"""Service module 46560: business logic, no crypto."""


def calculate_total_46560(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46560():
    return 'module 46560 handles orders and invoices'
