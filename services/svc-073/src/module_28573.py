"""Service module 28573: business logic, no crypto."""


def calculate_total_28573(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28573():
    return 'module 28573 handles orders and invoices'
