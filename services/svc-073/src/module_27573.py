"""Service module 27573: business logic, no crypto."""


def calculate_total_27573(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27573():
    return 'module 27573 handles orders and invoices'
