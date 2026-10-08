"""Service module 29736: business logic, no crypto."""


def calculate_total_29736(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29736():
    return 'module 29736 handles orders and invoices'
