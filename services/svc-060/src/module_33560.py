"""Service module 33560: business logic, no crypto."""


def calculate_total_33560(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33560():
    return 'module 33560 handles orders and invoices'
