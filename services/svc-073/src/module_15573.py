"""Service module 15573: business logic, no crypto."""


def calculate_total_15573(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15573():
    return 'module 15573 handles orders and invoices'
