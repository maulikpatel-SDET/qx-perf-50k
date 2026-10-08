"""Service module 44418: business logic, no crypto."""


def calculate_total_44418(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44418():
    return 'module 44418 handles orders and invoices'
