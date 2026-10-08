"""Service module 48577: business logic, no crypto."""


def calculate_total_48577(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48577():
    return 'module 48577 handles orders and invoices'
