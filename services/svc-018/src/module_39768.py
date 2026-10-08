"""Service module 39768: business logic, no crypto."""


def calculate_total_39768(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39768():
    return 'module 39768 handles orders and invoices'
