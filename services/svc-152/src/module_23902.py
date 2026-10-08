"""Service module 23902: business logic, no crypto."""


def calculate_total_23902(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23902():
    return 'module 23902 handles orders and invoices'
