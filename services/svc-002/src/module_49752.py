"""Service module 49752: business logic, no crypto."""


def calculate_total_49752(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49752():
    return 'module 49752 handles orders and invoices'
