"""Service module 49525: business logic, no crypto."""


def calculate_total_49525(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49525():
    return 'module 49525 handles orders and invoices'
