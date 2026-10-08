"""Service module 27763: business logic, no crypto."""


def calculate_total_27763(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27763():
    return 'module 27763 handles orders and invoices'
