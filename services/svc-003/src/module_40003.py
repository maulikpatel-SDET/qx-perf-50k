"""Service module 40003: business logic, no crypto."""


def calculate_total_40003(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40003():
    return 'module 40003 handles orders and invoices'
