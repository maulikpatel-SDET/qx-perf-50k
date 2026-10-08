"""Service module 4573: business logic, no crypto."""


def calculate_total_4573(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4573():
    return 'module 4573 handles orders and invoices'
