"""Service module 18573: business logic, no crypto."""


def calculate_total_18573(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18573():
    return 'module 18573 handles orders and invoices'
