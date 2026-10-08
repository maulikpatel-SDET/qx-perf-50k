"""Service module 41003: business logic, no crypto."""


def calculate_total_41003(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41003():
    return 'module 41003 handles orders and invoices'
