"""Service module 36418: business logic, no crypto."""


def calculate_total_36418(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36418():
    return 'module 36418 handles orders and invoices'
