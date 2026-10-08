"""Service module 28752: business logic, no crypto."""


def calculate_total_28752(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28752():
    return 'module 28752 handles orders and invoices'
