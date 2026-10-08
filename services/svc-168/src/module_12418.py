"""Service module 12418: business logic, no crypto."""


def calculate_total_12418(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12418():
    return 'module 12418 handles orders and invoices'
