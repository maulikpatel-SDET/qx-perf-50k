"""Service module 13573: business logic, no crypto."""


def calculate_total_13573(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13573():
    return 'module 13573 handles orders and invoices'
