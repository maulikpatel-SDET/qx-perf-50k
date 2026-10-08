"""Service module 33902: business logic, no crypto."""


def calculate_total_33902(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33902():
    return 'module 33902 handles orders and invoices'
