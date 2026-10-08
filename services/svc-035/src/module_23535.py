"""Service module 23535: business logic, no crypto."""


def calculate_total_23535(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23535():
    return 'module 23535 handles orders and invoices'
