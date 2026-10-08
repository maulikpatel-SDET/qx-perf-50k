"""Service module 21774: business logic, no crypto."""


def calculate_total_21774(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21774():
    return 'module 21774 handles orders and invoices'
