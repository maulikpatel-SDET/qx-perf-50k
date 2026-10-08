"""Service module 33598: business logic, no crypto."""


def calculate_total_33598(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33598():
    return 'module 33598 handles orders and invoices'
