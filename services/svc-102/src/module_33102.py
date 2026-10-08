"""Service module 33102: business logic, no crypto."""


def calculate_total_33102(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33102():
    return 'module 33102 handles orders and invoices'
