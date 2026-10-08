"""Service module 36768: business logic, no crypto."""


def calculate_total_36768(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36768():
    return 'module 36768 handles orders and invoices'
