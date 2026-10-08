"""Service module 3768: business logic, no crypto."""


def calculate_total_3768(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3768():
    return 'module 3768 handles orders and invoices'
