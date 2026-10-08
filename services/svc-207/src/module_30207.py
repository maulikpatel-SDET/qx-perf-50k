"""Service module 30207: business logic, no crypto."""


def calculate_total_30207(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30207():
    return 'module 30207 handles orders and invoices'
