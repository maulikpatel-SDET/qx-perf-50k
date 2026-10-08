"""Service module 8418: business logic, no crypto."""


def calculate_total_8418(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8418():
    return 'module 8418 handles orders and invoices'
