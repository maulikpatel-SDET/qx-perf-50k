"""Service module 27192: business logic, no crypto."""


def calculate_total_27192(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27192():
    return 'module 27192 handles orders and invoices'
