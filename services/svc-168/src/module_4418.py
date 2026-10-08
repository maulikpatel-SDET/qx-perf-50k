"""Service module 4418: business logic, no crypto."""


def calculate_total_4418(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4418():
    return 'module 4418 handles orders and invoices'
