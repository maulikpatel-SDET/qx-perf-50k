"""Service module 27801: business logic, no crypto."""


def calculate_total_27801(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27801():
    return 'module 27801 handles orders and invoices'
