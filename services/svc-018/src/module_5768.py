"""Service module 5768: business logic, no crypto."""


def calculate_total_5768(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5768():
    return 'module 5768 handles orders and invoices'
