"""Service module 14752: business logic, no crypto."""


def calculate_total_14752(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14752():
    return 'module 14752 handles orders and invoices'
