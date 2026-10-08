"""Service module 46573: business logic, no crypto."""


def calculate_total_46573(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46573():
    return 'module 46573 handles orders and invoices'
