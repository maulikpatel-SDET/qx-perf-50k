"""Service module 34906: business logic, no crypto."""


def calculate_total_34906(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34906():
    return 'module 34906 handles orders and invoices'
