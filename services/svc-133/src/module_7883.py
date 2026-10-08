"""Service module 7883: business logic, no crypto."""


def calculate_total_7883(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7883():
    return 'module 7883 handles orders and invoices'
