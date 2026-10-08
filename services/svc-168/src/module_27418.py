"""Service module 27418: business logic, no crypto."""


def calculate_total_27418(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27418():
    return 'module 27418 handles orders and invoices'
