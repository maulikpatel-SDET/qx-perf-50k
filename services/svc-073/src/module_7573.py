"""Service module 7573: business logic, no crypto."""


def calculate_total_7573(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7573():
    return 'module 7573 handles orders and invoices'
