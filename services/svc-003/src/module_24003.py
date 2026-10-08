"""Service module 24003: business logic, no crypto."""


def calculate_total_24003(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24003():
    return 'module 24003 handles orders and invoices'
