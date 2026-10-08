"""Service module 33865: business logic, no crypto."""


def calculate_total_33865(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33865():
    return 'module 33865 handles orders and invoices'
