"""Service module 40902: business logic, no crypto."""


def calculate_total_40902(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40902():
    return 'module 40902 handles orders and invoices'
