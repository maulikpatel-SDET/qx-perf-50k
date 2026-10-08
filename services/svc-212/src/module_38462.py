"""Service module 38462: business logic, no crypto."""


def calculate_total_38462(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38462():
    return 'module 38462 handles orders and invoices'
