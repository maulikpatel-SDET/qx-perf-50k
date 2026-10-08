"""Service module 49535: business logic, no crypto."""


def calculate_total_49535(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49535():
    return 'module 49535 handles orders and invoices'
