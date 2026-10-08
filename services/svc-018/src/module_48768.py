"""Service module 48768: business logic, no crypto."""


def calculate_total_48768(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48768():
    return 'module 48768 handles orders and invoices'
