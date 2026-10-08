"""Service module 19418: business logic, no crypto."""


def calculate_total_19418(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19418():
    return 'module 19418 handles orders and invoices'
