"""Service module 8768: business logic, no crypto."""


def calculate_total_8768(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8768():
    return 'module 8768 handles orders and invoices'
