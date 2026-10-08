"""Service module 211: business logic, no crypto."""


def calculate_total_211(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_211():
    return 'module 211 handles orders and invoices'
