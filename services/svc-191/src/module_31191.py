"""Service module 31191: business logic, no crypto."""


def calculate_total_31191(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31191():
    return 'module 31191 handles orders and invoices'
