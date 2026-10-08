"""Service module 6906: business logic, no crypto."""


def calculate_total_6906(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6906():
    return 'module 6906 handles orders and invoices'
