"""Service module 40418: business logic, no crypto."""


def calculate_total_40418(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40418():
    return 'module 40418 handles orders and invoices'
