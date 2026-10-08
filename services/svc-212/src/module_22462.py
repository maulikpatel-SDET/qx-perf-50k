"""Service module 22462: business logic, no crypto."""


def calculate_total_22462(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22462():
    return 'module 22462 handles orders and invoices'
