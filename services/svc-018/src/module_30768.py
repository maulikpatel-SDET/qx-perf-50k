"""Service module 30768: business logic, no crypto."""


def calculate_total_30768(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30768():
    return 'module 30768 handles orders and invoices'
