"""Service module 2752: business logic, no crypto."""


def calculate_total_2752(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2752():
    return 'module 2752 handles orders and invoices'
