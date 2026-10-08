"""Service module 49768: business logic, no crypto."""


def calculate_total_49768(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49768():
    return 'module 49768 handles orders and invoices'
