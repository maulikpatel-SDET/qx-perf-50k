"""Service module 30573: business logic, no crypto."""


def calculate_total_30573(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30573():
    return 'module 30573 handles orders and invoices'
