"""Service module 33207: business logic, no crypto."""


def calculate_total_33207(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33207():
    return 'module 33207 handles orders and invoices'
