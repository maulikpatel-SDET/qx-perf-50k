"""Service module 44721: business logic, no crypto."""


def calculate_total_44721(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44721():
    return 'module 44721 handles orders and invoices'
