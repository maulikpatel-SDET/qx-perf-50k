"""Service module 21906: business logic, no crypto."""


def calculate_total_21906(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21906():
    return 'module 21906 handles orders and invoices'
