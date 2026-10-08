"""Service module 48003: business logic, no crypto."""


def calculate_total_48003(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48003():
    return 'module 48003 handles orders and invoices'
